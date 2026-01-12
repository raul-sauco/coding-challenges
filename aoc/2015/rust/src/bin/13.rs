use itertools::Itertools;
use nom::{
    IResult, Parser,
    branch::alt,
    bytes::complete::tag,
    character::complete::{self, alpha1, line_ending},
    combinator::map,
    multi::separated_list1,
};
use rayon::prelude::*;
use rustc_hash::FxHashMap;

advent_of_code::solution!(13);

#[derive(Debug)]
struct Item<'a> {
    a: &'a str,
    b: &'a str,
    gain: i64,
}

fn parser(input: &str) -> IResult<&str, Vec<Item<'_>>> {
    separated_list1(line_ending, item).parse(input)
}

fn item(input: &str) -> IResult<&str, Item<'_>> {
    map(
        (
            alpha1,
            tag(" would "),
            alt((tag("gain "), tag("lose "))),
            complete::i64,
            tag(" happiness units by sitting next to "),
            alpha1,
            tag("."),
        ),
        |(a, _, gl, gain, _, b, _)| Item {
            a,
            b,
            gain: match gl {
                "lose " => -gain,
                "gain " => gain,
                _ => panic!("did not expect {gl}"),
            },
        },
    )
    .parse(input)
}

fn process(items: Vec<Item>) -> Vec<Vec<i64>> {
    let mut dict: FxHashMap<&'_ str, usize> = FxHashMap::default();
    for item in items.iter() {
        if !dict.contains_key(item.a) {
            dict.insert(item.a, dict.len());
        }
        if !dict.contains_key(item.b) {
            dict.insert(item.b, dict.len());
        }
    }
    let mut matrix = vec![vec![0; dict.len()]; dict.len()];
    for item in items.into_iter() {
        match (dict.get(item.a), dict.get(item.b)) {
            (Some(a), Some(b)) => {
                matrix[*a][*b] = item.gain;
            }
            _ => panic!("expected both a and b to exist in the dict"),
        }
    }
    matrix
}

fn compute_happiness(arrangement: Vec<usize>, matrix: &[Vec<i64>]) -> i64 {
    arrangement
        .into_iter()
        .circular_tuple_windows::<(_, _)>()
        .map(|(a, b)| matrix[a][b] + matrix[b][a])
        .sum()
}

// Part 1: 664 (2.7ms @ 354 samples)
pub fn part_one(input: &str) -> Option<i64> {
    let (_, items) = parser.parse(input).expect("a good parse");
    let matrix = process(items);
    // let mut res = i64::MIN;
    // for arrangement in (0..matrix.len()).permutations(matrix.len()) {
    //     res = res.max(compute_happiness(arrangement, &matrix));
    // }
    // Some(res)
    // For loop and iterator + fold run in about the same time 1.8/1.9ms
    Some(
        (0..matrix.len())
            .permutations(matrix.len())
            .fold(i64::MIN, |res, arrangement| {
                res.max(compute_happiness(arrangement, &matrix))
            }),
    )
    // The map/max version is a bit slower 2.5ms
    // (0..matrix.len())
    //     .permutations(matrix.len())
    //     .map(|arrangement| compute_happiness(arrangement, &matrix))
    //     .max()
}

// Part 2: 640 (8.6ms @ 81 samples)
pub fn part_two(input: &str) -> Option<i64> {
    let (_, items) = parser.parse(input).expect("a good parse");
    let mut matrix = process(items);
    for row in &mut matrix {
        row.push(0);
    }
    matrix.push(vec![0; matrix[0].len()]);
    let n = matrix.len();
    // Paralelize the outer loop, it brings time down from 25 to 9ms
    Some(
        (0..n)
            .into_par_iter()
            .map(|first| {
                let rest: Vec<_> = (0..n).filter(|&x| x != first).collect();
                rest.into_iter()
                    .permutations(n - 1)
                    .map(|mut perm| {
                        perm.insert(0, first);
                        compute_happiness(perm, &matrix)
                    })
                    .max()
                    .unwrap_or(i64::MIN)
            })
            .max()
            .unwrap_or(i64::MIN),
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        r"Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.",
        330
    )]
    fn test_part_one(#[case] input: &str, #[case] expected: i64) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
