use std::collections::BTreeMap;

use itertools::Itertools;
use nom::{
    IResult, Parser,
    character::complete::{char, line_ending, u64},
    combinator::map,
    multi::separated_list1,
};

advent_of_code::solution!(9);

#[derive(Debug)]
struct Tile {
    x: u64,
    y: u64,
}

fn rectangle_area(a: &Tile, b: &Tile) -> u64 {
    ((a.x).abs_diff(b.x) + 1) * ((a.y).abs_diff(b.y) + 1)
}

fn parser(input: &str) -> IResult<&str, Vec<Tile>> {
    separated_list1(line_ending, tile).parse(input)
}

fn tile(input: &str) -> IResult<&str, Tile> {
    map((u64, char(','), u64), |(x, _, y)| Tile { x, y }).parse(input)
}

// Part 1: 4763932976 (103.8µs @ 9400 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, tiles) = parser.parse(input).expect("a good parse");
    let res = tiles
        .iter()
        .tuple_combinations()
        .map(|(a, b)| rectangle_area(a, b))
        .max()
        .unwrap();
    Some(res)
}

// Part 2: 1501292304 (10.3ms @ 70 samples) - Using nested loop with vector.
pub fn part_two(input: &str) -> Option<u64> {
    let (_, tiles) = parser.parse(input).expect("a good parse");
    let lines = tiles
        .iter()
        .circular_tuple_windows()
        .collect::<Vec<(&Tile, &Tile)>>();
    let res = tiles
        .iter()
        .tuple_combinations()
        .map(|(a, b)| (a, b, rectangle_area(a, b)))
        .sorted_by_key(|t| t.2)
        .rev()
        .find(|(a, b, _)| {
            lines.iter().all(|(start_tile, end_tile)| {
                a.x.max(b.x) <= start_tile.x.min(end_tile.x)
                    || a.x.min(b.x) >= start_tile.x.max(end_tile.x)
                    || a.y.max(b.y) <= start_tile.y.min(end_tile.y)
                    || a.y.min(b.y) >= start_tile.y.max(end_tile.y)
            })
        });
    Some(res.unwrap().2)
}

// Part 2: 1501292304 (15.4ms @ 62 samples) - Using BTreeMap to iterate only over lines that may
// intersect the rectangle.
pub fn part_two_btree(input: &str) -> Option<u64> {
    let (_, tiles) = parser.parse(input).expect("a good parse");
    let (horizontal_lines, vertical_lines) = tiles.iter().circular_tuple_windows().fold(
        (BTreeMap::new(), BTreeMap::new()),
        |mut acc, (a, b)| {
            if a.x == b.x {
                acc.1.entry(a.x).or_insert(vec![]).push(if a.y < b.y {
                    a.y..=b.y
                } else {
                    b.y..=a.y
                });
            } else {
                acc.0.entry(a.y).or_insert(vec![]).push(if a.x < b.x {
                    a.x..=b.x
                } else {
                    b.x..=a.x
                });
            }
            acc
        },
    );
    let res = tiles
        .iter()
        .tuple_combinations()
        .map(|(a, b)| (a, b, rectangle_area(a, b)))
        .sorted_by_key(|t| t.2)
        .rev()
        .find(|(a, b, _area)| {
            let (x_start, x_end) = (a.x.min(b.x) + 1, a.x.max(b.x) - 1);
            let (y_start, y_end) = (a.y.min(b.y) + 1, a.y.max(b.y) - 1);
            let vertical_intersect = vertical_lines
                .range(x_start..=x_end)
                .flat_map(|(_key, v)| v.iter())
                .find(|line| !(*line.end() < y_start || *line.start() > y_end));
            let horizontal_intersect = horizontal_lines
                .range(y_start..=y_end)
                .flat_map(|(_key, v)| v.iter())
                .find(|line| !(*line.end() < x_start || *line.start() > x_end));
            matches!((horizontal_intersect, vertical_intersect), (None, None))
        });
    Some(res.unwrap().2)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(50));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(24));
    }
}
