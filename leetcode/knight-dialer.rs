// 935. Knight Dialer
// 🟠 Medium
//
// https://leetcode.com/problems/knight-dialer/
//
// Tags: Dynamic Programming

const MOD: usize = 1_000_000_007;
struct Solution;
impl Solution {
    /// The dynamic programming solution. Iterate n times computing the number of ways to fall on a
    /// given digit from the previous ones.
    ///
    /// Time complexity: O(n) - We iterate n times, for each, we compute 9 values.
    /// Space complexity: O(1) - We use an array of size 10 of extra memory.
    ///
    /// Runtime 3 ms Beats 70%
    /// Memory 1.98 MB Beats 95%
    pub fn knight_dialer(n: i32) -> i32 {
        let mut dp = [1; 10];
        for _ in 1..n {
            dp = [
                (dp[4] + dp[6]) % MOD,
                (dp[8] + dp[6]) % MOD,
                (dp[7] + dp[9]) % MOD,
                (dp[4] + dp[8]) % MOD,
                (dp[3] + dp[9] + dp[0]) % MOD,
                0,
                (dp[1] + dp[7] + dp[0]) % MOD,
                (dp[2] + dp[6]) % MOD,
                (dp[1] + dp[3]) % MOD,
                (dp[2] + dp[4]) % MOD,
            ];
        }
        (dp.into_iter().sum::<usize>() % 1_000_000_007) as i32
    }
}

// Tests.
fn main() -> Result<(), &'static str> {
    let tests = [(1, 10), (2, 20), (3, 46), (3131, 136006598)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::knight_dialer(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx Test {} failed expected: {} but got {}!\x1b[0m",
                i, t.1, res
            );
        }
    }
    println!("");
    if success == tests.len() {
        println!("\x1b[30;42m» All tests passed!\x1b[0m");
    } else if success == 0 {
        println!("\x1b[41m» All tests failed!\x1b[0m");
    } else {
        println!("\x1b[31;1;43m» Some tests failed!\x1b[0m");
    }
    Ok(())
}
