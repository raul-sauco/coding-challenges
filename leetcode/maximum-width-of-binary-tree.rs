// 662. Maximum Width of Binary Tree
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-width-of-binary-tree/
//
// Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

use std::{borrow::Borrow, cell::RefCell, collections::VecDeque, rc::Rc};

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
    /// Use breadth-first search, visit all the nodes in one level enqueueing
    /// children that are not null together with the index they would be at
    /// inside their own level, after processing each level, check the index
    /// difference between the left and right-most nodes and use that to compute
    /// the result.
    ///
    /// Time complexity: O(n) - We will visit all nodes in the tree but will not
    /// do any work for positions that hold a None value.
    /// Space complexity: O(n) - The queue will hold one entire level which
    /// could be n/2 in size.
    ///
    /// Runtime 2 ms Beats 50%
    /// Memory 2.4 MB Beats 83.33%
    pub fn width_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut q = VecDeque::from([(root.unwrap(), 0)]);
        let mut res = 1;
        while !q.is_empty() {
            // Process the current level.
            res = res.max(1 + q.back().unwrap().1 - q.front().unwrap().1);
            for _ in 0..q.len() {
                let (rc, idx) = q.pop_front().unwrap();
                // Push the children to the back of the queue by cloning the
                // Rc I believe this clones a pointer and is cheap.
                if let Some(left) = rc.as_ref().borrow().left.clone() {
                    q.push_back((left, idx * 2));
                };
                if let Some(right) = rc.as_ref().borrow().right.clone() {
                    q.push_back((right, idx * 2 + 1));
                };
            }
        }
        res
    }
}

// Tests.
fn main() {
    println!("\x1b[92m» No tests for this file\x1b[0m")
}
