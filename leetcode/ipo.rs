// 502. IPO
// 🔴 Hard
//
// https://leetcode.com/problems/ipo/
//
// Tags: Array - Greedy - Sorting - Heap (Priority Queue)

use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    /// We want to greedily pick the job that gives us the maximum gain out of the jobs that are
    /// available to us. We can use a heap to keep a list of jobs sorted by the capital required to
    /// start them. Have a main loop that iterates k times and does the following: First iterate
    /// over the sorted jobs vector starting at the index of the first job that we have not yet
    /// pushed into the heap, push into the heap any job for which we have enough capital,
    /// initially that will be w, but it increases with every job that we complete. Once we have
    /// all the jobs that we can embark on in the heap, we just pick the top job and increase our
    /// current capital by its net profit. If the heap is empty, it means that we cannot do any job
    /// and we can break out of the loop.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the zipped profits and capital vector has the
    /// hihgest time complexity. After that we iterate k times and do O(log(h)) work on each, where
    /// h is the size of the heap and it could be equal to n. Even though we have an inner loop
    /// that iterates over the sorted vector, that iterates over a maximum of n elements overall in
    /// the k iterations.
    /// Space complexity: O(n) - Both the sorted vector and the heap can grow to size n.
    ///
    /// Runtime 26 ms Beats 81%
    /// Memory 4.48 MB Beats 91%
    pub fn find_maximized_capital(k: i32, w: i32, profits: Vec<i32>, capital: Vec<i32>) -> i32 {
        let n = profits.len();
        let mut sorted = capital
            .into_iter()
            .zip(profits.into_iter())
            .collect::<Vec<_>>();
        sorted.sort_unstable();
        let mut idx = 0;
        let mut total = w;
        let mut heap = BinaryHeap::new();
        // Try to pick k jobs.
        for _ in 0..k {
            // Push any jobs that we could do with the current capital to the heap.
            while idx < n && sorted[idx].0 <= total {
                heap.push(sorted[idx].1);
                idx += 1;
            }
            if let Some(p) = heap.pop() {
                total += p;
            } else {
                // We still have room to pick jobs, but the capital is not enough.
                break;
            }
        }
        total
    }
}

// Tests.
fn main() {
    let tests = [
        (2, 0, vec![1, 2, 3], vec![0, 1, 1], 4),
        (3, 0, vec![1, 2, 3], vec![0, 1, 2], 6),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_maximized_capital(t.0, t.1, t.2.clone(), t.3.clone());
        if res == t.4 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.4, res
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
