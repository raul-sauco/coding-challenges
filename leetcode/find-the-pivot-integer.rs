// 2485. Find the Pivot Integer
// 🟢 Easy
//
// https://leetcode.com/problems/find-the-pivot-integer/
//
// Tags: Math - Prefix Sum

struct Solution;
impl Solution {
    /// The sum of values up to any x can be computed as x * (x+1) / 2. Use that fact to binary
    /// search the solution, if not found, return -1.
    ///
    /// Time complexity: O(log(n)) - Binary search from 1 to n.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 1 ms Beats 70%
    /// Memory 2.02 MB Beats 58%
    pub fn pivot_integer(n: i32) -> i32 {
        let n = n as usize;
        let (mut l, mut r) = (0, n);
        let sum = n * (n + 1) / 2;
        let (mut m, mut ls, mut rs);
        while l <= r {
            m = (r + l) / 2;
            ls = m * (m + 1) / 2;
            rs = sum - ls + m;
            if ls < rs {
                l += 1;
            } else if ls > rs {
                r -= 1;
            } else {
                return m as i32;
            }
        }
        -1
    }

    /// Use math, the middle of the arithmetic progression can be computed using the sqrt of the
    /// sum of the total if it exists.
    ///
    /// Time complexity: O(1) - Two math operations, this could be O(log(n)) depending on how sqrt
    /// is implemented.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 1 ms Beats 70%
    /// Memory 1.99 MB Beats 100%
    #[allow(dead_code)]
    pub fn pivot_integer_math(n: i32) -> i32 {
        let sum = n * (n + 1) / 2;
        let sqr = f64::sqrt(sum.into()) as i32;
        if sqr * sqr == sum {
            sqr
        } else {
            -1
        }
    }
}

// Tests.
fn main() {
    let tests = [(8, 6), (1, 1), (4, -1)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::pivot_integer(t.0);
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {} but got {}!!\x1b[0m",
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
