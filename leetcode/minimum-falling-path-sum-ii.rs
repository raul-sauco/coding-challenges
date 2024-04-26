// 1289. Minimum Falling Path Sum II
// 🔴 Hard
//
// https://leetcode.com/problems/minimum-falling-path-sum-ii/
//
// Tags: Array - Dynamic Programming - Matrix

struct Solution;
impl Solution {
    /// Use dynamic programming, for each row, we only need to keep two values, the minimum, that
    /// we will be able to add to all cells in the next row except the one directly below it, and
    /// the second smallest value, that we will add to the cell directly below the minimum. Iterate
    /// over the rows, then the nested values, keeping track of the two smallest sums of paths,
    /// then return the smaller one between the two.
    ///
    /// Time complexity: O(n*n) - Where n is the number of rows and it is equal to the number of
    /// columns. We visit each cell once and do O(1) work for each.
    /// Space complexity: O(1) - We use two arrays of size 2 of extra memory.
    ///
    /// Runtime 4 ms Beats 100%
    /// Memory 2.54 MB Beats 50%
    #[allow(dead_code)]
    pub fn min_falling_path_sum_1(grid: Vec<Vec<i32>>) -> i32 {
        grid.into_iter()
            .fold([(0i32, 0), (0i32, 1)], |acc, row| {
                let mut next = [(i32::MAX, 0), (i32::MAX, 1)];
                for (i, x) in row.into_iter().enumerate() {
                    let m = if i != acc[0].1 {
                        x + acc[0].0
                    } else {
                        x + acc[1].0
                    };
                    if m < next[0].0 {
                        next.swap(0, 1);
                        next[0] = (m, i);
                    } else if m < next[1].0 {
                        next[1] = (m, i);
                    }
                }
                next
            })
            .iter()
            .map(|arr| arr.0)
            .min()
            .unwrap()
    }

    /// Same solution but update the nested inner loop to an iterator and fold.
    ///
    /// Time complexity: O(n*n) - Where n is the number of rows and it is equal to the number of
    /// columns. We visit each cell once and do O(1) work for each.
    /// Space complexity: O(1) - We use two arrays of size 2 of extra memory.
    ///
    /// Runtime 4 ms Beats 100%
    /// Memory 2.64 MB Beats 50%
    pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        grid.into_iter()
            .fold([(0i32, 0), (0i32, 1)], |acc, row| {
                row.into_iter().enumerate().fold(
                    [(i32::MAX, 0), (i32::MAX, 1)],
                    |mut next, (i, x)| {
                        let m = if i != acc[0].1 {
                            x + acc[0].0
                        } else {
                            x + acc[1].0
                        };
                        if m < next[0].0 {
                            next.swap(0, 1);
                            next[0] = (m, i);
                        } else if m < next[1].0 {
                            next[1] = (m, i);
                        }
                        next
                    },
                )
            })
            .iter()
            .map(|arr| arr.0)
            .min()
            .unwrap()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![7]], 7),
        (vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]], 13),
        (
            vec![
                vec![-73, 61, 43, -48, -36],
                vec![3, 30, 27, 57, 10],
                vec![96, -76, 84, 59, -15],
                vec![5, -49, 76, 31, -7],
                vec![97, 91, 61, -46, 67],
            ],
            -192,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_falling_path_sum(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
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
