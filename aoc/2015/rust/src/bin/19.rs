use nom::{
    IResult, Parser,
    bytes::complete::tag,
    character::complete::{alpha1, line_ending},
    combinator::map,
    multi::separated_list1,
    sequence::separated_pair,
};
use rustc_hash::{FxHashMap, FxHashSet};

advent_of_code::solution!(19);

fn parser(input: &str) -> IResult<&str, (FxHashMap<&str, Vec<&str>>, &str)> {
    separated_pair(replacements, tag("\n\n"), alpha1).parse(input)
}

fn replacements(input: &str) -> IResult<&str, FxHashMap<&str, Vec<&str>>> {
    map(
        separated_list1(line_ending, separated_pair(alpha1, tag(" => "), alpha1)),
        |pairs| {
            let mut map: FxHashMap<&str, Vec<&str>> = FxHashMap::default();
            for (key, val) in pairs {
                map.entry(key).or_default().push(val);
            }
            map
        },
    )
    .parse(input)
}

// Part 1: 518 (59.5µs @ 5254 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, (map, mol)) = parser.parse(input.trim()).expect("a good parse");
    let mut results: FxHashSet<String> = FxHashSet::default();
    let n = mol.len();
    for i in 0..n {
        // Check matches for one char
        let slice = &mol[i..=i];
        if let Some(replacements) = map.get(slice) {
            for replacement in replacements {
                let mut res = String::with_capacity(n + replacement.len() - slice.len());
                res.push_str(&mol[..i]);
                res.push_str(replacement);
                res.push_str(&mol[i + 1..]);
                results.insert(res);
            }
        }

        if i == n - 1 {
            continue;
        }
        // Check matches for two chars
        let slice = &mol[i..=i + 1];
        if let Some(replacements) = map.get(slice) {
            for replacement in replacements {
                let mut res = String::with_capacity(n + replacement.len() - slice.len());
                res.push_str(&mol[..i]);
                res.push_str(replacement);
                res.push_str(&mol[i + 2..]);
                results.insert(res);
            }
        }
    }
    Some(results.len() as u64)
}

type Replacements<'a> = Vec<(&'a str, &'a str)>;

fn parser_2(input: &str) -> IResult<&str, (Replacements<'_>, &str)> {
    separated_pair(replacements_2, tag("\n\n"), alpha1).parse(input)
}

fn replacements_2(input: &str) -> IResult<&str, Vec<(&str, &str)>> {
    separated_list1(line_ending, separated_pair(alpha1, tag(" => "), alpha1)).parse(input)
}

// Part 2: 200 (57.5µs @ 6610 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, (mut rep, mol)) = parser_2.parse(input.trim()).expect("a good parse");
    rep.sort_unstable_by_key(|(_, b)| std::cmp::Reverse(b.len()));
    let mut mol: String = mol.to_owned();
    let mut steps = 0;
    let mut match_count;
    while mol != "e" {
        // Try replacing backwards starting with the longer needles
        for (replacement, needle) in rep.iter() {
            match_count = mol.matches(needle).count();
            if match_count > 0 {
                steps += match_count;
                mol = mol.replace(needle, replacement);
                break;
            }
        }
    }
    Some(steps as u64)
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        "H => HO
H => OH
O => HH

HOH",
        4
    )]
    #[case(
        "H => HO
H => OH
O => HH

HOHOHO",
        7
    )]
    fn test_part_one(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[rstest]
    #[case(
        "e => H
e => O
H => HO
H => OH
O => HH

HOH",
        3
    )]
    #[case(
        "e => H
e => O
H => HO
H => OH
O => HH

HOHOHO",
        6
    )]
    fn test_part_two(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_two(input), Some(expected));
    }
}
