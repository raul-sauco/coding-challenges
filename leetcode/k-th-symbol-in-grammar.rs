// 779. K-th Symbol in Grammar
// 🟠 Medium
//
// https://leetcode.com/problems/k-th-symbol-in-grammar/
//
// Tags: Math - Bit Manipulation - Recursion

struct Solution;
impl Solution {
    /// The brute force solution, generate all values for each row.
    ///
    /// Time complexity: O(2^n) - We generate all rows, each row up to n is
    /// double the size of the previous one.
    /// Space complexity: O(2^n)
    pub fn brute_force(n: i32, k: i32) -> i32 {
        let k = k as usize;
        let mut row = vec![0];
        let mut next_row = vec![];
        for _r in 0..n {
            for i in 0..row.len() {
                next_row.extend(if row[i] == 0 { vec![0, 1] } else { vec![1, 0] });
            }
            std::mem::swap(&mut row, &mut next_row);
            next_row.clear();
        }
        row[k - 1]
    }

    /// A recursive solution, for each row, the second half of the row is equal
    /// to the first half with the values reversed, we can check the length of
    /// the current row, if the index we are looking for is in the first half,
    /// we call the function with the next row and the same parameters, if the
    /// index is in the second row, we negate the result of calling the function
    /// with the same relative position in the first half of the vector but on
    /// the next row.
    ///
    /// Time complexity: O(n) - For each row, or value of n, we call once the
    /// recursize function.
    /// Space complexity: O(n) - The call stack grows to size n.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.04 MB Beats 50%
    pub fn kth_grammar(n: i32, k: i32) -> i32 {
        // A function that helps us work with 0-indexed values.
        fn helper(row_size: usize, col: usize) -> bool {
            if row_size == 1 || col == 0 {
                return false;
            }
            let next_row_size = row_size / 2;
            if col >= next_row_size {
                return !helper(next_row_size, col - next_row_size);
            }
            helper(next_row_size, col)
        }
        if helper(2i32.pow(n as u32 - 1) as usize, k as usize - 1) {
            1
        } else {
            0
        }
    }

    /// See the LeetCode editorial for an explanation on this.
    ///
    /// Time complexity: O(log(k))
    /// Space complexity: O(1)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.03 MB Beats 50%
    pub fn count_bits(_n: i32, k: i32) -> i32 {
        ((k - 1).count_ones() % 2) as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (7, 6, 0),
        (1, 1, 0),
        (2, 1, 0),
        (2, 2, 1),
        (13, 3459, 1),
        (20, 24288, 0),
    ];
    for t in tests {
        assert_eq!(Solution::brute_force(t.0, t.1), t.2);
        assert_eq!(Solution::kth_grammar(t.0, t.1), t.2);
        assert_eq!(Solution::count_bits(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
