// 78. Subsets
// 🟠 Medium
//
// https://leetcode.com/problems/subsets/
//
// Tags: Array - Backtracking - Bit Manipulation

use std::{collections::BTreeSet, iter::once};

struct Solution;
impl Solution {
    /// Recursive solution, pop the last element and generate all subsets for the remainder of the
    /// input, then use each vector in the result to create a new result vector with two entries
    /// for each original one, one with and one without the element that was popped.
    ///
    /// Time complexity: O(n*2^n) - For each n element we call subsets, that results in a binary
    /// tree of height n that splits in 2 at each level.
    /// Space complexity: O(n*2^n) - The number of subsets that are generated.
    ///
    /// Runtime 1 ms Beats 76%
    /// Memory 2.13 MB Beats 74%
    #[allow(dead_code)]
    pub fn subsets_push(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        match nums.pop() {
            Some(el) => {
                let mut subsets = Self::subsets(nums);
                for i in 0..subsets.len() {
                    subsets.push(once(el).chain(subsets[i].iter().map(|&x| x)).collect());
                }
                subsets
            }
            None => vec![vec![]],
        }
    }

    /// Similar logic but use iterators and flat_map to add the extra element to the result set.
    /// This results in two extra "clone" calls for each subset.
    ///
    /// Time complexity: O(n*2^n) - For each n element we call subsets, that results in a binary
    /// tree of height n that splits in 2 at each level.
    /// Space complexity: O(n*2^n) - The number of subsets that are generated.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.23 MB Beats 15%
    pub fn subsets(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        match nums.pop() {
            Some(el) => Self::subsets(nums)
                .iter()
                .flat_map(|ss| {
                    vec![
                        once(el).chain(ss.iter().map(|&x| x).into_iter()).collect(),
                        ss.clone(),
                    ]
                })
                .collect(),
            None => vec![vec![]],
        }
    }
}

// Tests.
fn main() {
    fn to_hm(v: &Vec<Vec<i32>>) -> BTreeSet<BTreeSet<i32>> {
        v.iter().map(|iv| iv.iter().map(|&x| x).collect()).collect()
    }
    let tests = [
        (vec![0], vec![vec![], vec![0]]),
        (
            vec![1, 2, 3],
            vec![
                vec![],
                vec![1],
                vec![2],
                vec![1, 2],
                vec![3],
                vec![1, 3],
                vec![2, 3],
                vec![1, 2, 3],
            ],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::subsets(t.0.clone());
        if to_hm(&res) == to_hm(&t.1) {
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
