// 1662. Check If Two String Arrays are Equivalent
// 🟢 Easy
//
// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
//
// Tags: Array - String

use itertools::EitherOrBoth::{Both, Left, Right};
use itertools::Itertools;

struct Solution;
impl Solution {
    #[allow(dead_code)]
    /// This solution does not run on LeetCode.
    pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
        word1
            .iter()
            .flat_map(|s| s.chars())
            .zip_longest(word2.iter().flat_map(|s| s.chars()))
            .all(|x| match x {
                Both(a, b) => a == b,
                Left(_) | Right(_) => false,
            })
    }

    /// Create a flattened iterator for each of the inputs, iterate over the characters generated
    /// by calling next on both iterators until we don't have more characters or the values
    /// generated don't match.
    ///
    /// Time complexity: O(min(m,n)) - Where m, n is the number of characters in all the Strings in
    /// word1, word2. The algorithm checks characters against each other until if finds a pair that
    /// is not equal or it runs out of characters in one of the inputs.
    /// Space complexity: O(1) - We use iterators to avoid allocating extra memory.
    ///
    /// Runtime 1 ms Beats 89.29%
    /// Memory 1.96 MB Beats 100%
    pub fn array_strings_are_equal_2(word1: Vec<String>, word2: Vec<String>) -> bool {
        let mut it1 = word1.iter().flat_map(|s| s.chars());
        let mut it2 = word2.iter().flat_map(|s| s.chars());
        loop {
            match (it1.next(), it2.next()) {
                (None, None) => return true,
                (None, Some(_)) | (Some(_), None) => return false,
                (Some(a), Some(b)) => {
                    if a != b {
                        return false;
                    }
                }
            }
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["ab", "c"], vec!["a", "bc"], true),
        (vec!["a", "cb"], vec!["ab", "c"], false),
        (vec!["abc", "d", "defg"], vec!["abcddef"], false),
        (vec!["abc", "d", "defg"], vec!["abcddefg"], true),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::array_strings_are_equal_2(
            t.0.iter().map(|x| x.to_string()).collect::<Vec<_>>(),
            t.1.iter().map(|x| x.to_string()).collect::<Vec<_>>(),
        );
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
    println!("");
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
