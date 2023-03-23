// 1319. Number of Operations to Make Network Connected
// 🟠 Medium
//
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/
//
// Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

use std::collections::HashSet;

struct Solution;
impl Solution {
    /**
     * Use union-find to compute the number of disjoint sets and the number of
     * redundant connections at the same time in O(e+v), the number of
     * connections that we need to make is equal to the number of disjoint sets
     * minus one, if the number of redundant connections is less than that, we
     * cannot connect the network, return -1.
     *
     * Time complexity: O(v+e) - We iterate over all existing connections e to
     * create the disjoint set structure, then iterate over all vertices v to
     * compute the number of unconnected components.
     * Space complexity: O(v) - We use two extra structures that are both of
     * size v.
     *
     * Runtime 15 ms Beats 47.83%
     * Memory 5.3 MB Beats 78.26%
     */
    pub fn make_connected(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut parents = (0..n).collect::<Vec<usize>>();
        let mut rank = vec![1; n];

        /**
         * Find function with path compression. O(α(n)).
         */
        fn find_parent(a: usize, parents: &mut Vec<usize>) -> usize {
            if a != parents[a] {
                parents[a] = find_parent(parents[a], parents);
            }
            parents[a]
        }

        /**
         * A union by rank function.
         */
        fn union(a: usize, b: usize, parents: &mut Vec<usize>, rank: &mut Vec<usize>) {
            let (pa, pb) = (find_parent(a, parents), find_parent(b, parents));
            if rank[pb] > rank[pa] {
                return union(b, a, parents, rank);
            }
            parents[pb] = pa;
            rank[pa] += rank[pb];
        }

        let mut redundant_connections = 0;
        // Iterate over the edges creating the disjoint set structure.
        for connection in connections {
            if find_parent(connection[0] as usize, &mut parents)
                == find_parent(connection[1] as usize, &mut parents)
            {
                redundant_connections += 1;
            } else {
                union(
                    connection[0] as usize,
                    connection[1] as usize,
                    &mut parents,
                    &mut rank,
                );
            }
        }
        let mut disjoint_sets = HashSet::<usize>::new();
        for i in 0..n {
            if !disjoint_sets.contains(&&find_parent(i, &mut parents)) {
                disjoint_sets.insert(find_parent(i, &mut parents));
            }
        }
        if disjoint_sets.len() - 1 > redundant_connections {
            -1
        } else {
            disjoint_sets.len() as i32 - 1
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (4, vec![vec![0, 1], vec![0, 2], vec![1, 2]], 1),
        (5, vec![vec![0, 1], vec![0, 2], vec![3, 4], vec![2, 3]], 0),
        (6, vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![1, 2]], -1),
        (
            6,
            vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![1, 2], vec![1, 3]],
            2,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::make_connected(t.0, t.1), t.2);
    }
    println!("All tests passed!")
}
