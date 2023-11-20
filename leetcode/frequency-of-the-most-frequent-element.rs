// 1838. Frequency of the Most Frequent Element
// 🟠 Medium
//
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/
//
// Tags: Array - Binary Search - Greedy - Sliding Window - Sorting - Prefix Sum

struct Solution;
impl Solution {
    /// Sort the input, I sorted it in reverse, because I thought it would be easier to reason
    /// about the sliding window algorithm that way, but in the editorial they sort ascending and
    /// it ends up being very similar. Use a sliding window to visit sections of the array, grow
    /// the window while the number of operations needed to make all elements equal to the
    /// greatest one is <= k, after that, start sliding the window to see if there is any greater
    /// window to the right. We don't need to shrink the window because we are only interested in
    /// the largest window, once we find a window of size n, we are not interested in finding any
    /// other unless they are of size >= n.
    ///
    /// Time complexity: O(n*log(n)) - For the sorting step, after that, the sliding window
    /// algorithm runs in O(n)
    /// Space complexity: O(n) - The mutable copy of the input, if we mutate the input instead,
    /// then it would be O(1)
    ///
    /// Runtime 21 ms Beats 89.16%
    /// Memory 3.21 MB Beats 81.77%
    pub fn max_frequency(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        nums.sort_unstable_by(|a, b| b.cmp(a));
        let mut res = 0;
        let mut ops = 0;
        let mut l = 0;
        for r in 0..nums.len() {
            // We need to convert nums[r] to nums[l]
            ops += nums[l] - nums[r];
            // If we have expanded the window too far, shrink it.
            if ops > k {
                l += 1;
                // We are using "difference between nums" operations less per num.
                ops -= (nums[l - 1] - nums[l]) * (r - l + 1) as i32;
            }
            res = res.max(r - l + 1);
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 4], 5, 3),
        (vec![1, 4, 8, 13], 5, 2),
        (vec![3, 9, 6], 2, 1),
    ];
    for t in tests {
        assert_eq!(Solution::max_frequency(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
