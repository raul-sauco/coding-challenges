// 921. Minimum Add to Make Parentheses Valid
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
//
// Tags: String - Stack - Greedy

struct Solution;
impl Solution {
    /// Iterate over the input keeping track of the number of open left parentheses we find, for
    /// each unmatched or extra parentheses we will need to add a matching one.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(1)
    ///
    /// Runtime 1 ms Beats 58%
    /// Memory 2.18 MB Beats 23%
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let (mut left, mut right) = (0, 0);
        for c in s.chars() {
            if c == '(' {
                right += 1;
            } else if right > 0 {
                right -= 1;
            } else {
                left += 1;
            }
        }
        right + left
    }
}

// Tests.
fn main() {
    let tests = [("())", 1), ("(((", 3)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_add_to_make_valid(t.0.to_string());
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
