// 1750. Minimum Length of String After Deleting Similar Ends
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
//
// Tags: Two Pointers - String

struct Solution;
impl Solution {
    /// Use a two pointer technique, check the left character against the right character, first
    /// moving the pointers along to the last character that is the same in each end. Remove the
    /// end characters when they are the same.
    ///
    /// Time complexity: O(n) - One pass to convert the string to a Vec<char>, then each element
    /// will at most be visited once.
    /// Space complexity: O(n) - We need a Vec<char> to check by index.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.38 MB Beats 25%
    pub fn minimum_length(s: String) -> i32 {
        let s = s.bytes().collect::<Vec<_>>();
        let (mut l, mut r) = (0, s.len() - 1);
        let mut b;
        while l < r && s[l] == s[r] {
            b = s[l];
            while l <= r && s[l] == b {
                l += 1;
            }
            while r > l && s[r] == b {
                r -= 1;
            }
        }
        r as i32 - l as i32 + 1
    }
}

// Tests.
fn main() {
    let tests = [
        ("a", 1),
        ("bb", 0),
        ("ca", 2),
        ("cabaabac", 0),
        ("aabccabba", 3),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::minimum_length(t.0.to_string());
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
