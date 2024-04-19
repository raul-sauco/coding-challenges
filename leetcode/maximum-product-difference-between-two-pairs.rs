// 1913. Maximum Product Difference Between Two Pairs
// 🟢 Easy
//
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
//
// Tags: Array - Sorting

struct Solution;
impl Solution {
    /// Iterate over the input, save the two biggest and two smallest values, return the product of
    /// the two biggest minus the product of the two smallest.
    ///
    /// Time complexity: O(n) - We visit each element and do O(1) work for each.
    /// Space complexity: O(1) - We store four i32 values.
    ///
    /// Runtime 2 ms Beats 84.21%
    /// Memory 2.16 MB Beats 57.89%
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        //todo
        let (mut a, mut b) = (0, 0);
        let (mut c, mut d) = (100000, 100000);
        for num in nums {
            if num > a {
                b = a;
                a = num;
            } else if num > b {
                b = num;
            }
            if num < c {
                d = c;
                c = num;
            } else if num < d {
                d = num;
            }
        }
        a * b - c * d
    }
}

// Tests.
fn main() {
    let tests = [(vec![5, 6, 2, 7, 4], 34), (vec![4, 2, 5, 9, 7, 4, 8], 64)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_product_difference(t.0.clone());
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
    println!("");
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
