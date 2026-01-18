use nom::{
    IResult, Parser,
    character::complete::{self, line_ending},
    multi::separated_list1,
};

advent_of_code::solution!(17);

fn parser(input: &str) -> IResult<&str, Vec<u16>> {
    separated_list1(line_ending, complete::u16).parse(input)
}

fn dfs(current_sum: u16, target_sum: u16, containers: &[u16], i: usize) -> u16 {
    if current_sum == target_sum {
        return 1;
    }
    if i >= containers.len() || current_sum > target_sum {
        return 0;
    }
    dfs(current_sum + containers[i], target_sum, containers, i + 1)
        + dfs(current_sum, target_sum, containers, i + 1)
}

fn min_containers(
    current_sum: u16,
    target_sum: u16,
    used_containers: u16,
    containers: &[u16],
    i: usize,
) -> Option<(u16, u16)> {
    if current_sum == target_sum {
        return Some((1, used_containers));
    }
    if i >= containers.len() || current_sum > target_sum {
        return None;
    }
    let take = min_containers(
        current_sum + containers[i],
        target_sum,
        used_containers + 1,
        containers,
        i + 1,
    );
    let skip = min_containers(current_sum, target_sum, used_containers, containers, i + 1);
    match (take, skip) {
        (None, None) => None,
        (None, Some(res)) | (Some(res), None) => Some(res),
        (Some(t), Some(s)) => match t.1.cmp(&s.1) {
            std::cmp::Ordering::Less => Some(t),
            std::cmp::Ordering::Equal => Some((t.0 + s.0, t.1)),
            std::cmp::Ordering::Greater => Some(s),
        },
    }
}

// Part 1: 1638 (196.0µs @ 4573 samples)
pub fn part_one(input: &str) -> Option<u16> {
    let (_, containers) = parser.parse(input).expect("a good parse");
    Some(dfs(0, 150, &containers, 0))
}

// Part 2: 17 (442.5µs @ 2148 samples)
pub fn part_two(input: &str) -> Option<u16> {
    let (_, containers) = parser.parse(input).expect("a good parse");
    min_containers(0, 150, 0, &containers, 0).map(|res| res.0)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3));
    }
}
