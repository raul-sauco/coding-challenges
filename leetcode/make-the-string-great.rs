// 1544. Make The String Great
// 🟢 Easy
//
// https://leetcode.com/problems/make-the-string-great/
//
// Tags: String - Stack

struct Solution;
impl Solution {
    /// Use a stack, iterate over the characters in the input pushing them into the stack unless
    /// the last character in the stack is the same character in the opposite case, in that case
    /// pop the top of the stack and do not push the current character.
    ///
    /// Time complexity: O(n) - We visit each character in the input and either push it into the
    /// stack or pop the last character in the stack, both of them constant time.
    /// Space complexity: O(n) - The stack.
    ///
    /// Runtime 1 ms Beats 68%
    /// Memory 1.98 MB Beats 97%
    pub fn make_good(s: String) -> String {
        let mut stack = Vec::with_capacity(s.len());
        for b in s.bytes() {
            if let Some(top) = stack.last() {
                if (b as i32 - *top as i32).abs() == 32 {
                    stack.pop();
                } else {
                    stack.push(b);
                }
            } else {
                stack.push(b);
            }
        }
        stack.into_iter().map(|b| b as char).collect()
    }
}

// Tests.
fn main() {
    let tests = [("s", "s"), ("leEeetcode", "leetcode"), ("abBAcC", "")];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::make_good(t.0.to_string());
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
