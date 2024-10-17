// 670. Maximum Swap
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-swap/
//
// Tags: Math - Greedy

struct Solution;
impl Solution {
    /// Put the largest digit as far left as possible, if multiple instances of the same digit are
    /// found, use the one furthest right.
    ///
    /// Time complexity: O(1) - The number of digits, but it maxes out at 8.
    /// Space complexity: O(1) - The digits vector has a max size of 8.
    ///
    /// Runtime 1 ms Beats 33%
    /// Memory 2.09 MB Beats 83%
    pub fn maximum_swap(num: i32) -> i32 {
        let mut digits = vec![];
        let mut mut_num = num;
        while mut_num > 0 {
            digits.push(mut_num % 10);
            mut_num /= 10;
        }
        let n = digits.len();
        let (mut max_digit_idx, mut s1, mut s2) = (0, 0, 0);
        for i in 1..n {
            if digits[i] > digits[max_digit_idx] {
                max_digit_idx = i;
            } else if digits[i] < digits[max_digit_idx] {
                s1 = i;
                s2 = max_digit_idx;
            }
        }
        digits.swap(s1, s2);
        mut_num = 0;
        for i in (0..digits.len()).rev() {
            mut_num *= 10;
            mut_num += digits[i];
        }
        mut_num
    }
}

// Tests.
fn main() {
    let tests = [(2736, 7236), (9973, 9973)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_swap(t.0);
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
