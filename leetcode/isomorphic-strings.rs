// 205. Isomorphic Strings
// 🟢 Easy
//
// https://leetcode.com/problems/isomorphic-strings/
//
// Tags: Hash Table - String

struct Solution;
impl Solution {
    /// Iterate over both input strings characters at the same time. Map characters in the first
    /// string to characters in the second string and mark the characters in the second string as
    /// seen. If we get a pair of characters that we have not seen before, link them, if we have
    /// seen them before, check that the pair matches the pair seen previously.
    ///
    /// Time complexity: O(n) - We iterate over the number of chars in the strings.
    /// Space complexity: O(1) - Constant extra memory used, two arrays of 128 usize/boolean.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.21 MB Beats 61%
    #[allow(dead_code)]
    pub fn is_isomorphic_fold(s: String, t: String) -> bool {
        let mut mapping: [Option<usize>; 128] = [None; 128];
        let mut seen = [false; 128];
        s.bytes()
            .map(|b| b as usize)
            .zip(t.bytes().map(|b| b as usize))
            .fold(true, |acc, (idx, b)| match mapping[idx] {
                Some(c) => acc && c == b,
                None => {
                    if seen[b] {
                        return false;
                    }
                    seen[b] = true;
                    mapping[idx] = Some(b);
                    acc
                }
            })
    }

    /// Same logic but break early when strings don't match using try_fold.
    ///
    /// Time complexity: O(n) - We iterate over the number of chars in the strings.
    /// Space complexity: O(1) - Constant extra memory used, two arrays of 128 usize/boolean.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.19 MB Beats 96%
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut mapping: [Option<usize>; 128] = [None; 128];
        let mut seen = [false; 128];
        s.bytes()
            .map(|b| b as usize)
            .zip(t.bytes().map(|b| b as usize))
            .try_fold(true, |acc, (idx, b)| match mapping[idx] {
                Some(c) => {
                    if c == b {
                        Ok(true)
                    } else {
                        Err(false)
                    }
                }
                None => {
                    if seen[b] {
                        return Err(false);
                    }
                    seen[b] = true;
                    mapping[idx] = Some(b);
                    Ok(acc)
                }
            })
            .unwrap_or(false)
    }
}

// Tests.
fn main() {
    let tests = [
        ("13", "42", true),
        ("egg", "add", true),
        ("foo", "bar", false),
        ("badc", "baba", false),
        ("paper", "title", true),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::is_isomorphic(t.0.to_string(), t.1.to_string());
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
