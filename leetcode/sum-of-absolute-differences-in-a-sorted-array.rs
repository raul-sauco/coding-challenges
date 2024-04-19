// 1685. Sum of Absolute Differences in a Sorted Array
// 🟠 Medium
//
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
//
// Tags: Array - Math - Prefix Sum

struct Solution;
impl Solution {
    /// Iterate once over all the values to get their sum. Iterate again keeping track of the sum
    /// of values before and after the current one. The sum of absolute differences to the right
    /// can be computed as the difference of the sum of values to the right and a vector of the
    /// same length that was formed for all values equal to the current one.
    ///
    /// Time complexity: O(n) - We iterate twice over the input values, for each value we do
    /// constant time work both times.
    /// Space complexity: O(1) - Not taking into account the output vector, we use constant extra
    /// memory.
    ///
    /// Runtime 31 ms Beats 100%
    /// Memory 3.30 MB Beats 100%
    pub fn get_sum_absolute_differences(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let x = n as i32 - 1;
        let mut postfix_sum = nums.iter().sum::<i32>();
        let mut res = vec![0; n];
        // Keep the sum of values to the left.
        let mut prefix_sum = 0;
        for i in 0..n {
            postfix_sum -= nums[i];
            // The sum of absolute differences to the right.
            // res[i] += postfix_sum - ((n - i - 1) as i32 * nums[i]);
            //
            // The sum of absolute differences to the left.
            // res[i] += i as i32 * nums[i] - prefix_sum;
            //
            // We can merge the two previous lines:
            // res[i] = postfix_sum - prefix_sum + (i as i32 * nums[i]) - ((n - i - 1) as i32 * nums[i]);
            //
            // And, if we operate on the terms, we can simplify to:
            res[i] = postfix_sum - prefix_sum + (2 * i as i32 - x) * nums[i];
            prefix_sum += nums[i];
        }
        res
    }

    /// Same solution, but merge `prefix_sum` and `postfix_sum` into one variable `current_sum`.
    ///
    /// Time complexity: O(n) - We iterate twice over the input values, for each value we do
    /// constant time work both times.
    /// Space complexity: O(1) - Not taking into account the output vector, we use constant extra
    /// memory.
    ///
    /// Runtime 31 ms Beats 100%
    /// Memory 3.30 MB Beats 100%
    pub fn get_sum_absolute_differences_2(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut total = nums.iter().sum::<i32>();
        (0..n)
            .zip(nums.iter())
            .map(|(i, el)| {
                total -= el * 2;
                total + (2 * i - n + 2) * el
            })
            .collect()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![5, 5], vec![0, 0]),
        (vec![-3, 5], vec![8, 8]),
        (vec![2, 3, 5], vec![4, 3, 5]),
        (vec![1, 4, 6, 8, 10], vec![24, 15, 13, 15, 21]),
    ];
    for t in tests {
        assert_eq!(Solution::get_sum_absolute_differences(t.0.clone()), t.1);
        assert_eq!(Solution::get_sum_absolute_differences_2(t.0.clone()), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
