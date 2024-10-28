// 2501. Longest Square Streak in an Array
// 🟠 Medium
//
// https://leetcode.com/problems/longest-square-streak-in-an-array/
//
// Tags: Array - Hash Table - Binary Search - Dynamic Programming - Sorting

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// One way to do it is to sort the input vector, then visit each number, check if we can
    /// append it to any of the existing sequences and either extend that sequence or create a new
    /// one. We determine if we can append to existing sequences using a hashmap with the next
    /// square that would go into the sequence as the key and the length that the sequence would
    /// have, once we append that next sequence, as the value.
    ///
    /// Time complexity: O(nlog(n)) - We sort the input vector, after that O(n)
    /// Space complexity: O(n) - The hashmap grows to size n.
    ///
    /// Runtime 28 ms Beats 100%
    /// Memory 5.17 MB Beats 100%
    pub fn longest_square_streak(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        // A hashmap of the next squares with the sequence length.
        let mut next_squares = HashMap::new();
        let mut res = -1;
        for num in nums {
            // Skip duplicates.
            if next_squares.contains_key(&(num * num)) {
                continue;
            }
            // Can I append to an existing sequence?
            if let Some(&counter) = next_squares.get(&num) {
                res = res.max(counter);
                next_squares.insert(num * num, counter + 1);
            } else {
                next_squares.insert(num * num, 2);
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![4, 3, 6, 16, 8, 2], 3), (vec![2, 3, 5, 6, 7], -1)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::longest_square_streak(t.0.clone());
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
