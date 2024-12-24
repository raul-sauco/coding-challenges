use std::{collections::HashSet, u32};

use nom::{
    bytes::complete::tag,
    character::complete::{char, digit1},
    combinator::{map, map_res},
    multi::separated_list1,
    sequence::{preceded, separated_pair, tuple},
    IResult,
};

advent_of_code::solution!(17);

#[derive(Debug, Clone)]
struct Register {
    a: u32,
    b: u32,
    c: u32,
}

fn parse_input(input: &str) -> IResult<&str, (Register, Vec<u32>)> {
    separated_pair(parse_registers, tag("\n\n"), parse_instructions)(input)
}

fn parse_registers(input: &str) -> IResult<&str, Register> {
    map(
        tuple((
            preceded(tag("Register A: "), map_res(digit1, str::parse)),
            preceded(tag("\nRegister B: "), map_res(digit1, str::parse)),
            preceded(tag("\nRegister C: "), map_res(digit1, str::parse)),
        )),
        |(a, b, c)| Register { a, b, c },
    )(input)
}

fn parse_instructions(input: &str) -> IResult<&str, Vec<u32>> {
    preceded(tag("Program: "), separated_list1(char(','), parse_number))(input)
}

fn parse_number(input: &str) -> IResult<&str, u32> {
    map_res(digit1, str::parse)(input)
}

fn get_combo_value(combo: u32, reg: &Register) -> u32 {
    match combo {
        0 | 1 | 2 | 3 => combo,
        4 => reg.a,
        5 => reg.b,
        6 => reg.c,
        _ => panic!("Invalid combo value {combo}"),
    }
}

fn solve(mut reg: Register, instructions: &Vec<u32>) -> Option<String> {
    let (mut i, n) = (0, instructions.len());
    let mut res = vec![];
    let mut seen = HashSet::new();
    while i < n - 1 {
        let (opcode, operand) = (instructions[i], instructions[i + 1]);
        let key = (reg.a, reg.b, reg.c, i);
        if seen.contains(&key) {
            return None;
        }
        seen.insert(key);
        match opcode {
            0 => reg.a = reg.a / 2u32.pow(get_combo_value(operand, &reg)),
            1 => reg.b ^= operand,
            2 => reg.b = get_combo_value(operand, &reg) % 8,
            3 => {
                if reg.a != 0 {
                    i = operand as usize;
                    continue;
                }
            }
            4 => reg.b ^= reg.c,
            5 => res.push((get_combo_value(operand, &reg) % 8).to_string()),
            6 => reg.b = reg.a / 2u32.pow(get_combo_value(operand, &reg)),
            7 => reg.c = reg.a / 2u32.pow(get_combo_value(operand, &reg)),
            _ => panic!("Invalid operand {operand}"),
        }
        i += 2;
    }
    Some(res.join(","))
}

pub fn part_one(input: &str) -> Option<String> {
    let (_, (reg, instructions)) = parse_input(input).unwrap();
    solve(reg, &instructions)
}

// TODO: Brute force is too slow to give a result, find a different method.
pub fn part_two(input: &str) -> Option<u32> {
    let (_, (reg, instructions)) = parse_input(input).unwrap();
    let expected = instructions
        .iter()
        .map(|num| num.to_string())
        .collect::<Vec<_>>()
        .join(",");
    let mut i = 0;
    loop {
        if solve(
            Register {
                a: i,
                b: reg.b,
                c: reg.c,
            },
            &instructions,
        )
        .is_some_and(|x| x == expected)
        {
            return Some(i);
        }
        i += 1;
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case(r#"Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"#,
            "4,6,3,5,6,3,5,2,1,0".to_string())]
    fn test_part_one(input: &str, expected: String) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[test_case(
        r#"Register A: 729
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"#,
        117440
    )]
    fn test_part_two(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }
}
