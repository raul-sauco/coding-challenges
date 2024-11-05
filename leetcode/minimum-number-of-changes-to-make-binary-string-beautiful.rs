// 2914. Minimum Number of Changes to Make Binary String Beautiful
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
//
// Tags: String

struct Solution;
impl Solution {
    /// Iterate over pairs of values, if they don't match, we need to do 1 more change.
    ///
    /// Time complexity: O(n) - We iterate over pairs of values in the input checking if they match
    /// in constant time.
    /// Space complexity: O(n) - The byte slice gets allocated, not sure how to avoid that.
    ///
    /// Runtime 1 ms Beats 100%
    /// Memory 2.27 MB Beats 83%
    pub fn min_changes(s: String) -> i32 {
        s.as_bytes()
            .chunks(2)
            .map(|chunk| if chunk[0] == chunk[1] { 0 } else { 1 })
            .sum()
    }
}

// Tests.
fn main() {
    let tests = [("1001", 2), ("10", 1), ("0000", 0), ("11000111", 1)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_changes(t.0.to_owned());
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
