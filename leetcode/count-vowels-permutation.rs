// 1220. Count Vowels Permutation
// 🔴 Hard
//
// https://leetcode.com/problems/count-vowels-permutation/
//
// Tags: Dynamic Programming

struct Solution;
impl Solution {
    /// For each length of the string we are creating, we can compute the number
    /// of ways that we can build it using the number of ways in which we built
    /// the string that is one character shorter for each of the 5 possible ways
    /// in which it can finish, then using that value and adding the vowels that
    /// we are allowed to for each ending.
    ///
    /// Time complexity: O(n) - One loop that runs n-1 times and does constant
    /// time work inside the loop.
    /// Space complexity: O(1) - We use one array of 5 elements of extra memory
    /// that will be stored in the stack.
    ///
    /// Runtime 1 ms Beats 100%
    /// Memory 1.99 MB Beats 90.91%
    pub fn count_vowel_permutation(n: i32) -> i32 {
        let modu = 1_000_000_007;
        let mut dp = [1i64; 5];
        for _ in 0..n - 1 {
            (dp[0], dp[1], dp[2], dp[3], dp[4]) = (
                (dp[1] + dp[2] + dp[4]) % modu,
                (dp[0] + dp[2]) % modu,
                (dp[1] + dp[3]) % modu,
                dp[2],
                (dp[2] + dp[3]) % modu,
            );
        }
        (dp.iter().sum::<i64>() % modu) as i32
    }
}

// Tests.
fn main() {
    let tests = [(1, 5), (2, 10), (5, 68), (20000, 759959057)];
    for t in tests {
        assert_eq!(Solution::count_vowel_permutation(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
