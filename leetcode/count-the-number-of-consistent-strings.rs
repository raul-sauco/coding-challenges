// 1684. Count the Number of Consistent Strings
// 🟢 Easy
//
// https://leetcode.com/problems/count-the-number-of-consistent-strings/
//
// Tags: Array - Hash Table - String - Bit Manipulation - Counting

use std::collections::HashSet;

struct Solution;
impl Solution {
    /// Use a way to check in O(1) whether a character is allowed, I used a hash set but we could
    /// also have used a binary array or the bits of a value with >26 bits, for example an i32.
    ///
    /// Time complexity: O(n) - Where n is the number of characters in all the words combined, we
    /// iterate over all characters checking that they are allowed.
    /// Space complexity: O(1) - The hashset can grow to a max of size 26.
    ///
    /// Runtime 16 ms Beats 48%
    /// Memory 2.62 MB Beats 55%
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let allowed: HashSet<char> = allowed.chars().collect();
        let mut res = 0;
        let mut good;
        for word in words {
            good = true;
            for c in word.chars() {
                if !allowed.contains(&c) {
                    good = false;
                    break;
                }
            }
            if good {
                res += 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        ("ab", vec!["ad", "bd", "aaab", "baa", "badab"], 2),
        ("abc", vec!["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
        (
            "cad",
            vec!["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], // typos:ignore
            4,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::count_consistent_strings(
            t.0.to_string(),
            t.1.iter().map(|s| s.to_string()).collect::<_>(),
        );
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
