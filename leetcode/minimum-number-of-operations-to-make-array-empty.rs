// 2870. Minimum Number of Operations to Make Array Empty
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
//
// Tags: Array - Hash Table - Greedy - Counting

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Store the counts of values in a hashmap, then iterate over the values and greedily
    /// determine the minimum deletions to remove each based on the modulus by 3.
    ///
    /// Time complexity: O(n) - We visit each element to build the hashmap, then we iterate over
    /// the values in the hashmap, with an upper bound of n values.
    /// Space complexity: O(n) - We store a max of n key-value pairs in the hashmap.
    ///
    /// Runtime 19 ms Beats 85.71%
    /// Memory 4.74 MB Beats 28.57%
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut counts = HashMap::new();
        for num in nums.iter() {
            counts.entry(num).and_modify(|n| *n += 1).or_insert(1);
        }
        let mut res = 0;
        for v in counts.values() {
            if *v == 1 {
                return -1;
            }
            match v % 3 {
                0 => {
                    res += v / 3;
                }
                1 | 2 => {
                    res += v / 3 + 1;
                }
                _ => unreachable!("Can't be!"),
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2, 3, 3, 2, 2, 4, 2, 3, 4], 4),
        (vec![2, 1, 2, 2, 3, 3], -1),
        (
            vec![
                14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12,
            ],
            7,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_operations(t.0.clone());
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
