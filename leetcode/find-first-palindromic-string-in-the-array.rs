// 2108. Find First Palindromic String in the Array
// 🟢 Easy
//
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
//
// Tags: Array - Two Pointers - String

struct Solution;
impl Solution {
    /// Use a two-pointer approach, since we cannot index characters in a String in Rust, use a
    /// forward and a backwards iterator to compare the characters.
    ///
    /// Time complexity: O(m*n) - We may iterate over every character in each word in the input.
    /// Space complexity: O(1) - We avoid storing a reversed copy of the input using iterators.
    ///
    /// Runtime 4 ms Beats 79.41%
    /// Memory 2.22 MB Beats 29.41%
    pub fn first_palindrome(words: Vec<String>) -> String {
        words
            .into_iter()
            .find(|w| {
                w.chars()
                    .take(w.len() / 2)
                    .eq(w.chars().rev().take(w.len() / 2))
            })
            .unwrap_or("".to_string())
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["abc", "car", "ada", "racecar", "cool"], "ada"),
        (vec!["notapalindrome", "racecar"], "racecar"),
        (vec!["def", "ghi"], ""),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::first_palindrome(t.0.iter().map(|s| s.to_string()).collect::<Vec<_>>());
        if res == t.1.to_string() {
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
