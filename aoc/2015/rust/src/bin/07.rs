use std::collections::VecDeque;

use nom::{
    IResult, Parser,
    branch::alt,
    bytes::complete::tag,
    character::complete::{alpha1, alphanumeric1, char, line_ending},
    combinator::map,
    multi::separated_list1,
};
use rustc_hash::FxHashMap;

advent_of_code::solution!(7);

#[derive(Debug)]
struct Gate<'a> {
    a: Input<'a>,
    b: Input<'a>,
    out: &'a str,
    instruction: Instruction,
}

impl Gate<'_> {
    fn is_live(&self) -> bool {
        match self.instruction {
            Instruction::And | Instruction::OR => {
                matches!((&self.a, &self.b), (Input::Value(_), Input::Value(_)))
            }
            Instruction::Lshift | Instruction::Rshift | Instruction::Not | Instruction::Pass => {
                matches!(&self.a, Input::Value(_))
            }
        }
    }

    fn get_output(&self) -> u16 {
        match self.instruction {
            Instruction::And => self.a.get_value() & self.b.get_value(),
            Instruction::OR => self.a.get_value() | self.b.get_value(),
            Instruction::Lshift => self.a.get_value() << self.b.get_value(),
            Instruction::Rshift => self.a.get_value() >> self.b.get_value(),
            Instruction::Not => !self.a.get_value(),
            Instruction::Pass => self.a.get_value(),
        }
    }

    fn set_input(&mut self, name: &str, value: u16) {
        match (&self.a, &self.b) {
            (Input::Wire(wa), Input::Wire(wb)) => {
                if *wa == name {
                    self.a = Input::Value(value);
                } else if *wb == name {
                    self.b = Input::Value(value);
                } else {
                    panic!("Tried to set input {name} to {value} but not found");
                }
            }
            (Input::Wire(wa), Input::Value(_)) | (Input::Wire(wa), Input::None) => {
                if *wa == name {
                    self.a = Input::Value(value);
                } else {
                    panic!("Tried to set input {name} to {value} but not found");
                }
            }
            (Input::Value(_), Input::Wire(wb)) | (Input::None, Input::Wire(wb)) => {
                if *wb == name {
                    self.b = Input::Value(value);
                } else {
                    panic!("Tried to set input {name} to {value} but not found");
                }
            }
            _ => panic!("Tried to set input {name} to {value} but no input matched on this gate"),
        }
    }
}

#[derive(Debug)]
enum Input<'a> {
    Wire(&'a str),
    Value(u16),
    None,
}

impl Input<'_> {
    fn from_str(input: &'_ str) -> Input<'_> {
        match input.parse::<u16>() {
            Ok(num) => Input::Value(num),
            Err(_) => Input::Wire(input),
        }
    }

    fn get_value(&self) -> u16 {
        match self {
            Input::Wire(_) => panic!("Getting value on 'Wire' Input"),
            Input::Value(val) => *val,
            Input::None => panic!("Getting value on 'NONE' Input"),
        }
    }
}

#[derive(Debug)]
enum Instruction {
    And,
    OR,
    Lshift,
    Rshift,
    Not,
    Pass,
}

fn parser(input: &str) -> IResult<&str, Vec<Gate<'_>>> {
    separated_list1(line_ending, gate).parse(input)
}

fn gate(input: &str) -> IResult<&str, Gate<'_>> {
    alt((double_gate, not_gate, direct_gate)).parse(input)
}

fn double_gate(input: &str) -> IResult<&str, Gate<'_>> {
    map(
        (
            alphanumeric1,
            char(' '),
            alt((tag("AND"), tag("OR"), tag("LSHIFT"), tag("RSHIFT"))),
            char(' '),
            alphanumeric1,
            tag(" -> "),
            alpha1,
        ),
        |(input_1, _, inst, _, input_2, _, output)| Gate {
            a: Input::from_str(input_1),
            b: Input::from_str(input_2),
            out: output,
            instruction: match inst {
                "AND" => Instruction::And,
                "OR" => Instruction::OR,
                "LSHIFT" => Instruction::Lshift,
                "RSHIFT" => Instruction::Rshift,
                _ => panic!("Unexpected instruction {inst}"),
            },
        },
    )
    .parse(input)
}

fn not_gate(input: &str) -> IResult<&str, Gate<'_>> {
    map(
        (tag("NOT "), alpha1, tag(" -> "), alpha1),
        |(_, input_1, _, output)| Gate {
            a: Input::from_str(input_1),
            b: Input::None,
            out: output,
            instruction: Instruction::Not,
        },
    )
    .parse(input)
}

fn direct_gate(input: &str) -> IResult<&str, Gate<'_>> {
    map(
        (alphanumeric1, tag(" -> "), alpha1),
        |(input_1, _, output)| Gate {
            a: Input::from_str(input_1),
            b: Input::None,
            out: output,
            instruction: Instruction::Pass,
        },
    )
    .parse(input)
}

// Topological sorting O(n)
// Part 1: 46065 (60.9µs @ 8459 samples)
pub fn part_one(input: &str) -> Option<u16> {
    let (_, gates) = parser.parse(input).expect("a good parse");
    // Queue of gate ids ready to be processed
    let mut queue = VecDeque::new();
    let mut descendents: FxHashMap<&str, Vec<usize>> = FxHashMap::default();
    let mut dict = FxHashMap::default();
    // Preprocess the gates
    for (id, gate) in gates.into_iter().enumerate() {
        if gate.is_live() {
            // If the gate has all its inputs, push it to the processing queue
            queue.push_back(id);
        } else {
            match (&gate.a, &gate.b) {
                (Input::Wire(wa), Input::Wire(wb)) => {
                    descendents.entry(wa).or_default().push(id);
                    descendents.entry(wb).or_default().push(id);
                }
                (Input::Wire(w), Input::Value(_))
                | (Input::Wire(w), Input::None)
                | (Input::Value(_), Input::Wire(w))
                | (Input::None, Input::Wire(w)) => descendents.entry(w).or_default().push(id),
                _ => (),
            }
        }
        dict.insert(id, gate);
    }
    while let Some(id) = queue.pop_front() {
        let gate = dict.get(&id).unwrap();
        let output = gate.get_output();
        let out_wire = gate.out;
        if out_wire == "a" {
            return Some(output);
        }
        if let Some(desc) = descendents.get(gate.out) {
            for descendent_id in desc.iter() {
                if let Some(descendent) = dict.get_mut(descendent_id) {
                    descendent.set_input(out_wire, output);
                    if descendent.is_live() {
                        queue.push_back(*descendent_id);
                    }
                } else {
                    panic!("Expected to find {} in the dict", out_wire);
                }
            }
        }
    }
    None
}

// Part 2: 14134 (51.3µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u16> {
    part_one(&input.replace("1674 -> b", "46065 -> b"))
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        "123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
1 AND x -> c
NOT x -> a
NOT y -> i",
        65412
    )]
    fn test_part_one(#[case] input: &str, #[case] expected: u16) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
