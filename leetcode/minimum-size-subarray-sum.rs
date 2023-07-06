// 209. Minimum Size Subarray Sum
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-size-subarray-sum/
//
// Tags: Array - Binary Search - Sliding Window - Prefix Sum

struct Solution;
impl Solution {
    /// Use a sliding window, increase the size on the right one element at a
    /// time adding it to a running sum, when the sum is greater or equal to
    /// the target, start decreasing its size from the left while updating the
    /// result at the same time, until the window sum becomes again smaller
    /// than the target, then go back to increasing on the right side.
    ///
    /// Time complexity: O(n) - We visit each element at most two times.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 3 ms Beats 93.10%
    /// Memory 2.9 MB Beats 94.25%
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut res = usize::MAX;
        let mut window_sum = 0;
        let mut window_size;
        let mut l = 0;
        for r in 0..nums.len() {
            window_sum += nums[r];
            while window_sum >= target {
                window_size = r - l + 1;
                // res = min(res, window_size);
                if window_size < res {
                    res = window_size;
                }
                window_sum -= nums[l];
                l += 1;
            }
        }
        if res == usize::MAX {
            0
        } else {
            res as i32
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (4, vec![1, 4, 4], 1),
        (7, vec![2, 3, 1, 2, 4, 3], 2),
        (11, vec![1, 1, 1, 1, 1, 1, 1, 1], 0),
    ];
    for t in tests {
        assert_eq!(Solution::min_sub_array_len(t.0, t.1), t.2);
    }
    println!("[92m» All tests passed![0m")
}
