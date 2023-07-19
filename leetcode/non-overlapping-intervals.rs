// 435. Non-overlapping Intervals
// 🟠 Medium
//
// https://leetcode.com/problems/non-overlapping-intervals/
//
// Tags: Array - Dynamic Programming - Greedy - Sorting

struct Solution;
impl Solution {
    /// Sort the intervals by end time, then iterate over them checking if the
    /// start time of each interval is equal or after the end time of the
    /// previous interval, for each interval that overlaps the previous one
    /// we add one to the result, when the interval does not overlap the
    /// previous one, we use it and update the end time of the last used
    /// interval.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the intervals has the highest
    /// time complexity, then we iterate over them in O(n)
    /// Space complexity: O(1) - Sorting may use extra memory depending on the
    ///
    /// Runtime 66 ms Beats 63.16%
    /// Memory 14.01 MB Beats 5.26%
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals = intervals.clone();
        intervals.sort_by_key(|k| k[1]);
        let mut res = 0;
        let mut boundary = i32::MIN;
        for interval in intervals {
            if interval[0] >= boundary {
                // This interval does not overlap the previous one.
                boundary = interval[1];
            } else {
                res += 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![1, 3]], 1),
        (vec![vec![1, 2], vec![1, 2], vec![1, 2]], 2),
    ];
    for t in tests {
        assert_eq!(Solution::erase_overlap_intervals(t.0), t.1);
    }
    println!("[92m» All tests passed![0m")
}
