// 1372. Longest ZigZag Path in a Binary Tree
// 🟠 Medium
//
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
//
// Tags: Dynamic Programming - Tree - Depth-First Search - Binary Tree

use std::{cell::RefCell, rc::Rc};

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
    /// Use any traversal method to visit all nodes, for each node, record the
    /// direction that we used to travel there and the length of the zig-zag
    /// path to it, the path will continue to grow for one of its children and
    /// will restart for the other one.
    ///
    /// Time complexity: O(n) - We visit all nodes and do O(1) work for each.
    /// Space complexity: O(1) - The stack can grow to size n.
    ///
    /// Runtime 16 ms Beats 100%
    /// Memory 5.7 MB Beats 100%
    pub fn longest_zig_zag(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut stack = vec![(root, 0, 0)];
        let mut res = 0;
        while !stack.is_empty() {
            let (current, l, r) = stack.pop().unwrap();
            match current {
                Some(current) => {
                    if l > res || r > res {
                        res = l.max(r);
                    }
                    stack.push((current.borrow().left.clone(), r + 1, 0));
                    stack.push((current.borrow().right.clone(), 0, l + 1));
                }
                None => continue,
            }
        }
        res
    }
}

// Tests.
fn main() {
    println!("\x1b[92m» No tests for this file\x1b[0m")
}
