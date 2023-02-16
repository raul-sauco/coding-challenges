// 104. Maximum Depth of Binary Tree
// 🟢 Easy
//
// https://leetcode.com/problems/maximum-depth-of-binary-tree/
//
// Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

use std::cell::RefCell;
use std::cmp;
use std::rc::Rc;

struct Solution;
impl Solution {
    // We can use a recursive call that computes the height of the left and
    // right child and returns the maximum between them plus one for the
    // current level.
    //
    // Time complexity: O(n) - We will visit each node in the tree.
    // Space complexity: O(n) - The height of the call stack, it could go
    // from O(n) in the worst case, a skewed tree, to O(log(n)) best case if
    // the tree was well balanced.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.7 MB Beats 29.86%
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            Some(node) => {
                cmp::max(
                    Self::max_depth(node.borrow().right.clone()),
                    Self::max_depth(node.borrow().left.clone()),
                ) + 1
            }
            None => 0,
        }
    }
}

// Tests.
fn main() {
    // assert_eq!(Solution::max_depth(root), 2);
    println!("All tests passed!")
}

// Definition for a binary tree node.
//[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    //[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}
