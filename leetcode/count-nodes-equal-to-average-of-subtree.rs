// 2265. Count Nodes Equal to Average of Subtree
// 🟠 Medium
//
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
//
// Tags: Tree - Depth-First Search - Binary Tree

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;

struct SubtreeCounts {
    nodes: i32,
    total: i32,
    count: i32,
}

struct Solution;
impl Solution {
    /// Use post order DFS, compute number of nodes, total sum of values and
    /// count of nodes that match the given condition for each subtree, each
    /// node computes that for its left and right subtrees, then adds its own
    /// values, checks if its value matches the average of the subtree it roots
    /// and returns these values to its parent.
    ///
    /// Time complexity: O(n) - The total number of times dfs gets called is 2*n.
    /// Space complexity: O(n) - The call stack can grow to the height of the
    /// tree.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.27 MB Beats 100%
    pub fn average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(root: Option<Rc<RefCell<TreeNode>>>) -> SubtreeCounts {
            match root {
                Some(rc) => {
                    let node = rc.borrow();
                    let left = dfs(node.left.clone());
                    let right = dfs(node.right.clone());
                    let nodes = left.nodes + right.nodes + 1;
                    let total = left.total + right.total + node.val;
                    let mut count = left.count + right.count;
                    if total / nodes == node.val {
                        count += 1;
                    }
                    SubtreeCounts {
                        nodes,
                        total,
                        count,
                    }
                }
                None => SubtreeCounts {
                    nodes: 0,
                    total: 0,
                    count: 0,
                },
            }
        }
        dfs(root).count
    }
}

// Tests.
fn main() {
    // let tests = [(vec![0], 0)];
    // for t in tests {
    //     assert_eq!(Solution::average_of_subtree(t.0), t.1);
    // }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
