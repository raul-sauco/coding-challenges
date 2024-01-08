// 938. Range Sum of BST
// 🟢 Easy
//
// https://leetcode.com/problems/range-sum-of-bst/
//
// Tags: Tree - Depth-First Search - Binary Search Tree - Binary Tree

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

#[allow(dead_code)]
struct Solution;
impl Solution {
    /// Recursive solution, explore any child of the current BST node that could provide valid
    /// values, for example, if root is already lower than the low boundary, we don't need to
    /// explore its left branch because any value there will be lower.
    ///
    /// Time complexity: O(n) - We could visit every node in the BST.
    /// Space complexity: O(n) - The call stack will grow to the height of the tree which could be
    /// the same as its size.
    ///
    /// Runtime 10 ms Beats 94.74%
    /// Memory 4.35 MB Beats 5.26%
    #[allow(dead_code)]
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        match root {
            None => 0,
            Some(node) => {
                let node = node.borrow();
                let val = node.val;
                let mut res = 0;
                if val >= low {
                    res += Self::range_sum_bst(node.left.clone(), low, high);
                }
                if val <= high {
                    res += Self::range_sum_bst(node.right.clone(), low, high);
                    if val >= low {
                        res += val;
                    }
                }
                res
            }
        }
    }
}

// Tests.
fn main() {
    todo!()
}
