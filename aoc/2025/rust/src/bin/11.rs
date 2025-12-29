use nom::{
    IResult, Parser,
    bytes::complete::tag,
    character::complete::{alpha1, line_ending, space1},
    combinator::map,
    multi::separated_list1,
    sequence::separated_pair,
};
use rustc_hash::FxHashMap;

advent_of_code::solution!(11);

fn devices(input: &str) -> IResult<&str, FxHashMap<&str, Vec<&str>>> {
    map(separated_list1(line_ending, device), |v| {
        v.into_iter().collect()
    })
    .parse(input)
}

fn device(input: &str) -> IResult<&str, (&str, Vec<&str>)> {
    separated_pair(alpha1, tag(": "), separated_list1(space1, alpha1)).parse(input)
}

fn count_paths<'a>(
    start: &'a str,
    target: &str,
    graph: &FxHashMap<&str, Vec<&'a str>>,
    cache: &mut FxHashMap<&'a str, usize>,
) -> usize {
    // If we have computed it already, return that
    if let Some(&count) = cache.get(start) {
        return count;
    }
    // Base case, we reached the target.
    let paths = if start == target {
        1
    } else {
        graph
            .get(start)
            .into_iter()
            .flat_map(|v| v.iter())
            .map(|&nei| count_paths(nei, target, graph, cache))
            .sum()
    };
    cache.insert(start, paths);
    paths
}

// Part 1: 788 (35.8µs @ 10000 samples)
pub fn part_one(input: &str) -> Option<u64> {
    let (_, devices) = devices(input).expect("a good parse");
    let mut cache = FxHashMap::default();
    Some(count_paths("you", "out", &devices, &mut cache) as _)
}

// Part 2: 316291887968000 (74.5µs @ 10000 samples)
pub fn part_two(input: &str) -> Option<u64> {
    let (_, devices) = devices(input).expect("a good parse");
    let mut cache_svr_fft = FxHashMap::default();
    let mut cache_fft_dac = FxHashMap::default();
    let mut cache_dac_out = FxHashMap::default();
    Some(
        (count_paths("svr", "fft", &devices, &mut cache_svr_fft)
            * count_paths("fft", "dac", &devices, &mut cache_fft_dac)
            * count_paths("dac", "out", &devices, &mut cache_dac_out)) as _,
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(5));
    }

    #[rstest]
    #[case(
        "svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out",
        2
    )]
    fn test_part_two(#[case] input: &str, #[case] expected: u64) {
        assert_eq!(part_two(input), Some(expected));
    }
}
