// 239. Sliding Window Maximum
// 🔴 Hard
//
// https://leetcode.com/problems/sliding-window-maximum/
//
// Tags: Array - Queue - Sliding Window - Heap (Priority Queue) - Monotonic Queue

use std::collections::VecDeque;

struct Solution;
impl Solution {
    /// We can use a monotonic queue to be able to access the max value in the
    /// sliding window in linear time. The monotonic queue will store a maximum
    /// of k elements and it guarantees that the order of the elements is
    /// strictly increasing from left to right.
    ///
    /// Since we are managing the monotonic queue manually, i.e. it is not a
    /// built-in structure like the heap of the previous solution, we can
    /// store element indexes in the queue and access the element in nums to
    /// check its value. This has the advantage that we check both value and
    /// position storing only one value.
    ///
    /// Time complexity: O(n) - We only visit each element once, and push/pop
    /// it from the queue a maximum of 1 time.
    /// Space complexity: O(n) - The queue is of max size k, but the result
    /// array size depends on the input size as well.
    ///
    /// Runtime 66 ms Beats 64.81%
    /// Memory 3.7 MB Beats 51.85%
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        // A monotonic queue with the indexes of the elements that we have seen
        // in strictly decreasing order, for any i < j we know q[i] > q[j].
        let mut q = VecDeque::<usize>::new();
        // Use a vector for the results.
        let mut res = vec![0; 1 + nums.len() - k];
        for (i, num) in nums.iter().enumerate() {
            // Pop any element from the back of the queue that is smaller or
            // equal to num, this maintains the monotonicity of the queue, we
            // can pop these elements because they are smaller and to the left
            // of nums, and we are moving the sliding window right, so they can
            // never be the sliding window maximum after we add num.
            while !q.is_empty() && nums[*q.back().unwrap()] <= *num {
                q.pop_back();
            }
            // Now we can append this value, it is guaranteed to be the smallest
            // in the monotonic queue.
            q.push_back(i);
            // Pop any elements that are outside the window.
            while i >= k && *q.front().unwrap() <= i - k {
                q.pop_front();
            }
            // If the window has k elements, add the biggest one to the result.
            if i >= k - 1 {
                res[1 + i - k] = nums[*q.front().unwrap()];
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], 1, vec![1]),
        (vec![1, 3, -1, -3, 5, 3, 6, 7], 3, vec![3, 3, 5, 5, 6, 7]),
        (
            vec![10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3],
            3,
            vec![10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::max_sliding_window(t.0, t.1), t.2);
    }
    println!("All tests passed!")
}
