// 1894. Find the Student that Will Replace the Chalk
// 🟠 Medium
//
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
//
// Tags: Array - Binary Search - Simulation - Prefix Sum

use std::i32;

struct Solution;
impl Solution {
    /// Compute the sum of the chalk used by all students in one iteration over all elements in
    /// chalk, mod the total chalk by that value to obtain the amount of chalk remaining in the
    /// last loop, which could also be the first. Then iterate over the elements using chalk
    /// until we don't have enough for the next student and return their index. We could do
    /// small optimizations, like use a prefix sum and then use binary search to find the index of
    /// the student in the last loop, but since we need to compute the sum of the input vector, we
    /// still need to visit each element.
    ///
    /// Time complexity: O(n) - We visit each element to compute the total sum and to find the
    /// index of the student that replaces the chalk.
    /// Space complexity: O(1) - We store the total sum and the remainder.
    ///
    /// Runtime 12 ms Beats 76%
    /// Memory 3.28 MB Beats 52%
    pub fn chalk_replacer(chalk: Vec<i32>, k: i32) -> i32 {
        let total = chalk.iter().map(|x| *x as usize).sum::<usize>();
        // The total chalk left on the last round.
        let mut rem = k as usize % total;
        for (i, c) in chalk.into_iter().map(|x| x as usize).enumerate() {
            if c > rem {
                return i as i32;
            }
            rem -= c;
        }
        unreachable!("initial remaining value should be less than chalk total")
    }
}

// Tests.
fn main() {
    let tests = [(vec![5, 1, 5], 22, 0), (vec![3, 4, 1, 2], 25, 1)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::chalk_replacer(t.0.clone(), t.1);
        if res == t.2 {
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
