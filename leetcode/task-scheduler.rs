// 621. Task Scheduler
// 🟠 Medium
//
// https://leetcode.com/problems/task-scheduler/
//
// Tags: Array - Hash Table - Greedy - Sorting - Heap (Priority Queue) - Counting

use std::collections::{BinaryHeap, VecDeque};

#[derive(Debug, Ord, PartialOrd, PartialEq, Eq)]
struct Task {
    cycles: i32,
    id: char,
}

struct Solution;
impl Solution {
    /// Simulate a scheduler, have a heap to pick the task that needs to run in the current cycle
    /// by choosing the task with the most cycles left, then a queue to push tasks into to cool
    /// down.
    ///
    /// Time complexity: O(m) - Where m is the number of cpu cycles that we will use, we are
    /// simulating the cpu and processing each task.
    /// Space complexity: O(1) - We have one task for each ID and the id count is limited to 26.
    ///
    /// Runtime 26 ms Beats 44%
    /// Memory 2.56 MB Beats 100%
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        if n == 0 {
            return tasks.len() as i32;
        }
        let mut counts = vec![0; 26];
        let base = b'A';
        for c in tasks {
            counts[(c as u8 - base) as usize] += 1;
        }
        let mut heap = BinaryHeap::new();
        for (i, count) in counts.into_iter().enumerate() {
            if count > 0 {
                heap.push(Task {
                    cycles: count,
                    id: (base + i as u8) as char,
                });
            }
        }
        let mut queue: VecDeque<(i32, Task)> = VecDeque::new();
        let mut time = 0;
        while !queue.is_empty() || !heap.is_empty() {
            if let Some(first) = queue.front() {
                if first.0 == time {
                    let (_timeout, task) = queue.pop_front().unwrap();
                    heap.push(task);
                }
            }
            time += 1;
            // Process the task with the most cycles left.
            if let Some(mut task) = heap.pop() {
                task.cycles -= 1;
                if task.cycles > 0 {
                    queue.push_back((time + n, task));
                }
            }
        }
        time
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!['A', 'A', 'A', 'B', 'B', 'B'], 2, 8),
        (vec!['A', 'C', 'A', 'B', 'D', 'B'], 1, 6),
        (vec!['A', 'A', 'A', 'B', 'B', 'B'], 3, 10),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::least_interval(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.2, res
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
