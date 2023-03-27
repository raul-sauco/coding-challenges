// 64. Minimum Path Sum
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-path-sum/
//
// Tags: Array - Dynamic Programming - Matrix

struct Solution;
impl Solution {
    /// Starting from the O(2^n) recursive solution, we can turn it around and
    /// transform it into a O(n) dynamic programming solution. We start at the
    /// top left, the intermediate value of each position will be the value of
    /// the cell at that position plus the minimum of the intermediate value
    /// above and the one to its left, since at that time we can guarantee that
    /// it is always better to use the minimum path to reach that cell.
    ///
    /// Time complexity: O(m+n) - We visit each cell on the grid and do O(1)
    /// work for each.
    /// Space complexity: O(n) - The dp array has the same length as one row
    /// of the matrix, we could optimize this by checking if rows or columns are
    /// smaller and iterating over the shorter ones, if we had a strict memory
    /// limit.
    ///
    /// Runtime 2 ms Beats 77.14%
    /// Memory 2.3 MB Beats 94.29%
    pub fn min_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        let mut dp: Vec<i32> = grid[0]
            .iter()
            .scan(0, |acc, &x| {
                *acc = *acc + x;
                Some(*acc)
            })
            .collect();
        for i in 1..m {
            for j in 0..n {
                if j == 0 {
                    dp[j] += grid[i][j];
                } else {
                    dp[j] = grid[i][j] + dp[j - 1].min(dp[j])
                }
            }
        }
        *dp.last().unwrap()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1, 2, 3], vec![4, 5, 6]], 12),
        (vec![vec![1, 3, 1], vec![1, 5, 1], vec![4, 2, 1]], 7),
    ];
    for t in tests {
        assert_eq!(Solution::min_path_sum(t.0), t.1);
    }
    println!("All tests passed!")
}
