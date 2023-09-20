// 1658. Minimum Operations to Reduce X to Zero
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
//
// Tags: Array - Hash Table - Binary Search - Sliding Window - Prefix Sum

struct Solution;
impl Solution {
    /// Use a two pointer approach to find the maximum subarray with sum equal
    /// to the sum of the values in nums - x.
    ///
    /// Time complexity: O(n) - We visit each element and do constant work for
    /// each.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 18 ms Beats 40%
    /// Memory 2.85 MB Beats 80%
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
        let target = nums.iter().sum::<i32>() - x;
        if target == 0 {
            return nums.len() as i32;
        }
        let (mut l, mut res, mut current_sum) = (0, 0, 0);
        for r in 0..nums.len() {
            current_sum += nums[r];
            if current_sum == target && 1 + r - l > res {
                res = 1 + r - l;
            }
            while current_sum >= target && l <= r {
                current_sum -= nums[l];
                l += 1;
                if current_sum == target && 1 + r - l > res {
                    res = 1 + r - l;
                }
            }
        }
        if res == 0 {
            -1
        } else {
            (nums.len() - res) as i32
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 1, 4, 2, 3], 5, 2),
        (vec![5, 6, 7, 8, 9], 4, -1),
        (vec![3, 2, 20, 1, 1, 3], 10, 5),
        (
            vec![
                8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904,
                8819, 1231, 6309,
            ],
            134365,
            16,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::min_operations(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
