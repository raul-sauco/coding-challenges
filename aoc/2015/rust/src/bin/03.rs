use rustc_hash::FxHashSet;

advent_of_code::solution!(3);

// Part 1: 2081 (41.6µs @ 8191 samples)
pub fn part_one(input: &str) -> Option<usize> {
    let mut visited: FxHashSet<_> = [(0, 0)].into_iter().collect();
    let mut cur = (0, 0);
    for dir in input.chars() {
        match dir {
            '>' => cur.0 += 1,
            '<' => cur.0 -= 1,
            'v' => cur.1 += 1,
            '^' => cur.1 -= 1,
            _ => panic!("Unexpected char {dir}"),
        }
        visited.insert(cur.clone());
    }
    Some(visited.len())
}

// Part 2: 2341 (43.1µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<usize> {
    let mut visited: FxHashSet<_> = [(0, 0)].into_iter().collect();
    let (mut santa, mut robo_santa) = ((0, 0), (0, 0));
    let mut cur;
    for (idx, c) in input.chars().enumerate() {
        cur = if idx % 2 == 0 {
            &mut robo_santa
        } else {
            &mut santa
        };
        match c {
            '>' => cur.0 += 1,
            '<' => cur.0 -= 1,
            'v' => cur.1 += 1,
            '^' => cur.1 -= 1,
            _ => panic!("Unexpected char {c}"),
        }
        visited.insert(cur.clone());
    }
    Some(visited.len())
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(">", 2)]
    #[case("^>v<", 4)]
    #[case("^v^v^v^v^v", 2)]
    fn test_part_one(#[case] input: &str, #[case] expected: usize) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[rstest]
    #[case(">v", 3)]
    #[case("^>v<", 3)]
    #[case("^v^v^v^v^v", 11)]
    fn test_part_two(#[case] input: &str, #[case] expected: usize) {
        assert_eq!(part_two(input), Some(expected));
    }
}
