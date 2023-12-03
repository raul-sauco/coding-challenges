// 1266. Minimum Time Visiting All Points
// 🟢 Easy
//
// https://leetcode.com/problems/minimum-time-visiting-all-points/
//
// Tags: Array - Math - Geometry

struct Solution;
impl Solution {
    /// Compare each pair of points in the input and compute the distance between them as the
    /// maximum of the absolute differences in the x and y axis.
    ///
    /// Time complexity: O(n) - We visit each point in the input.
    /// Space complexity: O(1) - We store one i32.
    ///
    /// Runtime 1 ms Beats 66.67%
    /// Memory 2.08 MB Beats 85.19%
    pub fn _min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut res = 0;
        for i in 1..points.len() {
            res += (points[i][0] - points[i - 1][0])
                .abs()
                .max((points[i][1] - points[i - 1][1]).abs());
        }
        res
    }

    /// Same logic as the previous solution but using iterators.
    ///
    /// Time complexity: O(n) - We visit each point in the input.
    /// Space complexity: O(1) - We store one i32.
    ///
    /// Runtime 1 ms Beats 66.67%
    /// Memory 2.38 MB Beats 25.93%
    pub fn __min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        points.windows(2).fold(0, |acc, v| {
            acc + (v[0][0] - v[1][0]).abs().max((v[0][1] - v[1][1]).abs())
        })
    }

    /// Same logic but use map + sum instead of fold.
    ///
    /// Time complexity: O(n) - We visit each point in the input.
    /// Space complexity: O(1) - We store one i32.
    ///
    /// Runtime 1 ms Beats 66.67%
    /// Memory 2.04 MB Beats 85.19%
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        points
            .windows(2)
            .map(|v| (v[0][0] - v[1][0]).abs().max((v[0][1] - v[1][1]).abs()))
            .sum()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![[1, 1], [3, 4], [-1, 0]], 7),
        (vec![[3, 2], [-2, 2]], 5),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_time_to_visit_all_points(
            t.0.iter().map(|a| a.to_vec()).collect::<Vec<_>>(),
        );
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
    println!("");
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
