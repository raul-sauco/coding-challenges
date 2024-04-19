// 2391. Minimum Amount of Time to Collect Garbage
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
//
// Tags: Array - String - Prefix Sum

struct Solution;
impl Solution {
    /// Iterate over both the travel time and the garbage, add as many units of each type of
    /// garbage as we find at that location, plus the time it took the particular truck to get
    /// there, then reset the travel time, for every type of garbage found. The last step in each
    /// iteration of the loop is to add the time it takes to get to the next location to the
    /// cumulative travel time.
    ///
    /// Time complexity: O(m*n) - We need to iterate over every char in every string in the input.
    /// Space complexity: O(1) - Constant extra space used.
    ///
    /// Runtime 31 ms Beats 20%
    /// Memory 9.10 MB Beats 100%
    pub fn garbage_collection(garbage: Vec<String>, travel: Vec<i32>) -> i32 {
        // let (mut total_metal, mut total_paper, mut total_glass) = (0, 0, 0);
        let mut res = 0;
        let (mut metal_travel, mut paper_travel, mut glass_travel) = (0, 0, 0);
        let (mut m, mut p, mut g) = (0, 0, 0);
        for (garbage_string, travel_time) in garbage
            .into_iter()
            .zip(travel.into_iter().chain(std::iter::once(0)))
        {
            // First collect any garbage at this location.
            for c in garbage_string.chars() {
                match c {
                    'M' => m += 1,
                    'P' => p += 1,
                    _ => g += 1,
                }
            }
            if m > 0 {
                // total_metal += m + metal_travel;
                res += m + metal_travel;
                m = 0;
                metal_travel = 0;
            }
            if p > 0 {
                // total_paper += p + paper_travel;
                res += p + paper_travel;
                p = 0;
                paper_travel = 0;
            }
            if g > 0 {
                // total_glass += g + glass_travel;
                res += g + glass_travel;
                g = 0;
                glass_travel = 0;
            }
            // Add travel times in case later we find some of that type of garbage.
            metal_travel += travel_time;
            paper_travel += travel_time;
            glass_travel += travel_time;
        }
        // total_metal + total_paper + total_glass
        res
    }

    /// Compute a prefix sum of travel times, then iterate in reverse over the garbage strings, if
    /// we have found the last index at which we have to pick up each type of garbage, only add the
    /// length of the garbage string to the result, otherwise iterate over the characters trying to
    /// find if this is the last index at which we have to pick up some garbage that don't need to
    /// pick up in the houses after the current one. For each type of garbage for which this is the
    /// last index at which is found, add the total travel time to this spot to the result.
    ///
    /// Time complexity: O(m*n) - We may need to iterate over every char in every string in the input.
    /// Space complexity: O(n) - The prefix sum vector has the same size as the input.
    ///
    /// Runtime 20 ms Beats 100%
    /// Memory 9.24 MB Beats 80%
    pub fn garbage_collection_2(garbage: Vec<String>, travel: Vec<i32>) -> i32 {
        let mut res = 0;
        let travel_time = std::iter::once(0)
            .chain(travel.into_iter().scan(0, |acc, x| {
                *acc += x;
                Some(*acc)
            }))
            .collect::<Vec<_>>();
        let (mut m, mut p, mut g) = (false, false, false);
        for (idx, garbage_string) in garbage.into_iter().enumerate().rev() {
            res += garbage_string.len() as i32;
            if !m || !p || !g {
                for c in garbage_string.chars() {
                    match c {
                        'M' => {
                            if !m {
                                m = true;
                                res += travel_time[idx];
                            }
                        }
                        'P' => {
                            if !p {
                                p = true;
                                res += travel_time[idx];
                            }
                        }
                        _ => {
                            if !g {
                                g = true;
                                res += travel_time[idx];
                            }
                        }
                    }
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["G", "P", "GP", "GG"], vec![2, 4, 3], 21),
        (vec!["MMM", "PGM", "GP"], vec![3, 10], 37),
    ];
    for t in tests {
        assert_eq!(
            Solution::garbage_collection(
                (t.0)
                    .clone()
                    .into_iter()
                    .map(|x| x.to_string())
                    .collect::<Vec<_>>(),
                t.1.clone()
            ),
            t.2
        );
        assert_eq!(
            Solution::garbage_collection_2(
                (t.0).into_iter().map(|x| x.to_string()).collect::<Vec<_>>(),
                t.1
            ),
            t.2
        );
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
