use std::ops::RangeInclusive;

use nom::{
    IResult, Parser,
    bytes::complete::tag,
    character::complete::{self, char, line_ending},
    multi::separated_list1,
    sequence::separated_pair,
};

advent_of_code::solution!(5);

fn parser(input: &str) -> IResult<&str, (Vec<RangeInclusive<u64>>, Vec<u64>)> {
    separated_pair(ranges, tag("\n\n"), ingredients).parse(input)
}

fn ranges(input: &str) -> IResult<&str, Vec<RangeInclusive<u64>>> {
    separated_list1(line_ending, range).parse(input)
}

fn range(input: &str) -> IResult<&str, RangeInclusive<u64>> {
    separated_pair(complete::u64, char('-'), complete::u64)
        .map(|(start, end)| start..=end)
        .parse(input)
}

fn ingredients(input: &str) -> IResult<&str, Vec<u64>> {
    separated_list1(line_ending, complete::u64).parse(input)
}

fn merge_ranges(ranges: &mut [RangeInclusive<u64>]) -> Vec<RangeInclusive<u64>> {
    if ranges.is_empty() {
        return vec![];
    }
    ranges.sort_by(|a, b| a.start().cmp(b.start()).then(a.end().cmp(b.end())));
    let mut res = vec![ranges[0].clone()];
    for range in &ranges[1..] {
        let last = res.last_mut().expect("non-empty res");
        if range.start() <= last.end() {
            *last = *last.start()..=(*range.end().max(last.end()));
        } else {
            res.push(range.clone());
        }
    }
    res
}

fn in_any_range(ranges: &[RangeInclusive<u64>], ingredient: u64) -> bool {
    ranges
        .binary_search_by(|r| {
            if ingredient < *r.start() {
                std::cmp::Ordering::Greater
            } else if ingredient > *r.end() {
                std::cmp::Ordering::Less
            } else {
                std::cmp::Ordering::Equal
            }
        })
        .is_ok()
}

// Part 1: 511 (33.4µs)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, (mut ranges, ingredients)) = parser.parse(input).expect("a good parse");
    ranges = merge_ranges(&mut ranges);
    Some(
        ingredients
            .into_iter()
            .filter(|&ing| in_any_range(&ranges, ing))
            .count() as _,
    )
}

// Part 2: 350939902751909 (20.8µs)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, (mut ranges, _ingredients)) = parser.parse(input).expect("a good parse");
    ranges = merge_ranges(&mut ranges);
    Some(
        ranges
            .into_iter()
            // .inspect(|range| println!("{:?}::{}", range, *range.end() - *range.start() + 1))
            .map(|range| *range.end() - *range.start() + 1)
            .sum::<u64>(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(14));
    }
}
