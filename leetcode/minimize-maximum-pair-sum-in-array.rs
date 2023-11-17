// 1877. Minimize Maximum Pair Sum in Array
// 🟠 Medium
//
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
//
// Tags: Array - Two Pointers - Greedy - Sorting

struct Solution;
impl Solution {
    /// Sort the input, then make pairs using the biggest and smallest unused elements, that way we
    /// guarantee that we are minimizing the pair sum.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the local copy of nums, after that, checking the
    /// pairs in O(n)
    /// Space complexity: O(n) - The local mutable copy of the input vector.
    ///
    /// Runtime 26 ms Beats 71.05%
    /// Memory 3.29 MB Beats 55.26%
    pub fn min_pair_sum(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let mut res = 0;
        let (mut l, mut r) = (0, nums.len() - 1);
        while l < r {
            res = res.max(nums[l] + nums[r]);
            l += 1;
            r -= 1;
        }
        res
    }

    /// Similar solution but using iterators.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the local copy of nums, after that, checking the
    /// pairs in O(n)
    /// Space complexity: O(n) - The local mutable copy of the input vector.
    ///
    /// Runtime 36 ms Beats 52.63%
    /// Memory 3.40 MB Beats 39.47%
    pub fn min_pair_sum_2(nums: Vec<i32>) -> i32 {
        let half = nums.len() / 2;
        let mut nums = nums;
        nums.sort_unstable();
        nums.iter()
            .take(half)
            .zip(nums.iter().rev().take(half))
            .map(|(a, b)| a + b)
            .max()
            .unwrap()
    }
}

// Tests.
fn main() {
    let tests = [(vec![3, 5, 2, 3], 7), (vec![3, 5, 4, 2, 4, 6], 8)];
    for t in tests {
        assert_eq!(Solution::min_pair_sum(t.0.clone()), t.1);
        assert_eq!(Solution::min_pair_sum_2(t.0.clone()), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
