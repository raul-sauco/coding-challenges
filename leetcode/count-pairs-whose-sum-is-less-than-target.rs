// 2824. Count Pairs Whose Sum is Less than Target
// 🟢 Easy
//
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
//
// Tags: Array - Two Pointers - Binary Search - Sorting

struct Solution;
impl Solution {
    /// Sort the input vector, then use two pointers to adjust the boundaries of a window with the
    /// left and right being the boundaries of the pairs that sum below the target.
    ///
    /// Time complexity: O(nlog(n)) - Sorting, after that linear time
    /// Space complexity: O(1) - Constant extra space if we ignore the extra space used by the
    /// sorting algorithm.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.08 MB Beats 97%
    pub fn count_pairs(mut nums: Vec<i32>, target: i32) -> i32 {
        nums.sort_unstable();
        let mut res = 0;
        let (mut l, mut r) = (0, nums.len() - 1);
        while l < r {
            if nums[l] + nums[r] >= target {
                r -= 1;
                continue;
            }
            res += r - l;
            l += 1;
        }
        res as _
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![-1, 1, 2, 3, 1], 2, 3),
        (vec![-6, 2, 5, -2, -7, -1, 3], -2, 10),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::count_pairs(t.0.clone(), t.1);
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
