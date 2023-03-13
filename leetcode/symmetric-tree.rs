// 101. Symmetric Tree
// 🟢 Easy
//
// https://leetcode.com/problems/symmetric-tree/
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
    // If the tree is symmetrical, we can recursively explore both left and
    // right sub trees comparing the symmetrical values of one to the other,
    // if at any point they differ, the tree is not symmetrical.
    //
    // Time complexity: O(n) - We visit each node once.
    // Space complexity: O(n) - Up to one call per node in the call stack.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.2 MB Beats 64.42%
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        // An internal function that checks two nodes situated in a
        // symmetrical position in the tree.
        fn dfs(left: Option<Rc<RefCell<TreeNode>>>, right: Option<Rc<RefCell<TreeNode>>>) -> bool {
            match (left, right) {
                (None, None) => true,
                (None, Some(_)) | (Some(_), None) => false,
                (Some(left), Some(right)) => {
                    left.borrow().val == right.borrow().val
                        && dfs(left.borrow().left.clone(), right.borrow().right.clone())
                        && dfs(left.borrow().right.clone(), right.borrow().left.clone())
                }
            }
        }
        match root {
            Some(root) => dfs(root.borrow().left.clone(), root.borrow().right.clone()),
            None => true,
        }
    }
}

// Tests.
fn main() {
    // let tests = [];
    // for test in tests {
    //     unimplemented!();
    // }
    println!("No tests for this file!")
}
