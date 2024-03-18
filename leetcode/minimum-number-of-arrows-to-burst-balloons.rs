// 452. Minimum Number of Arrows to Burst Balloons
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
//
// Tags: Array - Greedy - Sorting

struct Interval {
    start: i32,
    end: i32,
}

struct Solution;
impl Solution {
    /// We sort the intervals by start, then iterate through them keeping track of the position at
    /// which we fired the last arrow until we cannot "reuse" it to burst the next ballon, then we
    /// increment the count of arrows used and start updating the position at which we used the
    /// arrow greedily using the furthest right value we can until we are forced to again use a new
    /// arrow.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the highest time complexity, after that O(n)
    /// Space complexity: O(1) - Constant extra space used if we ignore the mutable copy of the
    /// input array and the extra memory used by the sorting algorithm.
    ///
    /// Runtime 45 ms Beats 53%
    /// Memory 9.34 MB Beats 67%
    #[allow(dead_code)]
    pub fn find_min_arrow_shots_sort_by_start(points: Vec<Vec<i32>>) -> i32 {
        let mut res = 1;
        let mut points = points;
        points.sort_unstable();
        let mut last_arrow = points[0][1];
        for point in points.into_iter().skip(1) {
            if point[0] > last_arrow {
                last_arrow = point[1];
                res += 1;
            } else if point[1] < last_arrow {
                last_arrow = point[1];
            }
        }
        res
    }

    /// Similar solution but sort by end time and use an Interval struct to clean up the code.
    /// Sorting by end lets us not have to check if we need to modify the point at which we
    /// previously used the last arrow.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the highest time complexity, after that O(n)
    /// Space complexity: O(1) - Constant extra space used if we ignore the mutable copy of the
    /// input array and the extra memory used by the sorting algorithm.
    ///
    /// Runtime 37 ms Beats 90%
    /// Memory 9.48 MB Beats 45%
    pub fn find_min_arrow_shots(points: Vec<Vec<i32>>) -> i32 {
        let mut res = 1;
        let mut intervals = points
            .iter()
            .map(|v| Interval {
                start: v[0],
                end: v[1],
            })
            .collect::<Vec<_>>();
        intervals.sort_unstable_by_key(|i| i.end);
        let mut last_arrow = intervals[0].end;
        for interval in intervals.into_iter().skip(1) {
            if interval.start > last_arrow {
                last_arrow = interval.end;
                res += 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        (vec![[1, 2], [2, 3], [3, 4], [4, 5]], 2),
        (vec![[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        (
            vec![[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]],
            2,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_min_arrow_shots(t.0.iter().map(|a| a.to_vec()).collect());
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
