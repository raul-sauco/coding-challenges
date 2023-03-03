// 80. Remove Duplicates from Sorted Array II
// 🟠 Medium
//
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/h
//
// Tags: Array - Two Pointers

struct Solution;
impl Solution {
    // Generic solution that leaves a maximum of n instances of the same element
    // in a given sorted input array. The solution uses two pointers, one to read
    // and one to write, to iterate over the input, when the element over the read
    // pointer is the same as the one n indexes back from the write pointer, it
    // skips it, otherwise, we know that we have less than n instances of that
    // element in the current output array, and we can add the current one.
    //
    // Time complexity: O(n) - We visit each value in the input once.
    // Space complexity: O(1) - We only use pointers.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.1 MB Beats 84.38%
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        // The maximum number of duplicates allowed.
        const MAX_DUPLICATES: usize = 2;
        // Nothing to do.
        if nums.len() <= MAX_DUPLICATES {
            return nums.len() as i32;
        }
        // A write pointer.
        let mut w = MAX_DUPLICATES;
        for r in MAX_DUPLICATES..nums.len() {
            // Check if the value two positions back is the same.
            if nums[r] != nums[w - MAX_DUPLICATES] {
                nums[w] = nums[r];
                w += 1;
            }
        }
        w as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], 1),
        (vec![1, 1], 2),
        (vec![1, 1, 1, 2, 2, 3], 5),
        (vec![0, 0, 1, 1, 1, 1, 2, 3, 3], 7),
    ];
    for test in tests {
        assert_eq!(Solution::remove_duplicates(&mut Vec::from(test.0)), test.1);
    }
    println!("All tests passed!")
}
