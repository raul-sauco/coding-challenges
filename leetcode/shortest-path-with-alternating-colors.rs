// 1129. Shortest Path with Alternating Colors
// 🟠 Medium
//
// https://leetcode.com/problems/shortest-path-with-alternating-colors/
//
// Tags: Breadth-First Search - Graph

struct Solution;
impl Solution {
    // Use a double ended queue and keep the information about the level and
    // the last edge color used to arrive at the node in the queue elements
    // themselves, this simplifies the algorithm.
    //
    // Time complexity: O(n) - We may visit each node once.
    // Space complexity: O(n) - There are several structures of size n.
    //
    // Runtime 3 ms Beats 85.71%
    // Memory 2.1 MB Beats 85.71%
    pub fn shortest_alternating_paths(
        n: i32,
        red_edges: Vec<Vec<i32>>,
        blue_edges: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        use std::collections::VecDeque;
        let mut adj: Vec<Vec<Vec<i32>>> = vec![vec![vec![]; n as usize], vec![vec![]; n as usize]];
        for edge in red_edges {
            adj[0][edge[0] as usize].push(edge[1]);
        }
        for edge in blue_edges {
            adj[1][edge[0] as usize].push(edge[1]);
        }
        let mut res = vec![-1; n as usize];
        res[0] = 0;
        let mut visited = vec![vec![false; 2]; n as usize];
        visited[0] = vec![true; 2];
        // A queue of vectors, each vector is [node, dist, color] where red == 0 and blue == 0
        let mut deq = VecDeque::from([(0, 0, 0), (0, 0, 1)]);
        while deq.len() > 0 {
            let (node, dist, col) = deq.pop_front().unwrap();
            let alt = if col == 0 { 1 } else { 0 };
            for neii in &adj[alt][node] {
                let nei = *neii as usize;
                if !visited[nei][alt] {
                    visited[nei][alt] = true;
                    let steps = dist + 1;
                    if res[nei] == -1 {
                        res[nei] = steps;
                    }
                    deq.push_back((nei, steps, alt));
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::shortest_alternating_paths(3, vec![vec![0, 1]], vec![vec![2, 1]]),
        vec![0, 1, -1]
    );
    assert_eq!(
        Solution::shortest_alternating_paths(3, vec![vec![0, 1]], vec![vec![1, 2]]),
        vec![0, 1, 2]
    );
    assert_eq!(
        Solution::shortest_alternating_paths(3, vec![vec![0, 1], vec![1, 2]], vec![]),
        vec![0, 1, -1]
    );
    println!("All tests passed!")
}
