// 896. Monotonic Array
// 🟢 Easy
//
// https://leetcode.com/problems/monotonic-array/
//
// Tags: Array

struct Solution;
impl Solution {
    /// One pass, two flags, visit each pair of values checking whether there
    /// are any increasing and decreasing pairs. If we find them both, return
    /// false.
    ///
    /// Time complexity: O(n) - We visit each pair of elements and do constant
    /// time work for each.
    /// Space complexity: O(1) - We use two booleans of extra memory.
    ///
    /// Runtime 16 ms Beats 37.70%
    /// Memory 3.25 MB Beats 54.10%
    pub fn is_monotonic(nums: Vec<i32>) -> bool {
        let (mut increasing, mut decreasing) = (false, false);
        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                if decreasing {
                    return false;
                }
                increasing = true;
            }
            if nums[i] < nums[i - 1] {
                if increasing {
                    return false;
                }
                decreasing = true;
            }
        }
        true
    }

    /// One pass, two flags, visit each pair of values checking whether there
    /// are any increasing and decreasing pairs. If we find them both, return
    /// false.
    ///
    /// Time complexity: O(n) - We visit each pair of elements and do constant
    /// time work for each.
    /// Space complexity: O(1) - We use two booleans of extra memory.
    ///
    /// Runtime 17 ms Beats 37.70%
    /// Memory 3.25 MB Beats 54.10%
    pub fn is_monotonic_2(nums: Vec<i32>) -> bool {
        let (mut increasing, mut decreasing) = (false, false);
        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                increasing = true;
            }
            if nums[i] < nums[i - 1] {
                decreasing = true;
            }
        }
        !(increasing && decreasing)
    }

    /// Use one flag, travel through the array until we find one increasing or
    /// decreasing value, register which one. Then exit that loop and loop
    /// through the remaining values making sure they maintain the monotonic
    /// nature of the array.
    ///
    /// Time complexity: O(n) - We visit each element in the input and do O(1)
    /// work for each.
    /// Space complexity: O(1) - We only store two boolean values.
    ///
    /// Runtime 8 ms Beats 91.80%
    /// Memory 3.25 MB Beats 54.10%
    pub fn is_monotonic_3(nums: Vec<i32>) -> bool {
        if nums.len() < 2 {
            return true;
        }
        for i in 1..nums.len() {
            if nums[i] == nums[0] {
                continue;
            }
            let increasing = nums[i] > nums[0];
            for j in i + 1..nums.len() {
                if nums[j] == nums[j - 1] {
                    continue;
                }
                if (increasing && nums[j] < nums[j - 1]) || (!increasing && nums[j] > nums[j - 1]) {
                    return false;
                }
            }
            break;
        }
        true
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 2, 3], true),
        (vec![6, 5, 4, 4], true),
        (vec![1, 3, 2], false),
    ];
    for t in tests {
        assert_eq!(Solution::is_monotonic(t.0.clone()), t.1);
        assert_eq!(Solution::is_monotonic_2(t.0.clone()), t.1);
        assert_eq!(Solution::is_monotonic_3(t.0.clone()), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
