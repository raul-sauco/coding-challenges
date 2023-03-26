// 2360. Longest Cycle in a Graph
// 🔴 Hard
//
// https://leetcode.com/problems/longest-cycle-in-a-graph/
//
// Tags: Depth-First Search - Graph - Topological Sort

use std::collections::HashMap;

struct Solution;
impl Solution {
    /**
     * Use depth-first search starting from every node, keep visited nodes in
     * a set to make sure we only visit each node once. Keep also a hashmap
     * of sets that we have visited along the current path pointing to the
     * position along the path at which we saw them, if we see a node that we
     * already saw in the current path, we have found a cycle, the size of
     * the cycle is the difference between the two positions at which we
     * found the current node, if we get to a node that does not have any
     * outbound edges, we can return 0 because the path will not have any
     * cycles.
     *
     * Time complexity: O(n) - We visit each node once and do O(1) work,
     * once a node is visited along one path, we will not visit it from
     * another path, if a path leads to a node that was visited already, it
     * will stop there.
     * Space complexity: O(n) - The list of visited nodes and the dictionary
     * of nodes seen along the path can both be of size n.
     *
     * Runtime 76 ms Beats 28.57%
     * Memory 7.4 MB Beats 14.29%
     */
    pub fn longest_cycle(edges: Vec<i32>) -> i32 {
        let n = edges.len();
        let mut visited = vec![false; n];
        let mut res = 0;
        // A function that explores a path starting at a given node.
        fn dfs(
            node: usize,
            pos: usize,
            visited: &mut Vec<bool>,
            path: &mut HashMap<usize, usize>,
            edges: &Vec<i32>,
        ) -> usize {
            if path.contains_key(&node) {
                return pos - path.get(&node).unwrap();
            }
            if visited[node] {
                return 0;
            }
            path.insert(node, pos);
            visited[node] = true;
            if edges[node] != -1 {
                return dfs(edges[node] as usize, pos + 1, visited, path, edges);
            }
            0
        }
        let mut path: HashMap<usize, usize>;
        for i in 0..n {
            if !visited[i] {
                path = HashMap::new();
                res = res.max(dfs(i, 0, &mut visited, &mut path, &edges));
            }
        }
        if res == 0 {
            -1
        } else {
            res as i32
        }
    }
}

// Tests.
fn main() {
    let tests = [(vec![2, -1, 3, 1], -1), (vec![3, 3, 4, 2, 3], 3)];
    for t in tests {
        assert_eq!(Solution::longest_cycle(t.0), t.1);
    }
    println!("All tests passed!")
}
