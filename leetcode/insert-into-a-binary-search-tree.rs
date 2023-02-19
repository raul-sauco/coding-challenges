// 701. Insert into a Binary Search Tree
// 🟠 Medium
//
// https://leetcode.com/problems/insert-into-a-binary-search-tree/
//
// Tags: Tree - Binary Search Tree - Binary Tree

use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    // Travel through the tree choosing to go right or left based on node
    // values until we find the leave below which we will need to insert
    // the new node.
    //
    // Time Complexity: Best: O(log(n)) Worst: O(n) - We will travel the
    // entire height of the tree, ideally, it would be a well balanced tree
    // and its height would be log(n), but a skewed tree could have a height
    // of n, since we are not doing any balancing, after multiple inserts,
    // depending on the order in which the values were inserted, the tree
    // could become skewed.
    // Space complexity: O(1) - We only store a reference to the root and to
    // the current node that we are visiting.
    //
    // Runtime 12 ms Beats 72.73%
    // Memory 2.6 MB Beats 72.73%
    pub fn insert_into_bst(
        root: Option<Rc<RefCell<TreeNode>>>,
        val: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let new_node = TreeNode {
            val,
            left: None,
            right: None,
        };
        if root.is_none() {
            return Some(Rc::new(RefCell::new(new_node)));
        }
        let mut n = root.clone();
        loop {
            match n {
                Some(node) => {
                    if val < node.borrow().val {
                        if node.borrow().left.is_some() {
                            n = node.borrow().left.clone();
                        } else {
                            node.borrow_mut().left = Some(Rc::new(RefCell::new(new_node)));
                            break;
                        }
                    } else {
                        if node.borrow().right.is_some() {
                            n = node.borrow().right.clone();
                        } else {
                            node.borrow_mut().right = Some(Rc::new(RefCell::new(new_node)));
                            break;
                        }
                    }
                }
                None => panic!("This code should never run"),
            }
        }
        root
    }

    // Travel through the tree choosing to go right or left based on node
    // values until we find the leave below which we will need to insert
    // the new node.
    //
    // Time Complexity: Best: O(log(n)) Worst: O(n) - We will travel the
    // entire height of the tree, ideally, it would be a well balanced tree
    // and its height would be log(n), but a skewed tree could have a height
    // of n, since we are not doing any balancing, after multiple inserts,
    // depending on the order in which the values were inserted, the tree
    // could become skewed.
    // Space complexity: Best: O(log(n)) Worst: O(n) - Each node that we
    // visit will add one call to the call stack.
    //
    // Runtime 8 ms Beats 90.91%
    // Memory 2.6 MB Beats 72.73%
    pub fn insert_into_bst_rec(
        root: Option<Rc<RefCell<TreeNode>>>,
        val: i32,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        // Always return a node reference, never None.
        Some(match root {
            // We are at the insertion point, create and return a new node.
            None => Rc::new(RefCell::new(TreeNode {
                val,
                left: None,
                right: None,
            })),
            // We are traveling down the tree decide whether to go right or left,
            // create a new node with the result of calling insert_into_bst on the
            // child and update the current child with that result.
            Some(node_ref) => {
                if val < node_ref.borrow().val {
                    let node = Self::insert_into_bst(node_ref.borrow().left.clone(), val);
                    node_ref.borrow_mut().left = node;
                } else {
                    let node = Self::insert_into_bst(node_ref.borrow().right.clone(), val);
                    node_ref.borrow_mut().right = node;
                }
                node_ref
            }
        })
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
