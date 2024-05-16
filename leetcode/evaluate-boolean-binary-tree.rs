// 2331. Evaluate Boolean Binary Tree
// 🟢 Easy
//
// https://leetcode.com/problems/evaluate-boolean-binary-tree/
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
    /// Check the value of the current node, if it is a boolean value, return that, otherwise first
    /// evaluate its left and right subtrees, then use the operator to return the and/or result.
    ///
    /// Time complexity: O(n) - We do a postorder traversal of the tree that visits all nodes.
    /// Space complexity: O(h) - The height of the call stack.
    ///
    /// Runtime 3 ms Beats 83%
    /// Memory 2.19 MB Beats 100%
    #[allow(dead_code)]
    pub fn evaluate_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match root {
            Some(root) => {
                let root = root.borrow();
                match root.val {
                    0 => false,
                    1 => true,
                    2 | 3 => {
                        let (left, right) = (
                            Self::evaluate_tree(root.left.clone()),
                            Self::evaluate_tree(root.right.clone()),
                        );
                        if root.val == 2 {
                            left || right
                        } else {
                            left && right
                        }
                    }
                    _ => unreachable!(),
                }
            }
            None => unreachable!(),
        }
    }
}

// Tests.
fn main() {
    println!("\n\x1b[92m» No tests in this file...\x1b[0m");
}
