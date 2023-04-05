// 2439. Minimize Maximum of Array
// 🟠 Medium
//
// https://leetcode.com/problems/minimize-maximum-of-array/
//
// Tags: Array - Binary Search - Dynamic Programming - Greedy - Prefix Sum

struct Solution;
impl Solution {
    /// Iterate over the array from left to right keeping the sum of
    /// values 0..i, at that point, at any point we can move values to the
    /// left, but never to the right, for any given i, the maximum value of
    /// the subarray at that point will be the ceiling of the average of the
    /// values on 0..i, the result will be the maximum of all the subarray
    /// maximums.
    ///
    /// Time complexity: O(n) - We iterate over all elements and do O(1) work
    /// for each.
    /// Space complexity: O(1) - We store three integers.
    ///
    /// Runtime 12 ms Beats 87.50%
    /// Memory 3.4 MB Beats 62.50%
    pub fn minimize_array_value(nums: Vec<i32>) -> i32 {
        nums.into_iter()
            .scan(0, |state, x| {
                *state = *state + x as u64;
                Some(*state)
            })
            .enumerate()
            .map(|(idx, ps)| ((ps + idx as u64) / (idx as u64 + 1)))
            .max()
            .unwrap() as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![10, 1], 10),
        (vec![3, 7, 1, 6], 5),
        (vec![6, 9, 3, 8, 14], 8),
        (vec![13, 13, 20, 0, 8, 9, 9], 16),
    ];
    for t in tests {
        assert_eq!(Solution::minimize_array_value(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
