advent_of_code::solution!(8);

use std::collections::{HashMap, HashSet};

use glam::IVec2;

#[derive(Debug)]
struct Grid {
    frequencies: HashMap<char, Vec<IVec2>>,
    num_rows: i32,
    num_cols: i32,
}

fn parse(input: &str) -> Grid {
    let mut frequencies: HashMap<char, Vec<IVec2>> = HashMap::new();
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            if c == '.' {
                continue;
            }
            frequencies
                .entry(c)
                .and_modify(|v| v.push(IVec2::new(x as i32, y as i32)))
                .or_insert(vec![IVec2::new(x as i32, y as i32)]);
        }
    }
    Grid {
        frequencies,
        num_rows: input.lines().count() as i32,
        num_cols: input.lines().next().unwrap().chars().count() as i32,
    }
}

pub fn part_one(input: &str) -> Option<u32> {
    let grid = parse(input);
    let mut res: HashSet<IVec2> = HashSet::new();
    for (_freq, antennas) in grid.frequencies {
        for i in 0..antennas.len() {
            for j in i + 1..antennas.len() {
                let (a, b) = (antennas[i], antennas[j]);
                // The vector from a to b scaled by 2 with the same start.
                let a_b = (2 * (b - a)) + a;
                let b_a = (2 * (a - b)) + b;
                for v in [a_b, b_a] {
                    if v.x >= 0 && v.x < grid.num_cols && v.y >= 0 && v.y < grid.num_rows {
                        res.insert(v);
                    }
                }
            }
        }
    }
    Some(res.len() as u32)
}

pub fn part_two(input: &str) -> Option<u32> {
    let grid = parse(input);
    let n = grid.num_rows.max(grid.num_cols);
    let mut res: HashSet<IVec2> = HashSet::new();
    for (_freq, antennas) in grid.frequencies {
        for i in 0..antennas.len() {
            for j in i + 1..antennas.len() {
                let (v1, v2) = (antennas[i], antennas[j]);
                for (a, b) in [(v1, v2), (v2, v1)] {
                    let (base, offset) = (b, b - a);
                    for mult in 0..n {
                        let v = base + offset * mult;
                        if v.x >= 0 && v.x < grid.num_cols && v.y >= 0 && v.y < grid.num_rows {
                            res.insert(v);
                        } else {
                            break;
                        }
                    }
                }
            }
        }
    }
    Some(res.len() as u32)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(14));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(34));
    }
}
