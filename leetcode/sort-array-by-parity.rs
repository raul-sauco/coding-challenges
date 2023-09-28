// 905. Sort Array By Parity
// 🟢 Easy
//
// https://leetcode.com/problems/sort-array-by-parity/
//
// Tags: Array - Two Pointers - Sorting

struct Solution;
impl Solution {
    /// Use two pointers, the pointer at the left stops when it points to an odd
    /// value, the one on the right stops when it points to an even value, when
    /// they both do, swap the elements they point to and shuffle the pointers.
    ///
    /// Time complexity: O(n) - We visit each element and do constant time work
    /// for each.
    /// Space complexity: O(1) - We are mutating the input vector in place by
    /// explicitly converting it to a mutable vector.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.06 MB Beats 97.22%
    pub fn sort_array_by_parity(nums: Vec<i32>) -> Vec<i32> {
        let (mut l, mut r) = (0, nums.len() - 1);
        let mut nums = nums;
        while l < r {
            if nums[l] % 2 != 0 && nums[r] % 2 == 0 {
                nums.swap(l, r);
                l += 1;
                r -= 1;
            } else {
                if nums[l] % 2 == 0 {
                    l += 1;
                }
                if nums[r] % 2 == 1 {
                    r -= 1;
                }
            }
        }
        nums
    }

    /// Easier to read solution, it sacrifices performance because it swaps
    /// elements when sometimes it is not necessary.
    ///
    /// Time complexity: O(n) - We visit each element and do constant time work
    /// for each.
    /// Space complexity: O(1) - We are mutating the input vector in place.
    ///
    /// Runtime 3 ms Beats 75%
    /// Memory 2.10 MB Beats 97.22%
    pub fn sort_array_by_parity_2(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        let mut l = 0;
        for r in 0..nums.len() {
            if nums[r] % 2 == 0 {
                nums.swap(l, r);
                l += 1;
            }
        }
        nums
    }

    /// Check if a given array has parity, parity is defined as all even values
    /// coming before any odd value.
    pub fn has_parity(nums: &Vec<i32>) -> bool {
        let mut odds = false;
        for num in nums {
            if odds && num % 2 == 0 {
                return false;
            }
            if num % 2 == 1 && !odds {
                odds = true;
            }
        }
        true
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0], vec![0]),
        (vec![3, 1, 2, 4], vec![4, 2, 1, 3]),
        (vec![3, 5, 7, 1], vec![3, 5, 7, 1]),
        (vec![3, 5, 7, 1, 25, 22, 33], vec![22, 5, 7, 1, 25, 3, 33]),
    ];
    for t in tests {
        assert!(Solution::has_parity(&Solution::sort_array_by_parity(
            t.0.clone()
        )));
        assert!(Solution::has_parity(&Solution::sort_array_by_parity_2(
            t.0.clone()
        )));
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
