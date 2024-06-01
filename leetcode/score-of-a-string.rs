// 3110. Score of a String
// 🟢 Easy
//
// https://leetcode.com/problems/score-of-a-string/
//
// Tags: String

struct Solution;
impl Solution {
    /// Iterate over windows of size 2 adding their score to the result.
    ///
    /// Time complexity: O(n) -
    /// Space complexity: O(1) -
    ///
    /// Runtime 2 ms Beats 48%
    /// Memory 2.02 MB Beats 81%
    pub fn score_of_string(s: String) -> i32 {
        s.as_bytes().windows(2).fold(0, |acc, sl| {
            acc + if sl[0] > sl[1] {
                sl[0] - sl[1]
            } else {
                sl[1] - sl[0]
            } as i32
        })
    }
}

// Tests.
fn main() {
    let tests = [
        ("hello", 13),
        ("zaz", 50),
        ("tgtktpytavhslrnrrxwtbfhqyqronmvlqdxbpsymhgwyb", 374),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::score_of_string(t.0.to_string());
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
