// 1269. Number of Ways to Stay in the Same Place After Some Steps
// 🔴 Hard
//
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
//
// Tags: Dynamic Programming

struct Solution;
impl Solution {
    /// Solution overview
    ///
    /// Time complexity: O(m*min(m, n)) - Nested loops the outer loop runs step
    /// times, the inner loop runs only through the relevant indexes given the
    /// number of total steps and the current step. At each step, we visit each
    /// index of the array and simulate taken the 2 or three possible moves,
    /// adding the ways to get to the current positions to the number of ways
    /// to get to the position after the move.
    /// Space complexity: O(n) - We use two extra vectors of memory of size
    /// min(step, arr_len).
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.10 MB Beats 100%
    pub fn num_ways(steps: i32, arr_len: i32) -> i32 {
        let steps = steps as usize;
        let arr_len = arr_len as usize;
        let modulus = 1_000_000_007;
        let n = std::cmp::min(steps, arr_len);
        let mut dp = vec![0; n];
        let mut next = dp.clone();
        // One way to reach idx 0 not taking any steps.
        dp[0] = 1;
        for step in 0..steps {
            for i in 0..n.min(step.min(steps / 2) + 1) {
                if i > 0 {
                    next[i - 1] = (dp[i] + next[i - 1]) % modulus;
                }
                next[i] = (dp[i] + next[i]) % modulus;
                if i < n - 1 {
                    next[i + 1] = (dp[i] + next[i + 1]) % modulus;
                }
                dp[i] = 0;
            }
            std::mem::swap(&mut next, &mut dp);
        }
        dp[0]
    }
}

// Tests.
fn main() {
    let tests = [
        (3, 2, 4),
        (2, 4, 2),
        (1, 2, 1),
        (2, 2, 2),
        (4, 2, 8),
        (100, 100, 345787718),
        (1000, 100, 911983206),
        (500, 1000000, 374847123),
    ];
    for t in tests {
        assert_eq!(Solution::num_ways(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
