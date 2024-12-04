advent_of_code::solution!(4);

use glam::{i32, IVec2};
use std::collections::HashMap;

/**
 * Display the 9 characters in the matrix centered around the given position.
*/
#[allow(dead_code)]
fn get_graph(matrix: &HashMap<IVec2, char>, pos: &IVec2) -> String {
    let mut graph = String::with_capacity(12);
    for y in -1..=1 {
        for x in -1..=1 {
            let offset = IVec2::new(x, y);
            if let Some(char) = matrix.get(&(*pos + offset)) {
                graph.push(*char);
            } else {
                graph.push('.');
            }
        }
        graph.push('\n');
    }
    graph
}

fn parse(input: &str) -> HashMap<IVec2, char> {
    let mut grid = HashMap::new();
    for (y, line) in input.lines().enumerate() {
        for (x, char) in line.chars().enumerate() {
            grid.insert(
                IVec2 {
                    x: x as i32,
                    y: y as i32,
                },
                char,
            );
        }
    }
    grid
}

/* ********************************** PART ONE *******************************/

const DIRECTIONS: [IVec2; 8] = [
    IVec2::new(0, -1),
    IVec2::new(0, 1),
    IVec2::new(-1, 0),
    IVec2::new(1, 0),
    IVec2::new(-1, -1),
    IVec2::new(1, -1),
    IVec2::new(-1, 1),
    IVec2::new(1, 1),
];

fn find_xmas(matrix: &HashMap<IVec2, char>, pos: IVec2) -> u32 {
    let target = "XMAS";
    let mut res = 0;
    let mut is_match;
    for dir in DIRECTIONS {
        is_match = true;
        for (i, c) in target.chars().enumerate() {
            if let Some(cell) = matrix.get(&(pos + dir * i as i32)) {
                if *cell != c {
                    is_match = false;
                    break;
                }
            } else {
                is_match = false;
                break;
            }
        }
        if is_match {
            res += 1;
        }
    }
    res
}

pub fn part_one(input: &str) -> Option<u32> {
    let matrix = parse(input);
    Some(matrix.keys().map(|k| find_xmas(&matrix, *k)).sum::<u32>())
}

/* ********************************** PART TWO *******************************/

const DIRECTIONS_X: [[IVec2; 2]; 2] = [
    [IVec2::new(-1, -1), IVec2::new(1, 1)],
    [IVec2::new(-1, 1), IVec2::new(1, -1)],
];

/**
* Find if the given coordinates in the matrix are at the center of a X-MAs group of cells, for that
* to be true, both diagonals need to form "MAS" or "SAM", given that main will call this method
* only when the char at pos is 'A', we only need to check that the oppossing corners are either SM
* or MS.
*/
fn is_x_mas_match(matrix: &HashMap<IVec2, char>, pos: &IVec2) -> bool {
    let (ms, sm) = ("MS".to_string(), "SM".to_string());
    let mut diagonal_chars = String::with_capacity(2);
    for diagonal in DIRECTIONS_X {
        diagonal_chars.clear();
        for offset in diagonal {
            if let Some(c) = matrix.get(&(pos + offset)) {
                diagonal_chars.push(*c);
            } else {
                return false;
            }
        }
        if diagonal_chars != ms && diagonal_chars != sm {
            return false;
        }
    }
    true
}

pub fn part_two(input: &str) -> Option<u32> {
    let matrix = parse(input);
    Some(
        matrix
            .iter()
            .filter(|&(pos, val)| *val == 'A' && is_x_mas_match(&matrix, pos))
            .count() as u32,
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(18));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(9));
    }
}
