use bitvec::prelude::*;
use itertools::Itertools;
use nom::{
    IResult, Parser,
    bytes::complete::is_not,
    character::complete::{self, char, line_ending, space1},
    combinator::map,
    multi::{separated_list0, separated_list1},
    sequence::delimited,
};
use rayon::prelude::*;
use z3::{Optimize, SatResult, ast::Int};

advent_of_code::solution!(10);

#[derive(Debug)]
struct Machine {
    target: BitVec,
    buttons: Vec<BitVec>,
    joltage: Vec<u16>,
}

impl Machine {
    fn button_pushes_to_target(&self) -> Option<usize> {
        (0..self.target.len()).find(|&k| {
            self.buttons
                .iter()
                .combinations(k)
                .map(|v| {
                    v.iter()
                        .fold(bitvec!(0; self.target.len()), |acc, &bv| acc ^ bv)
                })
                .any(|bv| *bv == self.target)
        })
    }

    fn to_joltage(&self) -> u64 {
        z3_solve_ilp(&self.buttons, &self.joltage)
            .unwrap()
            .iter()
            .sum()
    }
}

// Parsers
fn parser(input: &str) -> IResult<&str, Vec<Machine>> {
    separated_list1(line_ending, machine).parse(input)
}

fn machine(input: &str) -> IResult<&str, Machine> {
    let (input, target) = target(input)?;
    let (input, _) = space1(input)?;
    let (input, buttons_u8) = separated_list1(space1, button).parse(input)?;
    let (input, _) = space1(input)?;
    let (input, joltage) = joltage(input)?;
    let buttons = buttons_u8
        .into_iter()
        .map(|b| {
            let mut bv = bitvec!(0; target.len());
            for ri in b {
                bv.set(ri as usize, true);
            }
            bv
        })
        .collect::<Vec<_>>();
    Ok((
        input,
        Machine {
            target,
            buttons,
            joltage,
        },
    ))
}

fn target(input: &str) -> IResult<&str, BitVec> {
    map(delimited(char('['), is_not("]"), char(']')), |s: &str| {
        s.chars()
            .map(|c| match c {
                '#' => true,
                '.' => false,
                _ => panic!("did not expect a {c}"),
            })
            .collect::<BitVec>()
    })
    .parse(input)
}

fn button(input: &str) -> IResult<&str, Vec<u8>> {
    delimited(
        char('('),
        separated_list1(char(','), complete::u8),
        char(')'),
    )
    .parse(input)
}

fn joltage(input: &str) -> IResult<&str, Vec<u16>> {
    delimited(
        char('{'),
        separated_list0(char(','), complete::u16),
        char('}'),
    )
    .parse(input)
}

// Helper solver for part 2, directly uses Z3
fn z3_solve_ilp(matrix: &[BitVec], result: &[u16]) -> Option<Vec<u64>> {
    let opt = Optimize::new();
    let num_rows = matrix.len();
    let num_cols = matrix[0].len();
    assert_eq!(num_cols, result.len());

    // Buttons are rows, one multiplier per row
    let xs: Vec<Int> = (0..num_rows)
        .map(|j| Int::new_const(format!("x{j}")))
        .collect();

    // Constrain results to be non-negative
    let zero = Int::from_u64(0);
    for x in &xs {
        opt.assert(&x.ge(&zero));
    }
    // Can we use bitvec.ones() for this?
    for j in 0..num_cols {
        let mut terms = Vec::new();
        for i in 0..num_rows {
            if matrix[i][j] {
                terms.push(&xs[i]);
            }
        }
        let target = Int::from_u64(result[j] as u64);
        if terms.is_empty() {
            opt.assert(&target.eq(&zero));
        } else {
            let sum_expr = Int::add(&terms);
            opt.assert(&sum_expr.eq(&target));
        }
    }

    // Optimization Goal: Minimize the sum of all computed variables
    let total_sum_terms: Vec<&Int> = xs.iter().collect();
    let total_sum = Int::add(&total_sum_terms);
    opt.minimize(&total_sum);

    // Compute Z3 result
    match opt.check(&[]) {
        SatResult::Sat => {
            let model = opt.get_model().unwrap();
            Some(
                xs.iter()
                    .map(|x| model.eval(x, true).unwrap().as_u64().unwrap())
                    .collect(),
            )
        }
        _ => None,
    }
}

// Part 1: 545 (3.3ms @ 295 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, machines) = parser.parse(input).expect("a good parse");
    Some(
        machines
            .iter()
            .map(|machine| {
                machine
                    .button_pushes_to_target()
                    .expect("machine to target to be some")
            })
            .sum::<usize>() as u64,
    )
}

// TODO: Look at Gaussian Elimination.
// https://gist.github.com/icub3d/16eea2a8b4a94d193a148fef908779a9
//
// Part 2: 22430 (52.5ms @ 15 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, machines) = parser.parse(input).expect("a good parse");
    Some(
        machines
            .par_iter()
            .map(|machine| machine.to_joltage())
            .sum(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(7));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(33));
    }

    #[rstest]
    #[case("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}", 10)]
    #[case("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}", 12)]
    #[case("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}", 11)]
    fn test_to_joltage(#[case] input: &str, #[case] expected: u64) {
        let (_, machine) = machine(input).expect("a good parse");
        let solutions =
            z3_solve_ilp(&machine.buttons, &machine.joltage).expect("a solution vector");
        let total_pushes = solutions.iter().sum::<u64>();
        assert_eq!(total_pushes, expected);
    }
}
