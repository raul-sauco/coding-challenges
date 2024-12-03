use std::collections::HashMap;

advent_of_code::solution!(1);

fn parse(input: &str) -> (Vec<i32>, Vec<i32>) {
    input
        .lines()
        .map(|line| {
            let mut nums = line
                .split_whitespace()
                .map(|s| s.parse::<i32>().expect("A valid parse"));
            let left = nums.next().expect("A value on the left column");
            let right = nums.next().expect("A value on the right column");
            (left, right)
        })
        .collect::<Vec<_>>() // Propagate the error if any
        .into_iter()
        .unzip()
}

pub fn part_one(input: &str) -> Option<u32> {
    let (mut col1, mut col2) = parse(input);
    col1.sort_unstable();
    col2.sort_unstable();
    Some(
        col1.into_iter()
            .zip(col2)
            .map(|(a, b)| (a - b).unsigned_abs())
            .sum::<u32>(),
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    let (col1, col2) = parse(input);
    let mut counts = HashMap::new();
    for num in col2 {
        counts.entry(num).and_modify(|c| *c += 1).or_insert(1);
    }
    Some(col1.into_iter().fold(0, |acc, x| {
        if let Some(&right_count) = counts.get(&x) {
            acc + (x * right_count) as u32
        } else {
            acc
        }
    }))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(11));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(31));
    }
}
