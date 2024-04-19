// 191. Number of 1 Bits
// 🟢 Easy
//
// https://leetcode.com/problems/number-of-1-bits/
//
// Tags: Divide and Conquer - Bit Manipulation

struct Solution;
impl Solution {
    #![allow(dead_code)]
    /// And the number with 1 to check if the least significant bit is set, then shift bits by one
    /// to move into the next one.
    ///
    /// Time complexity: O(log2(n)) - At each iteration we divide the number by 2.
    /// Space complexity: O(1) - We store one i32 value.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 1.97 MB Beats 91.94%
    pub fn hamming_weight(n: u32) -> i32 {
        let mut count_ones = 0;
        let mut n = n;
        while n > 0 {
            count_ones += n & 1;
            n >>= 1;
        }
        count_ones as i32
    }

    /// Add n to n-1, that removes the least significant set bit, this solution will iterate only m
    /// times, where m is the number of '1' bits, while the previous one also does one iteration
    /// per each '0' bit.
    ///
    /// Time complexity: O(m) - Where m is the number of '1' bits and it can be, at most log2(n)
    /// Space complexity: O(1) - We store one i32 value.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 1.99 MB Beats 91.74%
    pub fn hamming_weight_2(n: u32) -> i32 {
        let mut count_ones = 0;
        let mut n = n;
        while n > 0 {
            n &= n - 1;
            count_ones += 1;
        }
        count_ones as i32
    }
}

// Tests.
fn main() {
    let tests = [
        // 00000000000000000000000000001011
        (11, 3),
        // 00000000000000000000000010000000
        (128, 1),
        // 11111111111111111111111111111101
        (4294967293, 31),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::hamming_weight_2(t.0.clone());
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
