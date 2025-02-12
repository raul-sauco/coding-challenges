// 2342. Max Sum of a Pair With Equal Sum of Digits
// 🟠 Medium
//
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
//
// Tags: Array - Hash Table - Sorting - Heap (Priority Queue)

struct Solution;
impl Solution {
    /// Create an array where the index is the digit sum of an element and the value is the maximum
    /// value found so far with that digit sum. Initialize its values to something smaller than any
    /// digit sum could be, i32::MIN, -1, 0... Iterate over the elements, for each one, compute the
    /// sum of its digits, if we have seen that sum before, get the sum of the current element and
    /// the previous max for that digit sum, and max that with the current overall max, the result,
    /// and update it if necessary. If the current num is the maximum for its digit sum, update
    /// that as well.
    ///
    /// Time complexity: O(n) - For each element, we get its digit sum, O(9) max, then do a max of
    /// 2 comparisons and one addition.
    /// Space complexity: O(1) - The array of size 100 with the max elements.
    ///
    /// Runtime 1 ms Beats 82%
    /// Memory 4.05 MB Beats 73%
    pub fn maximum_sum(nums: Vec<i32>) -> i32 {
        #[inline(always)]
        fn get_digits_sum(mut num: i32) -> usize {
            let mut res = 0;
            while num > 0 {
                res += num % 10;
                num /= 10;
            }
            res as usize
        }
        let mut res = -1;
        let mut max_by_digit_sum = [-1; 100];
        for num in nums {
            let digits_sum = get_digits_sum(num);
            if max_by_digit_sum[digits_sum] != -1 {
                res = res.max(num + max_by_digit_sum[digits_sum]);
                max_by_digit_sum[digits_sum] = max_by_digit_sum[digits_sum].max(num);
            } else {
                max_by_digit_sum[digits_sum] = num;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![18, 43, 36, 13, 7], 54), (vec![10, 12, 19, 14], -1)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_sum(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.1, res
            );
        }
    }
    println!();
    if success == tests.len() {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
