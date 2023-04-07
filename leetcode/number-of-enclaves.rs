// 1020. Number of Enclaves
// 🟠 Medium
//
// https://leetcode.com/problems/number-of-enclaves/
//
// Tags: Array - Depth-First Search - Breadth-First Search - Union Find - Matrix

struct Solution;
impl Solution {
    /// Iterate over all grid cells in the range 1..m-1 x 1..n-1, we don't need
    /// to visit the first and last row and columns because they will never
    /// lead to a closed island. For each cell that has land, start DFS to
    /// check if it is a closed island, while we do DFS, we will mark all cells
    /// that we visit to avoid revisiting them and count how many of them we
    /// are visiting, we also make sure to consume, that is visit, all the land
    /// cells that belong to the current island, if we get to any cell that is
    /// along the boundary, we return -1 to signify that this is not a closed
    /// island and return that value up the call chain.
    ///
    /// Time complexity: O(m*n) - The number of cells that we visit is directly
    /// proportional to the number of cells in the grid.
    /// Space complexity: O(m*n) - We make a local copy of matrix to keep track
    /// of nodes that we have visited, we could do the same with a hash set.
    ///
    /// Runtime 16 ms Beats 35.71%
    /// Memory 9.7 MB Beats 21.43%
    pub fn num_enclaves(grid: Vec<Vec<i32>>) -> i32 {
        // We can use the grid itself to mark visited cells.
        let mut grid = grid;
        let (num_rows, num_cols) = (grid.len(), grid[0].len());
        // A nested function that performs DFS from a given cell and returns
        // whether that cell is water or forms part of a closed island.
        fn num_enclaves_from_cell(grid: &mut Vec<Vec<i32>>, r: usize, c: usize) -> i32 {
            // Mark this cell as visited.
            grid[r][c] = 2;
            // If we are on a boundary, return -1 to show that it is not an
            // enclave.
            if r == 0 || r == grid.len() - 1 || c == 0 || c == grid[0].len() - 1 {
                return -1;
            }
            // Otherwise explore the four cardinalities.
            let dirs = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)];
            let mut res = 1;
            let mut is_valid_enclave = true;
            for (r, c) in dirs {
                // If that neighbor is land, check if it is closed.
                if grid[r][c] == 1 {
                    // If it is open, flag this enclave as open.
                    let enclaves = num_enclaves_from_cell(grid, r, c);
                    if enclaves == -1 {
                        is_valid_enclave = false;
                    } else {
                        res += enclaves;
                    }
                }
                // Do not break after finding that this island is not closed,
                // we want to exhaust the island visiting all connected cells.
            }
            if is_valid_enclave {
                res
            } else {
                -1
            }
        }
        let mut res = 0;
        // Iterate over cells that could be part of a closed island. This
        // automatically handles the edge case of small grids. Each time we see
        // an enclave that we haven't explored before, explore it.
        for r in 1..num_rows - 1 {
            for c in 1..num_cols - 1 {
                if grid[r][c] == 1 {
                    // Explore the enclave.
                    let enclaves = num_enclaves_from_cell(&mut grid, r, c);
                    // If the enclave is a closed enclave, add its number of
                    // cells to the result.
                    if enclaves != -1 {
                        res += enclaves;
                    }
                }
            }
        }
        res
    }

    /// A different approach, iterate over all the boundary cells, for each
    /// land cell, do DFS converting all cells in the same enclave to water,
    /// after we only need to iterate the grid counting how many land cells
    /// there are left because we have removed all the non-closed enclaves.
    ///
    /// Time complexity: O(m*n) - The number of cells that we visit is directly
    /// proportional to the number of cells in the grid.
    /// Space complexity: O(m*n) - We make a local copy of matrix to keep track
    /// of nodes that we have visited, we could do the same with a hash set.
    ///
    /// Runtime 19 ms Beats 14.29%
    /// Memory 14.4 MB Beats 7.14%
    pub fn num_enclaves_alt(grid: Vec<Vec<i32>>) -> i32 {
        let mut grid = grid;
        let (num_rows, num_cols) = (grid.len(), grid[0].len());
        // A nested function that performs DFS from a given cell and marks all
        // the cells in the same enclave as water.
        fn mark_full_enclave_as_open(grid: &mut Vec<Vec<i32>>, r: usize, c: usize) {
            // Mark this cell as water.
            grid[r][c] = 0;
            // Otherwise explore the four cardinalities.
            let mut dirs = vec![];
            if c < grid[0].len() - 1 {
                dirs.push((r, c + 1));
            }
            if c > 0 {
                dirs.push((r, c - 1));
            }
            if r < grid.len() - 1 {
                dirs.push((r + 1, c));
            }
            if r > 0 {
                dirs.push((r - 1, c));
            }
            for (r, c) in dirs {
                // If that neighbor is land, also mark it as water.
                if grid[r][c] == 1 {
                    mark_full_enclave_as_open(grid, r, c);
                }
            }
        }
        // Iterate over the boundary cells marking their groups as water.
        for r in [0, num_rows - 1] {
            for c in 0..num_cols {
                if grid[r][c] == 1 {
                    mark_full_enclave_as_open(&mut grid, r, c);
                }
            }
        }
        for c in [0, num_cols - 1] {
            for r in 0..num_rows {
                if grid[r][c] == 1 {
                    mark_full_enclave_as_open(&mut grid, r, c);
                }
            }
        }
        // Iterate over cells checking how many enclave cells there are left.
        let mut res = 0;
        for r in 1..num_rows - 1 {
            for c in 1..num_cols - 1 {
                if grid[r][c] == 1 {
                    res += 1;
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![
                vec![0, 0, 0, 0],
                vec![1, 0, 1, 0],
                vec![0, 1, 1, 0],
                vec![0, 0, 0, 0],
            ],
            3,
        ),
        (
            vec![
                vec![0, 1, 1, 0],
                vec![0, 0, 1, 0],
                vec![0, 0, 1, 0],
                vec![0, 0, 0, 0],
            ],
            0,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::num_enclaves(t.0.clone()), t.1);
        assert_eq!(Solution::num_enclaves_alt(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
