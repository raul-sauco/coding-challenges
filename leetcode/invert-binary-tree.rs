// 226. Invert Binary Tree
// 🟢 Easy
//
// https://leetcode.com/problems/invert-binary-tree/
//
// Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    // Use depth-first search to visit all nodes in the tree, for each node,
    // swap the position of its children.
    //
    // Time complexity: O(n) - We visit each node in the tree and, for each,
    // do O(1) work.
    // Space complexity: O(h) - The call stack can grow to the height of the
    // tree, which could be the same as n.
    //
    // Runtime 1 ms Beats 66.37%
    // Memory 2 MB Beats 65.49%
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        match root {
            Some(node_ref) => {
                let tmp = node_ref.borrow();
                Some(Rc::new(RefCell::new(TreeNode {
                    val: tmp.val,
                    left: Self::invert_tree(tmp.right.clone()),
                    right: Self::invert_tree(tmp.left.clone()),
                })))
            }
            None => None,
        }
    }
}

// Tests.
fn main() {
    // assert_eq!(Solution::min_diff_in_bst(root), 1);
    println!("All tests passed!")
}

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
