// 547. Number of Provinces
// 🟠 Medium
//
// https://leetcode.com/problems/number-of-provinces/
//
// Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

use std::collections::HashSet;

struct Solution {}
impl Solution {
    /// Use union find to create a DSU structure, the number of disjoint
    /// components is the number of provinces.
    ///
    /// Time complexity: O(n^2) - We iterate over every pair of values i and j
    /// and, when connected, we add them to the DSU in amortized O(1) time.
    /// Space complexity: O(n) - Both the parents and rank arrays are of size
    /// n, is_connected is given as an input parameter.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.2 MB Beats 80.65%
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        let n = is_connected.len();
        let mut parents = (0..n).into_iter().collect::<Vec<usize>>();
        let mut rank = vec![1; n];
        fn find_parent(i: usize, parents: &mut Vec<usize>) -> usize {
            if parents[i] != i {
                parents[i] = find_parent(parents[i], parents);
            }
            parents[i]
        }
        fn union(a: usize, b: usize, parents: &mut Vec<usize>, rank: &mut Vec<usize>) {
            let pa = find_parent(a, parents);
            let pb = find_parent(b, parents);
            if rank[pa] > rank[pb] {
                parents[pb] = pa;
                rank[pa] += rank[pb];
            } else {
                parents[pa] = pb;
                rank[pb] += rank[pa];
            }
        }
        for i in 0..n {
            for j in i + 1..n {
                if is_connected[i][j] == 1
                    && find_parent(i, &mut parents) != find_parent(j, &mut parents)
                {
                    union(i, j, &mut parents, &mut rank);
                }
            }
        }
        (0..n)
            .map(|x| find_parent(x, &mut parents))
            .collect::<HashSet<usize>>()
            .len() as i32
    }
}

fn main() {
    let tests = [
        (vec![vec![1, 1, 0], vec![1, 1, 0], vec![0, 0, 1]], 2),
        (vec![vec![1, 0, 0], vec![0, 1, 0], vec![0, 0, 1]], 3),
    ];
    for t in tests {
        assert_eq!(Solution::find_circle_num(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
