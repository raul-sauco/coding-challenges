// 34. Find First and Last Position of Element in Sorted Array
// 🟠 Medium
//
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    /// Do a binary search to find the first insert position, if the target is
    /// found, do a second binary search for the insert position for the next
    /// value, since the input consists of integers, target + 1 would have an
    /// insert position of the last position of target plus one.
    ///
    /// Time complexity: O(log(n)) - Two binary searches.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.32 MB Beats 65.83%
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut res = vec![-1, -1];
        if nums.len() == 0 {
            return res;
        }
        // Search for the first position at which we can insert the value x in
        // the vector nums. We can especify boundaries l and r for the search.
        fn binary_search(nums: &Vec<i32>, l: usize, r: usize, x: i32) -> usize {
            let mut mid;
            let (mut lo, mut hi) = (l, r);
            while lo < hi {
                mid = (lo + hi) / 2;
                if nums[mid] < x {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            lo
        }
        let first_idx = binary_search(&nums, 0, nums.len(), target);
        if first_idx < nums.len() && nums[first_idx] == target {
            res[0] = first_idx as i32;
            res[1] = binary_search(&nums, first_idx, nums.len(), target + 1) as i32 - 1;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![5, 7, 7, 8, 8, 10], 8, vec![3, 4]),
        (vec![5, 7, 7, 8, 8, 10], 6, vec![-1, -1]),
        (vec![], 0, vec![-1, -1]),
    ];
    for t in tests {
        assert_eq!(Solution::search_range(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
