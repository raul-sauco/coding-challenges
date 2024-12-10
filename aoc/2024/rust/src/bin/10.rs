advent_of_code::solution!(10);

use std::collections::{HashMap, HashSet};

use glam::{u32, IVec2};

fn parse_grid(input: &str) -> HashMap<IVec2, u32> {
    input
        .lines()
        .enumerate()
        .flat_map(|(y, line)| {
            line.chars().enumerate().map(move |(x, c)| {
                (
                    IVec2::new(x as i32, y as i32),
                    c.to_digit(10).expect("A digit"),
                )
            })
        })
        .collect()
}

fn dfs(
    grid: &HashMap<IVec2, u32>,
    visited: &mut HashSet<IVec2>,
    summits: &mut HashSet<IVec2>,
    pos: &IVec2,
    expected_height: u32,
) {
    if let Some(&height) = grid.get(pos) {
        if height != expected_height || visited.contains(pos) {
            return;
        }
        visited.insert(*pos);
        if height == 9 {
            summits.insert(*pos);
            return;
        }
        for dir in [IVec2::NEG_Y, IVec2::X, IVec2::Y, IVec2::NEG_X] {
            dfs(grid, visited, summits, &(pos + dir), height + 1);
        }
    }
}

fn count_summits(grid: &HashMap<IVec2, u32>, pos: &IVec2) -> u32 {
    let mut visited = HashSet::<IVec2>::new();
    let mut summits = HashSet::<IVec2>::new();
    for dir in [IVec2::NEG_Y, IVec2::X, IVec2::Y, IVec2::NEG_X] {
        dfs(grid, &mut visited, &mut summits, &(pos + dir), 1);
    }
    summits.len() as u32
}

pub fn part_one(input: &str) -> Option<u32> {
    let grid = parse_grid(input);
    Some(
        grid.iter()
            .map(|(pos, &height)| {
                if height == 0 {
                    count_summits(&grid, pos)
                } else {
                    0
                }
            })
            .sum(),
    )
}

fn count_trails(grid: &HashMap<IVec2, u32>, pos: &IVec2, expected_height: u32) -> u32 {
    if let Some(&height) = grid.get(pos) {
        if height != expected_height {
            return 0;
        }
        if height == 9 {
            return 1;
        }
        return [IVec2::NEG_Y, IVec2::X, IVec2::Y, IVec2::NEG_X]
            .iter()
            .map(|dir| count_trails(grid, &(pos + dir), height + 1))
            .sum();
    }
    0
}

pub fn part_two(input: &str) -> Option<u32> {
    let grid = parse_grid(input);
    Some(grid.keys().map(|pos| count_trails(&grid, pos, 0)).sum())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(36));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(81));
    }
}
