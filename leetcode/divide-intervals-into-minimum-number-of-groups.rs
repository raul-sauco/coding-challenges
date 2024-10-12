// 2406. Divide Intervals Into Minimum Number of Groups
// 🟠 Medium
//
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
//
// Tags: Array - Two Pointers - Greedy - Sorting - Heap (Priority Queue) - Prefix Sum

use std::{cmp::Reverse, collections::BinaryHeap};

struct Solution;
impl Solution {
    /// Sort the intervals to process them in order by start time. Use a heap to keep track of the
    /// earliest end time of any of the existing groups. For each interval, check if we can add it
    /// to the group at the top of the heap. This greedy solution works because we have guaranteed
    /// both that we have the group with the earliest end and the interval with the earliest start,
    /// if we cannot add it to that group, we cannot add any other later interval to that group and
    /// we cannot add this interval to any other groups, we need to create a new group.
    ///
    /// Time complexity: O(nlog(n)) - Sorting the intervals and pushing/popping from the heap.
    /// Space complexity: O(n) - The sorted intervals are size n, the heap can grow to size n.
    ///
    /// Runtime 37 ms Beats 100%
    /// Memory 9.78 MB Beats 33%
    pub fn min_groups(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals = intervals.iter().map(|v| (v[0], v[1])).collect::<Vec<_>>();
        intervals.sort_unstable();
        let mut groups = BinaryHeap::<Reverse<i32>>::new();
        for (start, end) in intervals {
            if let Some(Reverse(group_end)) = groups.peek().copied() {
                if start > group_end {
                    groups.pop();
                }
            }
            groups.push(Reverse(end));
        }
        groups.len() as _
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]], 3),
        (vec![[1, 3], [5, 6], [8, 10], [11, 13]], 1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_groups(t.0.iter().map(|a| a.to_vec()).collect());
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
