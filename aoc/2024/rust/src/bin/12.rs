advent_of_code::solution!(12);

use std::collections::{HashMap, HashSet, VecDeque};

use glam::IVec2;
use itertools::Itertools;

#[derive(Debug)]
struct Area {
    id: char,
    cells: HashSet<IVec2>,
    perimeter: u32,
}

impl Area {
    fn get_points(&self) -> u32 {
        self.cells.len() as u32 * self.perimeter
    }
}

fn parse(input: &str) -> HashMap<IVec2, char> {
    input
        .lines()
        .enumerate()
        .flat_map(|(y, line)| {
            line.chars()
                .enumerate()
                .map(move |(x, c)| (IVec2::new(x as i32, y as i32), c))
        })
        .collect()
}

fn process_cell(
    grid: &HashMap<IVec2, char>,
    pos: &IVec2,
    c: &char,
    visited: &mut HashSet<IVec2>,
) -> Area {
    let mut area = Area {
        id: *c,
        cells: HashSet::new(),
        perimeter: 0,
    };
    visited.insert(*pos);
    area.cells.insert(*pos);
    let mut q = VecDeque::from([*pos]);
    while let Some(coordinates) = q.pop_front() {
        for offset in [IVec2::NEG_Y, IVec2::X, IVec2::Y, IVec2::NEG_X] {
            let nei_pos = coordinates + offset;
            if let Some(nei_char) = grid.get(&nei_pos) {
                if c == nei_char {
                    if !area.cells.contains(&nei_pos) {
                        visited.insert(nei_pos);
                        area.cells.insert(nei_pos);
                        q.push_back(nei_pos);
                    }
                } else {
                    // Count the perimeter if this cell is another crop.
                    area.perimeter += 1;
                }
            } else {
                // Count the perimeter if out of grid bounds.
                area.perimeter += 1;
            }
        }
    }
    area
}

fn get_areas(grid: &HashMap<IVec2, char>) -> Vec<Area> {
    let mut visited = HashSet::<IVec2>::new();
    let mut areas: Vec<Area> = vec![];
    for (pos, c) in grid.iter() {
        if !visited.contains(pos) {
            areas.push(process_cell(&grid, pos, c, &mut visited));
        }
    }
    areas
}

pub fn part_one(input: &str) -> Option<u32> {
    let grid = parse(input);
    Some(
        get_areas(&grid)
            .into_iter()
            .map(|area| area.get_points())
            .sum(),
    )
}

fn count_cell_corners(id: &char, n: &IVec2, grid: &HashMap<IVec2, char>) -> u32 {
    [IVec2::NEG_Y, IVec2::X, IVec2::Y, IVec2::NEG_X]
        .iter()
        .circular_tuple_windows()
        .map(|(a, b)| {
            let ortho_a = grid.get(&(n + a)).is_some_and(|c| c == id);
            let ortho_b = grid.get(&(n + b)).is_some_and(|c| c == id);
            let diagonal_ab = grid.get(&(n + a + b)).is_some_and(|c| c != id);
            if (ortho_a && ortho_b && diagonal_ab) || (!ortho_a && !ortho_b) {
                1
            } else {
                0
            }
        })
        .sum()
}

fn count_area_corners(grid: &HashMap<IVec2, char>, area: &Area) -> u32 {
    area.cells
        .iter()
        .map(|n| count_cell_corners(&area.id, n, &grid))
        .sum()
}

pub fn part_two(input: &str) -> Option<u32> {
    let grid = parse(input);
    Some(
        get_areas(&grid)
            .iter()
            .map(|area| area.cells.len() as u32 * count_area_corners(&grid, area))
            .sum(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case(
        r#"AAAA
BBCD
BBCC
EEEC"#,
        Some(140);
        "input 1"
    )]
    #[test_case(
        r#"OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"#,
        Some(772);
        "input 2"
    )]
    #[test_case(
        r#"RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"#,
        Some(1930);
        "input 3"
    )]
    fn test_part_one(input: &str, expected: Option<u32>) {
        assert_eq!(part_one(input), expected);
    }

    #[test_case(
        r#"AAAA
BBCD
BBCC
EEEC"#,
        Some(80);
        "ABCDE Plants"
    )]
    #[test_case(
        r#"OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"#,
        Some(436);
        "XO Plants"
    )]
    #[test_case(
        r#"EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"#,
        Some(236);
        "E Shaped E plants"
    )]
    #[test_case(
        r#"AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"#,
        Some(368);
        "AB Plants"
    )]
    #[test_case(
        r#"RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"#,
        Some(1206);
        "Large field"
    )]
    fn test_part_two(input: &str, expected: Option<u32>) {
        assert_eq!(part_two(input), expected);
    }
}
