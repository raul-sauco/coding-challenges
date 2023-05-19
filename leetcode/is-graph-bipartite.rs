// 785. Is Graph Bipartite?
// 🟠 Medium
//
// https://leetcode.com/problems/is-graph-bipartite/
//
// Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

use std::collections::VecDeque;

struct Solution;

#[derive(Clone, Debug)]
enum State {
    Unvisited,
    Red,
    Blue,
}

/// Use a vector with the state of the nodes, they can be unvisited yet, or
/// belong to one of two groups. We are guaranteed to have, at least, one node,
/// start by visiting that one, node 0, and travel recursively to all the
/// neighbors using breadth-first search, any neighbor of a node needs to be in
/// the opposite group, if we ever find two neighbors in the same group, return
/// false. If we ever run out of nodes in the queue, check to see if we have
/// any unvisited nodes, enqueue them and start again.
///
/// Time complexity: O(n+e) - We may travel n nodes at most to find all unique
/// disjoint components, for each component, we will travel, at most, n nodes
/// using breadth-first search. For each node visited, we will explore all its
/// edges, when they lead to an unvisited node, we will add it to the queue.
/// Space complexity: O(n) - The queue can hold one entry per node, the vector
/// of groups is size n.
///
/// Runtime 0 ms Beats 100%
/// Memory 2.2 MB Beats 50%
impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
        let mut nodes: Vec<State> = vec![State::Unvisited; graph.len()];
        let mut next_unvisited = 1;
        // Use a FIFO for BFS.
        let mut q = VecDeque::new();
        // Enqueue the first node and make it "red".
        q.push_back(0);
        nodes[0] = State::Red;
        while let Some(n) = q.pop_front() {
            for nei in graph[n].iter() {
                let nei = *nei as usize;
                match nodes[nei] {
                    State::Unvisited => {
                        q.push_back(nei);
                        match nodes[n] {
                            State::Unvisited => unreachable!(),
                            State::Red => nodes[nei] = State::Blue,
                            State::Blue => nodes[nei] = State::Red,
                        }
                    }
                    State::Red => match nodes[n] {
                        State::Unvisited => unreachable!(),
                        State::Red => return false,
                        State::Blue => {}
                    },
                    State::Blue => match nodes[n] {
                        State::Unvisited => unreachable!(),
                        State::Red => {}
                        State::Blue => return false,
                    },
                }
            }
            // If the queue is empty, check if we have any unvisited nodes.
            while q.is_empty() && next_unvisited < graph.len() {
                match nodes[next_unvisited] {
                    State::Unvisited => {
                        q.push_back(next_unvisited);
                        nodes[next_unvisited] = State::Red;
                    }
                    State::Red | State::Blue => {}
                }
                next_unvisited += 1;
            }
        }
        // If we got here, the graph is bipartite.
        true
    }
}

// Tests.
fn main() {
    let tests = vec![
        (vec![vec![1, 3], vec![0, 2], vec![1, 3], vec![0, 2]], true),
        (vec![vec![4], vec![], vec![4], vec![4], vec![0, 2, 3]], true),
        (
            vec![vec![1, 2, 3], vec![0, 2], vec![0, 1, 3], vec![0, 2]],
            false,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::is_bipartite(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
