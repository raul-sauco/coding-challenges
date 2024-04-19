// 525. Contiguous Array
// 🟠 Medium
//
// https://leetcode.com/problems/contiguous-array/
//
// Tags: Array - Hash Table - Prefix Sum

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Brute force solution that somehow still passes. Compute a vector of prefix sums, for each
    /// element, check if we have a match with all the other positions.
    ///
    /// Time complexity: O(n^2) - Nested loops that iterate over all the elements in n.
    /// Space complexity: O(n) - The prefix sum vector.
    ///
    /// Runtime 1315 ms Beats 6%
    /// Memory 3 MB Beats 57%
    #[allow(dead_code)]
    pub fn find_max_length_brute_force(nums: Vec<i32>) -> i32 {
        let prefix_sums = nums
            .iter()
            .scan(0, |sum, num| {
                *sum += *num as usize;
                Some(*sum)
            })
            .collect::<Vec<_>>();
        let mut res = 0;
        let (mut length, mut count_ones);
        for end in (1..nums.len()).rev() {
            for start in 0..end {
                length = end - start + 1;
                if length <= res {
                    break;
                }
                if length % 2 == 1 {
                    continue;
                }
                count_ones = prefix_sums[end]
                    - if start == 0 {
                        0
                    } else {
                        prefix_sums[start - 1]
                    };
                if length == 2 * count_ones {
                    res = length;
                }
            }
        }
        res as i32
    }

    /// Use a hashmap with the difference between the count of ones minus the count of zeroes as
    /// the key and the index for that count as the value. iterate over the numbers in the input,
    /// for each number, check if we have seen that same count before, if we have, say at point
    /// start, the subarray between start and end has the same number of ones and zeroes, if this
    /// is the longest subarray seen so far, update the result with this length.
    ///
    /// Time complexity: O(n) - We visit each element once and do constant time work.
    /// Space complexity: O(n) - The lookup vector.
    ///
    /// Runtime 10 ms Beats 100%
    /// Memory 2.60 MB Beats 100%
    pub fn find_max_length(nums: Vec<i32>) -> i32 {
        let (mut res, mut sum) = (0, 0);
        // let mut lookup: HashMap<i32, i32> = HashMap::from_iter([(0, -1)]);
        let mut lookup = HashMap::new();
        lookup.insert(0, -1);
        for (end, num) in nums.iter().enumerate() {
            if num == &0 {
                sum -= 1;
            } else {
                sum += 1;
            }
            if let Some(start) = lookup.get(&sum) {
                res = res.max(end as i32 - start);
            } else {
                lookup.insert(sum, end as i32);
            }
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0, 1], 2),
        (vec![0, 1, 0], 2),
        (vec![0, 0, 1, 0, 0, 0, 1, 1], 6),
        (vec![0, 1, 1, 0, 1, 1, 1, 0], 4),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_max_length(t.0.clone());
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
