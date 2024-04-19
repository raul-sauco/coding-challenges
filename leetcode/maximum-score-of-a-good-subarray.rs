// 1793. Maximum Score of a Good Subarray
// 🔴 Hard
//
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/
//
// Tags: Array - Two Pointers - Binary Search - Stack - Monotonic Stack

struct Solution;
impl Solution {
    /// The brute force solution, iterate over all combinations of i..j and
    /// compute the subarray score.
    ///
    /// Time complexity: O(n^2) - We iterate over all combinations of i and j
    /// and do constant time operations for each.
    /// Space complexity: O(1) - Constant extra space used.
    pub fn brute_force(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut res = 0;
        let mut subarray_min;
        for i in 0..=k {
            subarray_min = i32::MAX;
            for j in i..nums.len() {
                if nums[j] < subarray_min {
                    subarray_min = nums[j];
                }
                if j >= k {
                    res = res.max((j - i + 1) as i32 * subarray_min);
                }
            }
        }
        res
    }

    /// We need to use the value at nums[k], starting from there, travel both
    /// left and right computing a vector of minimums. Use these minimums, and
    /// a two pointer approach, we start at both ends of the minimum array and
    /// move the pointer with the smaller value towards the middle, there is no
    /// advantage to moving the pointer with the higher value because the result
    /// is constrained by the minimum.
    ///
    /// Time complexity: O(n) - We iterate twice over the input, once to create
    /// the vector of minimums, and another time using the two pointer algorithm
    /// to get the max area of the rectangle with width r-l+1 and height min
    /// between mins left and right.
    /// Space complexity: O(n) - The subarray mins vector has the same size as
    /// the input.
    ///
    /// Runtime 20 ms Beats 48.89%
    /// Memory 2.92 MB Beats 64.44%
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let n = nums.len();
        let mut res = 0;
        let mut subarray_mins = nums.clone();
        for i in (0..k).rev() {
            subarray_mins[i] = subarray_mins[i + 1].min(nums[i]);
        }
        for i in k + 1..n {
            subarray_mins[i] = subarray_mins[i - 1].min(nums[i]);
        }
        // Two pointer algorithm.
        let (mut l, mut r) = (0, n - 1);
        while l <= r {
            if subarray_mins[l] <= subarray_mins[r] {
                res = res.max((r - l + 1) as i32 * subarray_mins[l]);
                l += 1;
            } else {
                res = res.max((r - l + 1) as i32 * subarray_mins[r]);
                r -= 1;
            }
        }
        res as i32
    }

    /// Similar to the previous solution but get rid of the auxiliary mins vector.
    ///
    /// Time complexity: O(n) - We iterate twice over the input, once to create
    /// the vector of minimums, and do constant time work for each element.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 13 ms Beats 93.33%
    /// Memory 3.08 MB Beats 28.67%
    pub fn maximum_score_2(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let n = nums.len();
        let mut res = nums[k];
        let (mut l, mut r) = (k, k);
        let mut cur_min = nums[k];
        while l > 0 || r < n - 1 {
            if (if l > 0 { nums[l - 1] } else { 0 }) < (if r < n - 1 { nums[r + 1] } else { 0 }) {
                r += 1;
                cur_min = cur_min.min(nums[r]);
            } else {
                l -= 1;
                cur_min = cur_min.min(nums[l]);
            }
            res = res.max((r - l + 1) as i32 * cur_min);
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 4, 3, 7, 4, 5], 3, 15),
        (vec![5, 5, 4, 5, 4, 5], 2, 24),
        (vec![5, 5, 4, 5, 4, 1, 1, 1], 0, 20),
    ];
    for t in tests {
        assert_eq!(Solution::brute_force(t.0.clone(), t.1), t.2);
        assert_eq!(Solution::maximum_score(t.0.clone(), t.1), t.2);
        assert_eq!(Solution::maximum_score_2(t.0.clone(), t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
