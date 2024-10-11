// 1942. The Number of the Smallest Unoccupied Chair
// 🟠 Medium
//
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/
//
// Tags: Array - Hash Table - Heap (Priority Queue)

use std::{cmp::Reverse, collections::BinaryHeap, i32};

struct Solution;
impl Solution {
    /// One way to solve this is to use priority queues, one for the arrival times of the friends,
    /// one for the friends currently using a chair sorted by the time at which they will leave,
    /// and one more for the chairs that are currently free, because we want the one with the
    /// lowest id. When a friend arrive, first pop any friends from the departure heap that will
    /// have left by the time this new arrival gets to the party, and add their chairs to the free
    /// chairs heap. Then get the lowest id amosgst the free chairs, either from the vacated chairs
    /// heap or the next yet unused chair and push that into the currently here heap. When we find
    /// the target friend, return its chair number.
    ///
    /// Time complexity: O(nlog(n)) - Sorting the arrivals, popping them from the heap, and pushing
    /// and popping into the departures and free chairs heaps.
    /// Space complexity: O(n) - The heaps, arrivals starts at size n, departures can also grow to
    /// size n.
    ///
    /// Runtime 21 ms Beats 80%
    /// Memory 3.06 MB Beats 60%
    pub fn smallest_chair(times: Vec<Vec<i32>>, target_friend: i32) -> i32 {
        let mut arrivals = times
            .into_iter()
            .enumerate()
            .map(|(i, v)| (Reverse(v[0]), v[1], i as i32))
            .collect::<BinaryHeap<_>>();
        let mut departures: BinaryHeap<(Reverse<i32>, i32)> = BinaryHeap::new();
        let mut vacated_chairs: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut next_chair = 0;
        while let Some((in_time, out_time, id)) = arrivals.pop() {
            while let Some((departure_time, vacated_chair)) = departures.peek() {
                if in_time.0 >= departure_time.0 {
                    vacated_chairs.push(Reverse(*vacated_chair));
                    departures.pop();
                } else {
                    break;
                }
            }
            let chair;
            if let Some(vacated_chair) = vacated_chairs.pop() {
                chair = vacated_chair.0;
            } else {
                chair = next_chair;
                next_chair += 1;
            }
            if id == target_friend {
                return chair;
            }
            departures.push((Reverse(out_time), chair));
        }
        unreachable!()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1, 4], vec![2, 3], vec![4, 6]], 1, 1),
        (vec![vec![3, 10], vec![1, 5], vec![2, 6]], 0, 2),
        (
            vec![
                vec![33889, 98676],
                vec![80071, 89737],
                vec![44118, 52565],
                vec![52992, 84310],
                vec![78492, 88209],
                vec![21695, 67063],
                vec![84622, 95452],
                vec![98048, 98856],
                vec![98411, 99433],
                vec![55333, 56548],
                vec![65375, 88566],
                vec![55011, 62821],
                vec![48548, 48656],
                vec![87396, 94825],
                vec![55273, 81868],
                vec![75629, 91467],
            ],
            6,
            2,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::smallest_chair(t.0.clone(), t.1);
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
