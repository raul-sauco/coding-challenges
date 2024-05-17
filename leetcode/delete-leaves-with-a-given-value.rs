// 1325. Delete Leaves With a Given Value
// 🟠 Medium
//
// https://leetcode.com/problems/delete-leaves-with-a-given-value/
//
// Tags: Tree - Depth-First Search - Binary Tree

use std::cell::RefCell;
use std::rc::Rc;

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

struct Solution;
impl Solution {
    /// Use a post order traversal, once we process the left and right subtrees, if the value
    /// matches the target return None, otherwise return the node.
    ///
    /// Time complexity: O(n) - Postorder traversal of the tree.
    /// Space complexity: O(h) - The call stack will grow to the height of the tree.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.26 MB Beats 100%
    #[allow(dead_code)]
    pub fn remove_leaf_nodes(
        root: Option<Rc<RefCell<TreeNode>>>,
        target: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        match root {
            Some(root) => {
                let mut node = root.borrow_mut();
                node.left = Self::remove_leaf_nodes(node.left.clone(), target);
                node.right = Self::remove_leaf_nodes(node.right.clone(), target);
                if node.val == target && node.left.is_none() && node.right.is_none() {
                    None
                } else {
                    Some(root.clone())
                }
            }
            None => None,
        }
    }
}

// Tests.
fn main() {
    println!("\n\x1b[92m» No tests in this file...\x1b[0m");
}
