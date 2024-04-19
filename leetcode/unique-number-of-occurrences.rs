// 1207. Unique Number of Occurrences
// 🟢 Easy
//
// https://leetcode.com/problems/unique-number-of-occurrences/
//
// Tags: Array - Hash Table

use std::collections::{HashMap, HashSet};

struct Solution;
impl Solution {
    /// Get the counts, then check if any of the counts has been seen more than once. The advantage
    /// of this solution is that it uses small arrays and I believe that it does not use the heap,
    /// even though that does not really show in the OJ results.
    ///
    /// Time complexity: O(n) - We visit each item twice, both times we do O(1) work.
    /// Space complexity: O(n) - Both extra arrays grow linearly with the size of the input.
    ///
    /// Runtime 1 ms Beats 71.65%
    /// Memory 2.40 MB Beats 23.68%
    #[allow(dead_code)]
    pub fn unique_occurrences_arr(arr: Vec<i32>) -> bool {
        let mut counter = [0; 2000];
        for num in arr {
            counter[(num + 1000) as usize] += 1;
        }
        let mut seen = [false; 1001];
        for c in counter {
            if c == 0 {
                continue;
            }
            if seen[c] {
                return false;
            }
            seen[c] = true;
        }
        true
    }

    /// Use a HashMap for the counts and a HashSet to check for uniqueness, I expected this to be
    /// less efficient than the previous solution because of both the use of the heap and having to
    /// hash the keys or values but it does not seem to be the case.
    ///
    /// Time complexity: O(n) - We visit each item twice, both times we do O(1) work.
    /// Space complexity: O(n) - Both structures grow linearly with the size of the input.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.14 MB Beats 52.63%
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut counter = HashMap::with_capacity(arr.len());
        for num in arr {
            *counter.entry(num).or_insert(0) += 1;
        }
        let counts: HashSet<_> = counter.values().collect();
        counter.len() == counts.len()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2], false),
        (vec![1, 2, 2, 1, 1, 3], true),
        (vec![-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], true),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::unique_occurrences(t.0.clone());
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
