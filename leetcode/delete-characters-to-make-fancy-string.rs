// 1957. Delete Characters to Make Fancy String
// 🟢 Easy
//
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/
//
// Tags: String

struct Solution;
impl Solution {
    /// Iterate over the input counting the frequency of characters, append to the result string
    /// while the current character is repeated a maximum of 2 times.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(n)
    ///
    /// Runtime 2 ms Beats 100%
    /// Memory 2.51 MB Beats 28.57%
    pub fn make_fancy_string(s: String) -> String {
        let mut res = String::with_capacity(s.len());
        let mut last = '?';
        let mut repeated = false;
        for c in s.chars() {
            if c == last {
                if repeated {
                    continue;
                }
                repeated = true;
            } else {
                last = c;
                repeated = false;
            }
            res.push(c);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [("leeetcode", "leetcode"), ("aaabaaaa", "aabaa")];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::make_fancy_string(t.0.to_string());
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
