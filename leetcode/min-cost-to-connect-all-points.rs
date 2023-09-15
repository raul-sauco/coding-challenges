// 1584. Min Cost to Connect All Points
// 🟠 Medium
//
// https://leetcode.com/problems/min-cost-to-connect-all-points/
//
// Tags: Array - Union Find - Graph - Minimum Spanning Tree

use std::collections::{BinaryHeap, HashSet};

struct Solution;
impl Solution {
    /// Use Prim's algorithm to find the minimum spanning tree.
    ///
    /// Time complexity: O(n^2) - For each vertex that we visit, we compute the
    /// distance to all remaining unvisited nodes.
    /// Space complexity: O(n^2) - The heap could hold edges between all nodes
    /// in the graph.
    ///
    /// Runtime 27 ms Beats 54.55%
    /// Memory 13.69 MB Beats 50.00%
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut visited = vec![false; n];
        let mut heap = BinaryHeap::new();
        let mut to_visit = n;
        let mut cost = 0;
        heap.push((0, 0));
        while to_visit > 0 {
            if let Some((dist, src)) = heap.pop() {
                if visited[src] {
                    continue;
                }
                to_visit -= 1;
                visited[src] = true;
                cost -= dist;
                for dest in 0..n {
                    if !visited[dest] {
                        let dist = (points[src][0] - points[dest][0]).abs()
                            + (points[src][1] - points[dest][1]).abs();
                        heap.push((-dist, dest));
                    }
                }
            } else {
                unreachable!("The graph is guaranteed to be connected");
            }
        }
        cost
    }

    /// Use Prim's algorithm to find the minimum spanning tree. This solution
    /// differs from the previous one in that it uses a hashmap to keep track of
    /// unvisited nodes, it has the advantage that we can iterate over only the
    /// unvisited nodes in the inner loop, instead of iterating over all nodes
    /// and then checking if they have been already visited. It has the
    /// disadvantage that accessing elements in a vector is faster and, in the
    /// online judge, this solution is slower.
    ///
    /// Time complexity: O(n^2) - For each vertex that we visit, we compute the
    /// distance to all remaining unvisited nodes.
    /// Space complexity: O(n^2) - The heap could hold edges between all nodes
    /// in the graph.
    ///
    /// Runtime 36 ms Beats 45.45%
    /// Memory 13.84 MB Beats 40.91%
    pub fn min_cost_connect_points_2(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut unvisited: HashSet<usize> = (0..n).collect();
        let mut heap = BinaryHeap::new();
        let mut cost = 0;
        heap.push((0, 0));
        while !unvisited.is_empty() {
            if let Some((dist, src)) = heap.pop() {
                if !unvisited.remove(&src) {
                    continue;
                }
                // unvisited.remove(src);
                cost -= dist;
                for dest in unvisited.iter() {
                    let dist = (points[src][0] - points[*dest][0]).abs()
                        + (points[src][1] - points[*dest][1]).abs();
                    heap.push((-dist, *dest));
                }
            } else {
                unreachable!("The graph is guaranteed to be connected");
            }
        }
        cost
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![3, 12], vec![-2, 5], vec![-4, 1]], 18),
        (
            vec![vec![0, 0], vec![2, 2], vec![3, 10], vec![5, 2], vec![7, 0]],
            20,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::min_cost_connect_points(t.0.clone()), t.1);
        assert_eq!(Solution::min_cost_connect_points_2(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
