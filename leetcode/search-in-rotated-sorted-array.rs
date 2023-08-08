// 33. Search in Rotated Sorted Array
// 🟠 Medium
//
// https://leetcode.com/problems/search-in-rotated-sorted-array/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    /// Neat idea and explanation found here:
    /// https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/14435/clever-idea-making-it-simple/
    ///
    /// Time complexity: O(log(n)) - The algorithm works like a binary search
    /// with an extra if statement executed in each iteration.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 1 ms Beats 68.47%
    /// Memory 2 MB Beats 79.73%
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut l, mut r) = (0, nums.len());
        let mut num;
        let mut mid;
        while l < r {
            mid = (l + r) / 2;
            num = if (nums[mid] < nums[0]) == (target < nums[0]) {
                nums[mid]
            } else {
                if target < nums[0] {
                    i32::MIN
                } else {
                    i32::MAX
                }
            };
            if num < target {
                l = mid + 1;
            } else if num > target {
                r = mid;
            } else {
                return mid as i32;
            }
        }
        -1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], 0, -1),
        (vec![4, 5, 6, 7, 0, 1, 2], 0, 4),
        (vec![4, 5, 6, 7, 0, 1, 2], 3, -1),
    ];
    for t in tests {
        assert_eq!(Solution::search(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m");
}
