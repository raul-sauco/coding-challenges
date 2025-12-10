use nom::{
    IResult, Parser,
    bytes::complete::tag,
    character::complete::{self},
    combinator::map,
    multi::separated_list1,
    sequence::separated_pair,
};
use rayon::iter::{IntoParallelIterator, ParallelIterator};

advent_of_code::solution!(2);

#[derive(Debug)]
struct Interval {
    start: u64,
    end: u64,
}

impl Interval {
    fn new(start: u64, end: u64) -> Self {
        Self { start, end }
    }
}

fn interval(input: &str) -> IResult<&str, Interval> {
    map(
        separated_pair(complete::u64, tag("-"), complete::u64),
        |(s, e)| Interval::new(s, e),
    )
    .parse(input)
}

fn intervals(input: &str) -> IResult<&str, Vec<Interval>> {
    separated_list1(tag(","), interval).parse(input)
}

// Part 1: 23560874270 (1.0ms @ 531 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, intervals) = intervals.parse(input).expect("a good parse");
    Some(
        intervals
            .into_par_iter()
            .flat_map(|interval| interval.start..=interval.end)
            .filter(|num| {
                let split = 10u64.pow(num.ilog10().div_ceil(2));
                num / split == num % split
            })
            .sum::<u64>(),
    )
}

pub fn part_two(input: &str) -> Option<u64> {
    let (_, intervals) = intervals.parse(input).expect("a good parse");
    Some(
        intervals
            .into_par_iter()
            .flat_map(|interval| interval.start..=interval.end)
            .map(|num| {
                let str = num.to_string();
                let half = str.len() / 2;
                // Test all the sizes, if any match, add the id
                for size in 0..half {
                    // If the num size is not divisible by the length we are testing
                    if str.len().rem_euclid(size + 1) != 0 {
                        continue;
                    }
                    let all_match = str[0..=size]
                        .chars()
                        .cycle()
                        .zip(str.chars())
                        .all(|(a, b)| a == b);
                    if all_match {
                        return num;
                    }
                }
                0
            })
            .sum::<u64>(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(1227775554));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4174379265));
    }
}
