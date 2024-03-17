// 57. Insert Interval
// 🟠 Medium
//
// https://leetcode.com/problems/insert-interval/
//
// Tags: Array

#[derive(Debug, Clone)]
struct Interval {
    start: i32,
    end: i32,
}

impl Interval {
    fn merge(&self, other: &Interval) -> Self {
        Interval {
            start: self.start.min(other.start),
            end: self.end.max(other.end),
        }
    }
}

struct Solution;
impl Solution {
    /// Iterate over the intervals in the input. Keep a mutable copy of the new interval, insert
    /// all intervals that come fully before the new interval, then merge the overlapping intervals
    /// with the new interval by mutating it but not inserting it yet. Once we intert in, append
    /// the remaining elements and return the result. If we exit the loop, we have not inserted the
    /// new interval yet, do it and return the result.
    ///
    /// Time complexity: O(n) - We iterate over the n elements in the input and do constant time
    /// work for each.
    /// Space complexity: O(1) - If we don't take into account the result vector.
    ///
    /// Runtime 2 ms Beats 73%
    /// Memory 2.65 MB Beats 51%
    #[allow(dead_code)]
    pub fn insert_1(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = vec![];
        let mut new_interval = new_interval;
        for (idx, int) in intervals.iter().enumerate() {
            if new_interval[1] < int[0] {
                res.push(new_interval);
                res.extend(intervals[idx..].into_iter().map(|v| v.clone()));
                return res;
            } else if new_interval[0] > int[1] {
                res.push(int.to_vec());
            } else {
                new_interval = vec![new_interval[0].min(int[0]), new_interval[1].max(int[1])];
            }
        }
        res.push(new_interval);
        res
    }

    /// Same logic as the previous solution but use a struct and impl to make it cleaner. I
    /// expected this solution to be slower because it iterates the input vector extra times to map
    /// the input to a Vec<Interval> and then map the result back to Vec<Vec<_>> but it got the
    /// sames times as the previous result.
    ///
    /// Time complexity: O(n) - We iterate over the n elements in the input and do constant time
    /// work for each.
    /// Space complexity: O(1) - If we don't take into account the result vector.
    ///
    /// Runtime 2 ms Beats 73%
    /// Memory 2.65 MB Beats 51%
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let intervals = intervals
            .iter()
            .map(|i| Interval {
                start: i[0],
                end: i[1],
            })
            .collect::<Vec<_>>();
        let mut res: Vec<Interval> = vec![];
        let mut new_interval = Interval {
            start: new_interval[0],
            end: new_interval[1],
        };
        for (idx, int) in intervals.iter().enumerate() {
            if new_interval.end < int.start {
                res.push(new_interval);
                res.extend(intervals[idx..].into_iter().map(|v| v.clone()));
                return res.iter().map(|i| vec![i.start, i.end]).collect::<Vec<_>>();
            } else if new_interval.start > int.end {
                res.push(int.clone());
            } else {
                new_interval = new_interval.merge(&int);
            }
        }
        res.push(new_interval);
        res.iter().map(|i| vec![i.start, i.end]).collect::<Vec<_>>()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![], vec![5, 7], vec![[5, 7]]),
        (vec![[1, 3], [6, 9]], vec![2, 5], vec![[1, 5], [6, 9]]),
        (
            vec![[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            vec![4, 8],
            vec![[1, 2], [3, 10], [12, 16]],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::insert(
            t.0.iter().map(|arr| arr.to_vec()).collect::<Vec<_>>(),
            t.1.clone(),
        );
        let expected = t.2.iter().map(|arr| arr.to_vec()).collect::<Vec<_>>();
        if res == expected {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, expected, res
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
