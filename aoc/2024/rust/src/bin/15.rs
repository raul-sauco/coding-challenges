advent_of_code::solution!(15);

use std::collections::HashMap;

use glam::IVec2;

#[derive(Debug, PartialEq)]
enum Cell {
    Wall,
    Box,
    Robot,
    Empty,
}

impl Cell {
    fn from_char(c: char) -> Self {
        match c {
            '#' => Cell::Wall,
            'O' => Cell::Box,
            '@' => Cell::Robot,
            _ => Cell::Empty,
        }
    }
}

#[derive(Debug)]
enum Dir {
    N,
    E,
    S,
    W,
}

impl Dir {
    fn from_char(c: char) -> Self {
        match c {
            '^' => Self::N,
            '>' => Self::E,
            'v' => Self::S,
            '<' => Self::W,
            _ => panic!("Bad direction {c}"),
        }
    }
}

fn parse_grid(input: &str) -> HashMap<IVec2, Cell> {
    input
        .lines()
        .enumerate()
        .flat_map(|(y, line)| {
            line.chars()
                .enumerate()
                .filter(|(_, c)| *c != '.')
                .map(move |(x, c)| (IVec2::new(x as i32, y as i32), Cell::from_char(c)))
        })
        .collect::<HashMap<_, _>>()
}

fn parse_moves(input: &str) -> Vec<Dir> {
    input
        .chars()
        .filter(|c| *c != '\n')
        .map(Dir::from_char)
        .collect()
}

fn parse_input(input: &str) -> (HashMap<IVec2, Cell>, Vec<Dir>) {
    let mut sp = input.split("\n\n");
    let grid = parse_grid(sp.next().unwrap());
    let moves = parse_moves(sp.next().unwrap());
    (grid, moves)
}

fn make_move(current_position: &IVec2, grid: &mut HashMap<IVec2, Cell>, dir: Dir) -> IVec2 {
    let v = match dir {
        Dir::N => IVec2::NEG_Y,
        Dir::E => IVec2::X,
        Dir::S => IVec2::Y,
        Dir::W => IVec2::NEG_X,
    };
    if let Some(c) = grid.get(&(current_position + v)) {
        match c {
            Cell::Box => {
                let first_box = current_position + v;
                for i in 2..50 {
                    let dest = current_position + v * i;
                    match grid.get(&dest) {
                        Some(dest_content) => {
                            match dest_content {
                                Cell::Wall => {
                                    return *current_position;
                                }
                                Cell::Box => continue,
                                _ => {
                                    // We found an empty cell.
                                    grid.insert(dest, Cell::Box);
                                    grid.remove(&first_box);
                                    return first_box;
                                }
                            }
                        }
                        None => {
                            // We found an empty cell.
                            grid.insert(dest, Cell::Box);
                            grid.remove(&first_box);
                            return first_box;
                        }
                    }
                }
            }
            Cell::Wall => {
                return *current_position;
            }
            _ => {
                return current_position + v;
            }
        }
    } else {
        // The destination cell is free.
        return current_position + v;
    }
    unreachable!("Should have returned next position")
}

pub fn part_one(input: &str) -> Option<u32> {
    let (mut grid, moves) = parse_input(input);
    let (start, _) = grid.iter().find(|(_, v)| **v == Cell::Robot).unwrap();
    let mut current_position = *start;
    grid.remove(&current_position);
    for dir in moves {
        current_position = make_move(&current_position, &mut grid, dir);
    }
    Some(
        grid.iter()
            .map(|(k, v)| if *v == Cell::Box { 100 * k.y + k.x } else { 0 })
            .sum::<i32>() as _,
    )
}

// TODO: Day 15 part 2
pub fn part_two(_input: &str) -> Option<u32> {
    None
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case(
        r#"########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"#,
        Some(2028); "Small grid"
    )]
    #[test_case(
        r#"##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"#,
        Some(10092); "Large grid"
    )]
    fn test_part_one(input: &str, expected: Option<u32>) {
        let result = part_one(input);
        assert_eq!(result, expected);
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
