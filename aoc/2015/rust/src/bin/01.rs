advent_of_code::solution!(1);

// Part 1: 232 (4.5µs @ 10000 samples)
pub fn part_one(input: &str) -> Option<i64> {
    Some(
        input
            .chars()
            .map(|c| match c {
                '(' => 1i64,
                ')' => -1i64,
                _ => panic!("unexpected char '{c}'"),
            })
            .sum::<i64>(),
    )
}

// Part 2: 1783 (1.4µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let mut floor: i32 = 0;
    for (idx, c) in input.chars().enumerate() {
        floor += match c {
            '(' => 1,
            ')' => -1,
            _ => panic!("unexpected char '{c}'"),
        };
        if floor == -1 {
            return Some(idx as u64 + 1);
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("(())", 0)]
    #[case("()()", 0)]
    #[case("(((", 3)]
    #[case("(()(()(", 3)]
    #[case("))(((((", 3)]
    #[case("())", -1)]
    #[case("))(", -1)]
    #[case(")))", -3)]
    #[case(")())())", -3)]
    fn test_part_one(#[case] input: &str, #[case] expected: i64) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[rstest]
    #[case(")", 1)]
    #[case("()())", 5)]
    fn test_part_two(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_two(input), Some(expected));
    }
}
