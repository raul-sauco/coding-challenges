use std::collections::HashSet;

use glam::IVec2;

advent_of_code::solution!(4);

fn parse_grid(input: &str) -> HashSet<IVec2> {
    let mut grid: HashSet<IVec2> = HashSet::new();
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            if c == '@' {
                grid.insert(IVec2::new(x as _, y as _));
            }
        }
    }
    grid
}

fn accessible(grid: &HashSet<IVec2>, pos: &IVec2) -> bool {
    let dirs = [
        IVec2::Y,
        IVec2::new(1, 1),
        IVec2::X,
        IVec2::new(1, -1),
        IVec2::NEG_Y,
        IVec2::new(-1, -1),
        IVec2::NEG_X,
        IVec2::new(-1, 1),
    ];
    let hits = dirs
        .iter()
        .map(|dir| if grid.contains(&(pos + dir)) { 1 } else { 0 })
        .sum::<i32>();
    hits < 4
}

pub fn part_one(input: &str) -> Option<u64> {
    let grid = parse_grid(input);
    let mut res = 0;
    for pos in &grid {
        if accessible(&grid, pos) {
            res += 1;
        }
    }
    Some(res)
}

pub fn part_two(input: &str) -> Option<u64> {
    let mut grid = parse_grid(input);
    let mut res = 0;
    let mut remove = HashSet::new();
    loop {
        for pos in &grid {
            if accessible(&grid, pos) {
                remove.insert(*pos);
                res += 1;
            }
        }
        if remove.is_empty() {
            break;
        }
        grid = &grid - &remove;
        remove.clear();
    }
    Some(res)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(13));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(43));
    }
}
