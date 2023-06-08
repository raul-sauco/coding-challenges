// 1351. Count Negative Numbers in a Sorted Matrix
// 🟢 Easy
//
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
//
// Tags: Array - Binary Search - Matrix

struct Solution;
impl Solution {
    /// Iterate over each row from the bottom up, to avoid the column pointer
    /// from becoming negative when going out of bounds. Keep a pointer c to
    /// the first negative value in the row, for each row, advance c until it
    /// finds the first negative value, then exit the nested loop and use the
    /// row length and c to compute the number of negative values in the
    /// current row, then move to the next row.
    ///
    /// Time complexity: O(m+n) - We iterate over all the rows while keeping a
    /// pointer to a column, the column pointer may visit each column once.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 3 ms Beats 72.73%
    /// Memory 2.2 MB Beats 90.91%
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let mut res = 0;
        let (m, n) = (grid.len(), grid[0].len());
        let mut c = 0;
        for r in (0..m).rev() {
            while c < n && grid[r][c] >= 0 {
                c += 1;
            }
            res += n - c;
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![3, 2], vec![1, 0]], 0),
        (
            vec![
                vec![4, 3, 2, -1],
                vec![3, 2, 1, -1],
                vec![1, 1, -1, -2],
                vec![-1, -1, -2, -3],
            ],
            8,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::count_negatives(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
