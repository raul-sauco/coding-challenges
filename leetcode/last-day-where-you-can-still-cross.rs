// 1970. Last Day Where You Can Still Cross
// 🔴 Hard
//
// https://leetcode.com/problems/last-day-where-you-can-still-cross/
//
// Tags: Array - Binary Search - Depth-First Search - Breadth-First Search - Union Find - Matrix

use std::collections::VecDeque;

struct Solution;
impl Solution {
    /// We can construct a matrix that represents the state at any day of the
    /// process and check if it would be possible to cross at that point, if
    /// we do a linear search for the last day in which it would be possible to
    /// cross, the complexity would be O((m*n)^2) which we can reduce using
    /// binary search to find the same day.
    ///
    /// Time complexity: O(m*n*log(m*n) - We use binary search to find the last
    /// day in which is possible to cross. The search space is the number of
    /// days from the first day, in which no cell is water, to the last day, in
    /// which all cells are water, which makes it equal to the number of cells.
    /// Each time we test if we can cross in a given day, we are creating a
    /// new matrix with the cells at that given day O(m*n) and then doing
    /// BFS in that matrix, which is also O(m*n)
    /// Space complexity: O(m*n) - The matrix we create inside the can_cross
    /// function is m*n. We also map the cells vector to a vector of usize
    /// tuples, the resulting copy also has size m*n.
    ///
    /// Runtime 84 ms Beats 88.89%
    /// Memory 4.3 MB Beats 11.11%
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        fn can_cross(day: usize, row: usize, col: usize, cells: &Vec<(usize, usize)>) -> bool {
            let mut matrix = vec![vec![true; col]; row];
            for i in 0..day {
                let (r, c) = cells[i];
                matrix[r][c] = false;
            }
            let mut queue = VecDeque::new();
            // Push everything in the first row that is accessible and mark it
            // visited.
            for c in 0..col {
                if matrix[0][c] {
                    queue.push_back((0, c));
                    matrix[0][c] = false;
                }
            }
            while let Some((r, c)) = queue.pop_front() {
                if r == row - 1 {
                    return true;
                }
                if matrix[r + 1][c] {
                    queue.push_back((r + 1, c));
                    matrix[r + 1][c] = false;
                }
                if c > 0 && matrix[r][c - 1] {
                    queue.push_back((r, c - 1));
                    matrix[r][c - 1] = false;
                }
                if c < col - 1 && matrix[r][c + 1] {
                    queue.push_back((r, c + 1));
                    matrix[r][c + 1] = false;
                }
                if r > 0 && matrix[r - 1][c] {
                    queue.push_back((r - 1, c));
                    matrix[r - 1][c] = false;
                }
            }
            false
        }

        let (row, col) = (row as usize, col as usize);
        let (mut l, mut r) = (col - 1, cells.len());
        let cells: Vec<(usize, usize)> = cells
            .iter()
            .map(|x| (x[0] as usize - 1, x[1] as usize - 1))
            .collect();
        while l + 1 < r {
            let day = (l + r) / 2;
            if !can_cross(day, row, col, &cells) {
                r = day;
            } else {
                l = day;
            }
        }
        l as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (
            2,
            2,
            vec![vec![1, 1], vec![2, 1], vec![1, 2], vec![2, 2]],
            2,
        ),
        (
            2,
            2,
            vec![vec![1, 1], vec![1, 2], vec![2, 1], vec![2, 2]],
            1,
        ),
        (
            3,
            3,
            vec![
                vec![1, 2],
                vec![2, 1],
                vec![3, 3],
                vec![2, 2],
                vec![1, 1],
                vec![1, 3],
                vec![2, 3],
                vec![3, 2],
                vec![3, 1],
            ],
            3,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::latest_day_to_cross(t.0, t.1, t.2), t.3);
    }
    println!("[92m» All tests passed![0m")
}
