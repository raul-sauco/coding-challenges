use nom::{
    IResult, Parser,
    character::complete::{char, line_ending, u64},
    combinator::map,
    multi::separated_list1,
};

advent_of_code::solution!(2);

#[derive(Debug)]
struct Box {
    length: u64,
    width: u64,
    height: u64,
}

impl Box {
    fn wrap(&self) -> u64 {
        let (lw, lh, wh) = (
            self.length * self.width,
            self.length * self.height,
            self.width * self.height,
        );
        2 * (lw + lh + wh) + lw.min(lh.min(wh))
    }

    fn ribbon(&self) -> u64 {
        let mut per = [self.length, self.width, self.height];
        per.sort_unstable();
        self.length * self.width * self.height + 2 * (per[0] + per[1])
    }
}

fn parser(input: &str) -> IResult<&str, Vec<Box>> {
    separated_list1(line_ending, gift_box).parse(input)
}

fn gift_box(input: &str) -> IResult<&str, Box> {
    map(
        (u64, char('x'), u64, char('x'), u64),
        |(length, _, width, _, height)| Box {
            length,
            width,
            height,
        },
    )
    .parse(input)
}

// Part 1: 1606483 (21.0µs @ 10000 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, boxes) = parser.parse(input).expect("a good parse");
    Some(boxes.iter().map(|b| b.wrap()).sum::<u64>())
}

// Part 2: 3842356 (22.2µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, boxes) = parser.parse(input).expect("a good parse");
    Some(boxes.iter().map(|b| b.ribbon()).sum::<u64>())
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        "2x3x4
1x1x10",
        101
    )]
    fn test_part_one(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[rstest]
    #[case(
        "2x3x4
1x1x10",
        48
    )]
    fn test_part_two(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_two(input), Some(expected));
    }
}
