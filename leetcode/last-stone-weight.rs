// 1046. Last Stone Weight
//🟢 Easy
//
// https://leetcode.com/problems/last-stone-weight/
//
// Tags: Array - Heap (Priority Queue)

use std::collections::BinaryHeap;

struct Solution;
impl Solution {
    /// Put the stones into a max heap, while the heap has more than one stone
    /// remaining in it, pop the two bigger stones and compute the result of the
    /// biggest one minus the second biggest one, if the result is > 0, push
    /// that result back into the heap.
    ///
    /// Time complexity: O(log(n) * n) - Each pop and push from the heap takes
    /// log(n) and each two pops reduces the size of the heap by one or two.
    /// Space complexity: O(n) - The heap has the same size as the input array
    /// initially.
    ///
    /// Runtime 1 ms Beats 72.73%
    /// Memory 2 MB Beats 81.82%
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut stones = BinaryHeap::from(stones);
        let mut rem;
        while stones.len() > 1 {
            rem = stones.pop().unwrap() - stones.pop().unwrap();
            if rem > 0 {
                stones.push(rem);
            }
        }
        match stones.pop() {
            Some(val) => val,
            None => 0,
        }
    }
}

// Tests.
fn main() {
    let tests = [(vec![1], 1), (vec![4, 4], 0), (vec![2, 7, 4, 1, 8, 1], 1)];
    for t in tests {
        assert_eq!(Solution::last_stone_weight(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m");
}
