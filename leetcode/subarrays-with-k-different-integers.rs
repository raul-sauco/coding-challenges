// 992. Subarrays with K Different Integers
// 🔴 Hard
//
// https://leetcode.com/problems/subarrays-with-k-different-integers/
//
// Tags: Array - Hash Table - Sliding Window - Counting

use std::collections::{HashMap, HashSet};

struct Solution;
impl Solution {
    /// Brute force solution, for each start and end, iterate over all elements counting how many
    /// different elements there are.
    ///
    /// Time complexity: O(n^2) - For each start, we calculate the count of elements ending at all
    /// ends.
    /// Space complexity: O(n) - The hashset of seen elements.
    #[allow(dead_code)]
    pub fn subarrays_with_k_distinct_brute_force(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let n = nums.len();
        let mut seen = HashSet::new();
        let mut res = 0;
        for start in 0..n {
            seen.clear();
            for end in start..n {
                seen.insert(nums[end]);
                if seen.len() == k {
                    res += 1;
                } else if seen.len() > k {
                    break;
                }
            }
        }
        res
    }

    /// Use a sliding window, slide the end pointer forward one element at a time adding that
    /// element to the count of elements that we have in the window at the time. Then check how
    /// many distinct elements we have, if we have more than k elements, slide both the start and
    /// middle pointers forward removing elements from the sliding window. Once we have at most k
    /// distinct elements in the sliding window, we can slide the middle pointer forward while we
    /// have more than one instance of the element under that pointer, the reason is that we could
    /// remove any of these elements, and because we have more than one instance, the number of
    /// distinct elements would not change. After that, if we have exactly k elements in the
    /// window, we know that we could use any element between start and middle as the start of a
    /// valid subarray, ending at end, with k distinct elements, we add that to the result.
    ///
    /// Time complexity: O(n) - We will visit each element a maximum of 2 times, to add it and pop
    /// it from the hashmap. The other operations are constant time.
    /// Space complexity: O(n) - The hashset of seen elements.
    ///
    /// Runtime 17 ms Beats 25%
    /// Memory 2.34 MB Beats 50%
    #[allow(dead_code)]
    pub fn subarrays_with_k_distinct_hash_map(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let n = nums.len();
        let mut counts = HashMap::new();
        let mut res = 0;
        let (mut start, mut middle) = (0, 0);
        for end in 0..n {
            counts.entry(nums[end]).and_modify(|e| *e += 1).or_insert(1);
            while counts.len() > k {
                // Slide the middle pointer to count valid subarrays.
                counts.entry(nums[middle]).and_modify(|e| *e -= 1);
                if *counts.get(&nums[middle]).unwrap() == 0 {
                    counts.remove(&nums[middle]);
                }
                middle += 1;
                start = middle;
            }
            while let Some(count) = counts.get(&nums[middle]) {
                if *count > 1 {
                    counts.entry(nums[middle]).and_modify(|e| *e -= 1);
                    middle += 1;
                } else {
                    break;
                }
            }
            if counts.len() == k {
                res += middle - start + 1;
            }
        }
        res as i32
    }

    /// Same logic as the previous solution but use a vector instead of a Hashmap.
    ///
    /// Time complexity: O(n) - We will visit each element a maximum of 2 times.
    /// Space complexity: O(n) - The vector of counts.
    ///
    /// Runtime 6 ms Beats [5%
    /// Memory 2.34 MB Beats 50%
    #[allow(dead_code)]
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        let mut k = k;
        let n = nums.len();
        // 0 < nums[i] <= n
        let mut counts = vec![0; n + 1];
        let mut res = 0;
        let (mut start, mut middle) = (0, 0);
        for end in 0..n {
            counts[nums[end] as usize] += 1;
            if counts[nums[end] as usize] == 1 {
                k -= 1;
            }
            while k < 0 {
                // Slide the middle pointer to count valid subarrays.
                counts[nums[middle] as usize] -= 1;
                if counts[nums[middle] as usize] == 0 {
                    k += 1;
                }
                middle += 1;
                start = middle;
            }
            while counts[nums[middle] as usize] > 1 {
                counts[nums[middle] as usize] -= 1;
                middle += 1;
            }
            if k == 0 {
                res += middle - start + 1;
            }
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [(vec![1, 2, 1, 2, 3], 2, 7), (vec![1, 2, 1, 3, 4], 3, 3)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::subarrays_with_k_distinct(t.0.clone(), t.1);
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
