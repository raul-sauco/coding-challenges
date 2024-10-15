// 2938. Separate Black and White Balls
// 🟠 Medium
//
// https://leetcode.com/problems/separate-black-and-white-balls/
//
// Tags: Two Pointers - String - Greedy

struct Solution;
impl Solution {
    /// Iterate the string from the left keeping track of where the last white ball in placed, for
    /// each white ball found, move it to the furthest left spot possible and increment the index
    /// of the next white ball, add the number of moves done to the result. Once you have placed
    /// all the white balls on the left, all the black ones will be on the right.
    ///
    /// Time complexity: O(n) - O(1) work for each element in the input.
    /// Space complexity: O(1)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.43 MB Beats 40%
    #[allow(dead_code)]
    pub fn minimum_steps_loop(s: String) -> i64 {
        let (mut res, mut next_white_idx) = (0, 0);
        for (i, b) in s.bytes().enumerate() {
            if b == b'0' {
                res += (i - next_white_idx) as i64;
                next_white_idx += 1;
            }
        }
        res
    }

    /// Same logic but using an iterator.
    ///
    /// Time complexity: O(n) - O(1) work for each element in the input.
    /// Space complexity: O(1)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.34 MB Beats 100%
    pub fn minimum_steps(s: String) -> i64 {
        s.bytes()
            .enumerate()
            .fold((0, 0), |(res, idx), (i, b)| {
                if b == b'0' {
                    (res + (i - idx) as i64, idx + 1)
                } else {
                    (res, idx)
                }
            })
            .0
    }
}

// Tests.
fn main() {
    let tests = [("101", 1), ("100", 2), ("0111", 0), ("0011000010", 11)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::minimum_steps(t.0.to_string());
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
