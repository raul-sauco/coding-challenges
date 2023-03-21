// 2348. Number of Zero-Filled Subarrays
// 🟠 Medium
//
// https://leetcode.com/problems/number-of-zero-filled-subarrays/
//
// Tags: Array - Sliding Window - Math

struct Solution;
impl Solution {
    /**
     * Use a for loop to iterate over the values, for each value, if we
     * are in sequence, add the sequence length to the result.
     *
     * Time complexity: O(n) -  We visit each element once and do O(1) work.
     * Space complexity: O(1) - We use constant extra memory.
     *
     * Runtime 18 ms Beats 66.67%
     * Memory 3.5 MB Beats 100%
     */
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        let (mut l, mut res) = (0, 0);
        for (r, num) in nums.iter().enumerate() {
            if *num == 0 {
                res += (r - l) + 1;
            } else {
                l = r + 1;
            }
        }
        res as i64
    }

    /**
     * Use an iterator to iterate over the values, for each value, if we
     * are in sequence, add the sequence length to the result.
     *
     * Time complexity: O(n) -  We visit each element once and do O(1) work.
     * Space complexity: O(1) - We use constant extra memory.
     *
     * Runtime 23 ms Beats 16.67%
     * Memory 3.5 MB Beats 83.33%
     */
    pub fn zero_filled_subarray_iter(nums: Vec<i32>) -> i64 {
        let mut l = 0;
        nums.iter().enumerate().fold(0, |sum, (i, num)| {
            if *num == 0 {
                sum + (i - l) + 1
            } else {
                l = i + 1;
                sum
            }
        }) as i64
    }

    /**
     * Use a while loop to iterate over the values, for each value, if we
     * are in sequence, add the sequence length to the result.
     *
     * Time complexity: O(n) -  We visit each element once and do O(1) work.
     * Space complexity: O(1) - We use constant extra memory.
     *
     * Runtime 23 ms Beats 16.67%
     * Memory 3.5 MB Beats 83.33%
     */
    pub fn zero_filled_subarray_while(nums: Vec<i32>) -> i64 {
        let (mut l, mut r, mut res) = (0, 0, 0);
        // A flag to determine whether we are inside a sequence.
        let mut in_sequence = false;
        while r < nums.len() {
            // Only compute when the new value is a zero.
            if nums[r] == 0 {
                // When we see a zero, if we are not in sequence, this zero is
                // the beginning of the sequence, update the left pointer.
                if !in_sequence {
                    l = r;
                    in_sequence = true;
                }
                // Now simply add the combinations that we can get from this
                // subarray, i.e. its length.
                res += (r - l) + 1;
            } else if in_sequence {
                // This non-zero value breaks any sequence.
                in_sequence = false;
            }
            r += 1;
        }
        res as i64
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2, 10, 2019], 0),
        (vec![0, 0, 0, 2, 0, 0], 9),
        (vec![1, 3, 0, 0, 2, 0, 0, 4], 6),
    ];
    for t in tests {
        assert_eq!(Solution::zero_filled_subarray(t.0.clone()), t.1);
        assert_eq!(Solution::zero_filled_subarray_iter(t.0.clone()), t.1);
        assert_eq!(Solution::zero_filled_subarray_while(t.0.clone()), t.1);
    }
    println!("All tests passed!")
}
