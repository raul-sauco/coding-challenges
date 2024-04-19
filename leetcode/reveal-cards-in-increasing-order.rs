// 950. Reveal Cards In Increasing Order
// 🟠 Medium
//
// https://leetcode.com/problems/reveal-cards-in-increasing-order/
//
// Tags: Array - Queue - Sorting - Simulation

use std::collections::{BinaryHeap, VecDeque};

struct Solution;
impl Solution {
    /// We can simulate popping the cards in sorted order but in reverse to solve the problem.
    ///
    /// Time complexity: O(n) - We pop n elements from the heap at a log(n) cost each.
    /// Space complexity: O(n) - Both the double ended queue and the binary heap will be size n at
    /// some point.
    ///
    /// Runtime 1 ms Beats 83%
    /// Memory 2.10 MB Beats 83%
    pub fn deck_revealed_increasing(deck: Vec<i32>) -> Vec<i32> {
        let mut queue = VecDeque::with_capacity(deck.len());
        let mut heap = BinaryHeap::from(deck);
        while let Some(num) = heap.pop() {
            if let Some(back) = queue.pop_back() {
                queue.push_front(back);
            }
            queue.push_front(num);
        }
        queue.into_iter().collect()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![17, 13, 11, 2, 3, 5, 7], vec![2, 13, 3, 11, 5, 17, 7]),
        (vec![1, 1000], vec![1, 1000]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::deck_revealed_increasing(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
