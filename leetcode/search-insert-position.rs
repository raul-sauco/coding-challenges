// 35. Search Insert Position
// 🟢 Easy
//
// https://leetcode.com/problems/search-insert-position/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    // A binary search problem with the added challenge that the value may
    // or may not exist in the given array, we can use a classic binary
    // search algorithm and a conditional in the return, if the value under
    // the pointer is equal or greater than the target value, return that
    // index, but if the value is lesser than the target, return the next
    // index to represent that we need to insert after that position.
    //
    // Time complexity: O(n*log(n)) - Each iteration reduces the search
    // space by half.
    // Space complexity: O(1) - Constant extra memory is used.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.1 MB Beats 54.45%
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let (mut l, mut r) = (0, nums.len() - 1);
        while l < r {
            let mid = l + (r - l) / 2;
            if nums[mid] < target {
                l = mid + 1;
            } else {
                r = if mid == 0 { 0 } else { mid - 1 };
            }
        }
        if nums[l] < target {
            (l + 1) as i32
        } else {
            l as i32
        }
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::search_insert(vec![4], 3), 0);
    assert_eq!(Solution::search_insert(vec![4], 5), 1);
    assert_eq!(Solution::search_insert(vec![-1], -1), 0);
    assert_eq!(Solution::search_insert(vec![1, 3], 0), 0);
    assert_eq!(Solution::search_insert(vec![2, 3, 5, 6], 1), 0);
    assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 2), 1);
    assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 5), 2);
    assert_eq!(Solution::search_insert(vec![1, 3, 5, 8], 7), 3);
    assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 7), 4);
    println!("All tests passed!")
}
