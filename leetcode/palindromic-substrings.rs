// 647. Palindromic Substrings
// 🟠 Medium
//
// https://leetcode.com/problems/palindromic-substrings/
//
// Tags: String - Dynamic Programming

struct Solution;
impl Solution {
    /// Visit each character, and each two character in the input, and expand from them while the
    /// two next characters match.
    ///
    /// Time complexity: O(n^2) - For each position, we run a two-pointer algorithm that could
    /// visit each position of the input.
    /// Space complexity: O(n) - The chars vector that we use to index characters.
    ///
    /// Runtime 1 ms Beats 77.14%
    /// Memory 2.16 MB Beats 42.86%
    pub fn count_substrings(s: String) -> i32 {
        let chars: Vec<_> = s.chars().collect();
        let mut res = 0;
        let (mut l, mut r);
        for i in 0..chars.len() {
            for j in [i, i + 1] {
                (l, r) = (i, j);
                while r < chars.len() && chars[l] == chars[r] {
                    res += 1;
                    if l == 0 {
                        break;
                    }
                    l -= 1;
                    r += 1;
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [("abc", 3), ("aaa", 6)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::count_substrings(t.0.to_string());
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
