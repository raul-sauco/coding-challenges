// 864. Shortest Path to Get All Keys
// 🔴 Hard
//
// https://leetcode.com/problems/shortest-path-to-get-all-keys/
//
// Tags: Array - Bit Manipulation - Breadth-First Search - Matrix

use std::collections::VecDeque;

struct Solution;
impl Solution {
    /// We do a BFS traversal of the grid keeping track of visited cells and
    /// the number of steps taken to get there for each different state of
    /// keys that we may be holding.
    ///
    /// Time complexity: O(m*n*2^k) - We keep track of one set of visited cells
    /// per each key holding state, for k keys, there are 2^k states.
    /// Space complexity: O(m*n*2^k) - The dp array has a copy of the grid for
    /// each key holding state.
    ///
    /// Runtime 8 ms Beats 100%
    /// Memory 2.2 MB Beats 100%
    pub fn shortest_path_all_keys(grid: Vec<String>) -> i32 {
        let mut start = (0, 0);
        let mut k = 0;
        let (m, n) = (grid.len(), grid[0].len());
        for i in 0..m {
            let row = grid[i].as_bytes();
            for j in 0..n {
                if row[j].is_ascii_lowercase() {
                    k += 1;
                } else if row[j] == b'@' {
                    start = (i as i32, j as i32);
                }
            }
        }

        // We need a copy of the grid for each key holding state.
        let num_grids = (1 << k) - 1;
        let mut dp = vec![vec![vec![i32::MAX; num_grids + 1]; n]; m];

        let mut queue = VecDeque::new();
        queue.push_back((start.0, start.1, 0, 0));
        dp[start.0 as usize][start.1 as usize][0] = 0;

        let mut ret = i32::MAX;

        while let Some((i, j, state, step)) = queue.pop_front() {
            if step > dp[i as usize][j as usize][state] {
                continue;
            }

            for (di, dj) in [(-1, 0), (0, 1), (1, 0), (0, -1)] {
                if i + di >= 0
                    && i + di < grid.len() as i32
                    && j + dj >= 0
                    && j + dj < grid[0].len() as i32
                {
                    let i = (i + di) as usize;
                    let j = (j + dj) as usize;
                    let tile = grid[i].as_bytes()[j];
                    if tile.is_ascii_uppercase() {
                        if state & (1 << (tile - b'A')) != 0 && dp[i][j][state] > step + 1 {
                            dp[i][j][state] = step + 1;
                            queue.push_back((i as i32, j as i32, state, step + 1));
                        }
                    } else if tile.is_ascii_lowercase() {
                        if state & (1 << (tile - b'a')) == 0 || dp[i][j][state] > step + 1 {
                            let new_state = state | (1 << (tile - b'a'));
                            dp[i][j][new_state] = step + 1;
                            if new_state == num_grids {
                                ret = ret.min(step + 1);
                            } else {
                                queue.push_back((i as i32, j as i32, new_state, step + 1));
                            }
                        }
                    } else if tile != b'#' {
                        if dp[i][j][state] > step + 1 {
                            dp[i][j][state] = step + 1;
                            queue.push_back((i as i32, j as i32, state, step + 1));
                        }
                    }
                }
            }
        }

        if ret == i32::MAX {
            -1
        } else {
            ret
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["@Aa".to_string()], -1),
        (
            vec![
                "@.a..".to_string(),
                "###.#".to_string(),
                "b.A.B".to_string(),
            ],
            8,
        ),
        (
            vec![
                "@..aA".to_string(),
                "..B#.".to_string(),
                "....b".to_string(),
            ],
            6,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::shortest_path_all_keys(t.0), t.1);
    }
    println!("[92m» All tests passed![0m")
}
