// 523. Continuous Subarray Sum
// 🟠 Medium
//
// https://leetcode.com/problems/continuous-subarray-sum/
//
// Tags: Array - Hash Table - Math - Prefix Sum

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Use the fact that for the subarray sum between i<>j to be a multiple of k, the mod k of
    /// both prefix sums up to i and j needs to be equal. There is a better explanation of why in
    /// the problem editorial. Initialize the `prefix_mod` to 0, keep a hash map of prefix mods
    /// seen, for each value, add the current value and mod it to get the prefix mod up to the
    /// current index, if we have seen that mod and the array between the indexes has at least
    /// length 2, we return true.
    ///
    /// Time complexity: O(n) - We visit each element in nums and do constant time work for each.
    /// Space complexity: O(n) - The HashMap of seen mods.
    ///
    /// Runtime 26 ms Beats 60%
    /// Memory 4.56 MB Beats 60%
    pub fn check_subarray_sum(nums: Vec<i32>, k: i32) -> bool {
        let mut pm = 0;
        let mut seen = HashMap::new();
        seen.insert(0, -1);
        for (i, num) in nums.into_iter().enumerate() {
            pm = (pm + num) % k;
            match seen.get(&pm) {
                Some(j) => {
                    if i as i32 - j > 1 {
                        return true;
                    }
                }
                None => {
                    seen.insert(pm, i as i32);
                }
            }
        }
        false
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2, 4, 3], 6, true),
        (vec![23, 2, 4, 6, 7], 6, true),
        (vec![23, 2, 6, 4, 7], 6, true),
        (vec![23, 2, 6, 4, 7], 13, false),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::check_subarray_sum(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
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
