// 238. Product of Array Except Self
// 🟠 Medium
//
// https://leetcode.com/problems/product-of-array-except-self/
//
// Tags: Array - Prefix Sum

struct Solution;
impl Solution {
    /// Iterate forward, then backwards over the elements of the input vector computing the product
    /// of all values up to the position before the current one, we can use one extra i32 value to
    /// store the current product, multiply that with the current position value in the result,
    /// then update the currentt product multiplying with the value in the input vector.
    ///
    /// Time complexity: O(n) - We visit twice each element on the input vector and do constant
    /// time work in each visit.
    /// Space complexity: O(n) - The result vector, or O(1) if we don't take it into account.
    ///
    /// Runtime 9 ms Beats 61%
    /// Memory 3.13 MB Beats 56%
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut res = vec![1; n];
        let mut cur = 1;
        for i in 0..n {
            res[i] *= cur;
            cur *= nums[i];
        }
        cur = 1;
        for i in (0..n).rev() {
            res[i] *= cur;
            cur *= nums[i];
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 4], vec![24, 12, 8, 6]),
        (vec![-1, 1, 0, -3, 3], vec![0, 0, 9, 0, 0]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::product_except_self(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
