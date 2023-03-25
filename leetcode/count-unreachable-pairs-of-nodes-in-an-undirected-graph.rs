// 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
// 🟠 Medium
//
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
//
// Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

use std::collections::HashSet;

struct Solution;
impl Solution {
    /**
     * A really nice problem, combinations and union find! The number of pairs
     * that cannot reach each other equals the total number of pairs, that can
     * be computed as C(n, 2) = n * (n-1) / 2, minus the number of pairs of
     * nodes that can reach each other, to compute the number of pairs that can
     * reach each other, we can compute the number of disjoint sets and their
     * size, for each disjoint set of size m, we can subtract the number of
     * pairs in that disjoint set C(n, 2) from the total.
     *
     * Time complexity: O(n+e) - Where n is the number of nodes (n) and e is
     * the number of edges, creating the data structures of size n requires
     * n time, as does creating the set of representatives and, in the worst
     * case, iterating over the set of representatives could be O(n), if no
     * vertices where connected (e == 0). Creating the union find structure
     * requires O(e), we iterate over all edges and do amortized O(1) work
     * for each.
     * Space complexity: O(n) - The parents and rank structures are O(n), the
     * representatives set would be O(n) is the worst case.
     *
     * Runtime 65 ms Beats 100%
     * Memory 15.6 MB Beats 100%
     */
    pub fn count_pairs(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        // Create the data structures. O(n).
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
            if pa == pb {
                return;
            }
            if rank[pb] > rank[pa] {
                return union(b, a, parents, rank);
            }
            parents[pb] = pa;
            rank[pa] += rank[pb];
        }

        // Create the disjoint set structure. O(e).
        for edge in edges {
            union(edge[0] as usize, edge[1] as usize, &mut parents, &mut rank);
        }
        // Create a set with the representatives of each disjoint group. O(n).
        let mut disjoint_sets = HashSet::<usize>::new();
        for i in 0..n {
            if !disjoint_sets.contains(&&find_parent(i, &mut parents)) {
                disjoint_sets.insert(find_parent(i, &mut parents));
            }
        }
        // Use representatives and rank to access the size of each disjoint set.
        let representatives: Vec<usize> = disjoint_sets.into_iter().collect();
        // The result is the product of the sizes of all disjoint groups
        // against all others. The naive way to compute the result would be to
        // directly apply that reasoning at O(m^2) where m is the number of
        // disjoint groups and it could be equal to n.
        // for i in 0..representatives.len() - 1 {
        //     for j in i + 1..representatives.len() {
        //         res += (rank[representatives[i]] * rank[representatives[j]]) as i64;
        //     }
        // }
        // The better way is to compute the total possible pairs in O(1).
        let mut res: i64 = n as i64 * (n as i64 - 1) / 2;
        // And subtract the connected pairs. Worst O(n).
        for representative in representatives {
            let r = rank[representative] as i64;
            res -= r * (r - 1) / 2;
        }
        res as i64
    }
}

// Tests.
fn main() {
    let tests = [
        (100000, vec![], 4999950000),
        (3, vec![vec![0, 1], vec![0, 2], vec![1, 2]], 0),
        (6, vec![vec![0, 1], vec![2, 3], vec![4, 5]], 12),
        (
            7,
            vec![vec![0, 2], vec![0, 5], vec![2, 4], vec![1, 6], vec![5, 4]],
            14,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::count_pairs(t.0, t.1), t.2);
    }
    println!("All tests passed!")
}
