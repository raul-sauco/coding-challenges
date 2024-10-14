// 2530. Maximal Score After Applying K Operations
// 🟠 Medium
//
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/
//
// Tags: Array - Greedy - Heap (Priority Queue)

use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    /// Use a heap to get the largest value in each of the k iterations. Pop the largest value and
    /// add it to the result, then push ceil(x/3) into the heap.
    ///
    /// Time complexity: O(nlog(n)) - We build the heap from the input, then pop/push k values.
    /// Space complexity: O(n) - The heap.
    ///
    /// Runtime 34 ms Beats 33%
    /// Memory 4.11 MB Beats 100%
    pub fn max_kelements(nums: Vec<i32>, k: i32) -> i64 {
        let mut score = 0;
        let mut nums = BinaryHeap::from(nums);
        for _ in 0..k {
            if let Some(val) = nums.pop() {
                score += val as i64;
                nums.push((val + 2) / 3);
            }
        }
        score
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![10, 10, 10, 10, 10], 5, 50),
        (vec![1, 10, 3, 3, 3], 3, 17),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_kelements(t.0.clone(), t.1);
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
