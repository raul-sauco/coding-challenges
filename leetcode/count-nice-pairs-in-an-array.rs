// 1814. Count Nice Pairs in an Array
// 🟠 Medium
//
// https://leetcode.com/problems/count-nice-pairs-in-an-array/
//
// Tags: Array - Hash Table - Math - Counting

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Once we realize that we can transform the equation that defines a nice pair to have both
    /// terms that depend on the current value that we are visiting on the same side:
    /// » nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
    /// We have simplified the problem and can use a similar solution as the classic two-sum, for
    /// each element on nums, compute its "pair value" and check the count of times that we have
    /// seen it previously, we can form a pair for each time we have seen that value. After that,
    /// either add 1 to the existing count, or add an entry with a value of 1 if previously not
    /// found in the hashmap.
    ///
    /// Time complexity: O(m*n) - We need to visit each digit m in the n values in the input.
    /// Space complexity: O(n) - The counts hashmap has the same size as the input.
    ///
    /// Runtime 15 ms Beats 80%
    /// Memory 3.75 MB Beats 60%
    pub fn count_nice_pairs(nums: Vec<i32>) -> i32 {
        // A function that reverses a number's digits.
        let rev = |mut x| {
            let mut reversed = 0;
            while x > 0 {
                reversed = reversed * 10 + (x % 10);
                x /= 10;
            }
            reversed
        };
        // A nice pair => nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        let mut res = 0;
        let mut counts: HashMap<i32, i64> = HashMap::new();
        for num in nums {
            counts
                .entry(num - rev(num))
                .and_modify(|count| {
                    res += *count;
                    *count += 1;
                })
                .or_insert(1);
        }
        (res % 1_000_000_007) as i32
    }
}

// Tests.
fn main() {
    let tests = [(vec![42, 11, 1, 97], 2), (vec![13, 10, 35, 24, 76], 4)];
    for t in tests {
        assert_eq!(Solution::count_nice_pairs(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
