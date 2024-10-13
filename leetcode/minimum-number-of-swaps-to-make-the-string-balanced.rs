// 1963. Minimum Number of Swaps to Make the String Balanced
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
//
// Tags: Two Pointers - String - Stack - Greedy

struct Solution;
impl Solution {
    /// Iterate the string, when the number of closing brackets is greater
    /// than the number of opening brackets, we swap one with the furthest right opening bracket in
    /// the string. We can do that using and updating counts rather than actually updating the
    /// input string.
    ///
    /// Time complexity: O(n) - We visit each character in the input and do constant time work for
    /// each.
    /// Space complexity: O(1)
    ///
    /// Runtime 8 ms Beats 76%
    /// Memory 4.70 MB Beats 75%
    pub fn min_swaps(s: String) -> i32 {
        // Not needed but helps with early break.
        let mut remaining_opening = s.len() / 2;
        let mut swaps = 0;
        let (mut opening, mut closing) = (0, 0);
        for c in s.chars() {
            match c {
                '[' => {
                    opening += 1;
                    remaining_opening -= 1;
                }
                _ => closing += 1,
            }
            if closing > opening {
                swaps += 1;
                remaining_opening -= 1;
                opening += 1;
                closing -= 1;
            }
            if remaining_opening == 0 {
                break;
            }
        }
        swaps
    }
}

// Tests.
fn main() {
    let tests = [("][][", 1), ("]]][[[", 2), ("[]", 0)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_swaps(t.0.to_string());
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
