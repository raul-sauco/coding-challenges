// 918. Maximum Sum Circular Subarray
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-sum-circular-subarray/
//
// Tags: Array - Divide and Conquer - Dynamic Programming - Queue - Monotonic Queue

struct Solution;
impl Solution {
    // The maximum sum if we can go over the end and use values at the
    // beginning of the array will be either the classical maximum that we
    // can obtain using Kadane's algorithm, if the maximum subarray does not
    // overlap the going around point, or the sum of all values in the array
    // minus the minimum subarray in the original input. We can compute both,
    // and the sum of values in the array, using a single pass and Kadane's
    // algorithm.
    //
    // Time complexity: O(n) - We visit each value in the input once.
    // Space complexity: O(1) - We use constant extra memory.
    //
    // Runtime 3 ms Beats 100%
    // Memory 2.5 MB Beats 63.64%
    pub fn max_subarray_sum_circular(nums: Vec<i32>) -> i32 {
        let mut max_sum = nums[0];
        let mut min_sum = nums[0];
        let mut current_max = nums[0];
        let mut current_min = nums[0];
        let mut total = nums[0];
        for num in nums.iter().skip(1) {
            current_max = if current_max < 0 {
                *num
            } else {
                current_max + num
            };
            max_sum = max_sum.max(current_max);
            current_min = if current_min > 0 {
                *num
            } else {
                current_min + num
            };
            min_sum = min_sum.min(current_min);
            total += *num;
        }
        if min_sum == total {
            max_sum
        } else {
            max_sum.max(total - min_sum)
        }
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::max_subarray_sum_circular(vec![5, -3, 5]), 10);
    assert_eq!(Solution::max_subarray_sum_circular(vec![-3, -2, -3]), -2);
    assert_eq!(Solution::max_subarray_sum_circular(vec![1, -2, 3, -2]), 3);
    assert_eq!(Solution::max_subarray_sum_circular(vec![5, -3, -7, 5]), 10);
    println!("All tests passed!")
}
