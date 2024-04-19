// 1356. Sort Integers by The Number of 1 Bits
// 🟢 Easy
//
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
//
// Tags: Array - Bit Manipulation - Sorting - Counting

use std::cmp::Ordering;

struct Solution;
impl Solution {
    /// Sort the input vector integers given the primary and secondary conditions
    /// given in the problem description.
    ///
    /// Time complexity: O(n*log(n)) - Sorting a vector of size n. I am considering
    /// count_ones() to be O(1). I believe this to be more efficient than catching
    /// the number of bits, once computed, in a hashmap because the hashmap key
    /// hashing may be more costly than count_ones().
    /// Space complexity: O(n) - We need the local mutable copy of arr. Otherwise,
    /// the code would be O(1) space because sort_unstable_by works in place.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory  2.02MB Beats 79.55%
    pub fn sort_by_bits(mut arr: Vec<i32>) -> Vec<i32> {
        arr.sort_unstable_by(|a, b| a.count_ones().cmp(&b.count_ones()).then(a.cmp(b)));
        arr
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![0, 1, 2, 3, 4, 5, 6, 7, 8],
            vec![0, 1, 2, 4, 8, 3, 5, 6, 7],
        ),
        (
            vec![1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
            vec![1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::sort_by_bits(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
