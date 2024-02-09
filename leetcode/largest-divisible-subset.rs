// 368. Largest Divisible Subset
// 🟠 Medium
//
// https://leetcode.com/problems/largest-divisible-subset/
//
// Tags: Array - Math - Dynamic Programming - Sorting

use std::collections::{HashMap, HashSet};

struct Solution;
impl Solution {
    /// Sort the input and iterate over the values building subsets, if we can append the current
    /// value after the end of any of the existing subsets, we don't need to check the values
    /// before that one because division is transitive.
    ///
    /// Time complexity: O(n^2) - The outer loop iterates over every number in the input, the inner
    /// loop iterates over all the numbers up to that one. There is also the extra O(log(n)*n) to
    /// sort the input in the preparatory step.
    /// Space complexity: O(n) - The hashmap with the length of subsets that we have seen. We store
    /// the length and the previous element so constant space per entry.
    ///
    /// Runtime 12 ms Beats 20%
    /// Memory 2.18 MB Beats 60%
    #[allow(dead_code)]
    pub fn largest_divisible_subset_hm(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        nums.sort();
        let mut max = (1, nums[0]);
        let mut dp: HashMap<i32, (usize, Option<i32>)> = HashMap::new();
        for num in nums {
            let mut longest: (usize, Option<i32>) = (1, None);
            for (key, val) in dp.iter() {
                if num % key == 0 && val.0 > longest.0 - 1 {
                    longest = (val.0 + 1, Some(*key));
                }
            }
            dp.insert(num, longest);
            if longest.0 > max.0 {
                max = (longest.0, num);
            }
        }
        let mut res = vec![];
        let mut next: Option<i32> = Some(max.1);
        while let Some(num) = next {
            res.push(num);
            next = dp.get(&num).expect("An entry").1;
        }
        res
    }

    /// Same logic as the previous solution but use two vectors instead of the hashmap to keep
    /// track of subset lengths and previous items for each num in nums.
    ///
    /// Time complexity: O(n^2) - The outer loop iterates over every number in the input, the inner
    /// loop iterates over all the numbers up to that one. There is also the extra O(log(n)*n) to
    /// sort the input in the preparatory step.
    /// Space complexity: O(n) - The vectors with the length of subsets that we have seen and the
    /// previous element in the subset.
    ///
    /// Runtime 10 ms Beats 100%
    /// Memory 2.18 MB Beats 60%
    pub fn largest_divisible_subset(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut nums = nums;
        nums.sort();
        let mut max = (1, 0);
        let mut precedents = vec![n + 1; n];
        let mut dp = vec![1; n];
        for i in 1..n {
            for j in 0..i {
                if nums[i] % nums[j] == 0 {
                    // We can append to nums[j] subset.
                    if dp[j] >= dp[i] {
                        dp[i] = dp[j] + 1;
                        precedents[i] = j;
                        if dp[i] > max.0 {
                            max = (dp[i], i);
                        }
                    }
                }
            }
        }
        let mut res = vec![];
        let mut next_idx = max.1;
        while next_idx < n {
            res.push(nums[next_idx]);
            next_idx = precedents[next_idx];
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3], vec![1, 2]),
        (vec![1, 2, 4, 8], vec![1, 2, 4, 8]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::largest_divisible_subset(t.0.clone());
        let expected = t.1.clone();
        if HashSet::<i32>::from_iter(res.clone()) == HashSet::from_iter(t.1.clone()) {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
