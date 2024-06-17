// 633. Sum of Square Numbers
// 🟠 Medium
//
// https://leetcode.com/problems/sum-of-square-numbers/
//
// Tags: Math - Two Pointers - Binary Search

use std::collections::HashSet;

struct Solution;
impl Solution {
    /// Brute force solution with an optimization, we compute all squares up to c, then iterate
    /// over 0..sqrt(c) checking if b is in the hashset.
    ///
    /// Time complexity: O(n) - Where n is sqrt(c) we iterate over all values in that range and do
    /// constant time work for each. We also compute all the squares in that same range.
    /// Space complexity: O(n) - The hashset will have all the squares between 0 and sqrt(c).
    ///
    /// Runtime 37 ms Beats 14%
    /// Memory 2.98 MB Beats 7%
    #[allow(dead_code)]
    pub fn judge_square_sum_hs(c: i32) -> bool {
        let c = c as i64;
        // The biggest value of one operant would be when the other is zero.
        let upper_limit = (c as f64).sqrt() as i64;
        let mut all_squares = HashSet::new();
        let (mut i, mut sqrt) = (0, 0);
        while sqrt <= c {
            all_squares.insert(sqrt);
            i += 1;
            sqrt = i * i;
        }
        for a in 0..=upper_limit {
            // c - a^2 == b ? true : loop
            if all_squares.contains(&(c - a * a)) {
                return true;
            }
        }
        false
    }

    /// Use binary search, we are looking for a,b and they both are between 0 and sqrt(c) start
    /// with both of them at the ends of the range and compute the result of a^2+b^2 when the
    /// result is smaller than c, we need to increase a, when the result is bigger, we need to
    /// decrease b.
    ///
    /// Time complexity: O(sqrt(c)*log(c)) - We do binary search in the space 0..sqrt(c)
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.11 MB Beats 50%
    pub fn judge_square_sum(c: i32) -> bool {
        let (mut l, mut r, c) = (0, (c as f64).sqrt() as usize, c as usize);
        let mut mid;
        while l <= r {
            mid = l * l + r * r;
            match mid.cmp(&c) {
                std::cmp::Ordering::Less => l += 1,
                std::cmp::Ordering::Equal => return true,
                std::cmp::Ordering::Greater => r -= 1,
            }
        }
        false
    }
}

// Tests.
fn main() {
    let tests = [
        (0, true),
        (1, true),
        (2, true),
        (3, false),
        (4, true),
        (5, true),
        (6, false),
        (7, false),
        (1531130, true),
        (i32::MAX, false),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::judge_square_sum(t.0);
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
