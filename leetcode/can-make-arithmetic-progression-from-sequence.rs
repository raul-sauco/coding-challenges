// 1502. Can Make Arithmetic Progression From Sequence
// 🟢 Easy
//
// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
//
// Tags: Array - Sorting

use std::collections::HashSet;

struct Solution;
impl Solution {
    /// Create a duplicate of the input array and sort it, check the difference
    /// between any two contiguous items and make sure the difference is the
    /// same between any two items in the sorted array.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the highest time complexity.
    /// Space complexity: O(n) - We make a copy of the input array. Besides that
    /// sorting the array also takes extra memory, O(log(n))
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.1 MB Beats 40%
    pub fn can_make_arithmetic_progression(arr: Vec<i32>) -> bool {
        if arr.len() < 3 {
            return true;
        }
        let mut nums = arr.clone();
        nums.sort();
        let diff = nums[1] - nums[0];
        for i in 2..nums.len() {
            if nums[i] - nums[i - 1] != diff {
                return false;
            }
        }
        true
    }

    /// Find the minimum and maximum values in the input, compute the difference
    /// as (max-min) / num elements-1 Then create an array of flags that
    /// represents whether we have already seen the element that needs to go at
    /// any given position in the sequence. Start iterating over the input
    /// elements matching their values to the indexes along the sequence at
    /// which they should be found, if that value has been seen before, or the
    /// element does not match an index, return false, otherwise mark that
    /// index as seen.
    ///
    /// Time complexity: O(n) - We iterate two times over all the elements in
    /// the input array, for each we do O(1) work.
    /// Space complexity: O(n) - The array of flags uses extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 40%
    pub fn can_make_arithmetic_progression_2(arr: Vec<i32>) -> bool {
        let n = arr.len() as i32;
        let (mut min, mut max) = (i32::MAX, i32::MIN);
        for num in arr.iter() {
            if *num > max {
                max = *num;
            }
            if *num < min {
                min = *num;
            }
        }
        if (max - min) % (n - 1) != 0 {
            return false;
        }
        let diff = (max - min) / (n - 1);
        if diff == 0 {
            return arr.into_iter().collect::<HashSet<i32>>().len() == 1;
        }
        let mut seen = vec![false; arr.len()];
        for num in arr {
            if (num - min) % diff != 0 {
                return false;
            }
            let idx = ((num - min) / diff) as usize;
            if seen[idx] {
                return false;
            }
            seen[idx] = true;
        }
        true
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 1, 5], true),
        (vec![1, 2, 4], false),
        (vec![0, 0, 0, 0], true),
    ];
    for t in tests {
        assert_eq!(Solution::can_make_arithmetic_progression(t.0.clone()), t.1);
        assert_eq!(
            Solution::can_make_arithmetic_progression_2(t.0.clone()),
            t.1
        );
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
