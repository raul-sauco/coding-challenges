// 1377. Frog Position After T Seconds
// 🔴 Hard
//
// https://leetcode.com/problems/frog-position-after-t-seconds/
//
// Tags: Tree - Depth-First Search - Breadth-First Search - Graph

use std::collections::VecDeque;

struct Solution;
impl Solution {
    /// Construct an adjacency list given the edges, then BFS over t levels or until we get to the
    /// target if it is a leave, for each node, store the probablility of landing there and
    /// distribute it equally between its children.
    ///
    /// Time complexity: O(e+n) - We iterate over the e edges to construct the adjacency list,
    /// then we iterate t times popping all the elements in the current level. Even though this is
    /// nested t*n, the maximum overall in t iterations is n nodes because we can't go back to a
    /// visited node. Inside we also iterate over the list of edges for the given node, but that is
    /// limited to a maximum of e edges overall.
    /// Space complexity: O(e+n) - We store all the edges in the adjacency list, and have n entries
    /// in the visited vector. The queue can also grow to size n, if all the nodes were in the same
    /// level, which in a tree is limited to n/2 + 1.
    ///
    /// Runtime 3 ms Beats 66.67%
    /// Memory 2.23 MB Beats 66.67%
    pub fn frog_position(n: i32, edges: Vec<Vec<i32>>, t: i32, target: i32) -> f64 {
        let n = n as usize + 1;
        let target = target as usize;
        let mut adj = vec![vec![]; n];
        for edge in edges {
            adj[edge[0] as usize].push(edge[1] as usize);
            adj[edge[1] as usize].push(edge[0] as usize);
        }
        let mut visited = vec![false; n];
        let mut queue = VecDeque::from([(1, 1.0)]);
        for current_time in 0..t {
            for _ in 0..queue.len() {
                if let Some((node, prob)) = queue.pop_front() {
                    visited[node] = true;
                    let neighbors = adj[node]
                        .iter()
                        .filter(|&&x| !visited[x])
                        .collect::<Vec<_>>();
                    if neighbors.len() == 0 && node == target {
                        return prob;
                    }
                    let nei_prob = prob / neighbors.len() as f64;
                    for &nei in neighbors {
                        if current_time == t - 1 && nei == target {
                            return nei_prob;
                        }
                        queue.push_back((nei, nei_prob));
                    }
                }
            }
        }
        0.0
    }
}

// Tests.
fn main() {
    let tests = [
        (3, vec![[2, 1], [3, 2]], 1, 2, 1.0),
        (
            7,
            vec![[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            2,
            4,
            0.16667,
        ),
        (
            7,
            vec![[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            1,
            7,
            0.33333,
        ),
        (
            8,
            vec![[2, 1], [3, 2], [4, 1], [5, 1], [6, 4], [7, 1], [8, 7]],
            7,
            7,
            0.0,
        ),
        (
            7,
            vec![[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]],
            20,
            6,
            0.16667,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res =
            Solution::frog_position(t.0, t.1.iter().map(|arr| arr.to_vec()).collect(), t.2, t.3);
        if (res - t.4).abs() < 0.00001 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.4, res
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
