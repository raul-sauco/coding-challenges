// 1361. Validate Binary Tree Nodes
// 🟠 Medium
//
// https://leetcode.com/problems/validate-binary-tree-nodes/
//
// Tags: Tree - Depth-First Search - Breadth-First Search - Union Find - Graph - Binary Tree

struct Solution;
impl Solution {
    /// Iterate over all the nodes, set children and parents as part of the same
    /// disjoint component. When we Union two nodes, if they are already part of
    /// the same component, we have a cycle, if a children has a parent different
    /// to the one we are trying to assign, a node has more than one parent, so
    /// the structure is not a tree.
    ///
    /// Time complexity: O(αn) - Amortized O(n) time, Union find with path
    /// compression.
    /// Space complexity: O(n) - The parents vector is of size n.
    ///
    /// Runtime 3 ms Beats 100%
    /// Memory 2.41 MB Beats 100%
    pub fn validate_binary_tree_nodes(n: i32, left_child: Vec<i32>, right_child: Vec<i32>) -> bool {
        let n = n as usize;
        let mut components = n;
        let mut parents: Vec<usize> = (0..n).collect();
        fn find_parent(parents: &mut Vec<usize>, a: usize) -> usize {
            if a != parents[a] {
                parents[a] = find_parent(parents, parents[a]);
            }
            parents[a]
        }

        fn union(parents: &mut Vec<usize>, parent: usize, child: usize) -> bool {
            let pp = find_parent(parents, parent);
            let cp = find_parent(parents, child);
            // If we have already processed this child or they are in the same
            // component already.
            if cp != child || pp == cp {
                return false;
            }
            parents[cp] = pp;
            true
        }

        for i in 0..n {
            for child in [left_child[i], right_child[i]] {
                if child == -1 {
                    continue;
                }
                if !union(&mut parents, i, child as usize) {
                    return false;
                }
                components -= 1;
            }
        }
        components == 1
    }
}

// Tests.
fn main() {
    let tests = [
        (2, vec![1, 0], vec![-1, -1], false),
        (3, vec![1, -1, -1], vec![-1, -1, 1], false),
        (3, vec![-1, 2, -1], vec![-1, -1, -1], false),
        (4, vec![3, -1, 1, -1], vec![-1, -1, 0, -1], true),
        (4, vec![1, -1, 3, -1], vec![2, -1, -1, -1], true),
        (4, vec![1, -1, 3, -1], vec![2, 3, -1, -1], false),
        (
            6,
            vec![1, -1, 3, -1, -1, -1],
            vec![2, -1, -1, -1, 5, -1],
            false,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::validate_binary_tree_nodes(t.0, t.1, t.2), t.3);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
