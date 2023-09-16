// 1631. Path With Minimum Effort
// 🟠 Medium
//
// https://leetcode.com/problems/path-with-minimum-effort/
//
// Tags: Array - Binary Search - Depth-First Search - Breadth-First Search - Union Find - Heap (Priority Queue) - Matrix

use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    /// Use Djikstra, the "distance" is the cost of getting to each cell, that
    /// way we make sure that we are traveling the path of least resistance,
    /// when we arrive at a cell from a "cheaper" path, we add it to the heap,
    /// when we arrive at a cell that we have already visited from a cheaper
    /// path, we ignore that branch and pop the next item from the heap.
    ///
    /// Time complexity: O(m*n*log(m*n)) - We may visit each cell in the matrix,
    /// each visit comes with a push/pop from the heap, that can grow to the
    /// size of 4*m*n because we may push each cell arriving from 4 different
    /// paths.
    /// Space complexity: O(m*n) - The auxiliary visited matrix has the same
    /// size as the input. The heap can grow to 4*m*n.
    ///
    /// Runtime 18 ms Beats 85.71%
    /// Memory 2.42 MB Beats 71.43%
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (heights.len(), heights[0].len());
        // Use an auxiliary matrix that stores the lowest cost to get to each
        // point in the original matrix.
        let mut visited = vec![vec![i32::MAX; n]; m];
        let mut heap: BinaryHeap<(i32, usize, usize)> = BinaryHeap::from([(0, 0, 0)]);
        visited[0][0] = 0;
        while let Some((cost, row, col)) = heap.pop() {
            if row == m - 1 && col == n - 1 {
                return -cost;
            }
            for (r, c) in [
                (row, col + 1),
                (row, col.wrapping_sub(1)),
                (row + 1, col),
                (row.wrapping_sub(1), col),
            ] {
                if r < m && c < n {
                    let diff = (heights[row][col] - heights[r][c]).abs();
                    let next_cost = (-cost).max(diff);
                    if next_cost < visited[r][c] {
                        visited[r][c] = next_cost;
                        heap.push((-next_cost, r, c));
                    }
                }
            }
        }
        unreachable!("The algorithm should always reach the bottom-right cell")
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1, 2, 2], vec![3, 8, 2], vec![5, 3, 5]], 2),
        (vec![vec![1, 2, 3], vec![3, 8, 4], vec![5, 3, 5]], 1),
        (
            vec![
                vec![1, 2, 1, 1, 1],
                vec![1, 2, 1, 2, 1],
                vec![1, 2, 1, 2, 1],
                vec![1, 2, 1, 2, 1],
                vec![1, 1, 1, 2, 1],
            ],
            0,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::minimum_effort_path(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
