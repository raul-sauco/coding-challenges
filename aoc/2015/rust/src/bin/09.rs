use bitvec::prelude::*;
use nom::{
    IResult, Parser,
    bytes::complete::tag,
    character::complete::{self, alpha1, line_ending},
    combinator::map,
    multi::separated_list1,
};
use rustc_hash::FxHashMap;

advent_of_code::solution!(9);

#[derive(Debug)]
struct Line<'a> {
    a: &'a str,
    b: &'a str,
    dist: u64,
}

fn parser(input: &str) -> IResult<&str, Vec<Line<'_>>> {
    separated_list1(line_ending, line).parse(input)
}

fn line(input: &str) -> IResult<&str, Line<'_>> {
    map(
        (alpha1, tag(" to "), alpha1, tag(" = "), complete::u64),
        |(a, _, b, _, dist)| Line { a, b, dist },
    )
    .parse(input)
}

// Given the AOC input, get a hashmap of node => Vec<(node, dist)>
fn process(input: &str) -> FxHashMap<usize, Vec<(usize, u64)>> {
    let (_, lines) = parser.parse(input).expect("a good parse");
    let mut dict: FxHashMap<&str, usize> = FxHashMap::default();
    let mut neighbors: FxHashMap<usize, Vec<(usize, u64)>> = FxHashMap::default();
    // A dictionary to convert str node ids to indexes
    for line in lines {
        if !dict.contains_key(line.a) {
            dict.insert(line.a, dict.len());
        }
        if !dict.contains_key(line.b) {
            dict.insert(line.b, dict.len());
        }
        match (dict.get(line.a), dict.get(line.b)) {
            (Some(&a), Some(&b)) => {
                // The edges are undirected
                neighbors.entry(a).or_default().push((b, line.dist));
                neighbors.entry(b).or_default().push((a, line.dist));
            }
            _ => panic!("expected to find the two nodes"),
        }
    }
    neighbors
}

fn dfs(
    current_node: usize,
    current_cost: u64,
    neighbors: &FxHashMap<usize, Vec<(usize, u64)>>,
    visited: &mut BitVec,
    best: u64,
) -> Option<u64> {
    if current_cost >= best {
        return None;
    }
    if visited.all() {
        return Some(current_cost);
    }
    let mut current_best = best;
    match neighbors.get(&current_node) {
        Some(neighs) => {
            for &(id, dist) in neighs {
                if visited[id] {
                    continue;
                }
                visited.set(id, true);
                if let Some(res) = dfs(id, current_cost + dist, neighbors, visited, current_best) {
                    current_best = current_best.min(res);
                }
                visited.set(id, false);
            }
        }
        None => panic!("expected to find node {current_node}"),
    }
    if current_best < best {
        Some(current_best)
    } else {
        None
    }
}

// Part 1: 251 (59.3µs @ 8717 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let neighbors = process(input);
    let mut visited = bitvec![0; neighbors.len()];
    let mut best = u64::MAX;
    for node in 0..visited.len() {
        visited.set(node, true);
        if let Some(res) = dfs(node, 0, &neighbors, &mut visited, best) {
            best = best.min(res);
        }
        visited.set(node, false);
    }
    Some(best)
}

fn dfs_max(
    current_node: usize,
    current_cost: u64,
    neighbors: &FxHashMap<usize, Vec<(usize, u64)>>,
    visited: &mut BitVec,
    best: u64,
) -> Option<u64> {
    if visited.all() {
        return Some(current_cost);
    }
    let mut current_best = best;
    match neighbors.get(&current_node) {
        Some(neighs) => {
            for &(id, dist) in neighs {
                if visited[id] {
                    continue;
                }
                visited.set(id, true);
                if let Some(res) =
                    dfs_max(id, current_cost + dist, neighbors, visited, current_best)
                {
                    current_best = current_best.max(res);
                }
                visited.set(id, false);
            }
        }
        None => panic!("expected to find node {current_node}"),
    }
    if current_best > best {
        Some(current_best)
    } else {
        None
    }
}

// Part 2: 898 (1.4ms @ 667 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let neighbors = process(input);
    let mut visited = bitvec![0; neighbors.len()];
    let mut best = u64::MIN;
    for node in 0..visited.len() {
        visited.set(node, true);
        if let Some(res) = dfs_max(node, 0, &neighbors, &mut visited, best) {
            best = best.max(res);
        }
        visited.set(node, false);
    }
    Some(best)
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        r"London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141",
        605
    )]
    fn test_part_one(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[rstest]
    #[case(
        r"London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141",
        982
    )]
    fn test_part_two(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_two(input), Some(expected));
    }
}
