// 70. Climbing Stairs
// 🟢 Easy
//
// https://leetcode.com/problems/climbing-stairs/
//
// Tags: Math - Dynamic Programming - Memoization

struct Solution;
impl Solution {
    /// See the Python solution for the other solutions, brute-force, memoized then dp. This DP
    /// solution uses the fact that at each step, we will be able to do two things, take one step
    /// or take two steps, then from each position, we can add the number of ways we have to get
    /// there to the next two positions, the equivalent of taking one or two steps.
    ///
    /// Time complexity: O(n) - The loop runs n times.
    /// Space complexity: O(1) - We use an array of fixed size 47 to force use of the stack, if
    /// value of n could be much greater, we would need to use a vector and the space complexity
    /// would be O(n)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.08 MB Beats 71.71%
    #[allow(dead_code)]
    pub fn climb_stairs_using_array(n: i32) -> i32 {
        if n < 1 || n > 45 {
            panic!("Expected the input to be in the range 1..45");
        }
        let n = n as usize;
        let mut dp = [0; 47];
        dp[0] = 1;
        for i in 0..n {
            dp[i + 1] += dp[i];
            dp[i + 2] += dp[i];
        }
        dp[n]
    }

    /// Similar logic but keep track only of the last two values computed instead of all of them.
    ///
    /// Time complexity: O(n) - The loop runs n times.
    /// Space complexity: O(1) - We use two integer variables of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.14 MB Beats 33.99%
    #[allow(dead_code)]
    pub fn climb_stairs_two_vars(n: i32) -> i32 {
        // a is dp[i-2], b is dp[i-1]
        let (mut prev, mut res) = (0, 1);
        for _ in 0..n {
            (prev, res) = (res, prev + res);
        }
        res
    }

    /// Same logic using an iterator and fold.
    ///
    /// Time complexity: O(n) - The loop runs n times.
    /// Space complexity: O(1) - We use an iterator that stores two i32 as its state.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.10 MB Beats 71.71%
    pub fn climb_stairs(n: i32) -> i32 {
        (0..n).fold((1, 0), |(res, prev), _| (res + prev, res)).0
    }
}

// Tests.
fn main() {
    let tests = [(1, 1), (2, 2), (3, 3), (45, 1836311903)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::climb_stairs(t.0);
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
