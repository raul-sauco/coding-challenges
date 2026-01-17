use std::collections::BTreeMap;

use nom::{
    IResult, Parser,
    bytes::complete::tag,
    character::complete::{self, alpha1, line_ending},
    multi::separated_list1,
    sequence::preceded,
};

advent_of_code::solution!(16);

fn get_target_sue<'a>() -> BTreeMap<&'a str, u16> {
    BTreeMap::from([
        ("children", 3),
        ("cats", 7),
        ("samoyeds", 2),
        ("pomeranians", 3),
        ("akitas", 0),
        ("vizslas", 0),
        ("goldfish", 5),
        ("trees", 3),
        ("cars", 2),
        ("perfumes", 1),
    ])
}

fn parser(input: &str) -> IResult<&str, Vec<BTreeMap<&str, u16>>> {
    separated_list1(line_ending, sue).parse(input)
}

fn sue(input: &str) -> IResult<&str, BTreeMap<&str, u16>> {
    let (input, id) = preceded(tag("Sue "), complete::u16).parse(input)?;
    let (input, _) = tag(": ").parse(input)?;
    let (input, props) =
        separated_list1(tag(", "), (alpha1, tag(": "), complete::u16)).parse(input)?;
    let mut map = BTreeMap::from_iter(props.iter().map(|(k, _, v)| (*k, *v)));
    map.insert("id", id);
    Ok((input, map))
}

fn matches(sue: &BTreeMap<&str, u16>, target: &BTreeMap<&str, u16>) -> bool {
    for (k, v) in sue.iter() {
        if let Some(val) = target.get(k)
            && v != val
        {
            return false;
        }
    }
    true
}

fn retroencabulator_match(sue: &BTreeMap<&str, u16>, target: &BTreeMap<&str, u16>) -> bool {
    for (k, v) in sue.iter() {
        if let Some(val) = target.get(k) {
            match *k {
                "cats" | "trees" => {
                    if v <= val {
                        return false;
                    }
                }
                "pomeranians" | "goldfish" => {
                    if v >= val {
                        return false;
                    }
                }
                _ => {
                    if v != val {
                        return false;
                    }
                }
            }
        }
    }
    true
}

// Part 1: 40 (78.4µs @ 7472 samples)
pub fn part_one(input: &str) -> Option<u16> {
    let (_, sues) = parser.parse(input).expect("a good parse");
    let target = get_target_sue();
    sues.iter()
        .find(|sue| matches(sue, &target))
        .expect("a matched sue")
        .get("id")
        .copied()
}

// Part 2: 241 (82.2µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u16> {
    let (_, sues) = parser.parse(input).expect("a good parse");
    let target = get_target_sue();
    // Sanity check to see if there are multiple matches
    // let filtered = sues
    //     .iter()
    //     .filter(|sue| retroencabulator_match(sue, &target))
    //     .collect::<Vec<_>>();
    // filtered[0].get("id").copied()
    // If we know that there is only one match find will exit on the (first) match
    sues.iter()
        .find(|sue| retroencabulator_match(sue, &target))
        .expect("a matched sue")
        .get("id")
        .copied()
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        r"Sue 38: cars: 10, akitas: 5, vizslas: 8
Sue 39: akitas: 5, trees: 9, children: 2
Sue 40: vizslas: 0, cats: 7, akitas: 0
Sue 41: cars: 9, trees: 10, perfumes: 8
Sue 42: akitas: 4, trees: 2, goldfish: 3
Sue 43: goldfish: 1, cats: 1, akitas: 8
Sue 44: goldfish: 8, akitas: 9, vizslas: 4",
        40
    )]
    fn test_part_one(#[case] input: &str, #[case] expected: u16) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[rstest]
    #[case(
        r"Sue 38: cars: 10, akitas: 5, vizslas: 8
Sue 39: akitas: 5, trees: 9, children: 2
Sue 40: vizslas: 0, cats: 7, akitas: 0
Sue 41: cars: 9, trees: 10, perfumes: 8
Sue 42: akitas: 4, trees: 2, goldfish: 3
Sue 43: goldfish: 1, cats: 1, akitas: 8
Sue 44: goldfish: 8, akitas: 9, vizslas: 4",
        40
    )]
    fn test_part_two(#[case] input: &str, #[case] expected: u16) {
        assert_eq!(part_two(input), Some(expected));
    }
}
