// 338. Counting Bits
// 🟢 Easy
//
// https://leetcode.com/problems/counting-bits/
//
// Tags: Dynamic Programming - Bit Manipulation

struct Solution;
impl Solution {
    /// In binary, each time that we add a most significant bit to the right,
    /// for example 1, 2, 4, 8, the binary representation of the number will
    /// only have one 1, lets call these values the "factors". The next values
    /// will have the same number of digits as the same position in the
    /// previous group plus one added when jumping group.
    ///
    /// Time complexity: O(n) - The loop runs once for each value up to n.
    /// Space complexity: O(1) - If we do not take into account the output
    /// vector, O(n) if we do.
    ///
    /// Runtime 4 ms Beats 76.87%
    /// Memory 2.57 MB Beats 76.19%
    pub fn count_bits(n: i32) -> Vec<i32> {
        let n = n as usize;
        let mut res = vec![0; n + 1];
        for i in 1..=n {
            res[i] = res[i >> 1] + (i & 1) as i32;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(2, vec![0, 1, 1]), (5, vec![0, 1, 1, 2, 1, 2])];
    for t in tests {
        assert_eq!(Solution::count_bits(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
