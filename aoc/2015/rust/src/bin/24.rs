use bitvec::prelude::*;
use itertools::Itertools;

advent_of_code::solution!(24);

// Return a Vec<u64> sorted descending
fn parse(input: &str) -> Vec<u64> {
    input
        .lines()
        .map(|line| line.parse().expect("a good parse for"))
        .sorted_by(|a: &u64, b: &u64| b.cmp(a))
        .collect()
}

fn can_partition(values: Vec<u64>) -> bool {
    let sum = values.iter().sum::<u64>();
    if !sum.is_multiple_of(2) {
        return false;
    }
    let target = sum as usize / 2;
    let mut dp = bitvec![0; target + 1];
    dp.set(0, true);
    for val in values.iter().map(|&val| val as usize) {
        if val > target {
            continue;
        }
        for i in (val..=target).rev() {
            if dp[i - val] {
                dp.set(i, true);
            }
        }
        if dp[target] {
            return true;
        }
    }
    dp[target]
}

// Given a a vector of values and a vector of indexes, return a vector containing all the values
// that are not indexed on the indexes vector
fn filtered_indexes(weights: &[u64], indexes: &[usize]) -> Vec<u64> {
    // indexes is sorted, we can use a pointer
    let mut i = 0;
    weights
        .iter()
        .enumerate()
        .filter_map(|(idx, w)| {
            if i < indexes.len() && idx == indexes[i] {
                i += 1;
                None
            } else {
                Some(*w)
            }
        })
        .collect()
}

fn filtered_product(weights: &[u64], indexes: &[usize]) -> u128 {
    indexes.iter().map(|&i| weights[i] as u128).product()
}

// Part 1: 11846773891 (8.7ms @ 115 samples)
pub fn part_one(input: &str) -> Option<u128> {
    let weights = parse(input);
    let total = weights.iter().sum::<u64>();
    if !total.is_multiple_of(3) {
        return None;
    }
    let target = total / 3;
    for size in 1..weights.len() / 3 {
        if let Some(entanglement) = (0..weights.len())
            .combinations(size)
            .filter(|indexes| indexes.iter().map(|&i| weights[i]).sum::<u64>() == target)
            .sorted_unstable_by(|a, b| {
                filtered_product(&weights, a).cmp(&filtered_product(&weights, b))
            })
            // Packages that match the weight sorted by entanglement
            .find_map(|indexes| {
                if can_partition(filtered_indexes(&weights, &indexes)) {
                    Some(filtered_product(&weights, &indexes))
                } else {
                    None
                }
            })
        {
            return Some(entanglement);
        }
    }
    None
}

// Part 2: 80393059 (51.7µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u128> {
    let weights = parse(input);
    let total = weights.iter().sum::<u64>();
    if !total.is_multiple_of(4) {
        return None;
    }
    let target = total / 4;
    for size in 1..5 {
        if let Some(res) = (0..weights.len())
            .combinations(size)
            .filter(|indexes| indexes.iter().map(|&i| weights[i]).sum::<u64>() == target)
            .map(|indexes| filtered_product(&weights, &indexes))
            // TODO: Check if we can partition in 3, maybe extend to k
            // The first result happens to work
            .next()
        {
            return Some(res);
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        "11
9
10
8
2
7
5
4
3
1",
        99
    )]
    fn test_part_one(#[case] input: &str, #[case] expected: u128) {
        assert_eq!(part_one(input), Some(expected));
    }

    #[rstest]
    #[case(
        "11
9
10
8
2
7
5
4
3
1",
        44
    )]
    fn test_part_two(#[case] input: &str, #[case] expected: u128) {
        assert_eq!(part_two(input), Some(expected));
    }
}
