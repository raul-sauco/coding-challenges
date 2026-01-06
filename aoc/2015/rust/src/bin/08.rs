use regex::Regex;

advent_of_code::solution!(8);

fn decode(line: &str) -> usize {
    // This line needs to go first, order matters
    let mut line = line.replace(r"\\", "S");
    line = line.replace(r#"\""#, "Q");
    let re = Regex::new(r"\\x([0-9A-Fa-f]{2})").unwrap();
    line = re.replace_all(&line, "X").into_owned();
    line.len()
}

fn encode(line: &str) -> usize {
    // This line needs to go first, order matters
    let mut line = line.replace(r"\\", "SSSS");
    line = line.replace(r#"\""#, "QQQQ");
    let re = Regex::new(r"\\x([0-9A-Fa-f]{2})").unwrap();
    line = re.replace_all(&line, "XXXXX").into_owned();
    line.len() + 4
}

// Tricky for me, I thought that just replacing the sequences literally would work, but depending
// on the order, it would result in the first replacement creating extra replacements and the wrong
// result. Updating the order of the replacements works because replacing // first results in the
// sequences being "interpreted" as escape sequences.
// Part 1: 1342 (2.8ms @ 322 samples)
pub fn part_one(input: &str) -> Option<usize> {
    Some(
        input
            .lines()
            .map(|line| line.len() - decode(&line[1..line.len() - 1]))
            .sum(),
    )
}

// Part 2: 2074 (2.9ms @ 348 samples)
pub fn part_two(input: &str) -> Option<usize> {
    Some(input.lines().map(|line| encode(line) - line.len()).sum())
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        r#"""
    "abc"
    "aaa\"aaa"
    "\x27""#,
        12
    )]
    fn test_part_one(#[case] input: &str, #[case] expected: usize) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[rstest]
    #[case("", 0)]
    #[case("abc", 3)]
    #[case("aaa\"aaa", 7)]
    #[case(r"\x27", 1)]
    #[case(r#"\"vhzlbwq\"xeimjt\\xe\x85umho\"m\"\"bmy"#, 30)]
    #[case(r#"ubgxxcvnltzaucrzg\\xcez"#, 22)] // Should strip to "ubgxxcvnltzaucrzgixcez"
    fn test_decode(#[case] input: &str, #[case] expected: usize) {
        assert_eq!(decode(input), expected);
    }

    #[rstest]
    #[case(
        r#"""
    "abc"
    "aaa\"aaa"
    "\x27""#,
        19
    )]
    fn test_part_two(#[case] input: &str, #[case] expected: usize) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[rstest]
    #[case(r#""""#, 6)]
    #[case(r#""abc""#, 9)]
    #[case(r#""aaa\"aaa""#, 16)]
    #[case(r#""\x27""#, 11)]
    fn test_encode(#[case] input: &str, #[case] expected: usize) {
        assert_eq!(encode(input), expected);
    }
}
