// 926. Flip String to Monotone Increasing
// 🟠 Medium
//
// https://leetcode.com/problems/flip-string-to-monotone-increasing/
//
// Tags: String - Dynamic Programming

struct Solution;
impl Solution {
    // Use dynamic programming, count the number of changes to make each
    // prefix monotonically increasing given the result of the prefix one
    // character shorter.
    //
    // Time complexity: O(n) - We visit each value once.
    // Space complexity: O(1) - We store two integers.
    //
    // Runtime 6 ms Beats 33.33%
    // Memory 2.3 MB Beats 83.33%
    pub fn min_flips_mono_incr(s: String) -> i32 {
        use std::cmp;
        let mut flips = 0;
        let mut res = 0;
        for c in s.chars() {
            if c == '1' {
                flips += 1;
            } else {
                res = cmp::min(flips, res + 1)
            }
        }
        res
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::min_flips_mono_incr(String::from("0")), 0);
    assert_eq!(Solution::min_flips_mono_incr(String::from("1")), 0);
    assert_eq!(Solution::min_flips_mono_incr(String::from("0011")), 0);
    assert_eq!(Solution::min_flips_mono_incr(String::from("00110")), 1);
    assert_eq!(Solution::min_flips_mono_incr(String::from("010110")), 2);
    assert_eq!(Solution::min_flips_mono_incr(String::from("00011000")), 2);
    println!("All tests passed!")
}
