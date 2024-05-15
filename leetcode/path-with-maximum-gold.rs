// 1219. Path with Maximum Gold
// 🟠 Medium
//
// https://leetcode.com/problems/path-with-maximum-gold/
//
// Tags: Array - Backtracking - Matrix

struct Solution;
impl Solution {
    /// We can use DFS, from each cell, do a dfs while marking the current cell as "visited", when
    /// we visit a cell that we are not allowed to visit, or go out of bounds, return 0, for each
    /// branch, return the maximum between its children.
    ///
    /// Time complexity: O(m*n*4^(m*n)) - We visit each cell and, for each, launch a dfs. Each dfs
    /// branches in a maximum of 4 calls at each level and it can have as many levels as the number
    /// of cells that contain gold.
    /// Space complexity: O(m*n) - The height of the call stack, which can grow to the number of
    /// cells that contain gold and it maxes out at the size of the input matrix.
    ///
    /// Runtime 61 ms Beats 50%
    /// Memory 2.04 MB Beats 100%
    pub fn get_maximum_gold(mut grid: Vec<Vec<i32>>) -> i32 {
        fn dfs(grid: &mut Vec<Vec<i32>>, row: i32, col: i32) -> i32 {
            if row < 0
                || row >= grid.len() as i32
                || col < 0
                || col >= grid[0].len() as i32
                || grid[row as usize][col as usize] == 0
            {
                return 0;
            }
            let mut gold = 0;
            let current_gold = grid[row as usize][col as usize];
            grid[row as usize][col as usize] = 0;
            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                gold = gold.max(dfs(grid, row + i, col + j));
            }
            grid[row as usize][col as usize] = current_gold;
            gold + current_gold
        }

        let mut gold = 0;
        for row in 0..grid.len() {
            for col in 0..grid[0].len() {
                gold = gold.max(dfs(&mut grid, row as i32, col as i32));
            }
        }
        gold
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![0, 6, 0], vec![5, 8, 7], vec![0, 9, 0]], 24),
        (
            vec![
                vec![1, 0, 7],
                vec![2, 0, 6],
                vec![3, 4, 5],
                vec![0, 3, 0],
                vec![9, 0, 20],
            ],
            28,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::get_maximum_gold(t.0.clone());
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
