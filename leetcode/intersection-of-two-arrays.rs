// 349. Intersection of Two Arrays
// 🟢 Easy
//
// https://leetcode.com/problems/intersection-of-two-arrays/
//
// Tags: Array - Hash Table - Two Pointers - Binary Search - Sorting

use std::collections::HashSet;

struct Solution;
impl Solution {
    /// Get a hashset from each input vector and compute their intersection, return the result as a
    /// vector.
    ///
    /// Time complexity: O(m+n) - We will visit each element in both input vectors.
    /// Space complexity: O(n) - To compute the intersection, at some point the iterators need to
    /// store the elements in memory.
    ///
    /// Runtime 1 ms Beats 83.16%
    /// Memory 2.17 MB Beats 74.74%
    #[allow(dead_code)]
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        nums1
            .into_iter()
            .collect::<HashSet<_>>()
            .intersection(&nums2.into_iter().collect::<HashSet<_>>())
            .map(|x| *x)
            .collect::<Vec<_>>()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 2, 1], vec![2, 2], vec![2]),
        (vec![4, 9, 5], vec![9, 4, 9, 8, 4], vec![4, 9]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::intersection(t.0.clone(), t.1.clone());
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
