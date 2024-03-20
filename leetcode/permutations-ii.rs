// 47. Permutations II
// 🟠 Medium
//
// https://leetcode.com/problems/permutations-ii/
//
// Tags: Array - Backtracking

use std::collections::HashSet;

struct Solution;
impl Solution {
    /// Have a backtrack function that produces the next digit on each call by iterating over all
    /// the digits in the input choosing each of the free ones, calling itself to generate the
    /// remaining digits, then backtracking.
    ///
    /// Time complexity: O(n!) - We compute all the permutations.
    /// Space complexity: O(n!) - We store all the permutations in the result vector.
    ///
    /// Runtime 15 ms Beats 26%
    /// Memory 2.14 MB Beats 90%
    #[allow(dead_code)]
    pub fn permute_unique_hashset(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn bt(
            nums: &Vec<i32>,
            seen: u8,
            complete: u8,
            current: &mut Vec<i32>,
            res: &mut HashSet<Vec<i32>>,
        ) {
            // Base case, we added all values
            if seen == complete {
                res.insert(current.clone());
                return;
            }
            for i in 0..nums.len() {
                if seen >> i & 1 == 1 {
                    continue;
                }
                current.push(nums[i]);
                bt(nums, seen | 1 << i, complete, current, res);
                current.pop();
            }
        }
        let mut res = HashSet::new();
        let mut current = vec![];
        let n = nums.len();
        let complete = (1 << n) - 1;
        bt(&nums, 0, complete as u8, &mut current, &mut res);
        res.into_iter().collect()
    }

    /// Similar solution but sort the input and skip identical values in the same call to bt, this
    /// eliminates the need for a hashset.
    ///
    /// Time complexity: O(n!) - We compute all the permutations.
    /// Space complexity: O(n!) - We store all the permutations in the result vector.
    ///
    /// Runtime 2 ms Beats 90%
    /// Memory 2.12 MB Beats 90%
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn bt(
            nums: &Vec<i32>,
            seen: u8,
            complete: u8,
            current: &mut Vec<i32>,
            res: &mut Vec<Vec<i32>>,
        ) {
            // Base case, we added all values
            if seen == complete {
                res.push(current.clone());
                return;
            }
            let mut prev = None;
            for i in 0..nums.len() {
                if seen >> i & 1 == 1 {
                    continue;
                }
                if let Some(prev) = prev {
                    if prev == nums[i] {
                        continue;
                    }
                }
                prev = Some(nums[i]);
                current.push(nums[i]);
                bt(nums, seen | 1 << i, complete, current, res);
                current.pop();
            }
        }
        let mut res = vec![];
        let mut current = vec![];
        let n = nums.len();
        let complete = (1 << n) - 1;
        let mut nums = nums;
        nums.sort_unstable();
        bt(&nums, 0, complete as u8, &mut current, &mut res);
        res
    }
}

// Tests.
fn main() {
    let tests = vec![
        (vec![1, 1, 2], vec![[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        (
            vec![1, 2, 3],
            vec![
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::permute_unique(t.0.clone());
        if res.iter().map(|a| a.to_vec()).collect::<HashSet<_>>()
            == t.1.iter().map(|a| a.to_vec()).collect::<HashSet<_>>()
        {
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
