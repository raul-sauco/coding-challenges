// 2486. Append Characters to String to Make Subsequence
// 🟠 Medium
//
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
//
// Tags: Two Pointers - String - Greedy

use std::i32;

struct Solution;
impl Solution {
    /// We need to match all characters in t, get a pointer to the first character in t and start
    /// trying to match it with a character in s, each time we match, we move both the pointer in s
    /// and t, while we cannot match, we move only the pointer in s. If we run out of characters in
    /// t, we have a full match and return 0, if we run out of characters in s, we need to match
    /// all remaining characters in t, including the one under the pointer.
    ///
    /// Time complexity: O(m+n) - We may iterate all characters in both input strings.
    /// Space complexity: O(1) - We use iterators.
    ///
    /// Runtime 2 ms Beats 66%
    /// Memory 2.20 MB Beats 66%
    #[allow(dead_code)]
    pub fn append_characters_loop(s: String, t: String) -> i32 {
        let (mut it_s, mut it_t) = (s.chars(), t.chars());
        let (mut s_next, mut t_next) = (it_s.next(), it_t.next());
        loop {
            match (s_next, t_next) {
                (None, None) | (Some(_), None) => return 0,
                (None, Some(_)) => break,
                (Some(cs), Some(ct)) => {
                    if cs == ct {
                        t_next = it_t.next();
                    }
                    s_next = it_s.next();
                }
            }
        }
        it_t.count() as i32 + 1
    }

    /// Similar logic but reusing the logic of the solution of 392. Is Subsequence.
    ///
    /// Time complexity: O(m+n) - We may iterate all characters in both input strings.
    /// Space complexity: O(1) - We use iterators.
    ///
    /// Runtime 2 ms Beats 66%
    /// Memory 2.30 MB Beats 33%
    pub fn append_characters(s: String, t: String) -> i32 {
        let mut s_chars = s.chars();
        let mut found;
        let mut remaining = t.len() as i32;
        for s_c in t.chars() {
            found = false;
            while let Some(t_c) = s_chars.next() {
                if s_c == t_c {
                    found = true;
                    break;
                }
            }
            if !found {
                return remaining;
            }
            remaining -= 1;
        }
        0
    }
}

// Tests.
fn main() {
    let tests = [
        ("coaching", "coding", 4),
        ("abcde", "a", 0),
        ("z", "abcde", 5),
        ("abczde", "abcde", 0),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::append_characters(t.0.to_string(), t.1.to_string());
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.2, res
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
