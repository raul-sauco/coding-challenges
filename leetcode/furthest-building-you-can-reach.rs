// 1642. Furthest Building You Can Reach
// 🟠 Medium
//
// https://leetcode.com/problems/furthest-building-you-can-reach/
//
// Tags: Array - Greedy - Heap (Priority Queue)

use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    /// Iterate over the input, greedily use ladders saving the gap sizes we bridge using ladders
    /// in a heap, once we run out of ladders, every time we see a positive height gain, compare
    /// with the top of the heap, if the top of the heap is smaller, pretend we used bricks to save
    /// that gap and we still have one ladder to bridge the current one, until we run out of
    /// bricks.
    ///
    /// Time complexity: O(n*log(n)) - We visit each element in the input, for each, we may push
    /// and pop from the heap in O(log(n))
    /// Space complexity: O(l) - The heap can have as many entries as the number of ladders.
    ///
    /// Runtime 7 ms Beats 100%
    /// Memory 2.99 MB Beats 100%
    pub fn furthest_building(heights: Vec<i32>, bricks: i32, ladders: i32) -> i32 {
        let n = heights.len();
        if n < 2 {
            return 0;
        }
        let mut ladders = ladders;
        let mut bricks = bricks;
        let mut heap: BinaryHeap<Reverse<i32>> = BinaryHeap::with_capacity(ladders as usize + 1);
        let mut height_difference;
        for i in 1..n {
            height_difference = heights[i] - heights[i - 1];
            if height_difference <= 0 {
                continue;
            }
            // Greedily use all the ladders.
            if ladders > 0 {
                heap.push(Reverse(height_difference));
                ladders -= 1;
            } else {
                // Out of ladders, pretend that we used bricks to span the shortest gap so far.
                if let Some(Reverse(top)) = heap.peek() {
                    if *top < height_difference {
                        heap.push(Reverse(height_difference));
                        height_difference = heap.pop().unwrap().0;
                    }
                }
                if height_difference > bricks {
                    return i as i32 - 1;
                }
                bricks -= height_difference;
            }
        }
        n as i32 - 1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![14, 3, 19, 3], 17, 0, 3),
        (vec![4, 2, 7, 6, 9, 14, 12], 5, 1, 4),
        (vec![4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::furthest_building(t.0.clone(), t.1, t.2);
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
