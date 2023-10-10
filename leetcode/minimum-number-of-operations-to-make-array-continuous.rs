// 2009. Minimum Number of Operations to Make Array Continuous
// 🔴 Hard
//
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    /// Sort the input, then use a sliding window technique, the sliding window
    /// is computed using the value of the left edge and the value that the
    /// right edge should have for the array to be continuous. When we find these
    /// two indexes, we know that the elements between these two indexes can be
    /// used as part of the continuous array, and we will need to change all
    /// the others. We try all left boundaries and keep the one that results in
    /// the least amount of substitutions.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the input vector has the highest
    /// complexity, the sliding window algorithm runs in O(n) because r never
    /// moves backwards.
    /// Space complexity: O(n) - We keep a local copy of nums, in languages that
    /// let us mutate the input, we could sort the input vector. Besides that,
    /// we use, probably, O(log(n)) extra space for the sorting and constant
    /// extra space besides that.
    ///
    /// Runtime 21 ms Beats 100%
    /// Memory 3.90 MB Beats 100%
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        // We are looking for a minimum number of substitutions.
        let mut res = i32::MAX;
        let n = nums.len();
        let offset = n as i32 - 1;
        // We want a sorted copy of nums with all duplicates removed.
        let mut nums = nums;
        nums.sort_unstable();
        nums.dedup();
        // Store the value that should be at the right end of the continuous vector.
        let mut x;
        let mut r = 0;
        for l in 0..nums.len() {
            x = nums[l] + offset;
            while r < nums.len() && nums[r] <= x {
                r += 1;
                // if r >= nums.len() || nums[r] > x {
                // break;
                //}
            }
            // We can use the elements between l and r-1 to build a continuous
            // sequence, how many more do we need? These we need to convert.
            res = res.min((n + l - r) as i32);
            if r == nums.len() {
                break;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![4, 2, 5, 3], 0),
        (vec![1, 2, 3, 5, 6], 1),
        (vec![1, 10, 100, 1000], 3),
    ];
    for t in tests {
        assert_eq!(Solution::min_operations(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
