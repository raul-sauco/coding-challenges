// 2563. Count the Number of Fair Pairs
// 🟠 Medium
//
// https://leetcode.com/problems/count-the-number-of-fair-pairs/
//
// Tags: Array - Two Pointers - Binary Search - Sorting

struct Solution;
impl Solution {
    /// Use the same logic as in "2824. Count Pairs Whose Sum is Less than Target" but do it twice,
    /// once to compute how many pairs' sum are below upper, then remove the count of pairs below
    /// lower and that is the solution. To count the number of pairs with sum below a boundary, we
    /// are using two pointers once we have the vector sorted.
    ///
    /// Time complexity: O(nlog(n)) - Sort the input vector, then iterate twice over all elements
    /// using two pointers to compute the number of pairs below a boundary.
    /// Space complexity: O(1) - Constant extra space used by the algorithm if we don't take into
    /// account the sorting algorithm, if we do O(log(n))
    ///
    /// Runtime 9 ms Beats 70%
    /// Memory 3.57 MB Beats 58%
    pub fn count_fair_pairs(mut nums: Vec<i32>, lower: i32, upper: i32) -> i64 {
        fn pairs_on_range(nums: &Vec<i32>, limit: i32) -> i64 {
            let (mut l, mut r, mut res) = (0, nums.len() - 1, 0);
            while l < r {
                if nums[l] + nums[r] < limit {
                    res += (r - l) as i64;
                    l += 1;
                } else {
                    r -= 1;
                }
            }
            res
        }
        nums.sort_unstable();
        pairs_on_range(&nums, upper + 1) - pairs_on_range(&nums, lower)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0, 1, 7, 4, 4, 5], 3, 6, 6),
        (vec![1, 7, 9, 2, 5], 11, 11, 1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::count_fair_pairs(t.0.clone(), t.1, t.2);
        if res == t.3 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.3, res
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
