advent_of_code::solution!(14);

use glam::{u32, IVec2};
use nom::{
    bytes::complete::tag,
    character::complete::{char, i32, newline, space1},
    combinator::map,
    multi::separated_list1,
    sequence::{preceded, separated_pair},
    IResult,
};

#[derive(Debug, PartialEq, Clone, Copy)]
struct Robot {
    position: IVec2,
    velocity: IVec2,
}

impl Robot {
    fn get_position_after_t_seconds(&self, t: i32, grid_size: IVec2) -> IVec2 {
        // let x = circular_index(num_cols, self.position.x + self.velocity.x * t);
        // let y = circular_index(num_rows, self.position.y + self.velocity.y * t);
        // IVec2::new(
        //     (self.position.x + self.velocity.x * t).rem_euclid(num_cols),
        //     (self.position.y + self.velocity.y * t).rem_euclid(num_rows),
        // )
        (self.position + self.velocity * t).rem_euclid(grid_size)
    }
}

#[allow(dead_code)]
fn circular_index(len: i32, index: i32) -> i32 {
    ((index % len) + len) % len
}

#[derive(Debug)]
enum Quadrant {
    NE,
    SE,
    SW,
    NW,
}

fn get_cuadrant(position: IVec2, grid_size: IVec2) -> Option<Quadrant> {
    let (x, y) = (grid_size.x / 2, grid_size.y / 2);
    match (position.x.cmp(&x), position.y.cmp(&y)) {
        (std::cmp::Ordering::Less, std::cmp::Ordering::Less) => Some(Quadrant::NW),
        (std::cmp::Ordering::Less, std::cmp::Ordering::Greater) => Some(Quadrant::SW),
        (std::cmp::Ordering::Greater, std::cmp::Ordering::Less) => Some(Quadrant::NE),
        (std::cmp::Ordering::Greater, std::cmp::Ordering::Greater) => Some(Quadrant::SE),
        _ => None,
    }
}

fn parse_vector(input: &str) -> IResult<&str, IVec2> {
    map(separated_pair(i32, char(','), i32), |(x, y)| {
        IVec2::new(x, y)
    })(input)
}

fn parse_robot(input: &str) -> IResult<&str, Robot> {
    separated_pair(
        preceded(tag("p="), parse_vector),
        space1,
        preceded(tag("v="), parse_vector),
    )(input)
    .map(|(rem, (position, velocity))| (rem, Robot { position, velocity }))
}

fn parse(input: &str) -> IResult<&str, Vec<Robot>> {
    separated_list1(newline, parse_robot)(input)
}

const GRID_SIZE: IVec2 = if cfg!(test) {
    IVec2::new(11, 7)
} else {
    IVec2::new(101, 103)
};

pub fn part_one(input: &str) -> Option<u32> {
    let (_, robots) = parse(input).unwrap();
    let robots_per_quadrant = robots
        .iter()
        .map(|r| r.get_position_after_t_seconds(100, GRID_SIZE))
        .fold([0; 4], |mut acc, position| {
            match get_cuadrant(position, GRID_SIZE) {
                Some(Quadrant::NE) => {
                    acc[0] += 1;
                    acc
                }
                Some(Quadrant::SE) => {
                    acc[1] += 1;
                    acc
                }
                Some(Quadrant::SW) => {
                    acc[2] += 1;
                    acc
                }
                Some(Quadrant::NW) => {
                    acc[3] += 1;
                    acc
                }
                None => acc,
            }
        });
    Some(robots_per_quadrant.into_iter().product::<u32>())
}

// 7623
pub fn part_two(input: &str) -> Option<u32> {
    let (_, robots) = parse(input).unwrap();
    let mut positions = [false; 10650];
    'times: for t in 1..10000 {
        positions.fill(false);
        // positions.clear();
        // if robots
        //     .iter()
        //     .map(|r| (r.position + r.velocity * t).rem_euclid(GRID_SIZE))
        //     .unique()
        //     .count()
        //     == robots.len()
        // {
        //     return Some(t as _);
        // }

        // Iterator + unique 71ms
        // for loop + hashset 32ms
        // for loop + array 2.7ms
        for pos in robots
            .iter()
            .map(|r| r.get_position_after_t_seconds(t, GRID_SIZE))
        {
            if positions[(pos.y * GRID_SIZE.y + pos.x) as usize] {
                continue 'times;
            }
            positions[(pos.y * GRID_SIZE.y + pos.x) as usize] = true;
        }
        return Some(t as _);
    }
    None
}

#[allow(dead_code)]
fn debug_grid(robots: Vec<Robot>, num_cols: i32, num_rows: i32) {
    dbg!(num_cols, num_rows);
    let mut grid = vec![vec!['.'; num_cols as usize]; num_rows as usize];
    dbg!(grid.len(), grid[0].len());
    for r in robots.into_iter() {
        grid[r.position.y as usize][r.position.x as usize] = '#';
    }
    grid.iter().for_each(|r| {
        r.iter().for_each(|c| print!("{c}"));
        println!();
    });
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(12));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }

    #[test_case("p=9,3 v=2,3",Robot {
        position: IVec2::new(9, 3),
        velocity: IVec2::new(2, 3)
    }; "Robot 1" )]
    #[test_case("p=7,6 v=-1,-3",Robot {
        position: IVec2::new(7, 6),
        velocity: IVec2::new(-1, -3)
    }; "Robot 2" )]
    fn test_parse_robot(input: &str, expected: Robot) {
        let (_, result) = parse_robot(input).unwrap();
        assert_eq!(result, expected);
    }

    #[test_case("p=2,4 v=2,-3", 0, IVec2::new(2, 4); "t 0" )]
    #[test_case("p=2,4 v=2,-3", 1, IVec2::new(4, 1); "t 1" )]
    #[test_case("p=2,4 v=2,-3", 2, IVec2::new(6, 5); "t 2" )]
    #[test_case("p=2,4 v=2,-3", 3, IVec2::new(8, 2); "t 3" )]
    #[test_case("p=2,4 v=2,-3", 4, IVec2::new(10, 6); "t 4" )]
    #[test_case("p=2,4 v=2,-3", 5, IVec2::new(1, 3); "t 5" )]
    fn test_position_after_t(robot_str: &str, t: i32, expected: IVec2) {
        let (_, robot) = parse_robot(robot_str).unwrap();
        assert_eq!(robot.get_position_after_t_seconds(t, GRID_SIZE), expected);
    }
}
