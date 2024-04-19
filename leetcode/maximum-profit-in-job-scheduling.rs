// 1235. Maximum Profit in Job Scheduling
// 🔴 Hard
//
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/
//
// Tags: Array - Binary Search - Dynamic Programming - Sorting

struct Solution;
impl Solution {
    /// We sort the input jobs by end time, then iterate over them saving the maximum profit that
    /// we can make up to a given time t, if we can improve on the current maximum profit by
    /// scheduling this new job, we schedule it by recording the new maximum profit and the current
    /// job end time on the dp array. Since we are iterating over the jobs based on end time, we
    /// are guaranteed to have a sorted dp array, that lets us use binary search to find the last
    /// job we can keep if we decide to use the current one.
    ///
    /// Time complexity: O(n*log(n)) - We iterate over all jobs, for each, we do binary search on
    /// the dp array to find the maximum profit before the start time of this job. Previously, we
    /// have also sorted the jobs array of length n.
    /// Space complexity: O(n) - The dp array could grow to the size of the input.
    ///
    /// Runtime  ms Beats %
    /// Memory  MB Beats %
    pub fn job_scheduling(start_time: Vec<i32>, end_time: Vec<i32>, profit: Vec<i32>) -> i32 {
        let mut jobs = (0..end_time.len())
            .map(|i| (start_time[i], end_time[i], profit[i]))
            .collect::<Vec<_>>();
        jobs.sort_unstable_by_key(|t| t.1);
        // At time 0 max 0 profit.
        let mut dp = vec![(0, 0)];
        let (mut l, mut r, mut m);
        for (start, end, p) in jobs {
            // "Do" this job. Find the max profit before the start of this job on the existing dp
            // array.
            (l, r) = (0, dp.len());
            while l < r {
                m = (l + r) / 2;
                if dp[m].0 > start {
                    r = m;
                } else {
                    l = m + 1;
                }
            }
            // l is the insert point.
            l -= 1;
            if dp[l].1 + p > dp.last().unwrap().1 {
                dp.push((end, dp[l].1 + p));
            }
        }
        dp.last().unwrap().1
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![1, 2, 3, 3],
            vec![3, 4, 5, 6],
            vec![50, 10, 40, 70],
            120,
        ),
        (
            vec![1, 2, 3, 4, 6],
            vec![3, 5, 10, 6, 9],
            vec![20, 20, 100, 70, 60],
            150,
        ),
        (vec![1, 1, 1], vec![2, 3, 4], vec![5, 6, 4], 6),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::job_scheduling(t.0.clone(), t.1.clone(), t.2.clone());
        if res == t.3 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.3, res
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
