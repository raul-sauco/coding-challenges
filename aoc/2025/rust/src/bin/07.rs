use std::mem::swap;

advent_of_code::solution!(7);

#[derive(Debug, Clone)]
enum Pos {
    Tachyon,
    Splitter,
    Space,
}

// fn print_state(state: &Vec<Pos>, count: u64) {
//     let str = state
//         .iter()
//         .map(|pos| match pos {
//             Pos::Tachyon => '|',
//             Pos::Splitter => '^',
//             Pos::Space => '.',
//         })
//         .collect::<String>();
//     println!("{str}\t{count}");
// }

// Part 1: 1609 (30.2µs)
pub fn part_one(input: &str) -> Option<u64> {
    let mut state = input
        .lines()
        .next()
        .expect("a first line")
        .chars()
        .map(|c| match c {
            '.' => Pos::Space,
            'S' => Pos::Tachyon,
            _ => panic!("Weird character {c}"),
        })
        .collect::<Vec<_>>();
    let mut count = 0;
    // print_state(&state, count);
    let mut next_state = vec![Pos::Space; state.len()];
    for line in input.lines().skip(1) {
        for (idx, c) in line.chars().enumerate() {
            match c {
                '.' => {
                    if let Pos::Tachyon = state[idx] {
                        next_state[idx] = Pos::Tachyon;
                    }
                }
                '|' => next_state[idx] = Pos::Tachyon,
                '^' => {
                    next_state[idx] = Pos::Splitter;
                    if let Pos::Tachyon = state[idx] {
                        count += 1;
                        // There are no splitters next to the edges
                        next_state[idx - 1] = Pos::Tachyon;
                        next_state[idx + 1] = Pos::Tachyon;
                    }
                }
                _ => panic!("Oooops! Found a {c} in the input"),
            }
        }
        swap(&mut state, &mut next_state);
        next_state.fill(Pos::Space);
        // print_state(&state, count);
    }
    Some(count)
}

#[derive(Debug, Clone, PartialEq, PartialOrd)]
enum Pos2 {
    Tachyon(u64),
    Splitter,
    Space,
}

// Part 2: 12472142047197 (39.2µs)
pub fn part_two(input: &str) -> Option<u64> {
    let mut state = input
        .lines()
        .next()
        .expect("a first line")
        .chars()
        .map(|c| match c {
            '.' => Pos2::Space,
            'S' => Pos2::Tachyon(1),
            _ => panic!("Weird character {c}"),
        })
        .collect::<Vec<_>>();
    // print_state(&state, count);
    for line in input.lines().skip(1) {
        state = compute_next_state(&state, line);
        // print_state_2(&state);
    }
    Some(
        state
            .iter()
            .map(|pos| match pos {
                Pos2::Tachyon(count) => *count,
                _ => 0,
            })
            .sum(),
    )
}

fn compute_next_state(state: &[Pos2], line: &str) -> Vec<Pos2> {
    let mut next_state = vec![Pos2::Space; state.len()];
    for (idx, c) in line.chars().enumerate() {
        match c {
            '.' => {
                if let Pos2::Tachyon(count) = state[idx] {
                    // next_state[idx] = Pos2::Tachyon(count);
                    next_state[idx] = Pos2::Tachyon(match next_state[idx] {
                        Pos2::Tachyon(other_count) => count + other_count,
                        Pos2::Splitter => panic!("Found splitters next to each other"),
                        Pos2::Space => count,
                    });
                }
            }
            '^' => {
                next_state[idx] = Pos2::Splitter;
                if let Pos2::Tachyon(count) = state[idx] {
                    // There are no splitters next to the edges
                    for i in [idx - 1, idx + 1] {
                        //   println!("{idx}::{:?}::{:?}", state[idx], state[i]);
                        next_state[i] = Pos2::Tachyon(match next_state[i] {
                            Pos2::Tachyon(other_count) => count + other_count,
                            Pos2::Splitter => panic!("Found splitters next to each other"),
                            Pos2::Space => count,
                        });
                    }
                }
            }
            _ => panic!("Oooops! Found a {c} in the input"),
        }
    }
    next_state
}

// fn print_state_2(state: &Vec<Pos2>) {
//     let str = state
//         .iter()
//         .map(|pos| match pos {
//             Pos2::Tachyon(c) => c.to_string(),
//             Pos2::Splitter => "^".to_string(),
//             Pos2::Space => ".".to_string(),
//         })
//         .collect::<Vec<_>>();
//     println!("{:?}", str);
// }

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(21));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(40));
    }

    fn str_to_state(input: Vec<&str>) -> Vec<Pos2> {
        input
            .iter()
            .map(|s| match *s {
                "." => Pos2::Space,
                "^" => Pos2::Splitter,
                _ => Pos2::Tachyon(s.parse::<u64>().expect("{s} to parse to a u64")),
            })
            .collect::<Vec<_>>()
    }

    fn state_to_str(input: Vec<Pos2>) -> Vec<String> {
        input
            .iter()
            .map(|pos| match pos {
                Pos2::Tachyon(num) => num.to_string(),
                Pos2::Splitter => "^".to_string(),
                Pos2::Space => ".".to_string(),
            })
            .collect::<Vec<_>>()
    }

    #[rstest]
    #[case(
        vec![".", ".", "1", ".", "5", ".", "4", "3", "4", ".", "2", ".", "1", ".", "."],
        "..^...^.....^..",
        vec![".", "1", "^", "1", "5", "4", "^", "7", "4", ".", "2", "1", "^", "1", "."],
    )]
    fn test_compute_next_state(
        #[case] str_state: Vec<&str>,
        #[case] line: &str,
        #[case] expected: Vec<&str>,
    ) {
        let state = str_to_state(str_state);
        let computed = compute_next_state(&state, line);
        assert_eq!(state_to_str(computed), expected);
    }
}
