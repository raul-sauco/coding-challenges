use nom::{
    IResult, Parser,
    branch::alt,
    bytes::complete::tag,
    character::complete::{self, newline},
    combinator::map,
    multi::separated_list1,
};

advent_of_code::solution!(1);

fn rotation(input: &str) -> IResult<&str, i32> {
    alt((
        map(tag("L").and(complete::i32), |(_, n)| -n),
        map(tag("R").and(complete::i32), |(_, n)| n),
    ))
    .parse(input)
}

fn lines(input: &str) -> IResult<&str, Vec<i32>> {
    separated_list1(newline, rotation).parse(input)
}

const DIAL_SIZE: i32 = 100;
const START_POS: i32 = 50;

pub fn part_one(input: &str) -> Option<u64> {
    let (_, rotations) = lines.parse(input).expect("a good parse");
    Some(
        rotations
            .iter()
            .fold((START_POS, 0), |(dial, clicks), rotation| {
                let new_pos = (dial + rotation).rem_euclid(DIAL_SIZE);
                (new_pos, if new_pos == 0 { clicks + 1 } else { clicks })
            })
            .1,
    )
}

pub fn part_two(input: &str) -> Option<u64> {
    let (_, rotations) = lines.parse(input).expect("a good parse");
    Some(
        rotations
            .into_iter()
            .fold((START_POS, 0), |(dial, clicks), rotation| {
                let landing_pos = dial + rotation;
                let mut zero_hits = (landing_pos / DIAL_SIZE).abs();
                if dial != 0 && landing_pos <= 0 {
                    zero_hits += 1;
                }
                (landing_pos.rem_euclid(DIAL_SIZE), clicks + zero_hits)
            })
            .1 as u64,
    )
}

// cargo time
// Part 1: 1150 (35.8µs @ 10000 samples)
// Part 2: 6738 (42.6µs @ 10000 samples)

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(6));
    }
}
