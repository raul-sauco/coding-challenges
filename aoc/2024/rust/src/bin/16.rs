advent_of_code::solution!(16);

use std::collections::{BinaryHeap, HashSet};

use glam::IVec2;

#[derive(Debug, PartialEq, Eq, Clone, Hash)]
struct Point {
    x: usize,
    y: usize,
}

impl Point {
    fn new(x: usize, y: usize) -> Self {
        Self { x, y }
    }
}

#[derive(Debug, Eq, PartialEq)]
struct Reindeer {
    cost: u32,
    position: Point,
    direction: IVec2,
    path: HashSet<Point>,
}

impl Ord for Reindeer {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        // Reverse the comparison to use in a max-heap
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for Reindeer {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(other.cost.cmp(&self.cost))
    }
}

impl Reindeer {
    fn make_move(&self) -> Self {
        let next_position = Point::new(
            (self.position.x as i32 + self.direction.x) as usize,
            (self.position.y as i32 + self.direction.y) as usize,
        );
        let mut next_path = self.path.clone();
        next_path.insert(next_position.clone());
        Self {
            cost: self.cost + 1,
            position: next_position,
            direction: self.direction,
            path: next_path,
        }
    }

    fn turn_90(&self) -> Self {
        Self {
            cost: self.cost + 1000,
            position: self.position.clone(),
            direction: IVec2 {
                x: -self.direction.y,
                y: self.direction.x,
            },
            path: self.path.clone(),
        }
    }

    fn turn_neg_90(&self) -> Self {
        Self {
            cost: self.cost + 1000,
            position: self.position.clone(),
            direction: IVec2 {
                x: self.direction.y,
                y: -self.direction.x,
            },
            path: self.path.clone(),
        }
    }

    fn dir_to_idx(&self) -> usize {
        match self.direction {
            IVec2::X => 0,
            IVec2::Y => 1,
            IVec2::NEG_X => 2,
            IVec2::NEG_Y => 3,
            _ => panic!("Invalid direction {:?}", self.direction),
        }
    }
}

fn parse_input(input: &str) -> Vec<Vec<char>> {
    let mut grid = vec![];
    let mut line = vec![];
    for c in input.chars() {
        match c {
            '#' | '.' | 'S' | 'E' => line.push(c),
            '\n' => {
                grid.push(line.clone());
                line.clear();
            }
            _ => panic!("Wrong character {c}"),
        }
    }
    grid.push(line);
    grid
}

fn find_start_end(grid: &[Vec<char>]) -> (Point, Point) {
    let (mut start, mut end) = (Point::new(0, 0), Point::new(0, 0));
    for (y, row) in grid.iter().enumerate() {
        for (x, c) in row.iter().enumerate() {
            if *c == 'S' {
                start = Point::new(x, y);
            }
            if *c == 'E' {
                end = Point::new(x, y);
            }
        }
    }
    (start, end)
}

pub fn part_one(input: &str) -> Option<u32> {
    let grid = parse_input(input);
    let (start, _end) = find_start_end(&grid);
    let mut visited = vec![vec![[u32::MAX; 4]; grid[0].len()]; grid.len()];
    let mut heap = BinaryHeap::from([Reindeer {
        cost: 0,
        position: start.clone(),
        direction: IVec2::X,
        path: HashSet::from([start]),
    }]);
    while let Some(reindeer) = heap.pop() {
        if visited[reindeer.position.y][reindeer.position.x][reindeer.dir_to_idx()] != u32::MAX {
            continue;
        } else {
            visited[reindeer.position.y][reindeer.position.x][reindeer.dir_to_idx()] =
                reindeer.cost;
        }
        match grid[reindeer.position.y][reindeer.position.x] {
            '#' => continue,
            'E' => return Some(reindeer.cost),
            _ => {
                heap.push(reindeer.make_move());
                heap.push(reindeer.turn_90());
                heap.push(reindeer.turn_neg_90());
            }
        }
    }
    unreachable!("The loop should return a value")
}

#[allow(dead_code)]
fn debug_grid(grid: &[Vec<char>], best_cells: &HashSet<Point>) {
    for (y, row) in grid.iter().enumerate() {
        for (x, c) in row.iter().enumerate() {
            let p = Point::new(x, y);
            if best_cells.contains(&p) {
                print!("O");
            } else {
                print!("{c}");
            }
        }
        println!();
    }
}

pub fn part_two(input: &str) -> Option<u32> {
    let grid = parse_input(input);
    let (start, _end) = find_start_end(&grid);
    let mut visited = vec![vec![[u32::MAX; 4]; grid[0].len()]; grid.len()];
    let mut heap = BinaryHeap::from([Reindeer {
        cost: 0,
        position: start.clone(),
        direction: IVec2::X,
        path: HashSet::from([start]),
    }]);
    let mut cells_in_best_paths = HashSet::new();
    let mut best_cost = None;
    while let Some(reindeer) = heap.pop() {
        if best_cost.is_some_and(|cost| cost < reindeer.cost) {
            break;
        }
        // TODO: Updating the comparisson to <= speeds up the execution from 40s to 50ms but it
        // gives 465 instead of the expected 494, check why.
        if visited[reindeer.position.y][reindeer.position.x][reindeer.dir_to_idx()] < reindeer.cost
        {
            continue;
        } else {
            visited[reindeer.position.y][reindeer.position.x][reindeer.dir_to_idx()] =
                reindeer.cost;
        }
        match grid[reindeer.position.y][reindeer.position.x] {
            '#' => continue,
            'E' => {
                // Current cost <= best_cost, rewrite.
                best_cost.get_or_insert(reindeer.cost);
                cells_in_best_paths.extend(reindeer.path);
            }
            _ => {
                heap.push(reindeer.make_move());
                heap.push(reindeer.turn_90());
                heap.push(reindeer.turn_neg_90());
            }
        }
    }
    // debug_grid(&grid, &cells_in_best_paths);
    Some(cells_in_best_paths.len() as u32)
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case(
        r#"###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"#,
        Some(7036)
    )]
    #[test_case(
        r#"#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"#,
        Some(11048)
    )]
    fn test_part_one(input: &str, expected: Option<u32>) {
        assert_eq!(part_one(input), expected);
    }

    #[test_case(
        r#"###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"#,
        Some(45)
    )]
    #[test_case(
        r#"#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"#,
        Some(64)
    )]
    fn test_part_two(input: &str, expected: Option<u32>) {
        assert_eq!(part_two(input), expected);
    }
}
