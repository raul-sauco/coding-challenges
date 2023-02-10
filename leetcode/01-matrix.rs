// 542. 01 Matrix
// 🟠 Medium
//
// https://leetcode.com/problems/01-matrix/
//
// Tags: Array - Dynamic Programming - Breadth-First Search - Matrix

struct Solution;
impl Solution {
    // Use BFS and a matrix with the current shortest distance between any
    // cell and land to compute the shortest distance between any cell and
    // land, we will only process cells the first time that we land in them
    // because the level keeps increasing.
    //
    // Time complexity: O(m+n) - We will visit m*n cells.
    // Space complexity: O(m+n) - The distance matrix has the same size as
    // the input matrix, m rows and n columns.
    //
    // Runtime 29 ms Beats 57.63%
    // Memory 3.1 MB Beats 61.2%
    pub fn update_matrix(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = mat.len();
        let n = mat[0].len();
        let mut dist: Vec<Vec<i32>> = vec![vec![100001; n]; m];
        let mut current_level = vec![];
        let mut level: i32 = 0;
        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 0 {
                    current_level.push((i as i32, j as i32));
                    dist[i][j] = 0;
                }
            }
        }
        while current_level.len() > 0 {
            let mut next_level = Vec::new();
            level += 1;
            // Process the current entire level.
            for _ in 0..current_level.len() {
                let (r, c) = current_level.pop().unwrap();
                for (nr, nc) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] {
                    if 0 <= nr
                        && nr < m as i32
                        && 0 <= nc
                        && nc < n as i32
                        && level < dist[nr as usize][nc as usize]
                    {
                        dist[nr as usize][nc as usize] = level;
                        next_level.push((nr, nc));
                    }
                }
            }
            current_level = next_level;
        }
        dist
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::update_matrix(vec![vec![0, 0, 0], vec![0, 1, 0], vec![0, 0, 0]]),
        vec![vec![0, 0, 0], vec![0, 1, 0], vec![0, 0, 0]]
    );
    assert_eq!(
        Solution::update_matrix(vec![vec![0, 0, 0], vec![0, 1, 0], vec![1, 1, 1]]),
        vec![vec![0, 0, 0], vec![0, 1, 0], vec![1, 2, 1]]
    );
    println!("All tests passed!")
}
