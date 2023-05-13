// 2466. Count Ways To Build Good Strings
// 🟠 Medium
//
// https://leetcode.com/problems/count-ways-to-build-good-strings/
//
// Tags: Dynamic Programming

struct Solution;
impl Solution {
    /// Use dynamic programming, create a dp array of intermediate results where
    /// dp[i] is how many different ways we can build a string of length i, we
    /// can use dp[i] to add zero 0s and one 1s to however many ways we could
    /// build that string and update dp[i+zero] and dp[i+one] with these values.
    ///
    /// Time complexity: O(n) - Where n is equal to the parameter high plus one,
    /// we iterate over all values 0..n and do O(1) work for each.
    /// Space complexity: O(n) - The dp array has a length of n.
    ///
    /// Runtime 4 ms Beats 100%
    /// Memory 2.6 MB Beats 100%
    pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
        let (zero, one) = (zero as usize, one as usize);
        let (low, high) = (low as usize, high as usize);
        let n = high;
        let mut res = 0;
        let m = 1_000_000_007;
        let mut dp = vec![0; n + 1];
        dp[0] = 1;
        for i in 0..n + 1 {
            // If this index is between high and low, add it to the result.
            if low <= i && i <= high {
                if i32::MAX - dp[i] < res {
                    res = (res as i64 + dp[i] as i64) as i32 % m;
                } else {
                    res = (res + dp[i]) % m;
                }
            }
            // Can we add zero 0s?
            if i + zero < n + 1 {
                dp[i + zero] = (dp[i + zero] + dp[i]) % m;
            }
            // Can we add one 1s?
            if i + one < n + 1 {
                dp[i + one] = (dp[i + one] + dp[i]) % m;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(3, 3, 1, 1, 8), (2, 3, 1, 2, 5)];
    for t in tests {
        assert_eq!(Solution::count_good_strings(t.0, t.1, t.2, t.3), t.4);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
