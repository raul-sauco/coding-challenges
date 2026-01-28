use nom::{
    IResult, Parser,
    branch::alt,
    bytes::complete::tag,
    character::complete::{self, alpha1, char, line_ending},
    combinator::map,
    multi::separated_list1,
};

advent_of_code::solution!(23);

#[derive(Debug)]
enum Instruction {
    Hlf { reg: bool },
    Tpl { reg: bool },
    Inc { reg: bool },
    Jmp { offset: i8 },
    Jie { reg: bool, offset: i8 },
    Jio { reg: bool, offset: i8 },
}

fn parser(input: &str) -> IResult<&str, Vec<Instruction>> {
    separated_list1(line_ending, instruction).parse(input)
}

fn instruction(input: &str) -> IResult<&str, Instruction> {
    alt((
        map((tag("hlf "), alpha1), |(_, r)| Instruction::Hlf {
            reg: r == "a",
        }),
        map((tag("tpl "), alpha1), |(_, r)| Instruction::Tpl {
            reg: r == "a",
        }),
        map((tag("inc "), alpha1), |(_, r)| Instruction::Inc {
            reg: r == "a",
        }),
        map((tag("jmp "), signed_i8), |(_, offset)| Instruction::Jmp {
            offset,
        }),
        map(
            (tag("jie "), alpha1, tag(", "), signed_i8),
            |(_, r, _, offset)| Instruction::Jie {
                reg: r == "a",
                offset,
            },
        ),
        map(
            (tag("jio "), alpha1, tag(", "), signed_i8),
            |(_, r, _, offset)| Instruction::Jio {
                reg: r == "a",
                offset,
            },
        ),
    ))
    .parse(input)
}

fn signed_i8(input: &str) -> IResult<&str, i8> {
    map(
        (alt((char('+'), char('-'))), complete::i8),
        |(sign, num)| {
            if sign == '+' { num } else { -num }
        },
    )
    .parse(input)
}

// Part 1: 170 (2.0µs @ 10000 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, instructions) = parser.parse(input).expect("a good parse");
    Some(simulate(instructions, 0, 0))
}

// Part 2: 247 (2.8µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, instructions) = parser.parse(input).expect("a good parse");
    Some(simulate(instructions, 1, 0))
}

fn simulate(instructions: Vec<Instruction>, mut a: u64, mut b: u64) -> u64 {
    let (mut idx, len) = (0, instructions.len());
    loop {
        if idx >= len {
            return b;
        }
        match instructions[idx] {
            Instruction::Hlf { reg } => {
                if reg {
                    a /= 2;
                } else {
                    b /= 2;
                }
                idx += 1;
            }
            Instruction::Tpl { reg } => {
                if reg {
                    a *= 3;
                } else {
                    b *= 3;
                }
                idx += 1;
            }
            Instruction::Inc { reg } => {
                if reg {
                    a += 1;
                } else {
                    b += 1;
                }
                idx += 1;
            }
            Instruction::Jmp { offset } => idx += offset as usize,
            Instruction::Jie { reg, offset } => {
                if (reg && a.is_multiple_of(2)) || (!reg && b.is_multiple_of(2)) {
                    idx += offset as usize;
                } else {
                    idx += 1;
                }
            }
            Instruction::Jio { reg, offset } => {
                if (reg && a == 1) || (!reg && b == 1) {
                    idx += offset as usize;
                } else {
                    idx += 1;
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
