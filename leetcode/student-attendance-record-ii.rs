// 552. Student Attendance Record II
// 🔴 Hard
//
// https://leetcode.com/problems/student-attendance-record-ii/
//
// Tags: Dynamic Programming

struct Solution;
impl Solution {
    /// Bottom up dynamic programming, given the number of ways to get n days with the 6
    /// significant variations, 0 and 1 absent days x 0, 1 and 2 consecutive late in the last
    /// days, we can deduce the transitions looking at what happens when we add one of (P, A, L) to
    /// each of them, once we have these transitions figured out, we loop over them n times. There
    /// are more efficient solutions in LeetCode.
    ///
    /// Time complexity: O(n) - We visit each number between 0 and 1 once and do constant time work
    /// for each.
    /// Space complexity: O(1) - We use an array of 6 u64 of extra memory.
    ///
    /// Runtime 8 ms Beats 92%
    /// Memory 2.02 MB Beats 100%
    pub fn check_record(n: i32) -> i32 {
        let mo = 1_000_000_007;
        // Use a dp array with 6 positions, corresponding to the states that we can have.
        // 0 => 0A0L
        // 1 => 0A1L
        // 2 => 0A2L
        // 3 => 1A0L
        // 4 => 1A1L
        // 5 => 1A2L
        let mut dp = [0u64; 6];
        dp[0] = 1;
        for _ in 0..n {
            dp = [
                (dp[0] + dp[1] + dp[2]) % mo,                         // 0 => 0A0L
                dp[0],                                                // 1 => 0A1L
                dp[1],                                                // 2 => 0A2L
                (dp[0] + dp[1] + dp[2] + dp[3] + dp[4] + dp[5]) % mo, // 3 => 1A0L
                dp[3],                                                // 4 => 1A1L
                dp[4],                                                // 5 => 1A2L
            ];
        }
        // dp.iter().fold(0, |acc, x| (acc + x) % mo) as i32
        (dp.iter().sum::<u64>() % mo) as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (1, 3),
        (2, 8),
        (3, 19),
        (4, 43),
        (10, 3536),
        (10101, 183236316),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::check_record(t.0);
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.1, res
            );
        }
    }
    println!();
    if success == tests.len() {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
