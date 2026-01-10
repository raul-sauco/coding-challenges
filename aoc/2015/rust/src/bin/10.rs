advent_of_code::solution!(10);

fn spell(input: &str) -> String {
    let mut spelling = String::new();
    let mut group = Vec::new();
    for c in input.chars() {
        match group.last() {
            Some(&last) => {
                if last == c {
                    group.push(c);
                } else {
                    spelling.push_str(&group.len().to_string());
                    spelling.push(last);
                    group.clear();
                    group.push(c);
                }
            }
            None => {
                group.push(c);
                continue;
            }
        }
    }
    spelling.push_str(&group.len().to_string());
    spelling.push(*group.last().expect("group not empty"));
    spelling
}

// Part 1: 360154 (11.3ms @ 85 samples)
pub fn part_one(input: &str) -> Option<usize> {
    let mut cur = input.trim().to_string();
    for _ in 0..40 {
        cur = spell(&cur);
    }
    Some(cur.len())
}

// Part 2: 5103798 (161.9ms @ 10 samples)
pub fn part_two(input: &str) -> Option<usize> {
    let mut cur = input.trim().to_string();
    for _ in 0..50 {
        cur = spell(&cur);
    }
    Some(cur.len())
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("1", 6)]
    fn test_part_one(#[case] input: &str, #[case] expected: usize) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
