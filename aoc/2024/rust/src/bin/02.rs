use itertools::Itertools;

advent_of_code::solution!(2);

pub fn part_one(input: &str) -> Option<u32> {
    fn is_safe_report(report: &Vec<u32>) -> bool {
        fn is_increasing(report: &Vec<u32>) -> bool {
            for (a, b) in report.iter().tuple_windows() {
                if a >= b || b - a > 3 {
                    return false;
                }
            }
            true
        }
        fn is_decreasing(report: &Vec<u32>) -> bool {
            for (a, b) in report.iter().tuple_windows() {
                if a <= b || a - b > 3 {
                    return false;
                }
            }
            true
        }
        is_increasing(report) || is_decreasing(report)
    }
    Some(
        input
            .lines()
            .map(|line| {
                let report = line
                    .split_ascii_whitespace()
                    .map(|s| s.parse::<u32>().expect("A valid number"))
                    .collect::<Vec<_>>();
                if is_safe_report(&report) {
                    1
                } else {
                    0
                }
            })
            .sum(),
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    fn is_safe_report(report: &Vec<u32>) -> bool {
        fn is_increasing(report: &Vec<u32>) -> bool {
            for (a, b) in report.iter().tuple_windows() {
                if a >= b || b - a > 3 {
                    return false;
                }
            }
            true
        }
        fn is_decreasing(report: &Vec<u32>) -> bool {
            for (a, b) in report.iter().tuple_windows() {
                if a <= b || a - b > 3 {
                    return false;
                }
            }
            true
        }
        if is_increasing(report) || is_decreasing(report) {
            return true;
        }
        for skip_idx in 0..report.len() {
            let clone = report
                .iter()
                .enumerate()
                .filter_map(|(idx, item)| if idx == skip_idx { None } else { Some(*item) })
                .collect::<Vec<_>>();
            if is_increasing(&clone) || is_decreasing(&clone) {
                return true;
            }
        }
        false
    }
    Some(
        input
            .lines()
            .map(|line| {
                let report = line
                    .split_ascii_whitespace()
                    .map(|s| s.parse::<u32>().expect("A valid number"))
                    .collect::<Vec<_>>();
                if is_safe_report(&report) {
                    1
                } else {
                    0
                }
            })
            .sum(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(2));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4));
    }
}
