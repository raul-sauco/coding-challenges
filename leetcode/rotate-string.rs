// 796. Rotate String
// 🟢 Easy
//
// https://leetcode.com/problems/rotate-string/
//
// Tags: String - String Matching

struct Solution;
impl Solution {
    /// The easiest solution is to concatenate one of the strings and check if the other is a
    /// substring of the concatenation.
    ///
    /// Time complexity: O(n^2) - The nested loop.
    /// Space complexity: O(n) - The char vec.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.21 MB Beats 26%
    #[allow(dead_code)]
    pub fn rotate_string_nsqr(s: String, goal: String) -> bool {
        let (m, n) = (s.len(), goal.len());
        if m != n {
            return false;
        }
        let goal = goal.chars().chain(goal.chars()).collect::<Vec<_>>();
        let first_char = s.chars().next().unwrap();
        for idx in 0..n {
            if goal[idx] != first_char {
                continue;
            }
            // Current character matches the first character, try a match.
            let mut is_match = true;
            for (i, c) in s.chars().enumerate() {
                if c != goal[idx + i] {
                    is_match = false;
                    break;
                }
            }
            if is_match {
                return true;
            }
        }
        false
    }

    /// The same solution is much cleaner using built-in functions, probably faster as well.
    ///
    /// Time complexity: O(n^2?) - String::contains internally uses std::find() which uses loops
    /// just like the previous solution does, they do remark that most times it will run in O(n)
    /// Space complexity: O(n) - Repeat creates a new string.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.11 MB Beats 26%
    #[allow(dead_code)]
    pub fn rotate_string(s: String, goal: String) -> bool {
        s.len() == goal.len() && goal.repeat(2).contains(&s)
    }
}

// Tests.
fn main() {
    let tests = [("abcde", "cdeab", true), ("abcde", "abced", false)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::rotate_string(t.0.to_owned(), t.1.to_owned());
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
