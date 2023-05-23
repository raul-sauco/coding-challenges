// 703. Kth Largest Element in a Stream
// 🟢 Easy
//
// https://leetcode.com/problems/kth-largest-element-in-a-stream/
//
// Tags: Tree - Design - Binary Search Tree - Heap (Priority Queue) - Binary Tree
// - Data Stream

use std::collections::BinaryHeap;

/// Use a binary heap, we can construct the heap with the given elements in
/// O(n), if we have been given more than k elements pop the extra ones at
/// O(log(n)) cost each. Then, for each addition, if it is greater than the
/// smaller element in the heap, push, then pop, and return the smallest
/// element. We can negate all values to have the smallest value be the top of
/// the heap and be able to access it in O(1), instead, if we had a data type
/// that had a more complex compare, we could use Rust's reverse ordering.
///
/// Time complexity: O(log(k)*n) - We use a heap of max size k, after we
/// construct the heap with the initial elements, we push and pop a maximum of
/// n elements.
/// Space complexity: O(k) - The size of the binary heap.
///
/// Runtime 9 ms Beats 71.43%
/// Memory 6.6 MB Beats 92.86%
struct KthLargest {
    pq: BinaryHeap<i32>,
    size: usize,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut pq = BinaryHeap::from(nums.into_iter().map(|x| -x).collect::<Vec<i32>>());
        let k = k as usize;
        while pq.len() > k {
            pq.pop();
        }
        KthLargest { pq: pq, size: k }
    }

    fn add(&mut self, val: i32) -> i32 {
        // Work with negative values to have a min heap.
        let val = -val;
        if self.pq.len() < self.size || val < *self.pq.peek().unwrap() {
            self.pq.push(val);
            if self.pq.len() > self.size {
                self.pq.pop();
            }
        }
        -self.pq.peek().unwrap()
    }
}
// Tests.
fn main() {
    let mut pq = KthLargest::new(3, vec![4, 5, 8, 2]);
    assert_eq!(pq.add(3), 4);
    assert_eq!(pq.add(5), 5);
    assert_eq!(pq.add(10), 5);
    assert_eq!(pq.add(9), 8);
    assert_eq!(pq.add(4), 8);
    let mut pq2 = KthLargest::new(2, vec![0]);
    assert_eq!(pq2.add(-1), -1);
    assert_eq!(pq2.add(1), 0);
    assert_eq!(pq2.add(-2), 0);
    assert_eq!(pq2.add(-4), 0);
    assert_eq!(pq2.add(3), 1);
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
