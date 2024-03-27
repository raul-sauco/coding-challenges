// 713. Subarray Product Less Than K
// 🟠 Medium
//
// https://leetcode.com/problems/subarray-product-less-than-k/
//
// Tags: Array - Sliding Window

struct Solution;
impl Solution {
    /// Use a sliding window approach, expand the window one element at a time on the right side
    /// and multiply the current product with that value. Then, while the current product is
    /// greater than or equal to k, shrink the window on the left one element at a time, removing
    /// its value from the product, until we either run out of elements in the window or the
    /// product goes below k. Once the product is below k, add the number of new subarrays that we
    /// can construct with the elements in the current windhow, equal to the number of elements in
    /// the window because we will be able to use the new element with any previously existing
    /// subarray.
    ///
    /// Time complexity: O(n) - We visit each element in the input and do constant time work for
    /// each.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 3 ms Beats 100%
    /// Memory 2.26 MB Beats 100%
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut res = 0;
        let mut product = 1;
        let mut l = 0;
        for r in 0..nums.len() {
            product *= nums[r];
            while product >= k && l <= r {
                product /= nums[l];
                l += 1;
            }
            res += 1 + r - l;
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3], 0, 0),
        (vec![10, 5, 2, 6], 100, 8),
        (vec![1, 1, 1, 1, 1], 2, 15),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::num_subarray_product_less_than_k(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
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
