// 201. Bitwise AND of Numbers Range
// 🟠 Medium
//
// https://leetcode.com/problems/bitwise-and-of-numbers-range/
//
// Tags: Bit Manipulation

struct Solution;
impl Solution {
    /// The only bits remaining after the range and will be the ones that are one for all values in
    /// the range, remove the least significant bit while the values are different, once they are
    /// the same, pad the value with zeroes to the same number of bits we had before and return it.
    ///
    /// Time complexity: O(1) - We are working with 32 bit integers, the loop will run 32 times at
    /// most. Inside the loop we do O(1) operations.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.19 MB Beats 32.56%
    pub fn range_bitwise_and(mut left: i32, mut right: i32) -> i32 {
        let mut i = 0;
        while left != right && left != 0 && right != 0 {
            left >>= 1;
            right >>= 1;
            i += 1;
        }
        if left == 0 || right == 0 {
            return 0;
        }
        left << i
    }

    /// Same logic as the previous solution, simplified by removing the zero checks.
    ///
    /// Time complexity: O(1) - We are working with 32 bit integers, the loop will run 32 times at
    /// most. Inside the loop we do O(1) operations.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 8 ms Beats 27.91%
    /// Memory 2.08 MB Beats 79.07%
    #[allow(dead_code)]
    pub fn range_bitwise_and_simple(mut left: i32, mut right: i32) -> i32 {
        let mut i = 0;
        while left != right {
            left >>= 1;
            right >>= 1;
            i += 1;
        }
        left << i
    }
}

// Tests.
fn main() {
    let tests = [(5, 7, 4), (0, 0, 0), (1, 2147483647, 0)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::range_bitwise_and(t.0, t.1);
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
