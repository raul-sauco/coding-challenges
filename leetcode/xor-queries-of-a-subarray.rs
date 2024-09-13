// 1310. XOR Queries of a Subarray
// 🟠 Medium
//
// https://leetcode.com/problems/xor-queries-of-a-subarray/
//
// Tags: Array - Bit Manipulation - Prefix Sum

struct Solution;
impl Solution {
    /// Since xor is associative, if we precompute the xor of all elements up to each index, after
    /// that we can efficiently compute the xor between any given two indexes i, j as the xor we
    /// had before that (i-1) XOR the prefix xor at the end of the interval.
    ///
    /// Time complexity: O(m+n) - We iterate over the m elements of arr to create a vector of
    /// prefix xor values, then we iterate over the n queries and compute each in constant time
    /// because we only access to elements on the precomputed vector.
    /// Space complexity: O(m) - The prefix xor vector that we keep in memory.
    ///
    /// Runtime 7 ms Beats 100%
    /// Memory 4.08 MB Beats 42%
    pub fn xor_queries(arr: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let pre = arr
            .into_iter()
            .scan(0, |acc, x| {
                *acc ^= x;
                Some(*acc)
            })
            .collect::<Vec<i32>>();
        queries
            .into_iter()
            .map(|q| {
                let (start, end) = (q[0] as usize, q[1] as usize);
                if start == 0 {
                    pre[end]
                } else {
                    pre[start - 1] ^ pre[end]
                }
            })
            .collect()
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![1, 3, 4, 8],
            vec![vec![0, 1], vec![1, 2], vec![0, 3], vec![3, 3]],
            vec![2, 7, 14, 8],
        ),
        (
            vec![4, 8, 2, 10],
            vec![vec![2, 3], vec![1, 3], vec![0, 0], vec![0, 3]],
            vec![8, 0, 4, 4],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::xor_queries(t.0.clone(), t.1.clone());
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
