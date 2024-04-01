// 58. Length of Last Word
// 🟢 Easy
//
// https://leetcode.com/problems/length-of-last-word/
//
// Tags: String

struct Solution;
impl Solution {
    // Iterate over the characters in the input string in reverse order, ignore any whitespace
    // found before non-whitespace chars, then count the non-whitespace chars until more whitespace
    // is found or we get to the beginning of the string.
    //
    // Time complexity: O(n) - We may iterate over all the input.
    // Space complexity: O(1) - We only use pointers.
    //
    // Runtime 1 ms Beats 71.17%
    // Memory 2.1 MB Beats 34.67%
    #[allow(dead_code)]
    pub fn length_of_last_word_for(s: String) -> i32 {
        // Count of characters in the last word.
        let mut count = 0;
        for char in s.chars().rev() {
            if char == ' ' {
                if count == 0 {
                    continue;
                }
                return count;
            }
            count += 1;
        }
        // If we exit the loop is because the last word starts at index 0
        count
    }

    /// Same logic using iterators.
    ///
    /// Time complexity: O(n) - We iterate over the last word and the following whitespace.
    /// Space complexity: O(1) - Constant extra space used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.14 MB Beats 25%
    pub fn length_of_last_word(s: String) -> i32 {
        s.trim_end()
            .chars()
            .rev()
            .take_while(|c| c.is_alphabetic())
            .count() as i32
    }
}

// Tests.
fn main() {
    let tests = [
        ("", 0),
        ("   ", 0),
        ("l  ", 1),
        ("Hello World", 5),
        ("luffy is still joyboy", 6),
        ("   fly me     to     the     moon    ", 4),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::length_of_last_word(t.0.to_string());
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
