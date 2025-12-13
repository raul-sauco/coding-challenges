advent_of_code::solution!(6);

#[derive(Debug)]
enum Op {
    Sum,
    Mul,
}

fn parse(input: &str) -> Vec<Vec<&str>> {
    input
        .lines()
        .map(|line| line.split_whitespace().collect::<Vec<_>>())
        .collect()
}

fn transpose<T: Clone>(m: &[Vec<T>]) -> Vec<Vec<T>> {
    (0..m[0].len())
        .map(|c| m.iter().map(|row| row[c].clone()).collect())
        .collect()
}

fn operands(input: Vec<&str>) -> Vec<Op> {
    input
        .into_iter()
        .map(|c| match c {
            "+" => Op::Sum,
            "*" => Op::Mul,
            _ => panic!("Unexpected char {c}"),
        })
        .collect::<Vec<_>>()
}

// Part 1: 6725216329103 (77.0µs @ 5587 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let mut parsed = parse(input);
    let operands = operands(parsed.pop().expect("a vec of operands"));
    let values = transpose(&parsed)
        .iter()
        .map(|v| {
            v.iter()
                .map(|str| str.parse::<u64>().expect("a valid u64"))
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    // assert_eq!(operands.len(), values.len());
    // dbg!(&parsed, &values, &operands);
    let res = operands
        .iter()
        .enumerate()
        .map(|(idx, op)| match op {
            Op::Sum => values[idx].iter().sum::<u64>(),
            Op::Mul => values[idx].iter().product::<u64>(),
        })
        // .inspect(|v| println!("{v}"))
        .sum::<u64>();
    Some(res)
}

// Part 2: 10600728112865 (21.3µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let grid: Vec<Vec<char>> = input
        .lines()
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect();
    let operands = &grid[0..grid.len() - 1];
    let operators = grid.last().expect("a vec of operators and whitespace");
    let mut ops = vec![];
    let mut res = 0;
    for col in (0..operands[0].len()).rev() {
        let mut op = 0;
        for row in operands.iter() {
            let c = row[col];
            if c != ' ' {
                op = op * 10 + c.to_digit(10).expect("a valid digit parse") as u64;
            }
        }
        // Ignore whitespace columns.
        if op == 0 {
            continue;
        }
        ops.push(op);
        let operator = operators[col];
        if !operator.is_whitespace() {
            let total = match operator {
                '+' => ops.iter().sum::<u64>(),
                '*' => ops.iter().product::<u64>(),
                _ => panic!("weird sign found {operator}"),
            };
            res += total;
            // println!("{operator}::{:?}\t{total}", ops);
            ops.clear();
        }
    }
    Some(res)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4277556));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3263827));
    }
}
