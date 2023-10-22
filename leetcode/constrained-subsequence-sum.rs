// 1425. Constrained Subsequence Sum
// 🔴 Hard
//
// https://leetcode.com/problems/constrained-subsequence-sum/
//
// Tags: Array - Dynamic Programming - Queue - Sliding Window - Heap (Priority Queue) - Monotonic Queue

use std::collections::{BinaryHeap, VecDeque};

struct Solution;
impl Solution {
    /// The maximum at each index will be the maximum between the value at that
    /// index and adding that value to any of the maximums up to k positions back,
    /// which are the valid ones that we are allowed to use. To avoid checking
    /// k values back for each position n, which would be O(k*n), we can use a
    /// heap, or a monotonic array I think, to get the best value more efficiently.
    /// This solution uses the heap.
    ///
    /// Time complexity: O(n*log(n)) - We will push n elements into the heap, of
    /// potential size n, we can also pop n - 1 elements from the heap.
    /// Space complexity: O(n) - The heap can grow to the size of the input.
    ///
    /// Runtime 32 ms Beats 100%
    /// Memory 4.74 MB Beats 100%
    pub fn constrained_subset_sum(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut heap = BinaryHeap::from([(nums[0], 0)]);
        let mut res = nums[0];
        for (idx, num) in nums.into_iter().enumerate().skip(1) {
            // Remove all elements out of range from the top of the heap.
            while heap.peek().unwrap().1 + k < idx {
                heap.pop();
            }
            if let Some((val, _i)) = heap.peek() {
                let max = num.max(num + val);
                heap.push((max, idx));
                res = res.max(max);
            }
        }
        res
    }

    /// The maximum at each index will be the maximum between the value at that
    /// index and adding that value to any of the maximums up to k positions back,
    /// which are the valid ones that we are allowed to use. To avoid checking
    /// k values back for each position n, which would be O(k*n), we can use a
    /// heap, or a monotonic queue, to get the best value more efficiently.
    /// This solution uses the monotonic queue.
    ///
    /// Time complexity: O(n) - We visit each element, for each we push one
    /// element to the queue, and may pop n elements, but overall, the maximum
    /// number of elements that we may pop is n, spread over the n elements that
    /// we visit.
    /// Space complexity: O(n) - The queue can grow to the size of the input.
    ///
    /// Runtime 28 ms Beats 100%
    /// Memory 5.06 MB Beats 100%
    pub fn constrained_subset_sum_2(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut queue = VecDeque::from([(nums[0], 0)]);
        let mut res = nums[0];
        for (idx, num) in nums.into_iter().enumerate().skip(1) {
            // Remove all elements out of range from the left end of the queue.
            while queue.front().unwrap().1 + k < idx {
                queue.pop_front();
            }
            if let Some((val, _i)) = queue.front() {
                let max = num.max(num + val);
                while let Some((back_val, back_idx)) = queue.back() {
                    if *back_val < max || back_idx + k < idx {
                        queue.pop_back();
                    } else {
                        break;
                    }
                }
                queue.push_back((max, idx));
                res = res.max(max);
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![10, 2, -10, 5, 20], 2, 37),
        (vec![-1, -2, -3], 1, -1),
        (vec![10, -2, -10, -5, 20], 2, 23),
    ];
    for t in tests {
        assert_eq!(Solution::constrained_subset_sum(t.0.clone(), t.1), t.2);
        assert_eq!(Solution::constrained_subset_sum_2(t.0.clone(), t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
