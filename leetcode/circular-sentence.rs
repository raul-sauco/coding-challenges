// 2490. Circular Sentence
// 🟢 Easy
//
// https://leetcode.com/problems/circular-sentence/
//
// Tags: String

struct Solution;
impl Solution {
    /// Save the first char in the input, then iterate over the chars in the input checking that
    /// the chars before and after blank spaces match, if any of them do not, return false,
    /// otherwise return first == last.
    ///
    /// Time complexity: O(n) - We may visit all chars in the input.
    /// Space complexity: O(1) - We store two chars and one bool.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.16 MB Beats 50%
    pub fn is_circular_sentence(sentence: String) -> bool {
        let first = sentence.chars().next().expect("A first char");
        let (mut last, mut after_blank) = (first, false);
        for c in sentence.chars() {
            match c {
                ' ' => after_blank = true,
                _ => {
                    if after_blank && c != last {
                        return false;
                    }
                    after_blank = false;
                    last = c;
                }
            }
        }
        first == last
    }
}

// Tests.
fn main() {
    let tests = [
        ("leetcode exercises sound delightful", true),
        ("eetcode", true),
        ("Leetcode is cool", false),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::is_circular_sentence(t.0.to_owned());
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
