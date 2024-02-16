// 1481. Least Number of Unique Integers after K Removals
// 🟠 Medium
//
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
//
// Tags: Array - Hash Table - Greedy - Sorting - Counting

use std::{cmp::Reverse, collections::HashMap};

struct Solution;
impl Solution {
    /// Use a hashmap to get the counts of elements in the input, then use a sorted vector to have
    /// access the the least frequent elements and remove k of them. Return the number of elements
    /// left in the counts vector.
    ///
    /// Time complexity: O(n*log(n)) - Linear time to construct the counter hashmap, transform it
    /// into the vector of counts, then, m*log(m) to sort it, where m is the number of unique
    /// elements in the input, and 1 <= m <= n.
    /// Space complexity: O(n) - Both the hashmap and the counts vector can have n elements.
    ///
    /// Runtime 16 ms Beats 90%
    /// Memory 7.11 MB Beats 10%
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, k: i32) -> i32 {
        let mut counter: HashMap<i32, usize> = HashMap::new();
        for val in arr {
            counter.entry(val).and_modify(|c| *c += 1).or_insert(1);
        }
        let mut counts = Vec::from_iter(counter.into_values());
        counts.sort_unstable_by_key(|x| Reverse(*x));
        let mut res = counts.len();
        let mut k = k as usize;
        while res > 0 && k >= counts[res - 1] {
            k -= counts[res - 1];
            res -= 1;
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![5, 5, 4], 1, 1),
        (vec![4, 3, 1, 1, 3, 3, 2], 3, 2),
        (vec![4, 3, 1, 1, 3, 3, 2], 10, 0),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_least_num_of_unique_ints(t.0.clone(), t.1);
        let expected = t.2;
        if res == expected {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, expected, res
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
