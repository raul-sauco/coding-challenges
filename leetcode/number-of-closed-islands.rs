// 1254. Number of Closed Islands
// 🟠 Medium
//
// https://leetcode.com/problems/number-of-closed-islands/
//
// Tags: Array - Depth-First Search - Breadth-First Search - Union Find - Matrix

struct Solution;
impl Solution {
    /// Iterate over all grid cells in the range 1..m-1 x 1..n-1, we don't need
    /// to visit the first and last row and columns because they will never
    /// lead to a closed island. For each cell that has land, start DFS to
    /// check if it is a closed island, while we do DFS, we will mark all cells
    /// that we visit to avoid revisiting them, we also make sure to consume,
    /// that is visit, all the land cells that belong to the current island.
    ///
    /// Time complexity: O(m*n) - The number of cells that we visit is directly
    /// proportional to the number of cells in the grid.
    /// Space complexity: O(m*n) - We make a local copy of matrix to keep track
    /// of nodes that we have visited, we could do the same with a hash set.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.1 MB Beats 100%
    pub fn closed_island(grid: Vec<Vec<i32>>) -> i32 {
        // We can use the grid itself to mark visited cells.
        let mut grid = grid;
        let (num_rows, num_cols) = (grid.len(), grid[0].len());
        // A nested function that performs DFS from a given cell and returns
        // whether that cell is water or forms part of a closed island.
        fn is_closed_island_part(grid: &mut Vec<Vec<i32>>, r: usize, c: usize) -> bool {
            // Mark this cell as visited.
            grid[r][c] = 2;
            // If we are on a boundary, return false.
            if r == 0 || r == grid.len() - 1 || c == 0 || c == grid[0].len() - 1 {
                return false;
            }
            // Otherwise explore the four cardinalities.
            let dirs = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)];
            let mut is_closed = true;
            for (r, c) in dirs {
                // If that neighbor is land, check if it is closed.
                if grid[r][c] == 0 && !is_closed_island_part(grid, r, c) {
                    is_closed = false;
                }
                // Do not break after finding that this island is not closed,
                // we want to exhaust the island visiting all connected cells.
            }
            is_closed
        }
        let mut num_closed_islands = 0;
        // Iterate over cells that could be part of a closed island. This
        // automatically handles the edge case of small grids.
        for r in 1..num_rows - 1 {
            for c in 1..num_cols - 1 {
                if grid[r][c] == 0 && is_closed_island_part(&mut grid, r, c) {
                    num_closed_islands += 1;
                }
            }
        }
        num_closed_islands
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![
                vec![1, 1, 1, 1, 1, 1, 1, 0],
                vec![1, 0, 0, 0, 0, 1, 1, 0],
                vec![1, 0, 1, 0, 1, 1, 1, 0],
                vec![1, 0, 0, 0, 0, 1, 0, 1],
                vec![1, 1, 1, 1, 1, 1, 1, 0],
            ],
            2,
        ),
        (
            vec![
                vec![0, 0, 1, 0, 0],
                vec![0, 1, 0, 1, 0],
                vec![0, 1, 1, 1, 0],
            ],
            1,
        ),
        (
            vec![
                vec![1, 1, 1, 1, 1, 1, 1],
                vec![1, 0, 0, 0, 0, 0, 1],
                vec![1, 0, 1, 1, 1, 0, 1],
                vec![1, 0, 1, 0, 1, 0, 1],
                vec![1, 0, 1, 1, 1, 0, 1],
                vec![1, 0, 0, 0, 0, 0, 1],
                vec![1, 1, 1, 1, 1, 1, 1],
            ],
            2,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::closed_island(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
