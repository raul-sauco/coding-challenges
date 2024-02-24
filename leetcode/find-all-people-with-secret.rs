// 2092. Find All People With Secret
// 🔴 Hard
//
// https://leetcode.com/problems/find-all-people-with-secret/
//
// Tags: Depth-First Search - Breadth-First Search - Union Find - Graph - Sorting

use serde::{Deserialize, Serialize};
use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::fs::File;
use std::io::Read;

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
struct Meeting {
    time: usize,
    a: usize,
    b: usize,
}

struct Solution;
impl Solution {
    /// Use a variation of Dijkstra in which we use the heap to guarantee that we process the
    /// meetings in ascending order by time. We start creating an adjacency list of people pointing
    /// to the meetings that they have, then we push the two people that know the secret to the
    /// heap with 0 as the time, then we start processing the meetings, for each person we pop, the
    /// time of that meeting is the time at which they got the secret, we process all their
    /// meetings, for each meeting at the same or a later time, that other person will also gain
    /// access to the secret, we push them to the heap with the meeting time as the ordering key.
    /// This algorithm works because we process the meetings that result in a transmission of the
    /// secret in the order they happen, independently of when we push them into the heap.
    ///
    /// Time complexity: O(m*n*log(n)) - We iterate over the m meetings to create the adjacency
    /// list. Then we may push/pop a maximum of min(m,n) elements from the heap, it cannot be more
    /// than the meetings, but it can't also be more than n because each element we pop results
    /// in one of the n people gaining access to the secret.
    /// Space complexity: O(m+n) - The adjacency matrix has m entries over its n rows, the heap
    /// could grow to have m meetings.
    ///
    /// Runtime 87 ms Beats 100%
    /// Memory 15.81 MB Beats 50%
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let n = n as usize;
        let mut adj: Vec<Vec<(usize, usize)>> = vec![vec![]; n];
        let (mut a, mut b, mut time);
        for meeting in meetings {
            (a, b, time) = (
                meeting[0] as usize,
                meeting[1] as usize,
                meeting[2] as usize,
            );
            adj[a].push((b, time));
            adj[b].push((a, time));
        }
        let mut have_secret = vec![false; n];
        let mut heap = BinaryHeap::from([(Reverse(0), 0), (Reverse(0), first_person as usize)]);
        while let Some((Reverse(secret_time), person)) = heap.pop() {
            if have_secret[person] {
                continue;
            }
            have_secret[person] = true;
            for (meeting_with, meeting_at) in &adj[person] {
                if &secret_time <= meeting_at {
                    heap.push((Reverse(*meeting_at), *meeting_with));
                }
            }
        }
        have_secret
            .iter()
            .enumerate()
            .filter(|(_, &hs)| hs)
            .map(|(i, _)| i as i32)
            .collect::<Vec<_>>()
    }

    /// Use Union-Find, sort the meetings by time, then iterate over them creating disjoint groups
    /// for each value of time. When the value of time changes, keep all the elements in the group
    /// with 0 as its parent, but reset all other groups to each element being its own parent,
    /// because they "haven't received the secret" in the time slot that we just left behind.
    ///
    /// Time complexity: O(m*log(m)+m*n) - We first sort m meetings. Then we iterate over the m
    /// meetings, for each we do union-find in amortized constant time, but we may also reset the
    /// parents array of length m.
    /// Space complexity: O(m+n) - We store a vector of meetings and a vector of n parents.
    ///
    /// Runtime 204 ms Beats 50%
    /// Memory 10.02 MB Beats 100%
    #[allow(dead_code)]
    pub fn find_all_people_uf(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let n = n as usize;
        let mut parents = (0..n).collect::<Vec<_>>();
        parents[first_person as usize] = 0;
        let mut meetings = meetings
            .into_iter()
            .map(|arr| Meeting {
                a: arr[0] as usize,
                b: arr[1] as usize,
                time: arr[2] as usize,
            })
            .collect::<Vec<_>>();
        meetings.sort_unstable();
        fn find_parent(a: usize, parents: &mut Vec<usize>) -> usize {
            let mut pa = parents[a];
            while pa != parents[pa] {
                pa = parents[pa];
            }
            parents[a] = pa;
            pa
        }
        fn union(a: usize, b: usize, parents: &mut Vec<usize>) {
            let pa = find_parent(a, parents);
            let pb = find_parent(b, parents);
            // Instead of using union by size, merging under the smaller parent value serves to
            // simplify the final return just finding elements where the parent is 0.
            if pa < pb {
                parents[pb] = pa;
            } else if pb < pa {
                parents[pa] = pb;
            }
            // Do nothing if they are already the same.
        }
        fn reset_disjoint_groups(parents: &mut Vec<usize>) {
            for i in 0..parents.len() {
                if find_parent(i, parents) == 0 {
                    parents[i] = 0;
                } else {
                    parents[i] = i;
                }
            }
        }
        let mut last_timestamp = meetings[0].time;
        for meeting in meetings {
            if meeting.time != last_timestamp {
                reset_disjoint_groups(&mut parents);
                last_timestamp = meeting.time;
            }
            union(meeting.a, meeting.b, &mut parents);
        }
        reset_disjoint_groups(&mut parents);
        parents
            .iter()
            .enumerate()
            .filter(|(_, &parent)| parent == 0)
            .map(|(i, _)| i as i32)
            .collect::<Vec<_>>()
    }
}

// A struct representing the tests parsed from the JSON file.
#[derive(Debug, Serialize, Deserialize)]
struct Test {
    n: i32,
    meetings: Vec<Vec<i32>>,
    first: i32,
    expected: Vec<i32>,
}

// Tests.
fn main() {
    let file = File::open("tests.json").expect("Unable to open file");
    let mut content = String::new();
    file.take(u64::MAX)
        .read_to_string(&mut content)
        .expect("Unable to read file");
    let tests: Vec<Test> = serde_json::from_str(&content).expect("Unable to parse JSON");
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_all_people(
            t.n,
            t.meetings.clone().iter().map(|arr| arr.to_vec()).collect(),
            t.first,
        );
        if res == t.expected {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.expected, res
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
