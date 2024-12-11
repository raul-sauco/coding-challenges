advent_of_code::solution!(11);

use std::collections::HashMap;

use glam::{u32, u64};
use nom::{
    character::complete::{digit1, space1},
    multi::separated_list1,
    IResult,
};

#[inline]
fn has_even_number_of_digits(n: u64) -> bool {
    // let num_digits =  (n as f32).log10().floor() as u32 + 1;
    (n as f32).log10().floor() as u32 % 2 == 1
}

fn split_number(n: u64) -> Vec<u64> {
    let num_digits = (n as f32).log10().floor() as u64 + 1;
    let half_digits = num_digits as u32 / 2;

    let divisor = 10u64.pow(half_digits); // Divisor to separate the halves
    let first_half = n / divisor; // Left half
    let second_half = n % divisor; // Right half

    vec![first_half, second_half]
}

fn transform(stone: u64) -> Vec<u64> {
    if stone == 0 {
        return vec![1];
    }
    if has_even_number_of_digits(stone) {
        return split_number(stone);
    }
    vec![stone * 2024]
}

fn parse(input: &str) -> IResult<&str, Vec<u64>> {
    separated_list1(space1, digit1)(input)
        .map(|(rem, v)| (rem, v.iter().map(|s| s.parse::<u64>().unwrap()).collect()))
}

pub fn part_one(input: &str) -> Option<u32> {
    let (_rem, mut numbers) = parse(input).unwrap();
    let mut next_numbers;
    for _ in 0..25 {
        next_numbers = numbers
            .iter()
            .flat_map(|stone| transform(*stone).into_iter())
            .collect();
        numbers = next_numbers;
    }
    Some(numbers.len() as _)
}

fn dfs(stone: u64, blinks: u32, cache: &mut HashMap<(u64, u32), u64>) -> u64 {
    if let Some(result) = cache.get(&(stone, blinks)) {
        return *result;
    }
    if blinks == 0 {
        return 1;
    }
    let result;
    if stone == 0 {
        result = dfs(1, blinks - 1, cache);
    } else if has_even_number_of_digits(stone) {
        result = split_number(stone)
            .into_iter()
            .map(|st| dfs(st, blinks - 1, cache))
            .sum();
    } else {
        result = dfs(stone * 2024, blinks - 1, cache);
    }
    cache.insert((stone, blinks), result);
    result
}

pub fn part_two(input: &str) -> Option<u64> {
    let (_rem, numbers) = parse(input).unwrap();
    let mut cache = HashMap::new();
    Some(
        numbers
            .into_iter()
            .map(|stone| dfs(stone, 75, &mut cache))
            .sum(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(55312));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(65601038650482));
    }
}
