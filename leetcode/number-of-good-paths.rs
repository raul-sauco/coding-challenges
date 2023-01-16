// 2421. Number of Good Paths
// 🔴 Hard
//
// https://leetcode.com/problems/number-of-good-paths/
//
// Tags: Array - Tree - Union Find - Graph

use std::collections::{BTreeMap, HashMap};

struct Solution;
impl Solution {
    // Use the union find algorithm, we process the nodes in increasing order
    // of value by using their neighbors information to add any nodes with
    // equal or inferior values into a series of disjoint sets. Once we have
    // created the disjoint groups that contain all nodes with a given value,
    // we count the number of nodes in each group, since we know that the
    // groups only contain nodes with equal or less value, we know that there
    // is a path between any two nodes in that group.
    //
    // Time complexity: O(n*log(n)) - Inserting into the BTreeMap keeps the
    // keys (node values) sorted, the union find algorithm has amortized time
    // complexity because we are using path compression and union by rank.
    // Space complexity: O(n) - The union find structures and the other
    // dictionaries used all have a linear relation with the number of nodes
    // in the input.
    //
    // Runtime 134 ms Beats 50%
    // Memory 9.8 MB Beats 50%
    pub fn number_of_good_paths(vals: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        // A nested function that finds the representative of a disjoint set,
        // in this problem the representative consists of the lexicographically
        // smallest member of the group.
        fn find_parent(parents: &mut Vec<usize>, a: usize) -> usize {
            if a != parents[a] {
                parents[a] = find_parent(parents, parents[a]);
            }
            parents[a]
        }
        // Merge two disjoint sets into one with the lexicographically
        // smaller parent as the parent of the merged result.
        fn union(parents: &mut Vec<usize>, rank: &mut Vec<usize>, a: usize, b: usize) {
            let pa = find_parent(parents, a);
            let pb = find_parent(parents, b);
            // Join the set with the lexicographically greater parent into
            // the set with the lexicographically smaller parent.
            if rank[pa] > rank[pb] {
                parents[pb] = pa;
                rank[pa] += rank[pb];
            } else {
                parents[pa] = pb;
                rank[pb] = pa;
            }
        }
        // Base case, only one node, so one path.
        if vals.len() == 1 {
            return 1;
        }
        let n = vals.len();
        // Initialize an array of parents, each char points to itself.
        let mut parents: Vec<usize> = (0..n).into_iter().collect();
        let mut rank: Vec<usize> = vec![1; n];
        // Create an adjacency list using a hashmap.
        let mut neighbors = HashMap::new();
        for edge in edges {
            neighbors
                .entry(edge[0] as usize)
                .or_insert(vec![])
                .push(edge[1] as usize);
            neighbors
                .entry(edge[1] as usize)
                .or_insert(vec![])
                .push(edge[0] as usize);
        }
        // Create a dictionary of values to all nodes with that value.
        // Use the BTreeMap to have the structure sorted by keys.
        let mut value_to_node = BTreeMap::new();
        for (node, val) in vals.iter().enumerate() {
            value_to_node.entry(val).or_insert(vec![]).push(node);
        }
        // Iterate over all nodes on each value from smalles to largest.
        let mut good_paths = 0;
        for (&value, nodes) in value_to_node {
            // Iterate over all nodes that have this value.
            for &node in &nodes {
                // Iterate over all this node's neighbors adding the ones
                // with the same or smaller values to the disjoint set.
                for &nei in &neighbors[&node] {
                    if vals[nei] <= value {
                        union(&mut parents, &mut rank, node, nei);
                    }
                }
            }
            let mut counts = HashMap::new();
            for &node in &nodes {
                let groups = counts.entry(find_parent(&mut parents, node)).or_insert(0);
                *groups += 1;
                good_paths += *groups;
            }
        }
        good_paths
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::number_of_good_paths(vec![1], vec![]), 1,);
    assert_eq!(
        Solution::number_of_good_paths(
            vec![1, 3, 2, 1, 3],
            vec![vec![0, 1], vec![0, 2], vec![2, 3], vec![2, 4]]
        ),
        6,
    );
    assert_eq!(
        Solution::number_of_good_paths(
            vec![1, 1, 2, 2, 3],
            vec![vec![0, 1], vec![1, 2], vec![2, 3], vec![2, 4]]
        ),
        7,
    );
    println!("All tests passed!")
}
