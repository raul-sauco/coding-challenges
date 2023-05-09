// 54. Spiral Matrix
// 🟠 Medium
//
// https://leetcode.com/problems/spiral-matrix/
//
// Tags: Array - Matrix - Simulation

enum State {
    Right,
    Up,
    Left,
    Down,
}

struct Solution;
impl Solution {
    /// Use a state machine with four states corresponding to the possible
    /// directions of movement, store the boundaries of the unvisited matrix and
    /// use a combination of state, position and boundary to determine the next
    /// move.
    ///
    /// Time complexity: O(m*n) - We will visit each cell in the matrix and do
    /// O(1) work for each.
    /// Space complexity: O(1) - We only store pointers and boundaries, all of
    /// them either usize or i32, if we don't take into account the input or
    /// output. If we do, then O(m*n).
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.2 MB Beats 31.82%
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut state = State::Right;
        // Initialize the boundaries, une inclusive values and match with ..=.
        let m = matrix.len();
        let n = matrix[0].len();
        let (mut left, mut right, mut top, mut bottom) = (0, n - 1, 0, m - 1);
        let (mut r, mut c) = (0, 0);
        let mut res = Vec::with_capacity(n * m);
        while res.capacity() != res.len() {
            // Always add the current cell.
            res.push(matrix[r][c]);
            match state {
                State::Right => {
                    if c == right {
                        state = State::Down;
                        top += 1;
                        r += 1;
                    } else {
                        c += 1;
                    }
                }
                State::Down => {
                    if r == bottom {
                        state = State::Left;
                        right -= 1;
                        c -= 1;
                    } else {
                        r += 1;
                    }
                }
                State::Left => {
                    if c == left {
                        state = State::Up;
                        bottom -= 1;
                        r -= 1;
                    } else {
                        c -= 1;
                    }
                }
                State::Up => {
                    if r == top {
                        state = State::Right;
                        left += 1;
                        c += 1;
                    } else {
                        r -= 1;
                    }
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
            vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]],
            vec![1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            vec![vec![1, 2, 3, 4], vec![5, 6, 7, 8], vec![9, 10, 11, 12]],
            vec![1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        (
            vec![
                vec![1, 2, 3, 4],
                vec![5, 6, 7, 8],
                vec![9, 10, 11, 12],
                vec![13, 14, 15, 16],
            ],
            vec![1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::spiral_order(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
