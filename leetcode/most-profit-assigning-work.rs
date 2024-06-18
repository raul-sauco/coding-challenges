// 826. Most Profit Assigning Work
// 🟠 Medium
//
// https://leetcode.com/problems/most-profit-assigning-work/
//
// Tags: Array - Two Pointers - Binary Search - Greedy - Sorting

#[derive(Ord, Eq, PartialEq, PartialOrd)]
struct Job {
    difficulty: i32,
    profit: i32,
}

struct Solution;
impl Solution {
    /// Combine the difficulty and profit vectors into one and sort them, sort the worker vector
    /// and iterate over the worker's capacity in ascending order. Keep a variable with the maximum
    /// profit between all the jobs that we are currently able to perform, for each worker, update
    /// the current maximum job profit visiting all jobs that the worker can do and update the
    /// total using that maximum. Since the workers are sorted, all the workers after the current
    /// one will be able to, at least, obtain that same profit.
    ///
    /// Time complexity: O(m*log(m) + n*log(n)) - We sort both the Jobs vector and the workers
    /// vector. After that O(m+n) we iterate over the workers, for each worker we may advance the
    /// index pointer n positions but that is also the maximum overall between all workers.
    /// Space complexity: O(m+n) - The sorted Vec<Job> and the copy of the worker vector.
    ///
    /// Runtime 6 ms Beats 50%
    /// Memory 2.24 MB Beats 100%
    pub fn max_profit_assignment(difficulty: Vec<i32>, profit: Vec<i32>, worker: Vec<i32>) -> i32 {
        let mut jobs = difficulty
            .into_iter()
            .zip(profit.into_iter())
            .map(|t| Job {
                difficulty: t.0,
                profit: t.1,
            })
            .collect::<Vec<_>>();
        let n = jobs.len();
        jobs.sort_unstable();
        let mut workers = worker;
        workers.sort_unstable();
        let (mut idx, mut cur_max, mut total_profit) = (0, 0, 0);
        for capacity in workers {
            // Update the max with any jobs this worker can do.
            while idx < n && jobs[idx].difficulty <= capacity {
                cur_max = cur_max.max(jobs[idx].profit);
                idx += 1;
            }
            total_profit += cur_max;
        }
        total_profit
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![85, 47, 57], vec![24, 66, 99], vec![40, 25, 25], 0),
        (
            vec![68, 35, 52, 47, 86],
            vec![67, 17, 1, 81, 3],
            vec![92, 10, 85, 84, 82],
            324,
        ),
        (
            vec![2, 4, 6, 8, 10],
            vec![10, 20, 30, 40, 50],
            vec![4, 5, 6, 7],
            100,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_profit_assignment(t.0.clone(), t.1.clone(), t.2.clone());
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
