// 852. Peak Index in a Mountain Array
// 🟠 Medium
//
// https://leetcode.com/problems/peak-index-in-a-mountain-array/
//
// Tags: Array - Binary Search

struct Solution;

impl Solution {
    /// Use binary search to find the peak, if the element after the mid pointer
    /// is greater, we can discard the left side up to, and including, the mid,
    /// if it is smaller, we can discard the right side excluding the middle.
    ///
    /// Time complexity: O(log(n)) - Binary search.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 6 ms Beats 82.93%
    /// Memory 3.10MB Beats 46.34%
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let (mut l, mut r) = (1, arr.len() - 2);
        let mut m;
        while l < r {
            m = (l + r) / 2;
            if arr[m] < arr[m + 1] {
                l = m + 1;
            } else {
                r = m;
            }
        }
        l as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 4, 5, 2], 4),
        (vec![0, 1, 2, 4, 2, 1], 3),
        (vec![1, 2, 3, 4, 5, 3, 1], 4),
        (vec![1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 0], 5),
    ];
    for t in tests {
        assert_eq!(Solution::peak_index_in_mountain_array(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
