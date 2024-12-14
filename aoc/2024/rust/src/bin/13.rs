advent_of_code::solution!(13);

use glam::{u32, IVec2};
use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::{digit1, newline},
    combinator::map_res,
    multi::separated_list1,
    sequence::{pair, preceded, tuple},
    IResult,
};

#[derive(Debug)]
struct ClawMachine {
    a: IVec2,
    b: IVec2,
    price: IVec2,
}

impl ClawMachine {
    // How many times do we need to press the a and b buttons to land in price.
    fn solve(&self) -> Option<IVec2> {
        let determinant = self.a.x * self.b.y - self.a.y * self.b.x;
        if determinant == 0 {
            // Prevent division by 0.
            return None;
        }
        let x = ((self.b.y * self.price.x - self.b.x * self.price.y) as f64 / determinant as f64)
            .round() as i32;
        let y = ((self.a.x * self.price.y - self.a.y * self.price.x) as f64 / determinant as f64)
            .round() as i32;
        // We need the number of times we press the buttons to result in exactly the price.
        if x * self.a + y * self.b == self.price {
            Some(IVec2::new(x, y))
        } else {
            None
        }
    }

    fn compute_cost(&self) -> Option<i64> {
        let addition = 10000000000000;
        // Cast to i64
        let (ax, ay) = (self.a.x as i64, self.a.y as i64);
        let (bx, by) = (self.b.x as i64, self.b.y as i64);
        // Cast the price position to i64 and add the extra offset.
        let (px, py) = (
            self.price.x as i64 + addition,
            self.price.y as i64 + addition,
        );
        // Same as "solve" but including the offset and using i64.
        let determinant = ax * by - ay * bx;
        if determinant == 0 {
            return None;
        }
        let a_pushes = ((by * px - bx * py) as f64 / determinant as f64).round() as i64;
        let b_pushes = ((ax * py - ay * px) as f64 / determinant as f64).round() as i64;
        // Only count exact hits to the price cell, ignore rounded values.
        if a_pushes * ax + b_pushes * bx == px && a_pushes * ay + b_pushes * by == py {
            Some(3 * a_pushes + b_pushes)
        } else {
            None
        }
    }
}

fn parse_line(input: &str) -> IResult<&str, IVec2> {
    tuple((
        alt((tag("Button A: "), tag("Button B: "), tag("Prize: "))),
        preceded(
            alt((tag("X+"), tag("X="))),
            map_res(digit1, str::parse::<i32>),
        ),
        preceded(
            alt((tag(", Y+"), tag(", Y="))),
            map_res(digit1, str::parse::<i32>),
        ),
    ))(input)
    .map(|(rem, (_, a, b))| (rem, IVec2::new(a, b)))
}

fn parse_claw_machine(input: &str) -> IResult<&str, ClawMachine> {
    separated_list1(newline, parse_line)(input).map(|(rem, v)| {
        (
            rem,
            ClawMachine {
                a: v[0],
                b: v[1],
                price: v[2],
            },
        )
    })
}

fn parse(input: &str) -> IResult<&str, Vec<ClawMachine>> {
    separated_list1(pair(newline, newline), parse_claw_machine)(input)
}

pub fn part_one(input: &str) -> Option<u32> {
    let (_rem, machines) = parse(input).unwrap();
    Some(
        machines
            .iter()
            .map(|machine| machine.solve().map_or(0, |sol| (3 * sol.x + sol.y) as u32))
            .sum(),
    )
}

pub fn part_two(input: &str) -> Option<i64> {
    let (_rem, machines) = parse(input).unwrap();
    Some(
        machines
            .iter()
            .map(|machine| machine.compute_cost().unwrap_or(0))
            .sum(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case(
        r#"Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"#,
        Some(480);
        "Input 1"
    )]
    fn test_part_one(input: &str, expected: Option<u32>) {
        assert_eq!(part_one(input), expected);
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
