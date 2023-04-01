// 704. Binary Search
// 🟢 Easy
//
// https://leetcode.com/problems/binary-search/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    /// Use binary search! Use a left and right pointer, at each iteration
    /// compute the mid-point between them, when the value at that mid index is
    /// greater than the target, we know that the target will be to the left if
    /// it found in the array, when the value is lesser, it will be found to
    /// the right.
    ///
    /// Time complexity: O(log(n)) - Each iteration discards half of the
    /// search space.
    /// Space complexity: O(1) - We use constant space.
    ///
    /// Runtime 5 ms Beats 66.86%
    /// Memory 2.2 MB Beats 79.66%
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut l, mut r) = (0, nums.len() - 1);
        let mut mid;
        while l < r {
            // mid = (l+r) / 2; works as well, 10^4 won't overflow.
            mid = l + (r - l) / 2;
            if nums[mid] < target {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        if nums[l] == target {
            l as i32
        } else {
            -1
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![5], 5, 0),
        (vec![-4, -2, 0, 1], 2, -1),
        (vec![-1, 0, 3, 5, 9, 12], 9, 4),
        (vec![-1, 0, 3, 5, 9, 12], 2, -1),
    ];
    for t in tests {
        assert_eq!(Solution::search(t.0.clone(), t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
