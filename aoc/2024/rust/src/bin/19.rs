advent_of_code::solution!(19);

use nom::{
    bytes::complete::tag,
    character::complete::{alpha1, newline},
    multi::separated_list1,
    sequence::separated_pair,
    IResult,
};

#[derive(Debug, Default)]
struct PatternTrie {
    is_word_end: bool,
    children: [Option<Box<PatternTrie>>; 26],
}

/**
 * A Trie implementation with an insert and a get_word_root methods.
 */
impl PatternTrie {
    fn new() -> Self {
        Default::default()
    }

    fn insert_pattern(&mut self, word: &str) {
        let mut node = self;
        for b in word.bytes() {
            node = node.children[(b - b'a') as usize]
                .get_or_insert_with(|| Box::new(PatternTrie::new()));
        }
        node.is_word_end = true;
    }

    /// Create a pattern trie where the patterns are reversed, this helps to use tabular dynamic
    /// programming to determine how many different ways we can generate a design.
    fn insert_reversed_pattern(&mut self, word: &str) {
        let mut node = self;
        for b in word.bytes().rev() {
            node = node.children[(b - b'a') as usize]
                .get_or_insert_with(|| Box::new(PatternTrie::new()));
        }
        node.is_word_end = true;
    }

    fn can_produce_design(&self, design: &str) -> bool {
        let mut node = self;
        for (i, b) in design.bytes().enumerate() {
            match node.children[(b - b'a') as usize].as_ref() {
                Some(child) => node = child,
                None => return false,
            }
            if node.is_word_end
                && (i == design.len() - 1 || self.can_produce_design(&design[i + 1..]))
            {
                return true;
            }
        }
        false
    }
}

fn parse_input(input: &str) -> IResult<&str, (Vec<&str>, Vec<&str>)> {
    separated_pair(
        separated_list1(tag(", "), alpha1),
        tag("\n\n"),
        separated_list1(newline, alpha1),
    )(input)
}

pub fn part_one(input: &str) -> Option<u32> {
    let (_, (patterns, designs)) = parse_input(input).expect("a good parse");
    let mut trie = PatternTrie::new();
    for pattern in patterns {
        trie.insert_pattern(pattern);
    }
    Some(
        designs
            .iter()
            .map(|design| {
                if trie.can_produce_design(design) {
                    1
                } else {
                    0
                }
            })
            .sum(),
    )
}

// Use DP to count the possible ways to build the given design. O(n*max(p))
// n - length of the design.
// max(p) - max length of patterns found in the Pattern Trie.
// For each index in the design, we start matching backwards, when we match an entire pattern, we
// add the ways that we could build the design up to the character before we started using that
// pattern.
fn count_possible_ways(root: &PatternTrie, design: &str) -> u64 {
    // Convert the design string to a Vec<u8> where the u8 value is byte - b'a';
    let design = design.bytes().map(|b| b - b'a').collect::<Vec<_>>();
    // A DP array where each index contains the number of different ways that we can build the
    // given design up to that length.
    let mut dp = vec![0; design.len() + 1];
    // One way to build the string ""
    dp[0] = 1;
    for i in 0..design.len() {
        let mut match_idx = i;
        let mut node = root;
        while let Some(child) = node.children[(design[match_idx]) as usize].as_ref() {
            if child.is_word_end {
                dp[i + 1] += dp[match_idx];
            }
            node = child;
            if match_idx == 0 {
                break;
            }
            match_idx -= 1;
        }
    }
    *dp.last().unwrap()
}

pub fn part_two(input: &str) -> Option<u64> {
    let (_, (patterns, designs)) = parse_input(input).expect("a good parse");
    let mut trie = PatternTrie::new();
    for pattern in patterns {
        trie.insert_reversed_pattern(pattern);
    }
    let mut total = 0;
    for design in designs {
        let ways = count_possible_ways(&trie, design);
        total += ways;
    }
    Some(total)
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"#,
        6;
        "Part One"
    )]
    fn test_part_one(input: &str, expected: u32) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

b"#,
        1;
        "part_two_b")]
    fn test_part_two_b(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

g"#,
        1;
        "Part Two: Test g")]
    fn test_part_two_g(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

r"#,
        1;
        "Part Two: Test r")]
    fn test_part_two_r(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

w"#,
        0;
        "Part Two: Test w")]
    fn test_part_two_w(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

br"#,
        2;
        "Part Two: Test br")]
    fn test_part_two_br(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

gbr"#,
        3;
        "Part Two: Test gbr")]
    fn test_part_two_gbr(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

bgbr"#,
        3;
        "Part Two: Test bgbr")]
    fn test_part_two_bgbr(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

rrbgbr"#,
        6;
        "Part Two: Test rrbgbr")]
    fn test_part_two_rrbgbr(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }

    #[test_case(
        r#"r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"#,
        16;
        "Part Two"
    )]
    fn test_part_two(input: &str, expected: u32) {
        assert_eq!(part_two(input), Some(expected));
    }
}
