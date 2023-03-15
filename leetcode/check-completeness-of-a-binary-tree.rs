// 958. Check Completeness of a Binary Tree
// 🟠 Medium
//
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/
//
// Tags: Tree - Breadth-First Search - Binary Tree

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

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
    // Use BFS, for each non-null node, check if we have seen a null position
    // before, if we have, return false.
    //
    // Time complexity: O(n) - We visit each node once.
    // Space complexity: O(n) - A level could have up to (n+1) / 2 nodes.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.1 MB Beats 25%
    pub fn is_complete_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut queue = VecDeque::from(vec![root]);
        let mut seen_none = false;
        while !queue.is_empty() {
            match queue.pop_front().unwrap() {
                Some(node) => {
                    if seen_none {
                        return false;
                    }
                    queue.push_back(node.borrow().left.clone());
                    queue.push_back(node.borrow().right.clone());
                }
                None => seen_none = true,
            }
        }
        true
    }
}

// Tests.
fn main() {
    // let tests = [];
    // for test in tests {
    //     assert_eq!(Solution::four_sum(test.0, test.1), test.2);
    // }
    println!("No tests on this file!")
}
