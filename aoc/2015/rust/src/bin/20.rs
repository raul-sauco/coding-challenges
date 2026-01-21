advent_of_code::solution!(20);

// Part 1: 776160 (7.8ms @ 89 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let target: usize = input.trim().parse().expect("a usize input");
    let mut presents = vec![10; 1_000_000];
    let mut give;
    for elf in 2..800_000 {
        give = elf * 10;
        for house in (elf..presents.len()).step_by(elf) {
            presents[house] += give;
        }
    }
    presents
        .iter()
        .enumerate()
        .skip(1)
        .find(|&(_, &p)| p >= target)
        .map(|(i, _)| i as u64)
}

// Part 2: 786240 (3.6ms @ 285 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let target: usize = input.trim().parse().expect("a usize input");
    let limit = 1_000_000;
    let mut presents = vec![10; limit];
    let mut give;
    for elf in 2..800_000 {
        give = elf * 11;
        for house in (elf..(elf * 50).min(limit)).step_by(elf) {
            presents[house] += give;
        }
    }
    presents
        .iter()
        .enumerate()
        .skip(1)
        .find(|&(_, &p)| p >= target)
        .map(|(i, _)| i as u64)
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("140", 8)]
    #[case("30", 2)]
    #[case("33100000", 776160)]
    fn test_part_one(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
