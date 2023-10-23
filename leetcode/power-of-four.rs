// 342. Power of Four
// 🟢 Easy
//
// https://leetcode.com/problems/power-of-four/
//
// Tags: Math - Bit Manipulation - Recursion

struct Solution;
impl Solution {
    /// We can check that the number has the following properties:
    /// - Is greater than 0
    /// - Only contains one 1 bit, on the most significant position, by doing
    ///   binary and with n-1.
    /// - The 1 bit, on the most significant position, is in an even indexed
    ///   position, we can check that by doing binary and with a value that has
    ///   all zeroes in these positions and all ones in odd indexed positions,
    ///   the number 1431655765, in binary 0b1010101010101010101010101010101.
    ///
    /// Time complexity: O(1)
    /// Space complexity: O(1)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 1.94 MB Beats 84.62%
    pub fn is_power_of_four(n: i32) -> bool {
        n > 0 && n & (n - 1) == 0 && n & 1431655765 == n
    }
}

// Tests.
fn main() {
    let tests = [
        (1, true),
        (5, false),
        (16, true),
        (30, false),
        (-2147483648, false),
    ];
    for t in tests {
        assert_eq!(Solution::is_power_of_four(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
