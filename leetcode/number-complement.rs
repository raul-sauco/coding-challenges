// 476. Number Complement
// 🟢 Easy
//
// https://leetcode.com/problems/number-complement/
//
// Tags: Bit Manipulation

struct Solution;
impl Solution {
    /// Try all values (2^n)-1 with n 0..32 until we find one that is greater than num, that will
    /// be a number with the same most significant bit but all the other bits set to 1, we can xor
    /// that with the input.
    ///
    /// Time complexity: O(log(n)) - Each execution of the loop multiplies the value by 2.
    /// Space complexity: O(1) - Constant extra memory.
    ///
    /// Runtime 1 ms Beats 61%
    /// Memory 2.15 MB Beats 72%
    #[allow(dead_code)]
    pub fn find_complement_it_up(num: i32) -> i32 {
        let mut ones = 1;
        while ones < num {
            ones = (ones << 1) | 1;
        }
        ones ^ num
    }

    /// Use log to get the position of the most significant bit, shift it left, that gives us a
    /// number with a leading 1 just to the left of the most significant bit of num and all zeroes
    /// to the right, subtract one to get an integer that is all ones with the most significant
    /// being the same as the most significant bit in the input, xor.
    ///
    /// Time complexity: O(log(n)) - Internally the log function is log(n) worst case though I
    /// think it has some optimizations.
    /// Space complexity: O(1) - Constant extra memory.
    ///
    /// Runtime 1 ms Beats 74%
    /// Memory 2.06 MB Beats 72%
    #[allow(dead_code)]
    pub fn find_complement_log(num: i32) -> i32 {
        2i32.pow((num).ilog2() + 1) - 1 ^ num
        // For question 1009. Complement of Base 10 Integer 0 <= n < 10^9
        // if num == 0 {
        //     1
        // } else {
        //     2i32.pow((num).ilog2() + 1) - 1 ^ num
        // }
    }

    /// Clever solution by StefanPochmann, duplicates the mask at each step starting with one 1 at
    /// the same position as the most significant bit of the input.
    ///
    /// Time complexity: O(1) - Constant number of operations.
    /// Space complexity: O(1) - Constant extra memory.
    ///
    /// Runtime 1 ms Beats 74%
    /// Memory 2.13 MB Beats 18%
    #[allow(dead_code)]
    pub fn find_complement(num: i32) -> i32 {
        [1, 2, 4, 8, 16]
            .into_iter()
            .fold(num, |mask, x| (mask >> x) | mask)
            ^ num
    }
}

// Tests.
fn main() {
    let tests = [(5, 2), (7, 0), (10, 5)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_complement(t.0);
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
