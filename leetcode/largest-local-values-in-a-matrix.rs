// 2373. Largest Local Values in a Matrix
// 🟢 Easy
//
// https://leetcode.com/problems/largest-local-values-in-a-matrix/
//
// Tags: Array - Matrix

use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    /// The "clever" solution using a heap turns out to be very unefficient.
    ///
    /// Time complexity: O(n^2*log(n)) - We visit each cell, in each we may push/pop from the heap.
    /// Space complexity: O(n^2) - The heap.
    ///
    /// Runtime 7 ms Beats 18%
    /// Memory 2.31 MB Beats 9%
    pub fn largest_local(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len() - 2;
        let mut res = vec![vec![0; n]; n];
        let mut heap = BinaryHeap::new();
        // Compute the result for each cell.
        for r in 0..n {
            heap.clear();
            // Push the initial 4 values.
            for offset_r in 0..2 {
                for offset_c in 0..2 {
                    heap.push((grid[r + offset_r][offset_c], r + offset_r, offset_c));
                }
            }
            // Add the two first values of the next row.
            for offset in [0, 1] {
                heap.push((grid[r + 2][offset], r + 2, offset));
            }
            for c in 0..n {
                // Add the three cells in the next column.
                for offset in 0..3 {
                    heap.push((grid[r + offset][c + 2], r + offset, c + 2));
                }
                // Pop any values that we have left behind.
                while let Some(&top) = heap.peek() {
                    if top.1 < r || top.2 < c || top.2 > c + 2 {
                        heap.pop();
                    } else {
                        res[r][c] = top.0;
                        break;
                    }
                }
            }
        }
        res
    }

    /// This function does the brute force computation.
    #[allow(dead_code)]
    fn get_largest(grid: &Vec<Vec<i32>>, r: usize, c: usize) -> i32 {
        let mut max = 0;
        for i in r..r + 3 {
            for j in c..c + 3 {
                max = max.max(grid[i][j]);
            }
        }
        max
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![
                vec![9, 9, 8, 1],
                vec![5, 6, 2, 6],
                vec![8, 2, 6, 4],
                vec![6, 2, 2, 2],
            ],
            vec![vec![9, 9], vec![8, 6]],
        ),
        (
            vec![
                vec![1, 1, 1, 1, 1],
                vec![1, 1, 1, 1, 1],
                vec![1, 1, 2, 1, 1],
                vec![1, 1, 1, 1, 1],
                vec![1, 1, 1, 1, 1],
            ],
            vec![vec![2, 2, 2], vec![2, 2, 2], vec![2, 2, 2]],
        ),
        (
            vec![
                vec![20, 8, 20, 6, 16, 16, 7, 16, 8, 10],
                vec![12, 15, 13, 10, 20, 9, 6, 18, 17, 6],
                vec![12, 4, 10, 13, 20, 11, 15, 5, 17, 1],
                vec![7, 10, 14, 14, 16, 5, 1, 7, 3, 11],
                vec![16, 2, 9, 15, 9, 8, 6, 1, 7, 15],
                vec![18, 15, 18, 8, 12, 17, 19, 7, 7, 8],
                vec![19, 11, 15, 16, 1, 3, 7, 4, 7, 11],
                vec![11, 6, 5, 14, 12, 18, 3, 20, 14, 6],
                vec![4, 4, 19, 6, 17, 12, 8, 8, 18, 8],
                vec![19, 15, 14, 11, 11, 13, 12, 6, 16, 19],
            ],
            vec![
                vec![20, 20, 20, 20, 20, 18, 18, 18],
                vec![15, 15, 20, 20, 20, 18, 18, 18],
                vec![16, 15, 20, 20, 20, 15, 17, 17],
                vec![18, 18, 18, 17, 19, 19, 19, 15],
                vec![19, 18, 18, 17, 19, 19, 19, 15],
                vec![19, 18, 18, 18, 19, 20, 20, 20],
                vec![19, 19, 19, 18, 18, 20, 20, 20],
                vec![19, 19, 19, 18, 18, 20, 20, 20],
            ],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::largest_local(t.0.clone());
        if res == t.1 {
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
