// 2022. Convert 1D Array Into 2D Array
// 🟢 Easy
//
// https://leetcode.com/problems/convert-1d-array-into-2d-array/
//
// Tags: Array - Matrix - Simulation

struct Solution;
impl Solution {
    /// Use nested for loops to generate the result.
    ///
    /// Time complexity: O(m*n) - We iterate over the m*n positions.
    /// Space complexity: O(m*n) - The result matrix.
    ///
    /// Runtime 32 ms Beats 20%
    /// Memory 4.41 MB Beats %
    #[allow(dead_code)]
    pub fn construct2_d_array_for(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        let (m, n) = (m as usize, n as usize);
        if m * n != original.len() {
            return vec![];
        }
        let mut res = vec![vec![0; n]; m];
        for r in 0..m {
            for c in 0..n {
                res[r][c] = original[r * n + c];
            }
        }
        res
    }

    /// The iterator version of the same solution.
    ///
    /// Time complexity: O(m*n) - We iterate over the m*n positions.
    /// Space complexity: O(m*n) - The result matrix.
    ///
    /// Runtime 28 ms Beats 66%
    /// Memory 4.60 MB Beats 40%
    pub fn construct2_d_array(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        if m * n == original.len() as i32 {
            original
                .chunks_exact(n as usize)
                .map(|chunk| chunk.to_vec())
                .collect()
        } else {
            vec![]
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![1, 1, 1, 1],
            4,
            1,
            vec![vec![1], vec![1], vec![1], vec![1]],
        ),
        (vec![1, 2, 3, 4], 2, 2, vec![vec![1, 2], vec![3, 4]]),
        (vec![1, 2, 3], 1, 3, vec![vec![1, 2, 3]]),
        (vec![1, 2], 1, 1, vec![]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::construct2_d_array(t.0.clone(), t.1, t.2);
        if res == t.3 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.3, res
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
