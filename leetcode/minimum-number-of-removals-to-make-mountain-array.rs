// 1671. Minimum Number of Removals to Make Mountain Array
// 🔴 Hard
//
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
//
// Tags: Array - Binary Search - Dynamic Programming - Greedy

use std::i32;

struct Solution;
impl Solution {
    /// Run LIS forward and backwards, then use the combined result to find peak candidates and
    /// compute the number of removals needed to make them into the mountain peak in constant time
    /// using the longest increasing sequence up to that index and the longest decreasing sequence
    /// from that index to the end of the vector.
    ///
    /// Time complexity: O(n*log(n)) - Same as the LIS problem, but we run it twice.
    /// Space complexity: O(n) - The lis vectors that we store.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.18 MB Beats 100%
    pub fn minimum_mountain_removals(nums: Vec<i32>) -> i32 {
        // This function returns a vector of the lis that can be formed with the values in the
        // iterator received as a parameter.
        fn lis_at_idx<'a, I>(iter: I, n: usize) -> Vec<usize>
        where
            I: Iterator<Item = &'a i32>,
        {
            let mut dp = vec![i32::MIN; n + 1];
            let mut lis_at_idx = vec![1; n];
            let mut lis = 0;
            let (mut l, mut m, mut r);
            for (idx, &num) in iter.enumerate() {
                (l, r) = (0, lis + 1);
                while l < r {
                    m = (l + r) / 2;
                    if dp[m] >= num {
                        r = m;
                    } else {
                        l = m + 1;
                    }
                }
                dp[l] = num;
                lis = lis.max(l);
                lis_at_idx[idx] = lis;
            }
            lis_at_idx
        }

        let n = nums.len();
        let forward = lis_at_idx(nums.iter(), n);
        let mut backwards = lis_at_idx(nums.iter().rev(), n);
        backwards.reverse();
        (0..n)
            .map(|idx| {
                if forward[idx] > 1 && backwards[idx] > 1 {
                    1 + n - forward[idx] - backwards[idx]
                } else {
                    usize::MAX
                }
            })
            .min()
            .unwrap() as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 3, 1], 0),
        (vec![1, 2, 1, 2, 1, 2, 1], 4),
        (vec![1, 2, 3, 4, 5, 3, 1], 0),
        (vec![1, 3, 2, 1, 2, 3, 2, 1], 3),
        (vec![2, 1, 1, 5, 6, 2, 3, 1], 3),
        (vec![1, 2, 3, 2, 1, 2, 3, 4], 3),
        (vec![3, 10, 9, 8, 7, 8, 9, 10], 3),
        (vec![1, 2, 5, 3, 4, 5, 3, 1, 6, 8], 3),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::minimum_mountain_removals(t.0.clone());
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
