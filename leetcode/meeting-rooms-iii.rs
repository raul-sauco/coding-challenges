// 2402. Meeting Rooms III
// 🔴 Hard
//
// https://leetcode.com/problems/meeting-rooms-iii/
//
// Tags: Array - Hash Table - Sorting - Heap (Priority Queue) - Simulation

use std::{cmp::Reverse, collections::BinaryHeap};

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
struct Meeting {
    start: usize,
    end: usize,
}

impl Meeting {
    fn new(start: i32, end: i32) -> Self {
        Self {
            start: start as usize,
            end: end as usize,
        }
    }
}

struct Solution;
impl Solution {
    /// Use two heaps, one with free room numbers, one with busy room numbers and the time they
    /// will be freed at. Sort the meetings and iterate over them, for each, first check if any of
    /// the rooms in the busy heap will be free by the time the meeting starts, pop them from the
    /// busy heap and add them to the free heap. After that, if there are any free rooms, use the
    /// one with the lowest number, add that room and the meeting end time to the busy heap. If
    /// there are no free rooms, wait for one, by popping the busy room that will be freed first,
    /// then push it back into the busy heap with the new end time for the meeting, computed as the
    /// time at which the room became free plus the duration of the meeting.
    ///
    /// Time complexity: O(m*log(m) + m*log(n)) - If m is the number of meetings, we sort the
    /// meetings vector at O(m*log(m)) then we iterate over the m meetings, for each, we will push
    /// and pop from two heaps of size n.
    /// Space complexity: O(m+n) - We keep a sorted copy of the meetings vector of size m, then we
    /// use two heaps of size n.
    ///
    /// Runtime 44 ms Beats 83.33%
    /// Memory 11.28 MB Beats 16.67%
    pub fn most_booked(n: i32, meetings: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut meetings = meetings
            .iter()
            .map(|v| Meeting::new(v[0], v[1]))
            .collect::<Vec<_>>();
        meetings.sort_unstable();
        let mut occupancy = vec![0; n];
        let mut free_rooms = BinaryHeap::from_iter((0..n).map(Reverse));
        let mut busy_rooms: BinaryHeap<Reverse<(usize, usize)>> = BinaryHeap::new();
        for meeting in meetings {
            // Update free rooms up to start time.
            while let Some(Reverse((end_time, _room_number))) = busy_rooms.peek() {
                if end_time <= &meeting.start {
                    if let Some(Reverse((_end_time, room_number))) = busy_rooms.pop() {
                        free_rooms.push(Reverse(room_number));
                    }
                } else {
                    break;
                }
            }
            if let Some(Reverse(free_room)) = free_rooms.pop() {
                occupancy[free_room] += 1;
                busy_rooms.push(Reverse((meeting.end, free_room)));
            } else {
                if let Some(Reverse((end_time, room_number))) = busy_rooms.pop() {
                    let duration = meeting.end - meeting.start;
                    busy_rooms.push(Reverse((end_time + duration, room_number)));
                    occupancy[room_number] += 1;
                } else {
                    unreachable!("There should always be busy rooms if there are none free");
                }
            }
        }
        occupancy
            .iter()
            .enumerate()
            .fold((0, 0), |acc, (i, &v)| if v > acc.1 { (i, v) } else { acc })
            .0 as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (2, vec![[0, 10], [1, 2], [12, 14], [13, 15]], 0),
        (2, vec![[0, 10], [1, 5], [2, 7], [3, 4]], 0),
        (3, vec![[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]], 1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::most_booked(
            t.0,
            t.1.clone().into_iter().map(|arr| arr.to_vec()).collect(),
        );
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
