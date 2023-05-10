// 59. Spiral Matrix II
// 🟠 Medium
//
// https://leetcode.com/problems/spiral-matrix-ii/
//
// Tags: Array - Matrix - Simulation

enum State {
    Right,
    Down,
    Left,
    Up,
}

struct Solution;
impl Solution {
    /// Use a state machine with four states, corresponding to the four
    /// directions we can travel. Depending on the state, use current row and
    /// column values and unvisited row and column values to determine if we
    /// need to update or preserve the state.
    ///
    /// Time complexity: O(n^2) - We do O(1) work, adjusting state and some
    /// usize and i32 values, for each value between 1 and n^2.
    /// Space complexity: O(1) - If we do not take into account the output
    /// matrix, otherwise O(n^2).
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 96.42%
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut matrix = vec![vec![0; n]; n];
        let mut state = State::Right;
        let (mut r, mut c) = (0, 0);
        let (mut top, mut right, mut bottom, mut left) = (0, n - 1, n - 1, 0);
        for i in 1..=(n * n) {
            matrix[r][c] = i as i32;
            match state {
                State::Right => {
                    if c == right {
                        top += 1;
                        state = State::Down;
                        r += 1;
                    } else {
                        c += 1;
                    }
                }
                State::Down => {
                    if r == bottom {
                        right = right - 1;
                        state = State::Left;
                        c -= 1;
                    } else {
                        r += 1;
                    }
                }
                State::Left => {
                    if c == left {
                        bottom -= 1;
                        state = State::Up;
                        r -= 1;
                    } else {
                        c -= 1;
                    }
                }
                State::Up => {
                    if r == top {
                        left += 1;
                        state = State::Right;
                        c += 1;
                    } else {
                        r -= 1;
                    }
                }
            }
        }
        matrix
    }
}

// Tests.
fn main() {
    let tests = [
        (1, vec![vec![1]]),
        (3, vec![vec![1, 2, 3], vec![8, 9, 4], vec![7, 6, 5]]),
        (
            4,
            vec![
                vec![1, 2, 3, 4],
                vec![12, 13, 14, 5],
                vec![11, 16, 15, 6],
                vec![10, 9, 8, 7],
            ],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::generate_matrix(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
