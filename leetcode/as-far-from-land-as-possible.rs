// 1162. As Far from Land as Possible
// 🟠 Medium
//
// https://leetcode.com/problems/as-far-from-land-as-possible/
//
// Tags: Array - Dynamic Programming - Breadth-First Search - Matrix

struct Solution;
impl Solution {
    // Use BFS and a matrix with the current shortest distance between any
    // cell and land to compute the shortest distance between any cell and
    // land, we will only revisit cells when the new distance to land is
    // less than the shortest previous distance found, which may, in turn,
    // influence its neighbors by providing a shorter path to land.
    //
    // Time complexity: O(m+n) - We can travel a maximum of n levels, on each
    // level, we will only visit cells to which we have not previously found
    // a shorter route, in total we will visit m*n cells during the BFS.
    // Space complexity: O(m+n) - The distance matrix has the same size as
    // the input matrix, m rows and n columns.
    //
    // Runtime 12 ms Beats 66.67%
    // Memory 2.3 MB Beats 93.33%
    pub fn max_distance(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dist: Vec<Vec<usize>> = vec![vec![1000; n]; m];
        let mut current_level: Vec<(i16, i16)> = vec![];
        let mut level: usize = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    current_level.push((i as i16, j as i16));
                    dist[i][j] = 0;
                }
            }
        }
        if current_level.len() == 0 || current_level.len() == (m * n) {
            return -1;
        }
        while current_level.len() > 0 {
            let mut next_level = Vec::<(i16, i16)>::new();
            level += 1;
            // Process the current entire level.
            for _ in 0..current_level.len() {
                let (r, c) = current_level.pop().unwrap();
                for (nr, nc) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] {
                    if 0 <= nr
                        && nr < m as i16
                        && 0 <= nc
                        && nc < n as i16
                        && level < dist[nr as usize][nc as usize]
                    {
                        dist[nr as usize][nc as usize] = level;
                        next_level.push((nr, nc));
                    }
                }
            }
            current_level = next_level;
        }
        (level - 1) as i32
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::max_distance(vec![vec![1, 0, 1], vec![0, 0, 0], vec![1, 0, 1]]),
        2
    );
    assert_eq!(
        Solution::max_distance(vec![vec![1, 0, 0], vec![0, 0, 0], vec![0, 0, 0]]),
        4
    );
    println!("All tests passed!")
}
