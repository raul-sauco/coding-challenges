// 1887. Reduction Operations to Make the Array Elements Equal
// 🟠 Medium
//
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
//
// Tags: Array - Sorting

struct Solution;
impl Solution {
    /// Sort the numbers, then traverse them from greatest to smallest, for every step down that we
    /// need to take, each of the numbers to the right will need to be updated, we can add that
    /// many operations to the result.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the highest time complexity, after that the
    /// algorithm runs in O(n)
    /// Space complexity: O(n) - The mutable copy of nums, if we didn't use it, then it would be
    /// log(n) for the sorting (Quicksort for `sort_unstable`)
    ///
    /// Runtime 23 ms Beats 83.33%
    /// Memory 2.46 MB Beats 66.67%
    pub fn reduction_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut nums = nums;
        nums.sort_unstable();
        let mut res = 0;
        for i in (1..n).rev() {
            if nums[i - 1] != nums[i] {
                res += n - i;
            }
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![5], 0),
        (vec![5, 1, 3], 3),
        (vec![1, 1, 1], 0),
        (vec![1, 1, 2, 2, 3], 4),
    ];
    for t in tests {
        assert_eq!(Solution::reduction_operations(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
