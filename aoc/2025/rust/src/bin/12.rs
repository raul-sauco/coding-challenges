use nom::{
    IResult, Parser,
    bytes::complete::{tag, take_until},
    character::complete::{char, digit1, line_ending, not_line_ending, space1, u8},
    combinator::map,
    multi::separated_list1,
    sequence::preceded,
};

advent_of_code::solution!(12);

#[derive(Debug)]
#[allow(dead_code)]
struct Tree {
    x: u8,
    y: u8,
    area: u16,
    counts: Vec<u8>,
}

#[derive(Debug)]
#[allow(dead_code)]
struct Shape<'a> {
    lines: Vec<&'a str>,
    filled: u8,
}

fn parser(input: &str) -> IResult<&str, (Vec<Shape<'_>>, Vec<Tree>)> {
    let (input, shapes) = map(
        separated_list1(tag("\n\n"), take_until("\n\n")),
        |v: Vec<&str>| {
            v.iter()
                .map(|&s| {
                    let (rem, shape) = shape(s).expect("a good shape");
                    assert!(rem.is_empty());
                    shape
                })
                .collect::<Vec<_>>()
        },
    )
    .parse(input)?;
    let (input, trees) = preceded(tag("\n\n"), separated_list1(line_ending, tree)).parse(input)?;
    Ok((input, (shapes, trees)))
}

fn shape(input: &str) -> IResult<&str, Shape<'_>> {
    map(
        preceded(
            (digit1, char(':'), line_ending),
            separated_list1(line_ending, not_line_ending),
        ),
        |lines| Shape {
            filled: lines
                .iter()
                .flat_map(|line: &&str| line.chars())
                .filter(|&c| c == '#')
                .count() as u8,
            lines,
        },
    )
    .parse(input)
}

fn tree(input: &str) -> IResult<&str, Tree> {
    map(
        (
            u8,
            char('x'),
            u8,
            char(':'),
            space1,
            separated_list1(space1, u8),
        ),
        |(x, _, y, _, _, counts)| Tree {
            x,
            y,
            area: x as u16 * y as u16,
            counts,
        },
    )
    .parse(input)
}

fn can_fit(tree: &Tree, shapes: &[Shape]) -> bool {
    tree.counts
        .iter()
        .enumerate()
        .map(|(idx, &count)| count as u16 * shapes[idx].filled as u16)
        .sum::<u16>()
        <= tree.area
}

// Part 1: 567 (93.4µs @ 9240 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, (shapes, trees)) = parser.parse(input).expect("a good parse");
    Some(trees.iter().filter(|tree| can_fit(tree, &shapes)).count() as _)
}

pub fn part_two(_input: &str) -> Option<u64> {
    None
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
        assert_eq!(result, None);
    }
}
