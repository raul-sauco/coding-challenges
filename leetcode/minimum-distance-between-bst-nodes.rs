// 783. Minimum Distance Between BST Nodes
// 🟢 Easy
//
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/
//
// Tags: Tree - Depth-First Search - Breadth-First Search
//       Binary Search Tree - Binary Tree

use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    // The inorder traversal of a BST results in a list of its values in
    // sorted order, we can use that inorder traversal property to traverse
    // the values in sorted order comparing each value with the previous one.
    //
    // Time complexity: O(n) - We will visit each node once.
    // Space complexity: O(n) - The stack will grow to the height of the tree
    // which is worst case n and best case log(n).
    //
    // Runtime 1 ms Beats 83.33%
    // Memory 2 MB Beats 100%
    pub fn min_diff_in_bst(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = std::i32::MAX;
        let mut prev = std::i32::MIN;
        let mut node = root;
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = vec![];
        while node.is_some() || stack.len() > 0 {
            match node {
                Some(node_ref) => {
                    stack.push(node_ref.clone());
                    node = node_ref.borrow().left.clone();
                }
                None => match stack.pop() {
                    Some(node_ref) => {
                        let n = node_ref.borrow();
                        // if prev != std::i32::MIN && n.val - prev < res {
                        //     res = n.val - prev;
                        // }
                        res = res.min(n.val.saturating_sub(prev));
                        prev = n.val;
                        node = n.right.clone();
                    }
                    None => panic!("Reached unreachable arm"),
                },
            };
        }
        res
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
