advent_of_code::solution!(7);

use nom::{
    bytes::complete::tag,
    character::complete::{digit1, newline, space1},
    combinator::map_res,
    multi::separated_list1,
    sequence::separated_pair,
    IResult,
};
use rayon::iter::*;

#[derive(Debug)]
struct Operation {
    expected: usize,
    operands: Vec<usize>,
}

impl Operation {
    fn is_viable(&self, with_concat: bool) -> bool {
        self.dfs(1, self.operands[0], with_concat)
    }

    fn dfs(&self, idx: usize, current_total: usize, with_concat: bool) -> bool {
        // Base case, we are out of operands
        if idx == self.operands.len() {
            return current_total == self.expected;
        }
        // Base case, we have gone over expected
        if current_total > self.expected {
            return false;
        }
        // Otherwise, try both sum and mul
        self.dfs(idx + 1, current_total + self.operands[idx], with_concat)
            || self.dfs(idx + 1, current_total * self.operands[idx], with_concat)
            || if with_concat {
                self.dfs(
                    idx + 1,
                    format!("{}{}", current_total, self.operands[idx])
                        .parse::<usize>()
                        .unwrap(),
                    with_concat,
                )
            } else {
                false
            }
    }
}

fn parse(input: &str) -> IResult<&str, Vec<Operation>> {
    separated_list1(newline, parse_operation)(input)
}

fn parse_usize(input: &str) -> IResult<&str, usize> {
    map_res(digit1, |s: &str| s.parse::<usize>())(input)
}

fn parse_operation(input: &str) -> IResult<&str, Operation> {
    let (input, (expected, operands)) =
        separated_pair(parse_usize, tag(": "), separated_list1(space1, parse_usize))(input)?;
    Ok((input, Operation { expected, operands }))
}

// Part 1: 5702958180383 (627.6µs) No Rayon
// Part 1: 5702958180383 (495.5µs) With Rayon's par_iter
pub fn part_one(input: &str) -> Option<u128> {
    let (remaining, operations) = parse(input).unwrap();
    assert_eq!(remaining, "\n");
    Some(
        operations
            .par_iter()
            .filter_map(|operation| {
                if operation.is_viable(false) {
                    Some(operation.expected as u128)
                } else {
                    None
                }
            })
            .sum(),
    )
}

// Part 2: 92612386119138 (222.2ms) No rayon.
// Part 2: 92612386119138 (64.5ms) With Rayon's par_iter.
pub fn part_two(input: &str) -> Option<u128> {
    let (_, operations) = parse(input).unwrap();
    Some(
        operations
            .par_iter()
            .filter_map(|operation| {
                if operation.is_viable(true) {
                    Some(operation.expected as u128)
                } else {
                    None
                }
            })
            .sum(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3749));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(11387));
    }
}
