// 347. Top K Frequent Elements
// 🟠 Medium
//
// https://leetcode.com/problems/top-k-frequent-elements/
//
// Tags: Array - Hash Table - Divide and Conquer - Sorting - Heap (Priority Queue)
// - Bucket Sort - Counting - Quickselect

use std::collections::HashMap;

struct Solution;

/// Iterate over the elements to get their frequencies, then use a vector of
/// size m, where m is the maximum frequency of any element in the input, to
/// bucket sort the elements. Finally, iterate over the sorted elements and
/// pick the k most frequent to create the result vector.
///
/// Time complexity: O(n) - We iterate over all elements to create a hashmap of
/// their frequencies, then iterate over that hashmap and bucket sort them in
/// O(n), then iterate over the bucket sorted elements in O(k), where k <= n,
/// and create the result vector.
/// Space complexity: O(n) - The frequencies hashmap nad the buckets vector can
/// both grow to size n.
///
/// Runtime 2 ms Beats 85.57%
/// Memory 2.3 MB Beats 99.2%
impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut frequencies = HashMap::new();
        let mut highest_frequency = 0;
        for num in nums {
            *frequencies.entry(num).or_insert(0) += 1;
            highest_frequency = highest_frequency.max(*frequencies.get(&num).unwrap());
        }
        // Bucket sort the elements.
        let mut buckets = vec![vec![]; highest_frequency as usize + 1];
        for (key, val) in frequencies {
            buckets[val].push(key);
        }
        // Get the k most frequent.
        let k = k as usize;
        let mut res = Vec::with_capacity(k);
        let (mut i, mut j) = (buckets.len() - 1, 0);
        while res.len() < k {
            // Do we have an element at the current index?
            if j < buckets[i].len() {
                res.push(buckets[i][j]);
                j += 1;
            } else {
                i -= 1;
                j = 0;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = vec![
        (vec![1], 1, vec![1]),
        (vec![1, 1, 1, 2, 2, 3], 2, vec![1, 2]),
    ];
    for t in tests {
        assert_eq!(Solution::top_k_frequent(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
