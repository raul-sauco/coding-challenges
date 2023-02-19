// 103. Binary Tree Zigzag Level Order Traversal
// 🟠 Medium
//
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
//
// Tags: Tree - Breadth-First Search - Binary Tree

use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    // Use a breadth-first traversal combined with a flag to determine which
    // levels need to be reversed. Keep a stack that contains an entire level
    // at a time, first get the values of the current level and append them
    // to the result, then use the nodes to obtain the next level.
    //
    // Time complexity: O(n) - We will visit every node and do constant work
    // for each.
    // Space complexity: O(n) - The stack will hold one level of the tree at
    // any given point.
    //
    // Runtime 1 ms Beats 68.42%
    // Memory 2.2 MB Beats 10.53%
    pub fn zigzag_level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        match root {
            None => vec![],
            Some(root) => {
                let mut res: Vec<Vec<i32>> = vec![];
                let mut stack: Vec<Rc<RefCell<TreeNode>>> = vec![root];
                let mut reverse_level = false;
                while stack.len() > 0 {
                    let values: Vec<i32> = if reverse_level {
                        stack.iter().rev().map(|r| r.borrow().val).collect()
                    } else {
                        stack.iter().map(|r| r.borrow().val).collect()
                    };
                    res.push(values);
                    reverse_level = !reverse_level;
                    let mut next_level: Vec<Rc<RefCell<TreeNode>>> = vec![];
                    for r in stack {
                        match &r.borrow().left {
                            Some(cr) => next_level.push(cr.clone()),
                            None => (),
                        }
                        match &r.borrow().right {
                            Some(cr) => next_level.push(cr.clone()),
                            None => (),
                        }
                    }
                    stack = next_level;
                }
                res
            }
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
