// 1903. Largest Odd Number in String
// 🟢 Easy
//
// https://leetcode.com/problems/largest-odd-number-in-string/
//
// Tags: Math - String - Greedy

struct Solution;
impl Solution {
    /// Start checking the digits from the back of the string, the first odd digit that we find can
    /// be proved to form the largest odd starting at the first character and ending at this odd.
    ///
    /// Time complexity: O(log(n)) - Where n is num as an int, we iterate over each digit of num in
    /// the worst case.
    /// Space complexity: O(1) - We use an iterator and a string slice.
    ///
    /// Runtime 3 ms Beats 34.38%
    /// Memory 2.32 MB Beats 56.25%
    pub fn largest_odd_number(num: String) -> String {
        for (i, d) in num.chars().rev().enumerate() {
            if "13579".contains(d) {
                return num[..num.len() - i].to_string();
            }
        }
        "".to_string()
    }
}

// Tests.
fn main() {
    let tests = [("52", "5"), ("4206", ""), ("35427", "35427")];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::largest_odd_number(t.0.to_string());
        if res == t.1.to_string() {
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
