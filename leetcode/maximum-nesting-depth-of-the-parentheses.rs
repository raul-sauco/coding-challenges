// 1614. Maximum Nesting Depth of the Parentheses
// 🟢 Easy
//
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
//
// Tags: String - Stack

struct Solution;
impl Solution {
    /// Iterate the characters in the input keeping track of the level of nesting, '(' adds one to
    /// the current level, ')' brings us one level up. This solution is valid only because they
    /// guarantee that the input is a "valid parentheses string (VPS)" if that was not the case, we
    /// would need a stack to keep track of the opening parentheses.
    ///
    /// Time complexity: O(n) - We visit each character in the input.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 1 ms Beats 86%
    /// Memory 1.96 MB Beats 100%
    pub fn max_depth(s: String) -> i32 {
        let (mut current_depth, mut max_depth) = (0, 0);
        for c in s.chars() {
            match c {
                '(' => {
                    current_depth += 1;
                    max_depth = max_depth.max(current_depth);
                }
                ')' => current_depth -= 1,
                _ => (),
            }
        }
        max_depth
    }
}

// Tests.
fn main() {
    let tests = [("(1+(2*3)+((8)/4))+1", 3), ("(1)+((2))+(((3)))", 3)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_depth(t.0.to_string());
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
