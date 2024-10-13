// 632. Smallest Range Covering Elements from K Lists
// 🔴 Hard
//
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
//
// Tags: Array - Hash Table - Greedy - Sliding Window - Sorting - Heap (Priority Queue)

use std::{cmp::Reverse, collections::BinaryHeap, i32};

struct Solution;
impl Solution {
    /// Use a heap with one value from each list to keep track of ranges, keep track of the largest
    /// value in the heap manually. Keep popping the top of the heap and pushing the next value
    /// from the same list, for each pop, recompute the current range of values and, if it is
    /// strictly smaller than the current smallest, update the result.
    ///
    /// Time complexity: O(nlog(k)) - We use a heap of size k where we may push all the values in
    /// all the lists in nums. Each push/pop is log(k).
    /// Space complexity: O(K) - Where k is the number of lists in nums, we push one value per list
    /// into the heap.
    ///
    /// Runtime 9 ms Beats 84%
    /// Memory 2.74 MB Beats 92%
    pub fn smallest_range(nums: Vec<Vec<i32>>) -> Vec<i32> {
        // A heap with value, list index and item index.
        let mut heap: BinaryHeap<(Reverse<i32>, usize, usize)> = BinaryHeap::new();
        // Keep track of the largest value in the heap.
        let mut largest = i32::MIN;
        for (idx, list) in nums.iter().enumerate() {
            largest = largest.max(list[0]);
            heap.push((Reverse(list[0]), idx, 1));
        }
        // Initialize res with the initial values in the heap.
        let mut res = (heap.peek().expect("Non-empty heap").0 .0, largest);
        while let Some((_, list_idx, item_index)) = heap.pop() {
            // Base case, we are out of items on this list.
            if nums[list_idx].len() <= item_index {
                break;
            }
            let num = nums[list_idx][item_index];
            largest = largest.max(num);
            heap.push((Reverse(num), list_idx, item_index + 1));
            let top = heap.peek().expect("A top value").0 .0;
            if largest - top < res.1 - res.0 {
                res = (top, largest);
            }
        }
        vec![res.0, res.1]
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![
                vec![4, 10, 15, 24, 26],
                vec![0, 9, 12, 20],
                vec![5, 18, 22, 30],
            ],
            vec![20, 24],
        ),
        (
            vec![vec![1, 2, 3], vec![1, 2, 3], vec![1, 2, 3]],
            vec![1, 1],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::smallest_range(t.0.clone());
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
