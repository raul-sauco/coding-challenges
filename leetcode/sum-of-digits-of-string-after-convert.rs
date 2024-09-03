// 1945. Sum of Digits of String After Convert
// 🟢 Easy
//
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
//
// Tags: String - Simulation

struct Solution;
impl Solution {
    /// Convert the input string to an integer, then sum its digits k time.
    ///
    /// Time complexity: O(n) - We iterate over each character to get its integer value.
    /// Space complexity: O(1) - We use usize extra memory.
    ///
    /// Runtime 1 ms Beats 68%
    /// Memory 2.14 MB Beats 36%
    pub fn get_lucky(s: String, k: i32) -> i32 {
        fn sum_digits(mut num: usize) -> usize {
            let mut res = 0;
            while num > 0 {
                res += num % 10;
                num /= 10;
            }
            res
        }
        let mut num = s.bytes().map(|b| sum_digits((b - b'a' + 1) as usize)).sum();
        for _ in 0..k - 1 {
            num = sum_digits(num);
            if num < 10 {
                return num as i32;
            }
        }
        num as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (String::from("iiii"), 1, 36),
        (String::from("leetcode"), 2, 6),
        (String::from("zbax"), 2, 8),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::get_lucky(t.0.clone(), t.1);
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
