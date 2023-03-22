// 2492. Minimum Score of a Path Between Two Cities
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
//
// Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

use std::cmp::min;

struct Solution;
impl Solution {
    /**
     * Use a modified version of union find that, each time that connects
     * components, it also keeps the value of the min value edge that has
     * been seen between the two components that are being connected and the
     * new edge that is being added, then return the minimum edge of the
     * set that contains node 1, since we are guaranteed that 1 and n are
     * connected, this set also contains n.
     *
     * Time Complexity: O(e) - Where e is the number of edges, we iterate
     * over the edges and, for each, we do a union operation that runs in
     * amortized O(1) time.
     * Space complexity: O(n) - Where n is the number of nodes, we have three
     * structures of size n.
     *
     * Runtime 29 ms Beats 100%
     * Memory 10.4 MB Beats 100%
     */
    pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut parents = (0..n + 1).collect::<Vec<usize>>();
        let mut rank = vec![1; n + 1];
        let mut scores = vec![usize::MAX; n + 1];

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
        fn union(
            a: usize,
            b: usize,
            dist: usize,
            parents: &mut Vec<usize>,
            rank: &mut Vec<usize>,
            scores: &mut Vec<usize>,
        ) {
            let (pa, pb) = (find_parent(a, parents), find_parent(b, parents));
            if rank[pb] > rank[pa] {
                return union(b, a, dist, parents, rank, scores);
            }
            parents[pb] = pa;
            rank[pa] += rank[pb];
            scores[pa] = min(dist, min(scores[pa], scores[pb]));
        }

        // Iterate over the edges creating the disjoint set structure.
        for road in roads {
            union(
                road[0] as usize,
                road[1] as usize,
                road[2] as usize,
                &mut parents,
                &mut rank,
                &mut scores,
            );
        }
        scores[find_parent(1, &mut parents)] as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (4, vec![vec![1, 2, 2], vec![1, 3, 4], vec![3, 4, 7]], 2),
        (
            4,
            vec![vec![1, 2, 9], vec![2, 3, 6], vec![2, 4, 5], vec![1, 4, 7]],
            5,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::min_score(t.0, t.1), t.2);
    }
    println!("All tests passed!")
}
