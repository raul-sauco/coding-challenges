advent_of_code::solution!(3);

use regex::Regex;

pub fn part_one(input: &str) -> Option<u32> {
    Some(
        Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)")
            .unwrap()
            .captures_iter(input)
            .map(|capture| {
                [1, 2].into_iter().fold(1, |acc, x| {
                    acc * capture
                        .get(x)
                        .map(|m| m.as_str().parse::<u32>().unwrap())
                        .unwrap()
                })
            })
            .sum::<u32>(),
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    let re = Regex::new(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))").unwrap();
    let mut active = true;
    let mut res = 0;
    for capture in re.captures_iter(input) {
        match &capture[0] {
            "do()" => active = true,
            "don't()" => active = false,
            _ => {
                if active {
                    res += [2, 3].into_iter().fold(1, |acc, x| {
                        acc * capture
                            .get(x)
                            .map(|m| m.as_str().parse::<u32>().unwrap())
                            .unwrap()
                    });
                }
            }
        }
    }
    Some(res)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(161));
    }

    #[test]
    fn test_part_two() {
        let input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";
        let result = part_two(&input);
        assert_eq!(result, Some(48));
    }
}
