advent_of_code::solution!(18);

use std::collections::{HashSet, VecDeque};

use glam::IVec2;
use nom::{
    bytes::complete::tag,
    character::complete::digit1,
    combinator::{map, map_res},
    multi::separated_list1,
    sequence::separated_pair,
    IResult,
};

const TARGET: IVec2 = if cfg!(test) {
    IVec2::new(6, 6)
} else {
    IVec2::new(70, 70)
};

const TAKE: usize = if cfg!(test) { 12 } else { 1024 };

const DIRS: [IVec2; 4] = [IVec2::NEG_Y, IVec2::X, IVec2::Y, IVec2::NEG_X];

fn parse_input(input: &str) -> IResult<&str, Vec<IVec2>> {
    separated_list1(tag("\n"), ivec2)(input)
}

fn ivec2(input: &str) -> IResult<&str, IVec2> {
    map(
        separated_pair(parse_number, tag(","), parse_number),
        |(x, y)| IVec2::new(x, y),
    )(input)
}

fn parse_number(input: &str) -> IResult<&str, i32> {
    map_res(digit1, str::parse)(input)
}

fn solve(corrupted: &HashSet<IVec2>) -> Option<u32> {
    let mut visited = HashSet::from([IVec2::new(0, 0)]);
    let mut queue = VecDeque::from([(0, IVec2::new(0, 0))]);
    while let Some((count, pos)) = queue.pop_front() {
        for &dir in DIRS.iter() {
            let nei = pos + dir;
            if nei.x < 0
                || nei.x > TARGET.x
                || nei.y < 0
                || nei.y > TARGET.y
                || corrupted.contains(&nei)
                || visited.contains(&nei)
            {
                continue;
            }
            // Valid, unvisited cell.
            if nei == TARGET {
                return Some(count + 1);
            }
            visited.insert(nei);
            queue.push_back((count + 1, nei));
        }
    }
    None
}

pub fn part_one(input: &str) -> Option<u32> {
    let (_rem, coordinates) = parse_input(input).unwrap();
    let corrupted = coordinates.into_iter().take(TAKE).collect::<HashSet<_>>();
    solve(&corrupted)
}

pub fn part_two(input: &str) -> Option<String> {
    let (_rem, coordinates) = parse_input(input).unwrap();
    let (mut l, mut r) = (0, coordinates.len());
    while l < r {
        let mid = (l + r) / 2;
        let corrupted = coordinates[..mid].iter().cloned().collect::<HashSet<_>>();
        if solve(&corrupted).is_some() {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    Some(format!("{},{}", coordinates[l - 1].x, coordinates[l - 1].y))
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case(
        r#"5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"#,
        22
    )]
    fn test_part_one(input: &str, expected: u32) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[test_case(
        r#"5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"#,
        "6,1"
    )]
    fn test_part_two(input: &str, expected: &str) {
        assert_eq!(part_two(input), Some(expected.to_string()));
    }
}
