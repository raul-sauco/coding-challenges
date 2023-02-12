// 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
// 🟠 Medium
//
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
//
// Tags: Array - Sliding Window

struct Solution;
impl Solution {
    // For the average to be greater than or equal to the threshold, the sum
    // of values needs to be equal to or greater than threshold * k when the
    // size of the subarray is k. That lets us compute the solution in linear
    // time.
    //
    // Time complexity: O(n) - We visit each element once.
    // Space complexity: O(1) - We use constant extra space.
    //
    // Runtime 9 ms Beats 77.78%
    // Memory 3.4 MB Beats 22.22%
    pub fn num_of_subarrays(arr: Vec<i32>, k: i32, threshold: i32) -> i32 {
        if k > arr.len() as i32 {
            return 0;
        }
        let mut count = 0;
        let t = threshold * k;
        let mut window_sum: i32 = arr[..k as usize].iter().sum();
        if window_sum >= t {
            count += 1;
        }
        for r in k as usize..arr.len() {
            window_sum += arr[r] - arr[r - k as usize];
            if window_sum >= t {
                count += 1;
            }
        }
        count
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::num_of_subarrays(vec![20, 20], 3, 4), 0);
    assert_eq!(
        Solution::num_of_subarrays(vec![2, 2, 2, 2, 5, 5, 5, 8], 3, 4),
        3
    );
    assert_eq!(
        Solution::num_of_subarrays(vec![11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5),
        6
    );
    println!("All tests passed!")
}
