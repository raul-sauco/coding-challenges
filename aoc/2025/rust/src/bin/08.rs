use std::{cmp::Reverse, collections::BinaryHeap};

use glam::I64Vec3;
use itertools::Itertools;
use nom::{
    IResult, Parser,
    character::complete::{char, i64, line_ending, space0},
    combinator::map,
    multi::separated_list1,
    sequence::delimited,
};

advent_of_code::solution!(8);

#[derive(Debug)]
struct UnionFind {
    parents: Vec<usize>,
    rank: Vec<usize>,
    components: usize,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            parents: (0..n).collect(),
            rank: vec![1; n],
            components: n,
        }
    }

    fn find_parent(&mut self, a: usize) -> usize {
        if a != self.parents[a] {
            self.parents[a] = self.find_parent(self.parents[a]);
        }
        self.parents[a]
    }

    fn union(&mut self, a: usize, b: usize) {
        let (pa, pb) = (self.find_parent(a), self.find_parent(b));
        if pa == pb {
            return;
        }
        if self.rank[pb] > self.rank[pa] {
            return self.union(b, a);
        }
        self.parents[pb] = pa;
        self.rank[pa] += self.rank[pb];
        self.components -= 1;
    }
}

fn parser(input: &str) -> IResult<&str, Vec<I64Vec3>> {
    separated_list1(line_ending, vec).parse(input)
}

fn vec(input: &str) -> IResult<&str, I64Vec3> {
    map(
        (
            i64,
            delimited(space0, char(','), space0),
            i64,
            delimited(space0, char(','), space0),
            i64,
        ),
        |(x, _, y, _, z)| I64Vec3 { x, y, z },
    )
    .parse(input)
}

// 10 connections on the test and 1000 for the regular input
const CONNECTIONS: usize = 1000;
const CIRCUITS: usize = 3;

// Part 1: 81536 (4.5ms @ 122 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, res) = parser.parse(input).expect("a good parse");
    let mut heap: BinaryHeap<(Reverse<i64>, usize, usize)> = res
        .iter()
        .enumerate()
        .tuple_combinations()
        .map(|((a_idx, a), (b_idx, b))| (Reverse((a - b).length_squared()), a_idx, b_idx))
        .collect();
    let mut uf = UnionFind::new(res.len());
    for _ in 0..CONNECTIONS {
        if let Some((_, a, b)) = heap.pop() {
            uf.union(a, b);
        } else {
            break;
        }
    }
    let largest = uf
        .rank
        .select_nth_unstable(res.len() - CIRCUITS - 1)
        .2
        .iter()
        .product::<usize>();
    Some(largest as _)
}

// Part 2: 7017750530 (5.4ms @ 206 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, res) = parser.parse(input).expect("a good parse");
    let mut heap: BinaryHeap<(Reverse<i64>, usize, usize)> = res
        .iter()
        .enumerate()
        .tuple_combinations()
        .map(|((a_idx, a), (b_idx, b))| (Reverse((a - b).length_squared()), a_idx, b_idx))
        .collect();
    let mut uf = UnionFind::new(res.len());
    loop {
        if let Some((_, a, b)) = heap.pop() {
            uf.union(a, b);
            if uf.components == 1 {
                let va = res[a];
                let vb = res[b];
                return Some((va.x * vb.x) as u64);
            }
        } else {
            panic!("I thought the heap still had values!");
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(40));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(25272));
    }
}
