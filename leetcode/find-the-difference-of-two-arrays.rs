// 2215. Find the Difference of Two Arrays
// 🟢 Easy
//
// https://leetcode.com/problems/find-the-difference-of-two-arrays/
//
// Tags: Array - Hash Table

use std::collections::HashSet;

struct Solution;
impl Solution {
    /// Get two sets with the elements of nums1 and nums2 respectively, then
    /// get the differences between sets as vectors.
    ///
    /// Time complexity: O(n) - We iterate over all values and do O(1) work.
    /// Space complexity: O(n) - We use two hash sets of size n of extra memory.
    ///
    /// Runtime 14 ms Beats 47.62%
    /// Memory 2.3 MB Beats 42.86%
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let sa = nums1.iter().cloned().collect::<HashSet<_>>();
        let sb = nums2.iter().cloned().collect::<HashSet<_>>();
        vec![
            (&sa - &sb).iter().cloned().collect::<Vec<_>>(),
            (&sb - &sa).iter().cloned().collect::<Vec<_>>(),
        ]
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 3], vec![1, 1, 2, 2], vec![vec![3], vec![]]),
        (vec![1, 2, 3], vec![2, 4, 6], vec![vec![3, 1], vec![6, 4]]),
    ];
    for t in tests {
        assert_eq!(Solution::find_difference(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
