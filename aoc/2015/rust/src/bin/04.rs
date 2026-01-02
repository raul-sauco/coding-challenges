advent_of_code::solution!(4);
use md5::{Digest, Md5};

pub fn part_one(input: &str) -> Option<u64> {
    let input = input.trim_end();
    for i in 1..2_000_000 {
        let mut hasher = Md5::new();
        let test_str = format!("{input}{i}");
        hasher.update(&test_str);
        let result = hasher.finalize();
        if result[0] == 0 && result[1] == 0 && result[2] < 16 {
            return Some(i as u64);
        }
    }
    None
}

pub fn part_two(input: &str) -> Option<u64> {
    let input = input.trim_end();
    for i in 1..2_000_000 {
        let mut hasher = Md5::new();
        let test_str = format!("{input}{i}");
        hasher.update(&test_str);
        let result = hasher.finalize();
        if result[0] == 0 && result[1] == 0 && result[2] == 0 {
            return Some(i as u64);
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("abcdef", 609043)]
    #[case("pqrstuv", 1048970)]
    fn test_part_one(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_one(input), Some(expected));
    }

    // #[test]
    // fn test_part_two() {
    //     let result = part_two(&advent_of_code::template::read_file("examples", DAY));
    //     assert_eq!(result, None);
    // }
}
