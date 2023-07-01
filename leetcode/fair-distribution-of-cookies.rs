// 2305. Fair Distribution of Cookies
// 🟠 Medium
//
// https://leetcode.com/problems/fair-distribution-of-cookies/
//
// Tags: Array - Dynamic Programming - Backtracking - Bit Manipulation - Bitmask

use std::cell::Cell;

struct Solution;
/// Since the constrains are pretty small, both k and n are <= 8, we can use
/// a brute force backtracking solution, iterate over the cookies and try the
/// result of giving it to each of the children.
///
/// Time complexity: O(k^n) - We iterate over n cookies, for each, we branch
/// the search by computing the result of assigning it to any of the n children.
/// Space complexity: O(k+n) - The dp vector has size k, the call stack will
/// reach height n.
///
/// Runtime 21 ms Beats 75%
/// Memory 2.2 MB Beats 25%
impl Solution {
    pub fn distribute_cookies(cookies: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut dp = vec![0; k];
        fn dfs(
            i: usize,
            k: usize,
            n: usize,
            dp: &mut Vec<i32>,
            cookies: &Vec<i32>,
            zero_count: &Cell<usize>,
        ) -> i32 {
            if n - i < zero_count.get() {
                return i32::MAX;
            }
            if i == n {
                return *dp.iter().max().unwrap();
            }
            let mut res = i32::MAX;
            for j in 0..k {
                zero_count.set(zero_count.get() -  if dp[j] == 0 { 1 } else { 0 });
                dp[j] += cookies[i];
                res = res.min(dfs(i + 1, k, n, dp, cookies, zero_count));
                dp[j] -= cookies[i];
                zero_count.set(zero_count.get() +  if dp[j] == 0 { 1 } else { 0 });
            }
            res
        }

        let zero_count = Cell::new(k);
        dfs(0, k, cookies.len(), &mut dp, &cookies, &zero_count)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![8, 15, 10, 20, 8], 2, 31),
        (vec![6, 1, 3, 2, 2, 4, 1, 2], 3, 7),
    ];
    for t in tests {
        assert_eq!(Solution::distribute_cookies(t.0, t.1), t.2);
    }
    println!("[92m» All tests passed![0m")
}
