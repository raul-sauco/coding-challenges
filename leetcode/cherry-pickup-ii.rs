// 1463. Cherry Pickup II
// 🔴 Hard
//
// https://leetcode.com/problems/cherry-pickup-ii/
//
// Tags: Array - Dynamic Programming - Matrix

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Iterate over the rows, for each row, simulate the maximum 9 moves that the robots can make
    /// and choose the best results between them.
    ///
    /// Time complexity: O(m*n^2) - We iterate over all the rows, for each row, we iterate over all
    /// the possible combinations of the positions of the two robots in the previous row.
    /// Space complexity: O(n^2) - We store a dp hashmap with the best result that we can get with
    /// the robots at positions l and r.
    ///
    /// Runtime 67 ms Beats 18.18%
    /// Memory 2.27 MB Beats 100%
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        let (rows, cols) = (grid.len(), grid[0].len());
        let mut dp: HashMap<(i32, i32), i32> = HashMap::new();
        // We start with robots in the first and last column.
        dp.insert((0, cols as i32 - 1), grid[0][0] + grid[0][cols - 1]);
        let mut next: HashMap<(i32, i32), i32>;
        let (mut next_l, mut next_r);
        for i in 1..rows {
            next = HashMap::new();
            for ((r1, r2), val) in dp.iter() {
                for l in [-1, 0, 1] {
                    for r in [-1, 0, 1] {
                        (next_l, next_r) = (r1 + l, r2 + r);
                        // Check that indexes are within bounds and have not crossed.
                        if next_l >= 0 && next_r < cols as i32 && next_l <= next_r {
                            let mut move_val = val + grid[i][next_l as usize];
                            if next_l != next_r {
                                move_val += grid[i][next_r as usize];
                            }
                            next.entry((next_l, next_r))
                                .and_modify(|x| *x = move_val.max(*x))
                                .or_insert(move_val);
                        }
                    }
                }
            }
            std::mem::swap(&mut dp, &mut next);
        }
        *dp.values().max().unwrap()
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![vec![3, 1, 1], vec![2, 5, 1], vec![1, 5, 5], vec![2, 1, 1]],
            24,
        ),
        (
            vec![
                vec![1, 0, 0, 0, 0, 0, 1],
                vec![2, 0, 0, 0, 0, 3, 0],
                vec![2, 0, 9, 0, 0, 0, 0],
                vec![0, 3, 0, 5, 4, 0, 0],
                vec![1, 0, 2, 3, 0, 0, 6],
            ],
            28,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::cherry_pickup(t.0.clone());
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
