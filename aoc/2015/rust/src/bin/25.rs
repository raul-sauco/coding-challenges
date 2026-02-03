advent_of_code::solution!(25);

const SEED: u64 = 20151125;
const MULTIPLIER: u64 = 252533;
const MOD: u64 = 33554393;

// Parse integers out of a text ignoring everything else
fn parse(input: &str) -> Vec<u64> {
    input
        .split(|c: char| !c.is_ascii_digit())
        .filter(|s| !s.is_empty())
        .map(|s| s.parse().unwrap())
        .collect()
}

// Get the triangular number at row, col (1-indexed)
fn position_at(row: u64, col: u64) -> u64 {
    ((row + col - 2) * (row + col - 1) / 2) + col
}

// Modular exponentiation
fn modexp(mut base: u64, mut exp: u64, m: u64) -> u64 {
    let mut result = 1;
    base %= m;
    while exp > 0 {
        if exp % 2 == 1 {
            result = (result * base) % m;
        }
        base = (base * base) % m;
        exp /= 2;
    }
    result
}

// Part 1: 8997277 (161.0ns @ 10000 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let nums = parse(input);
    let (row, col) = (nums[0], nums[1]);
    // We multiply n-1 times
    let exp = position_at(row, col) - 1;
    Some(SEED * modexp(MULTIPLIER, exp, MOD) % MOD)
}

pub fn part_two(_input: &str) -> Option<u64> {
    None
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("row 1 col 1.", 20151125)]
    #[case("row 2 col 1.", 31916031)]
    #[case("row 6 col 6.", 27995004)]
    fn test_part_one(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }

    #[rstest]
    #[case(1, 1, 1)]
    #[case(2, 4, 14)]
    #[case(5, 2, 17)]
    fn test_position_at(#[case] row: u64, #[case] col: u64, #[case] expected: u64) {
        assert_eq!(position_at(row, col), expected);
    }
}
