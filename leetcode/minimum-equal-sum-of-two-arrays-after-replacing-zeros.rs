// 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
//
// Tags: Array - Greedy

struct Solution;
impl Solution {
    /// Compute the minimum and maximum we can get from each array, return the minimum value common
    /// to both intervals or -1 if there is no common value.
    ///
    /// Time complexity: O(n+m)
    /// Space complexity: O(1)
    ///
    /// Runtime 16 ms Beats 60%
    /// Memory 3.82 MB Beats %
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        fn min_max(nums: &Vec<i32>) -> (i64, i64) {
            let (s, z) = nums.iter().fold((0, 0), |(s, c), &x| {
                (s + x as i64, c + if x == 0 { 1 } else { 0 })
            });
            let min = s + z as i64;
            let max = if z > 0 { i64::MAX } else { min };
            (min, max)
        }
        let (a, b) = (min_max(&nums1), min_max(&nums2));
        let (start, end) = (a.0.max(b.0), a.1.min(b.1));
        if start > end {
            -1
        } else {
            start
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 2, 0, 1, 0], vec![6, 5, 0], 12),
        (vec![2, 0, 2, 0], vec![1, 4], -1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_sum(t.0.clone(), t.1.clone());
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
