// 539. Minimum Time Difference
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-time-difference/
//
// Tags: Array - Math - String - Sorting

struct Solution;
impl Solution {
    /// Convert the times to minutes of the day, sort and iterate over pairs to find the minimum
    /// difference.
    ///
    /// Time complexity: O(nlog(n)) - Sorting has the highest time complexity.
    /// Space complexity: O(n) - The minutes array takes extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 3.01 MB Beats 100%
    #[allow(dead_code)]
    pub fn find_min_difference_sort(time_points: Vec<String>) -> i32 {
        let mut times = time_points
            .into_iter()
            .map(|t| {
                let parts = t.split(':').collect::<Vec<&str>>();
                parts[0].parse::<i32>().expect("A valid hours number") * 60
                    + parts[1].parse::<i32>().expect("A valid minutes number")
            })
            .collect::<Vec<_>>();
        times.sort_unstable();
        times.windows(2).fold(
            24 * 60 + times[0] - times.last().expect("At least one value"),
            |acc, w| acc.min(w[1] - w[0]),
        )

        // Using a loop we can break earlier if res goes to 0.
        // Runtime 0 ms Beats 100%
        // Memory 3.24 MB Beats 25%
        // let mut res = 24 * 60 + times[0] - times.last().expect("At least one value");
        // for i in 1..times.len() {
        //     res = res.min(times[i] - times[i - 1]);
        //     if res == 0 {
        //         return 0;
        //     }
        // }
        // res
    }

    /// Since we have a known range of minute values 0..24*60, we can use bucket sort.
    ///
    /// Time complexity: O(nlog(n)) - Linear time.
    /// Space complexity: O(1) - The buckets array has a constant size.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 3.16 MB Beats 62%
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {
        let mut buckets = [false; 1440];
        let (mut first, mut last) = (usize::MAX, usize::MIN);
        for t in time_points {
            let parts = t.split(':').collect::<Vec<&str>>();
            let idx = parts[0].parse::<usize>().expect("A valid hours number") * 60
                + parts[1].parse::<usize>().expect("A valid minutes number");
            if buckets[idx] {
                // If we have seen the same time before, the min diff is 0.
                return 0;
            }
            buckets[idx] = true;
            first = first.min(idx);
            last = last.max(idx);
        }
        let mut res = 1440 + first - last;
        let mut last_idx = first;
        for i in first + 1..=last {
            if buckets[i] {
                res = res.min(i - last_idx);
                last_idx = i;
            }
        }
        res as _
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["23:59", "00:00"], 1),
        (vec!["00:00", "23:59", "00:00"], 0),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_min_difference(t.0.iter().map(|s| s.to_string()).collect());
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
