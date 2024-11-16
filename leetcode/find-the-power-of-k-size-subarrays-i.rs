// 3254. Find the Power of K-Size Subarrays I
// 🟠 Medium
//
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
//
// Tags: Array - Sliding Window

struct Solution;
impl Solution {
    /// Iterate over the input vector, keep track of the count of increasing values up to the
    /// current point, if we have k or more, the k sized subarray is good, we can return its
    /// greatest value, the last one as the result for this subarray, otherwise -1.
    ///
    /// Time complexity: O(n) - We iterate over the input and do constant time workfor each
    /// element that we visit.
    /// Space complexity: O(1) - We store the count of good elements.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.17 MB Beats 87%
    pub fn results_array(nums: Vec<i32>, k: i32) -> Vec<i32> {
        if k == 1 {
            return nums;
        }
        let n = nums.len();
        let k = k as usize;
        let mut res = vec![-1; n - k + 1];
        let mut good = 1;
        for i in 0..n - 1 {
            good = if nums[i] + 1 == nums[i + 1] {
                good + 1
            } else {
                1
            };
            if good >= k {
                res[2 + i - k] = nums[i + 1];
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 4, 3, 2, 5], 3, vec![3, 4, -1, -1, -1]),
        (vec![2, 2, 2, 2, 2], 4, vec![-1, -1]),
        (vec![3, 2, 3, 2, 3, 2], 2, vec![-1, 3, -1, 3, -1]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::results_array(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.2, res
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
