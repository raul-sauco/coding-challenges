advent_of_code::solution!(6);

use glam::{i32, IVec2, IVec3};
use std::collections::{HashMap, HashSet};

fn get_grid(input: &str) -> HashMap<IVec2, char> {
    let mut grid = HashMap::new();
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            grid.insert(IVec2::new(x as i32, y as i32), c);
        }
    }
    grid
}

fn find_guard(input: &str) -> IVec2 {
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            if c == '^' {
                return IVec2::new(x as i32, y as i32);
            }
        }
    }
    unreachable!(
        "We couldn't find the guard in the grid using '^'. \
        Maybe your guard is facing another direction? '>', '<'..."
    );
}

fn get_visited_cells(grid: &HashMap<IVec2, char>, guard: &IVec2) -> HashSet<IVec2> {
    // Shadow and dereference.
    let mut guard = *guard;
    // In my example and input, the guard starts facing north.
    let dirs = [IVec2::NEG_Y, IVec2::X, IVec2::Y, IVec2::NEG_X];
    let mut current_dir = 0;
    let mut visited: HashSet<IVec2> = HashSet::new();
    visited.insert(guard);
    while let Some(next_char) = grid.get(&(guard + dirs[current_dir])) {
        match next_char {
            '.' | '^' => {
                // Move to the next cell.
                guard += dirs[current_dir];
                visited.insert(guard);
            }
            '#' => {
                // Obstacle, turn right.
                current_dir = (current_dir + 1) % dirs.len();
            }
            _ => unreachable!("'{next_char}' is not valid cell content"),
        }
    }
    visited
}

pub fn part_one(input: &str) -> Option<u32> {
    let grid = get_grid(input);
    let guard = find_guard(input);
    assert_eq!(*grid.get(&guard).unwrap(), '^');
    Some(get_visited_cells(&grid, &guard).len() as u32)
}

fn has_cycle(grid: &HashMap<IVec2, char>, guard: &IVec2) -> bool {
    // Shadow and dereference.
    let mut guard = *guard;
    // In my example and input, the guard starts facing north.
    let dirs = [IVec2::NEG_Y, IVec2::X, IVec2::Y, IVec2::NEG_X];
    let mut current_dir = 0;
    let mut visited: HashSet<IVec3> = HashSet::new();
    visited.insert(IVec3::new(guard.x, guard.y, current_dir as i32));
    while let Some(next_char) = grid.get(&(guard + dirs[current_dir])) {
        match next_char {
            '.' | '^' => {
                // Move to the next cell.
                guard += dirs[current_dir];
                let dir_pos = IVec3::new(guard.x, guard.y, current_dir as i32);
                if visited.contains(&dir_pos) {
                    return true;
                }
                visited.insert(dir_pos);
            }
            '#' => {
                // Obstacle, turn right.
                current_dir = (current_dir + 1) % dirs.len();
            }
            _ => unreachable!("'{next_char}' is not valid cell content"),
        }
    }
    // If we get here, we exited the grid, no cycle.
    false
}

pub fn part_two(input: &str) -> Option<u32> {
    let mut grid = get_grid(input);
    let guard = find_guard(input);
    let mut res = 0;
    // Brute-force trying to place the obstacle at each position works but it is slow.
    for cell in get_visited_cells(&grid, &guard) {
        // Update the cell to be an obstacle.
        grid.entry(cell).and_modify(|c| *c = '#');
        // Does an obstacle here generate a cycle?
        if has_cycle(&grid, &guard) {
            res += 1;
        }
        // Backtrack, '.' and '^' are equivalent once we find the guard.
        grid.entry(cell).and_modify(|c| *c = '.');
    }
    Some(res)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(41));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(6));
    }
}
