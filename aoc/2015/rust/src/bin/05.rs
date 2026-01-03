use itertools::Itertools;
use rustc_hash::FxHashSet;

advent_of_code::solution!(5);

fn is_nice(input: &str) -> bool {
    let mut vowels = 0;
    let mut duets = 0;
    for pair in input.chars().zip_longest(input.chars().skip(1)) {
        match pair {
            itertools::EitherOrBoth::Both(a, b) => {
                if (a == 'a' && b == 'b')
                    || (a == 'c' && b == 'd')
                    || (a == 'p' && b == 'q')
                    || (a == 'x' && b == 'y')
                {
                    return false;
                }
                if a == b {
                    duets += 1;
                }
                if "aeiou".contains(a) {
                    vowels += 1;
                }
            }
            itertools::EitherOrBoth::Left(a) => {
                if "aeiou".contains(a) {
                    vowels += 1;
                }
            }
            itertools::EitherOrBoth::Right(b) => {
                panic!("Right iterator longer than expected gave {b}")
            }
        }
    }
    vowels > 2 && duets > 0
}

pub fn part_one(input: &str) -> Option<usize> {
    Some(input.lines().filter(|line| is_nice(line)).count())
}

fn is_nice_2(input: &str) -> bool {
    let mut contains_pair = false;
    let mut duets = FxHashSet::default();
    let mut last_duet: Option<String> = None;
    for (a, b) in input.chars().zip(input.chars().skip(1)) {
        let s = format!("{a}{b}");
        if duets.contains(&s) {
            contains_pair = true;
            break;
        } else {
            if let Some(ld) = last_duet {
                duets.insert(ld);
            }
            last_duet = Some(s);
        }
    }
    // Quick return
    if !contains_pair {
        return false;
    }
    for w in input.chars().tuple_windows::<(_, _, _)>() {
        if w.0 == w.2 {
            return true;
        }
    }
    false
}

pub fn part_two(input: &str) -> Option<usize> {
    Some(input.lines().filter(|line| is_nice_2(line)).count())
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(2));
    }

    #[rstest]
    #[case(
        "aabcbefgaa
aaa
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy",
        3
    )]
    fn test_part_two(#[case] input: &str, #[case] expected: usize) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[rstest]
    #[case("ugknbfddgicrmopn", true)]
    #[case("aaa", true)]
    #[case("jchzalrnumimnmhp", false)]
    #[case("haegwjzuvuyypxyu", false)]
    #[case("dvszwmarrgswjxmb", false)]
    fn test_is_nice(#[case] input: &str, #[case] expected: bool) {
        assert_eq!(is_nice(input), expected);
    }

    #[rstest]
    #[case("aabcbefgaa", true)]
    #[case("aaa", false)]
    #[case("qjhvhtzxzqqjkmpb", true)]
    #[case("xxyxx", true)]
    #[case("uurcxstgmygtbstg", false)]
    #[case("ieodomkazucvgmuy", false)]
    fn test_is_nice_2(#[case] input: &str, #[case] expected: bool) {
        assert_eq!(is_nice_2(input), expected);
    }
}
