// 2000. Reverse Prefix of Word
// 🟢 Easy
//
// https://leetcode.com/problems/reverse-prefix-of-word/
//
// Tags: Two Pointers - String

struct Solution;
impl Solution {
    /// Check if the character is found in the input, if found reverse the characters up to and
    /// including that index, then append the remaining characters and return that.
    ///
    /// Time complexity: O(n) - We iterate over the characters once to find the first index of, if
    /// found, we iterate in reverse over the characters up to that index then forward over the
    /// characters after that index, building the result.
    /// Space complexity: O(1) - Unless iterators are internally using extra memory, which I don't
    /// think is the case, then constant extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.07 MB Beats 90%
    pub fn reverse_prefix(word: String, ch: char) -> String {
        match word.chars().position(|c| c == ch) {
            Some(i) => word[..=i]
                .chars()
                .rev()
                .chain(word[i + 1..].chars())
                .collect(),
            None => word,
        }
    }
}

// Tests.
fn main() {
    let tests = [
        ("abcdefd", 'd', "dcbaefd"),
        ("xyxzxe", 'z', "zxyxxe"),
        ("abcd", 'z', "abcd"),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::reverse_prefix(t.0.to_string(), t.1);
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
