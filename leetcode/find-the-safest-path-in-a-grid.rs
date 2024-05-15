// 2812. Find the Safest Path in a Grid
// 🟠 Medium
//
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/
//
// Tags: Array - Binary Search - Breadth-First Search - Union Find - Matrix

use std::collections::{BinaryHeap, VecDeque};

struct Solution;
impl Solution {
    /// Two parts, first convert the grid of thieves into a grid of distance from each cell to the
    /// closets thieve, we can do that in O(n^2) using BFS with each cell with a thieve on it as
    /// the start, once we visit all the cells, we have computed the distance between the thieves
    /// and all cells. Then we use that distance matrix and a Dijkstra traverse that priorizes
    /// based on safety instead of distance, we start by pushing the start cell into the heap, when
    /// we pop a cell, we check if the safety value of that path has decreased to 0, in that case,
    /// we can already return 0 because the safety of paths cannot improve, only decrease, and that
    /// top path is the "safest" in the heap. If the cell we popped is the bottom-right cell, we
    /// return the safety of the path we took to get there, including the safety of the
    /// bottom-right cell. Otherwise we visit its 4-directional neighbors and push any of them
    /// within bounds that we have not visited previously.
    ///
    /// Time complexity: O(n^2*log(n)) - We push/pop elements from the heap of size n^2, at most we
    /// will push/pop each of the n^2 elements once because we are marking them as visited.
    /// Space complexity: O(n^2) - The grid copy with safety values, the double ended queue and the
    /// binary heap.
    ///
    /// Runtime 61 ms Beats 100%
    /// Memory 5.22 MB Beats 100%
    pub fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len() as i32;
        let mut grid = Self::get_safety_grid(&grid);
        let mut pq = BinaryHeap::from([(grid[0][0], 0, 0)]);
        while let Some((safety, r, c)) = pq.pop() {
            // Safety cannot improve, only decrease. If we get to 0, return that.
            if safety == 0 {
                return 0;
            }
            if r == n - 1 && c == n - 1 {
                return safety;
            }
            for (i, j) in [(0, -1), (0, 1), (-1, 0), (1, 0)] {
                let (nr, nc) = (r + i, c + j);
                if nr < 0 || nr >= n || nc < 0 || nc >= n || grid[nr as usize][nc as usize] < 0 {
                    continue;
                }
                pq.push((safety.min(grid[nr as usize][nc as usize]), nr, nc));
                grid[nr as usize][nc as usize] *= -1;
            }
        }
        unreachable!("We should always reach the bottom-right corner inside the loop")
    }

    fn get_safety_grid(grid: &Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len();
        let mut matrix = vec![vec![i32::MAX; n]; n];
        let mut queue = VecDeque::new();
        for r in 0..n {
            for c in 0..n {
                if grid[r][c] == 1 {
                    queue.push_back((r as i32, c as i32, 0));
                    matrix[r][c] = 0;
                }
            }
        }
        // let mut queue = (0..n)
        //     .flat_map(move |r| {
        //         (0..n)
        //             .filter(move |&c| grid[r][c] == 1)
        //             .map(move |c| (r as i32, c as i32, 0))
        //     })
        //     .collect::<VecDeque<_>>();
        while let Some((r, c, level)) = queue.pop_front() {
            for (i, j) in [(0, -1), (0, 1), (-1, 0), (1, 0)] {
                let (nr, nc) = (r + i, c + j);
                if nr >= 0
                    && nr < n as i32
                    && nc >= 0
                    && nc < n as i32
                    && matrix[nr as usize][nc as usize] == i32::MAX
                {
                    queue.push_back((nr, nc, level + 1));
                    matrix[nr as usize][nc as usize] = level + 1;
                }
            }
        }
        matrix
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![0, 1, 1], vec![0, 1, 1], vec![1, 1, 1]], 0),
        (vec![vec![1, 0, 0], vec![0, 0, 0], vec![0, 0, 1]], 0),
        (vec![vec![0, 0, 1], vec![0, 0, 0], vec![0, 0, 0]], 2),
        (
            vec![
                vec![0, 0, 0, 1],
                vec![0, 0, 0, 0],
                vec![0, 0, 0, 0],
                vec![1, 0, 0, 0],
            ],
            2,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_safeness_factor(t.0.clone());
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
