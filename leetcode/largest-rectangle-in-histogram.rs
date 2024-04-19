// 84. Largest Rectangle in Histogram
// 🔴 Hard
//
// https://leetcode.com/problems/largest-rectangle-in-histogram/
//
// Tags: Array - Stack - Monotonic Stack

use std::iter::once;

struct Solution;
impl Solution {
    /// Use a monotonic non-decreasing stack, before pushing the current height into the stack, pop
    /// any greater heights, since we won't be able to use the taller section in a rectangle with
    /// the current height. When we pop heights, compute the largest rectangle we could build using
    /// that height and update the maximum seen if needed.
    ///
    /// Time complexity: O(n) - We visit each height once and do amortized constant time work.
    /// Space complexity: O(n) - The padded copy of the input and the stack.
    ///
    /// Runtime 13 ms Beats 41%
    /// Memory 3.70 MB Beats 60%
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let heights = once(0)
            .chain(heights.into_iter().map(|x| x as usize))
            .chain(once(0))
            .collect::<Vec<_>>();
        let mut stack = vec![0];
        let mut res = 0;
        for i in 1..heights.len() {
            if let Some(last) = stack.last_mut() {
                if heights[*last] == heights[i] {
                    *last = i;
                    continue;
                }
            }
            while heights[*stack.last().unwrap()] > heights[i] {
                // Compute the maximum rectangle we can obtain with this height and the next
                // smaller height to its left.
                res = res.max(heights[stack.pop().unwrap()] * (i - stack.last().unwrap() - 1));
            }
            stack.push(i);
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2, 4], 4),
        (vec![2, 0, 2], 2),
        (vec![2, 1, 5, 6, 2, 3], 10),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::largest_rectangle_area(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
