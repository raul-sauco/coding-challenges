use bitvec::prelude::*;
use nom::{
    IResult, Parser,
    branch::alt,
    bytes::complete::tag,
    character::complete::{char, line_ending, u16},
    combinator::map,
    multi::separated_list1,
};

advent_of_code::solution!(6);

#[derive(Debug)]
struct Op {
    action: Action,
    top: usize,
    right: usize,
    bottom: usize,
    left: usize,
}

#[derive(Debug)]
enum Action {
    On,
    Off,
    Toggle,
}

impl Action {
    fn new(input: &str) -> Action {
        match input {
            "turn on" => Self::On,
            "turn off" => Self::Off,
            "toggle" => Self::Toggle,
            _ => panic!("Cannot use Action {input}"),
        }
    }
}

fn parser(input: &str) -> IResult<&str, Vec<Op>> {
    separated_list1(line_ending, op).parse(input)
}

fn op(input: &str) -> IResult<&str, Op> {
    map(
        (
            alt([tag("turn on"), tag("turn off"), tag("toggle")]),
            char(' '),
            u16,
            char(','),
            u16,
            tag(" through "),
            u16,
            char(','),
            u16,
        ),
        |(action, _, left, _, top, _, right, _, bottom)| Op {
            action: Action::new(action),
            top: top as usize,
            right: right as usize,
            bottom: bottom as usize,
            left: left as usize,
        },
    )
    .parse(input)
}

// Part 1: 377891 (5.1ms @ 186 samples)
pub fn part_one(input: &str) -> Option<usize> {
    let (_, ops) = parser.parse(input).expect("a good parse");
    let mut grid: [BitVec; 1000] = std::array::from_fn(|_| bitvec![0; 1000]);
    let mut mask = bitvec![0; 1000];
    for op in ops {
        for row in grid[op.top..=op.bottom].iter_mut() {
            match op.action {
                Action::On => row[op.left..=op.right].fill(true),
                Action::Off => row[op.left..=op.right].fill(false),
                Action::Toggle => {
                    mask.fill(false);
                    mask[op.left..=op.right].fill(true);
                    *row ^= &mask;
                }
            }
        }
    }
    Some(grid.iter().map(|bv| bv.count_ones()).sum())
}

// Part 2: 14110788 (7.2ms @ 119 samples)
pub fn part_two(input: &str) -> Option<usize> {
    let (_, ops) = parser.parse(input).expect("a good parse");
    let mut grid: [Vec<usize>; 1000] = std::array::from_fn(|_| vec![0; 1000]);
    for op in ops {
        for row in grid[op.top..=op.bottom].iter_mut() {
            match op.action {
                Action::On => row[op.left..=op.right].iter_mut().for_each(|led| *led += 1),
                Action::Off => row[op.left..=op.right].iter_mut().for_each(|led| {
                    if *led > 0 {
                        *led -= 1
                    }
                }),
                Action::Toggle => row[op.left..=op.right].iter_mut().for_each(|led| *led += 2),
            }
        }
    }
    Some(grid.iter().map(|v| v.iter().sum::<usize>()).sum())
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        "turn on 887,9 through 959,629
turn on 454,398 through 844,448
turn off 539,243 through 500059,965
turn off 370,819 through 676,868
turn off 145,40 through 370,997
turn off 301,3 through 808,453
turn on 351,678 through 951,908
",
        65274
    )]
    fn test_part_one(#[case] input: &str, #[case] expected: usize) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
