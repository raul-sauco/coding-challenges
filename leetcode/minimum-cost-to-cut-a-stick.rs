// 1547. Minimum Cost to Cut a Stick
// 🔴 Hard
//
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
//
// Tags: Array - Dynamic Programming - Sorting

struct Solution {}
impl Solution {
    /// Start with the trivial stick sections, the ones in which we do not want
    /// to do any cuts, and have a cost of 0. Then start growing the sections
    /// deciding in each step which is the next least costly cut.
    ///
    /// Time complexity: O(m^3) - Three levels of nested loops in which we may
    /// iterate over a maximum of m values.
    /// Space complexity: O(m^2) - The cache that we use is of size m*m where
    /// m is the number of cuts that we want to do.
    ///
    /// Runtime 11 ms Beats 66.67%
    /// Memory 2.3 MB Beats 66.67%
    pub fn min_cost(n: i32, cuts: Vec<i32>) -> i32 {
        let m = cuts.len();
        let mut cuts = cuts;
        cuts.push(0);
        cuts.push(n);
        cuts.sort_unstable();
        let mut dp = vec![vec![0; m + 2]; m + 2];
        for diff in 2..m + 2 {
            for left in 0..m + 2 - diff {
                let right = left + diff;
                dp[left][right] = i32::MAX;
                for mid in left + 1..right {
                    dp[left][right] = dp[left][right]
                        .min(dp[left][mid] + dp[mid][right] + cuts[right] - cuts[left]);
                }
            }
        }
        dp[0][m + 1]
    }
}

fn main() {
    let tests = [(7, vec![1, 3, 4, 5], 16), (9, vec![5, 6, 1, 4, 2], 22)];
    for t in tests {
        assert_eq!(Solution::min_cost(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
