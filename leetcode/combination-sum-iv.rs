// 377. Combination Sum IV
// 🟠 Medium
//
// https://leetcode.com/problems/combination-sum-iv/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// We can use bottom-up dynamic programming, for each value up to target,
    /// we visit all the values in the input vector, for each value, we can add
    /// the ways to combine up to ct-val to the ways to combine up to ct.
    ///
    /// Time complexity: O(n*t) - Two nested loops, in the outer loop we iterate
    /// target times, in the inner one we iterate over all values smaller than
    /// the current combination target, that could be all n of them.
    /// Space complexity: O(n+t) - We copy the input vector n and create a new
    /// vector dp of size t.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.34 MB Beats 16%
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
        let mut nums = nums.clone();
        nums.sort_unstable();
        let t = target as usize;
        let mut dp = vec![0; t + 1];
        dp[0] = 1;
        for ct in 1..t + 1 {
            for num in nums.iter() {
                let numz = *num as usize;
                if numz > ct {
                    break;
                }
                dp[ct] += dp[ct - numz];
            }
        }
        dp[t]
    }
}

// Tests.
fn main() {
    let tests = [(vec![1, 2, 3], 4, 7), (vec![9], 3, 0)];
    for t in tests {
        assert_eq!(Solution::combination_sum4(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
