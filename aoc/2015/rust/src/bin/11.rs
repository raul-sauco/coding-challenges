use itertools::Itertools;

advent_of_code::solution!(11);

fn generate_next(input: Vec<u8>) -> Vec<u8> {
    let mut next = Vec::with_capacity(input.len());
    // Start the carry as true to add 1
    let mut carry = true;
    for b in input.into_iter().rev() {
        if carry {
            if b == b'z' {
                next.push(b'a');
                // carry = true;
            } else {
                next.push(b + 1);
                carry = false;
            }
        } else {
            next.push(b);
        }
    }
    if carry {
        next.push(b'a');
    }
    next.reverse();
    next
}

fn is_valid(input: &[u8]) -> bool {
    if input.iter().any(|b| matches!(b, b'i' | b'o' | b'l')) {
        return false;
    }
    let mut has_triplet = false;
    for (a, b, c) in input.iter().tuple_windows::<(_, _, _)>() {
        if *b == a + 1 && *c == b + 1 {
            has_triplet = true;
            break;
        }
    }
    if !has_triplet {
        return false;
    }
    let mut skip_one = false;
    let mut duplets = 0;
    for (a, b) in input.iter().tuple_windows::<(_, _)>() {
        // If the last pair was a duplet, we already used the current left element
        if skip_one {
            skip_one = false;
            continue;
        }
        if a == b {
            duplets += 1;
            skip_one = true;
        }
    }
    duplets > 1
}

// Part 1: hepxxyzz (6.5ms @ 159 samples)
pub fn part_one(input: &str) -> Option<String> {
    let mut current: Vec<u8> = input.trim().bytes().collect();
    while !is_valid(&current) {
        current = generate_next(current);
    }
    Some(String::from_utf8(current).expect("valid utf8 values"))
}

// Part 2: heqaabcc (23.1ms @ 38 samples)
pub fn part_two(input: &str) -> Option<String> {
    let first = part_one(input).unwrap();
    let next = generate_next(first.bytes().collect::<Vec<_>>());
    part_one(&String::from_utf8(next).unwrap())
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("hijklmmn", false)]
    #[case("abbceffg", false)]
    #[case("abbcegjk", false)]
    #[case("abbcegjk", false)]
    #[case("abceegjjk", true)]
    fn test_is_valid(#[case] input: &str, #[case] expected: bool) {
        let input = input.bytes().collect::<Vec<_>>();
        assert_eq!(is_valid(&input), expected);
    }

    #[rstest]
    #[case("hijklmmn", "hijklmmo")]
    #[case("abbceffg", "abbceffh")]
    fn test_generate_next(#[case] input: &str, #[case] expected: String) {
        let input = input.bytes().collect::<Vec<_>>();
        let result = String::from_utf8(generate_next(input)).expect("a test string");
        assert_eq!(result, expected);
    }

    #[rstest]
    #[case("abcdefgh", "abcdffaa")]
    #[case("ghijklmn", "ghjaabcc")]
    fn test_part_one(#[case] input: &str, #[case] expected: String) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[rstest]
    #[case("abcdefgh", "abcdffbb")]
    #[case("hepxxyzz", "heqaabcc")]
    fn test_part_two(#[case] input: &str, #[case] expected: String) {
        assert_eq!(part_two(input), Some(expected));
    }
}
