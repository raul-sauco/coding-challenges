// 1657. Determine if Two Strings Are Close
// 🟠 Medium
//
// https://leetcode.com/problems/determine-if-two-strings-are-close/
//
// Tags: Hash Table - String - Sorting - Counting

struct Solution;
impl Solution {
    /// String lengths need to be the same, the same characters need to exists in both of them,
    /// because we can only change an existing character to another one, and the counts of any
    /// group of characters need to also be the same, because we can change either none or all of
    /// the same characters to another existing character.
    ///
    /// Time complexity: O(n) - We visit each character in both strings, if they are not the same
    /// length, we return false in O(1) before iterating over the characters. After that we operate
    /// and sort the counts, which have a fixed size of 26, so that work is O(1) as well.
    /// Space complexity: O(1) - We store a 2D array of 2*26 positions.
    ///
    /// Runtime 5 ms Beats 83.08%
    /// Memory 2.42 MB Beats 27.69%
    pub fn close_strings(word1: String, word2: String) -> bool {
        if word1.len() != word2.len() {
            return false;
        }
        let mut counts = [[0; 26]; 2];
        word1.bytes().zip(word2.bytes()).for_each(|(a, b)| {
            counts[0][(a - b'a') as usize] += 1;
            counts[1][(b - b'a') as usize] += 1;
        });
        if counts[0]
            .iter()
            .zip(counts[1].iter())
            .any(|(&a, &b)| (a > 0) != (b > 0))
        {
            return false;
        }
        counts[0].sort_unstable();
        counts[1].sort_unstable();
        counts[0] == counts[1]
    }
}

// Tests.
fn main() {
    let tests = [
        ("abc", "bca", true),
        ("a", "aa", false),
        ("cabbba", "abbccc", true),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::close_strings(t.0.to_string(), t.1.to_string());
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
