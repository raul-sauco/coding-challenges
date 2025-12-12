use nom::{
    IResult, Parser,
    character::complete::{digit1, newline},
    combinator::map,
    multi::separated_list1,
};

advent_of_code::solution!(3);

fn battery_bank(input: &str) -> IResult<&str, Vec<u32>> {
    map(digit1, |bat: &str| {
        bat.chars()
            .map(|c| c.to_digit(10).expect("a digit"))
            .collect()
    })
    .parse(input)
}

fn select_two(bank: Vec<u32>) -> u32 {
    let (idx, first) = bank.iter().take(bank.len() - 1).enumerate().fold(
        (0, 0),
        |(max_idx, max_num), (idx, &num)| {
            if num > max_num {
                (idx, num)
            } else {
                (max_idx, max_num)
            }
        },
    );
    let second = bank[idx + 1..].iter().max().expect("a second digit");
    (first * 10) + second
}

fn battery_banks(input: &str) -> IResult<&str, Vec<Vec<u32>>> {
    separated_list1(newline, battery_bank).parse(input)
}

fn select_n(bank: Vec<u32>, n: usize) -> u64 {
    let mut res = 0;
    let mut first_valid_index = 0;
    let mut num;
    for i in (1..=n).rev() {
        (first_valid_index, num) = pick_max(&bank, first_valid_index, bank.len() - i);
        res = res * 10 + num as u64;
    }
    res
}

fn pick_max(bank: &[u32], start: usize, end: usize) -> (usize, u32) {
    let (idx, max) =
        bank[start..=end]
            .iter()
            .enumerate()
            .fold((0, 0), |(max_idx, max_num), (idx, &num)| {
                if num > max_num {
                    (idx, num)
                } else {
                    (max_idx, max_num)
                }
            });
    // println!("{start}:{end}\t{idx}\t{max}");
    (start + idx + 1, max)
}

// Part 1: 17554 (41.2µs @ 10000 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, res) = battery_banks.parse(input).expect("a good parse");
    Some(res.into_iter().map(select_two).sum::<u32>() as _)
}

// Part 2: 175053592950232 (55.4µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, res) = battery_banks.parse(input).expect("a good parse");
    Some(res.into_iter().map(|v| select_n(v, 12)).sum::<u64>())
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;
    use test_case::test_case;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(357));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3121910778619));
    }

    #[test_case("987654321111111", 98)]
    #[test_case("811111111111119", 89)]
    #[test_case("234234234234278", 78)]
    #[test_case("818181911112111", 92)]
    #[test_case("397555622535653942", 99)]
    fn test_select_two(input: &str, expected: u32) {
        let (_, res) = battery_bank.parse(input).expect("a good parse");
        let actual = select_two(res);
        assert_eq!(actual, expected);
    }

    #[test_case("987654321111111", 12, 987654321111)]
    #[test_case("811111111111119", 12, 811111111119)]
    #[test_case("234234234234278", 12, 434234234278)]
    #[test_case("818181911112111", 12, 888911112111)]
    #[test_case("397555622535653942", 12, 976535653942)]
    fn test_select_n(input: &str, n: usize, expected: u64) {
        let (_, res) = battery_bank.parse(input).expect("a good parse");
        let actual = select_n(res, n);
        assert_eq!(actual, expected);
    }
}
