// 1493. Longest Subarray of 1's After Deleting One Element
// 🟠 Medium
//
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
//
// Tags: Array - Dynamic Programming - Sliding Window

struct Solution;
impl Solution {
    /// Use a sliding window technique, expand the window by one element at a
    /// time on the right side, when the window contains more than one zero,
    /// shrink it from the left until we are back to containing only one zero.
    /// Return the size of the greatest window seen minus one because we must
    /// delete one element.
    ///
    /// Time complexity: O(n) - We visit each element and do constant work.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 6 ms Beats 56.45%
    /// Memory 2.4 MB Beats 56.45%
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut l = 0;
        let mut zero_count = 0;
        for r in 0..nums.len() {
            if nums[r] == 0 {
                zero_count += 1;
            }
            while zero_count > 1 {
                if nums[l] == 0 {
                    zero_count -= 1;
                }
                l += 1;
            }
            // Compute the window size -1 because we must delete one element.
            let window_size = r - l;
            if window_size > res {
                res = window_size;
            }
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 1, 1], 2),
        (vec![1, 1, 0, 1], 3),
        (vec![0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
    ];
    for t in tests {
        assert_eq!(Solution::longest_subarray(t.0), t.1);
    }
    println!("[92m» All tests passed![0m")
}
