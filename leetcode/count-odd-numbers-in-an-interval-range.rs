// 1523. Count Odd Numbers in an Interval Range
// 🟢 Easy
//
// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
//
// Tags: Math

struct Solution;
impl Solution {
    // Count the number of elements between the low and the high, for even
    // length series, the number of odd values will be half the length, for
    // odd length series, we need to check if they start in an odd or even
    // value, if they start in an odd value, it will be the result of the
    // integer division by the length plus one.
    //
    // Time complexity: O(1) - We perform an addition, division and modulus
    // operations.
    // Space complexity: O(1) - We use constant extra memory.
    //
    // Runtime 1 ms Beats 83.52%
    // Memory 2 MB Beats 60.80%
    pub fn count_odds(low: i32, high: i32) -> i32 {
        let size = high - low + 1;
        if size % 2 == 0 || low % 2 == 0 {
            size / 2
        } else {
            size / 2 + 1
        }
        // One line solution by Lee@215
        // (high + 1) / 2 - low / 2
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::count_odds(3, 7), 3);
    assert_eq!(Solution::count_odds(2, 5), 2);
    assert_eq!(Solution::count_odds(8, 10), 1);
    println!("All tests passed!")
}
