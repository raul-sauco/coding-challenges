// 404. Sum of Left Leaves
// 🟢 Easy
//
// https://leetcode.com/problems/sum-of-left-leaves/
//
// Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

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
    /// Simple dfs with an extra check to only add node values if they are a left child and a leaf.
    /// To determine if a node is a left child we can pass this value from the parent on the call.
    ///
    /// Time complexity: O(n) - We will visit all nodes in the tree.
    /// Space complexity: O(h) - The call stack will grow to the height of the tree.
    ///
    /// Runtime 1 ms Beats 77%
    /// Memory 2.25 MB Beats 40%
    #[allow(dead_code)]
    pub fn sum_of_left_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(opt: Option<&Rc<RefCell<TreeNode>>>, is_left_child: bool) -> i32 {
            match opt {
                None => 0,
                Some(wrapped) => {
                    let node = wrapped.borrow();
                    if node.left.is_none() && node.right.is_none() {
                        return if is_left_child { node.val } else { 0 };
                    }
                    dfs(node.left.as_ref(), true) + dfs(node.right.as_ref(), false)
                }
            }
        }
        dfs(root.as_ref(), false)
    }
}

// Tests.
fn main() {
    println!("\n\x1b[92m» No tests for this file\x1b[0m");
}
