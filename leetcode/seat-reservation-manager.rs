// 1845. Seat Reservation Manager
// 🟠 Medium
//
// https://leetcode.com/problems/seat-reservation-manager/
//
// Tags: Design - Heap (Priority Queue)

use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct SeatManager {
    pool: BinaryHeap<Reverse<i32>>,
    last: i32,
}

/// We can use a heap with n elements, to optimize the memory efficiency, we can
/// store in the heap only elements that have been unreserved, and keep a pointer
/// to the next element that has not been reserved yet. If there are no elements
/// in the heap, we return the next unused seat number, if there are elements in
/// the heap, we know that they will be smaller than the next unreserved number,
/// and return the smallest element in the heap.
///
/// Time complexity: O(n*log(n)) - Worst case we end up with a heap of size n
/// and each push/pop costs log(n). When the heap is empty, reserve is O(1).
/// Space complexity: O(n) - Worst case scenario the heap fills up to size n.
///
/// Runtime 62 ms Beats 100%
/// Memory 27.96 MB Beats 100%
impl SeatManager {
    fn new(_n: i32) -> Self {
        // If this was not a Leetcode problem where they guarantee they will not
        // call reserve when there are no seats, we would want to keep track of n
        // and return "no seats" when we are out.
        SeatManager {
            pool: BinaryHeap::new(),
            last: 0,
        }
    }

    fn reserve(&mut self) -> i32 {
        match self.pool.pop() {
            Some(s) => s.0,
            None => {
                self.last += 1;
                self.last
            }
        }
    }

    fn unreserve(&mut self, seat_number: i32) {
        self.pool.push(Reverse(seat_number));
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * let obj = SeatManager::new(n);
 * let ret_1: i32 = obj.reserve();
 * obj.unreserve(seatNumber);
 */

// Tests.
fn main() {
    let mut sm = SeatManager::new(5);
    assert_eq!(sm.reserve(), 1);
    assert_eq!(sm.reserve(), 2);
    sm.unreserve(2);
    assert_eq!(sm.reserve(), 2);
    assert_eq!(sm.reserve(), 3);
    assert_eq!(sm.reserve(), 4);
    assert_eq!(sm.reserve(), 5);
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
