advent_of_code::solution!(5);

use nom::{
    bytes::complete::tag,
    character::complete::{digit1, line_ending},
    combinator::map_res,
    multi::separated_list1,
    sequence::separated_pair,
    IResult,
};
use std::{
    cmp::Ordering,
    collections::{HashMap, HashSet},
};

struct ParsedData {
    pairs: Vec<(u32, u32)>,
    books: Vec<Vec<u32>>,
}

fn parse_u32(input: &str) -> IResult<&str, u32> {
    map_res(digit1, str::parse::<u32>)(input)
}

fn parse_ordering(input: &str) -> IResult<&str, Vec<(u32, u32)>> {
    separated_list1(line_ending, separated_pair(parse_u32, tag("|"), parse_u32))(input)
}

fn parse_books(input: &str) -> IResult<&str, Vec<Vec<u32>>> {
    separated_list1(line_ending, separated_list1(tag(","), parse_u32))(input)
}

fn parse(input: &str) -> IResult<&str, ParsedData> {
    separated_pair(parse_ordering, tag("\n\n"), parse_books)(input)
        .map(|(rest, (pairs, books))| (rest, ParsedData { pairs, books }))
}

fn is_sorted_book(rules: &HashMap<u32, HashSet<u32>>, book: &Vec<u32>) -> bool {
    let mut seen = HashSet::new();
    for page in book {
        if let Some(not_allowed_pages) = rules.get(page) {
            if seen.intersection(not_allowed_pages).count() > 0 {
                return false;
            }
        }
        seen.insert(*page);
    }
    true
}

/// Given a vector of tuples with values that need to be before | after each other, return a hashmap
/// of u32 => HashSet<u32> where the hashsets contain values that cannot come before the key.
fn get_rules(pairs: Vec<(u32, u32)>) -> HashMap<u32, HashSet<u32>> {
    let mut rules: HashMap<u32, HashSet<u32>> = HashMap::new();
    for (before, after) in pairs {
        rules
            .entry(before)
            .and_modify(|hm| {
                hm.insert(after);
            })
            .or_insert(HashSet::from([after]));
    }
    rules
}

pub fn part_one(input: &str) -> Option<u32> {
    let (_, data) = parse(input).unwrap();
    let rules = get_rules(data.pairs);
    Some(
        data.books
            .into_iter()
            .filter(|book| is_sorted_book(&rules, book))
            .map(|v| v[v.len() / 2])
            .sum(),
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    let (_, data) = parse(input).unwrap();
    let rules = get_rules(data.pairs);
    Some(
        data.books
            .into_iter()
            .filter(|book| !is_sorted_book(&rules, book))
            .map(|mut book| {
                book.sort_by(|a, b| {
                    if rules
                        .get(a)
                        .is_some_and(|not_before| not_before.contains(b))
                    {
                        Ordering::Less
                    } else {
                        Ordering::Greater
                    }
                });
                book[book.len() / 2]
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
        assert_eq!(result, Some(143));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(123));
    }
}
