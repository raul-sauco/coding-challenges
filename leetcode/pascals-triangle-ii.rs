// 119. Pascal's Triangle II
// 🟢 Easy
//
// https://leetcode.com/problems/pascals-triangle-ii/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// Generate the rows one at a time, each element is the sum of the elements
    /// at i-1 + i positions in the previous row.
    ///
    /// Time complexity: O(n^2) - We generate n rows, for each row, we visit
    /// row_length elements.
    /// Space complexity: O(n) - We use an extra vector of size n.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.05 MB Beats 51.22%
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let mut row = vec![1];
        let mut a = 1;
        let mut b;
        for _ in 0..row_index as usize {
            for i in 0..row.len() {
                b = a;
                a = row[i];
                if i == 0 {
                    continue;
                }
                row[i] = a + b;
            }
            row.push(1);
        }
        row
    }

    /// Similar logic but we can save the extra variable if we iterate over the
    /// elements on the row backwards.
    ///
    /// Time complexity: O(n^2) - We generate n rows, for each row, we visit
    /// row_length elements.
    /// Space complexity: O(n) - We use an extra vector of size n.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.14 MB Beats 24.39%
    pub fn get_row_2(row_index: i32) -> Vec<i32> {
        let n = row_index as usize;
        let mut row = vec![0; n + 1];
        row[0] = 1;
        for i in 1..=n {
            for j in (1..=i).rev() {
                row[j] += row[j - 1];
            }
        }
        row
    }
}

// Tests.
fn main() {
    let tests = [(3, vec![1, 3, 3, 1]), (0, vec![1]), (1, vec![1, 1])];
    for t in tests {
        assert_eq!(Solution::get_row(t.0), t.1);
        assert_eq!(Solution::get_row_2(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
