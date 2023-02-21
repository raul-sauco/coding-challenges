// 540. Single Element in a Sorted Array
// 🟠 Medium
//
// https://leetcode.com/problems/single-element-in-a-sorted-array/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    // Use a modified version of binary search that checks the neighbors of
    // the value under mid to determine whether to discard the right of left
    // half of the remaining array at each step. We can use the fact that, on
    // the sequence before the single value, the pointers for the duplicates
    // will be (even, odd) while after the single value they will be
    // (odd, even). When both values right and left of the mid are different,
    // we have found the single value and we can return it.
    // Credits to StefanPochmann for the idea to use XOR with 1 to determine
    // if we are right or left of the single value, which simplifies the code
    // a lot.
    //
    // Time complexity: O(n*log(n)) - At each step we stop considering half
    // of the current search space.
    // Space complexity: O(1) - We use constant extra memory.
    //
    // Runtime 0 ms Beats 100%
    // Memory 3 MB Beats 100%
    pub fn single_non_duplicate(nums: Vec<i32>) -> i32 {
        let mut l = 0;
        let mut r = nums.len() - 1 as usize;
        while l < r {
            let mid = l + (r - l) / 2;
            if nums[mid] == nums[mid ^ 1] {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        nums[l]
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::single_non_duplicate(vec![1, 1, 2, 3, 3, 4, 4, 8, 8]),
        2
    );
    assert_eq!(
        Solution::single_non_duplicate(vec![3, 3, 7, 7, 10, 11, 11]),
        10
    );
    println!("All tests passed!")
}
