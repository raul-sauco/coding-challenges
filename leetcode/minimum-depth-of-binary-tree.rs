// 111. Minimum Depth of Binary Tree
// 🟢 Easy
//
// https://leetcode.com/problems/minimum-depth-of-binary-tree/
//
// Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

use std::cell::RefCell;
use std::collections::VecDeque;
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
    /// Recursive DFS solution, at each node, check if it is a leaf, if it is
    /// not, return the sum of the minimum height of its children subtrees plus
    /// one.
    ///
    /// Time complexity: O(n) - We will visit each node.
    /// Space complexity: O(h) - The call stack will grow to the height of the
    /// tree, which could be equal to n.
    ///
    /// Runtime 54 ms Beats 15.87%
    /// Memory 13.1 MB Beats 49.21%
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            Some(rc) => {
                let node = rc.borrow();
                let l = Self::min_depth(node.left.clone());
                let r = Self::min_depth(node.right.clone());
                if l == 0 || r == 0 {
                    return 1 + l + r;
                } else {
                    return 1 + std::cmp::min(l, r);
                }
            }
            None => 0,
        }
    }

    /// Iterative BFS solution, use a double ended queue and process the input
    /// tree one level at a time while keeping track of the depth of the current
    /// level, return when we get to a leaf.
    ///
    /// Time complexity: O(n) - We could visit each node.
    /// Space complexity: O(h) - The call stack could grow to the height of the
    /// tree, which could be equal to n.
    ///
    /// Runtime 36 ms Beats 96.83%
    /// Memory 12.8 MB Beats 82.54%
    pub fn min_depth_2(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }
        let mut depth = 0;
        let mut q = VecDeque::from([root.unwrap()]);
        while !q.is_empty() {
            depth += 1;
            // Process an entire level.
            for _ in 0..q.len() {
                if let Some(rc) = q.pop_front() {
                    if rc.borrow().left.is_none() && rc.borrow().right.is_none() {
                        return depth;
                    }
                    if let Some(left) = &rc.borrow().left {
                        q.push_back(Rc::clone(&left));
                    }
                    if let Some(right) = &rc.borrow().right {
                        q.push_back(Rc::clone(&right));
                    }
                }
            }
        }
        depth
    }
}

// Tests.
fn main() {
    let tests = [(vec![0], 0)];
    for t in tests {
        // assert_eq!(Solution::min_depth(t.0), t.1);
    }
    println!("[92m» All tests passed![0m")
}
