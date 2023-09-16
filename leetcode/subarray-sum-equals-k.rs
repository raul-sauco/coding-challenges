// 560. Subarray Sum Equals K
// 🟠 Medium
//
// https://leetcode.com/problems/subarray-sum-equals-k/
//
// Tags: Array - Hash Table - Prefix Sum

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Iterate over the array keeping the sum of values up to the current index,
    /// we store all sums that we have seen in a hashmap of sum => number of
    /// times that we have seen that sum. At each index, we check if we can find
    /// the value of the current sum - k in the hashmap, if we can, we add the
    /// number of times that we have seen it to the result, because the subarray
    /// between the current index and the indexes with s - k have a sum that
    /// equals k.
    ///
    /// Time complexity: O(n) - We iterate over the input array once and do
    /// constant time work for each element.
    /// Space complexity: O(n) - The hashmap will have an element for each
    /// element in the input.
    ///
    /// Runtime 12 ms Beats 75.00%
    /// Memory 2.49 MB Beats 85.14%
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut res = 0;
        let mut seen: HashMap<i32, i32> = HashMap::with_capacity(nums.len());
        seen.insert(0, 1);
        let mut prefix_sum = 0;
        let mut diff;
        for num in nums {
            prefix_sum += num;
            diff = prefix_sum - k;
            if let Some(entry) = seen.get(&diff) {
                res += entry;
            }
            seen.entry(prefix_sum)
                .and_modify(|counter| *counter += 1)
                .or_insert(1);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![1, 1, 1], 2, 2), (vec![1, 2, 3], 3, 2)];
    for t in tests {
        assert_eq!(Solution::subarray_sum(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
