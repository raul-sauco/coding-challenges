// 258. Add Digits
// 🟢 Easy
//
// https://leetcode.com/problems/add-digits/
//
// Tags: Math - Simulation - Number Theory

struct Solution;
impl Solution {
    /// Using math we can compute the digital root of a value using the mod
    /// of the value and the base-1.
    ///
    /// Time complexity: O(1) - Constant time.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 67.21%
    pub fn add_digits(num: i32) -> i32 {
        if num == 0 {
            0
        } else {
            1 + (num - 1) % 9
        }
    }

    /// Iterative version, extract the last digit and add it while the result is
    /// greater than 9.
    ///
    /// Time complexity: O(log(n)) - In each iteration, we divide by 100.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 67.21%
    pub fn add_digits_it(num: i32) -> i32 {
        let mut num = num;
        while num > 9 {
            num = num / 10 + num % 10;
        }
        num
    }
}

// Tests.
fn main() {
    let tests = [(0, 0), (38, 2), (2147483647, 1)];
    for t in tests {
        assert_eq!(Solution::add_digits(t.0), t.1);
        assert_eq!(Solution::add_digits_it(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m");
}
