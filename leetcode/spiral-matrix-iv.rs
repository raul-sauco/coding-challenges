// 2326. Spiral Matrix IV
// 🟠 Medium
//
// https://leetcode.com/problems/spiral-matrix-iv/
//
// Tags: Array - Linked List - Matrix - Simulation

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

// impl ListNode {
//     #[inline]
//     fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

struct Solution;
impl Solution {
    /// Create an m*n 2D vector and fill it using the values in the linked list use a current
    /// position and a direction to determine which position in the matrix to write the value to,
    /// check boundaries and the value of the cell to determine if we are still within bounds,
    /// first time around, or we have already written to that cell, in the inner loops.
    ///
    /// Time complexity: O(m*n) - We create an initial 2D vector of m*n positions and fill it with
    /// -1, then we iterate over the values in the linked list that are, at most, m*n.
    /// Space complexity: O(m*n) - The result matrix.
    ///
    /// Runtime 86 ms Beats 76%
    /// Memory 10.61 MB Beats 68%
    #[allow(dead_code)]
    pub fn spiral_matrix_submit(m: i32, n: i32, mut head: Option<Box<ListNode>>) -> Vec<Vec<i32>> {
        let mut res = vec![vec![-1i32; n as usize]; m as usize];
        let mut dir = (0, 1);
        let mut pos = (0, 0);
        let mut next;
        while let Some(mut node) = head {
            head = node.next.take();
            res[pos.0 as usize][pos.1 as usize] = node.val;
            next = (pos.0 + dir.0, pos.1 + dir.1);
            if next.0 < 0
                || next.0 >= m
                || next.1 < 0
                || next.1 >= n
                || res[next.0 as usize][next.1 as usize] != -1
            {
                dir = (dir.1, -dir.0);
                next = (pos.0 + dir.0, pos.1 + dir.1);
            }
            pos = next;
        }
        res
    }
    /// Use a vector instead of the linked list for testing
    pub fn spiral_matrix(m: i32, n: i32, head: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = vec![vec![-1i32; n as usize]; m as usize];
        let mut dir = (0, 1);
        let mut pos = (0, 0);
        let mut next;
        for num in head {
            println!(
                "Pos: ({},{}). Dir ({},{}) » num: {}",
                pos.0, pos.1, dir.0, dir.1, num
            );
            res[pos.0 as usize][pos.1 as usize] = num;
            next = (pos.0 + dir.0, pos.1 + dir.1);
            if next.0 < 0
                || next.0 >= m
                || next.1 < 0
                || next.1 >= n
                || res[next.0 as usize][next.1 as usize] != -1
            {
                dir = (dir.1, -dir.0);
                next = (pos.0 + dir.0, pos.1 + dir.1);
            }
            pos = next;
            Self::print_matrix(&res);
        }
        res
    }
    fn print_matrix(matrix: &Vec<Vec<i32>>) {
        if matrix.is_empty() || matrix[0].is_empty() {
            return;
        }

        // Find the maximum width for each column
        let mut col_widths = vec![0; matrix[0].len()];

        for row in matrix {
            for (i, &val) in row.iter().enumerate() {
                let width = val.to_string().len();
                if width > col_widths[i] {
                    col_widths[i] = width;
                }
            }
        }

        // Print the matrix with aligned columns
        for row in matrix {
            for (i, &val) in row.iter().enumerate() {
                print!("{:>width$} ", val, width = col_widths[i]);
            }
            println!();
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (
            3,
            5,
            vec![3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0],
            vec![
                vec![3, 0, 2, 6, 8],
                vec![5, 0, -1, -1, 1],
                vec![5, 2, 4, 9, 7],
            ],
        ),
        (1, 4, vec![0, 1, 2], vec![vec![0, 1, 2, -1]]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::spiral_matrix(t.0, t.1, t.2.clone());
        if res == t.3 {
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
