// 304. Range Sum Query 2D - Immutable
// 🟠 Medium
//
// https://leetcode.com/problems/range-sum-query-2d-immutable/
//
// Tags: Array - Design - Matrix - Prefix Sum

struct NumMatrix {
    sums: Vec<Vec<i32>>,
}

/// Compute a matrix of prefix sums where sums[i][j] is the sum of all elements
/// between sums[0][0] and sums[i][j] including. Store this prefix sums matrix
/// in the struct. When we receive a query [r1, c1, r2, c2] we can compute in
/// O(1) as the sum of all elements up to r2, c2 minus the columns to the left,
/// if any, of c1, minus the rows above, if any of r1, if there is an area
/// above and to the left of r1, c1, we will have subtracted it twice, we add
/// it once and we have the range sum.
///
/// Time complexity: O(m*n) - For the new method, we read all elements of the
/// input and create a matrix of the same size with prefix sums. For the
/// sum_region method, the time complexity is O(1).
/// Space complexity: O(m*n) - We store a matrix of prefix sums of the same
/// size as the input matrix.
///
/// Runtime 102 ms Beats 100%
/// Memory 13.7 MB Beats 65.52%
impl NumMatrix {
    fn new(matrix: Vec<Vec<i32>>) -> Self {
        let mut sums: Vec<Vec<i32>> = vec![];
        for i in 0..matrix.len() {
            let mut row = vec![];
            let mut row_sum = 0;
            for j in 0..matrix[0].len() {
                row_sum += matrix[i][j];
                row.push(row_sum);
                if i > 0 {
                    row[j] += sums[i - 1][j]
                }
            }
            sums.push(row);
        }
        Self { sums }
    }

    fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
        let (row1, col1) = (row1 as usize, col1 as usize);
        let (row2, col2) = (row2 as usize, col2 as usize);
        // Start with the sum at the bottom-right.
        let mut range_sum = self.sums[row2][col2];
        // If the range does not go all the way left, remove these columns.
        if col1 > 0 {
            range_sum -= self.sums[row2][col1 - 1];
        }
        // If the range does not go all the way to the top, remove these rows.
        if row1 > 0 {
            range_sum -= self.sums[row1 - 1][col2];
        }
        // If we removed twice the top-left cells, add them once.
        if col1 > 0 && row1 > 0 {
            range_sum += self.sums[row1 - 1][col1 - 1]
        }
        range_sum
    }
}

// Tests.
fn main() {
    let num_matrix = NumMatrix::new(vec![
        vec![3, 0, 1, 4, 2],
        vec![5, 6, 3, 2, 1],
        vec![1, 2, 0, 1, 5],
        vec![4, 1, 0, 1, 7],
        vec![1, 0, 3, 0, 5],
    ]);
    assert_eq!(num_matrix.sum_region(2, 1, 4, 3), 8);
    assert_eq!(num_matrix.sum_region(1, 1, 2, 2), 11);
    assert_eq!(num_matrix.sum_region(1, 2, 2, 4), 12);
    println!("All tests passed!")
}
