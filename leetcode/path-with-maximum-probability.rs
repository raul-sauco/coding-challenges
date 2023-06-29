// 1514. Path with Maximum Probability
// 🟠 Medium
//
// https://leetcode.com/problems/path-with-maximum-probability/
//
// Tags: Array - Graph - Heap (Priority Queue) - Shortest Path

use std::collections::BinaryHeap;

// Deal with f64 not supporting Ord in Rust.
#[derive(PartialEq)]
struct SortableF64(f64);

impl PartialOrd for SortableF64 {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        self.0.partial_cmp(&other.0)
    }
}

impl Ord for SortableF64 {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.partial_cmp(other).unwrap()
    }
}

impl Eq for SortableF64 {}

struct Solution;
impl Solution {
    /// Use Dijkstra's algorithm with a modification, the total path weight is
    /// not the sum of the edge weights, instead, it is the product of the
    /// probabilities of the edges along the path. Instead of visiting first
    /// the nodes with the least weight, as we usually do for the shortest path
    /// we will visit the nodes with the highest probability.
    ///
    /// Time complexity: O(n+e*log(n)) - We start visiting all edges to build
    /// the adjacency list, then we may end up visiting each edge and pushing
    /// popping it from the binary heap.
    /// Space complexity: O(n+e) - The adjacency list has an entry per edge,
    /// the heap can do as well. The vector of maximum probabilities has an
    /// entry per node.
    ///
    /// Runtime 27 ms Beats 50%
    /// Memory 5.1 MB Beats 88.24%
    pub fn max_probability(
        n: i32,
        edges: Vec<Vec<i32>>,
        succ_prob: Vec<f64>,
        start: i32,
        end: i32,
    ) -> f64 {
        let n = n as usize;
        let start = start as usize;
        let end = end as usize;
        let mut adj = vec![vec![]; n];
        for i in 0..edges.len() {
            let a = edges[i][0] as usize;
            let b = edges[i][1] as usize;
            adj[a].push((b, succ_prob[i]));
            adj[b].push((a, succ_prob[i]));
        }
        let mut heap: BinaryHeap<(SortableF64, usize)> =
            BinaryHeap::from(vec![(SortableF64(1.0), start)]);
        let mut max_prob_to_node = vec![0.0; n];
        max_prob_to_node[start] = 1.0;
        while let Some((SortableF64(cur_prob), cur)) = heap.pop() {
            if cur == end {
                return cur_prob;
            }
            for (nei, edge_prob) in &adj[cur] {
                let next_prob = cur_prob * edge_prob;

                if next_prob > max_prob_to_node[*nei] {
                    max_prob_to_node[*nei] = next_prob;
                    heap.push((SortableF64(next_prob), *nei));
                }
            }
        }
        0.0000
    }
}

// Tests.
fn main() {
    let tests = [
        (
            3,
            vec![vec![0, 1], vec![1, 2], vec![0, 2]],
            vec![0.5, 0.5, 0.2],
            0,
            2,
            0.25000,
        ),
        (
            3,
            vec![vec![0, 1], vec![1, 2], vec![0, 2]],
            vec![0.5, 0.5, 0.3],
            0,
            2,
            0.30000,
        ),
        (3, vec![vec![0, 1]], vec![0.5], 0, 2, 0.00000),
    ];
    for t in tests {
        assert_eq!(Solution::max_probability(t.0, t.1, t.2, t.3, t.4), t.5);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
