// 847. Shortest Path Visiting All Nodes
// 🔴 Hard
//
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/
//
// Tags: Dynamic Programming - Bit Manipulation - Breadth-First Search - Graph - Bitmask

use std::collections::VecDeque;

struct Solution;
impl Solution {
    /// Start a BFS from each node, when we pop an element, we get the set of
    /// visited nodes and the length of the path taken to get there. We use that
    /// to check the result of traveling to each of its neighbors, for each
    /// neighbor, if the path resulting of traveling there is the shortest path
    /// to that node having that set of visited nodes along it, then store that
    /// result in the dp array. The 2D dp array stores the shortest paths to
    /// each state, and it is used to avoid cycles. A state is represented by a
    /// n bits bitmask, with bits set for the nodes that we have visited along
    /// the path, and the index of the last node along that path.
    ///
    /// Time complexity: O(n*2^n) - When we pop elements from the queue, we check
    /// if we have visited the same state before, if we have, since we are doing
    /// BFS, the path would have been shorter, and we can stop exploring the
    /// current path, that means that the number of elements that we will push
    /// into the queue is capped by the size of the dp matrix.
    /// Space complexity: O(n*2^n) - The dp matrix uses the most extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.70 MB Beats 75%
    pub fn shortest_path_length(graph: Vec<Vec<i32>>) -> i32 {
        let n = graph.len();
        if n == 1 {
            return 0;
        }
        let all_visited = (1 << n) - 1;
        let mut dp = vec![vec![usize::MAX; n]; 2usize.pow(n as u32)];
        // Initialize a queue by visiting all the nodes initially.
        let mut queue = VecDeque::new();
        for i in 0..n {
            queue.push_back((1 << i, i));
            // Set the path traveled to reach that node to 0;
            dp[1 << i][i] = 0;
        }
        // Breadth-first search checking if the new path to a node is the shortest
        // that we have seen so far.
        let mut path_length: usize;
        while let Some((bm, node)) = queue.pop_front() {
            path_length = dp[bm][node] + 1;
            let mut nei: usize;
            for adj in graph[node].iter() {
                nei = *adj as usize;
                // Check if traveling to this neighbor results in the
                // shortest path with that neighbor as the end of the path and
                // the same set of visited nodes.
                let next_bm = bm | (1 << nei);
                if path_length < dp[next_bm][nei] {
                    if next_bm == all_visited {
                        return path_length as i32;
                    }
                    dp[next_bm][nei] = path_length;
                    queue.push_back((next_bm, nei));
                }
            }
        }
        unreachable!("?")
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![]], 0),
        (vec![vec![1, 2, 3], vec![0], vec![0], vec![0]], 4),
        (
            vec![vec![1], vec![0, 2, 4], vec![1, 3, 4], vec![2], vec![1, 2]],
            4,
        ),
        (
            vec![
                vec![1, 3, 4],
                vec![0, 2, 5],
                vec![1],
                vec![0],
                vec![0, 5],
                vec![1, 4, 6],
                vec![5],
            ],
            7,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::shortest_path_length(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
