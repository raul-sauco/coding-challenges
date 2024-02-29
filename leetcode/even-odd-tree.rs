// 1609. Even Odd Tree
// 🟠 Medium
//
// https://leetcode.com/problems/even-odd-tree/
//
// Tags: Tree - Breadth-First Search - Binary Tree

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
    /// Do a double BFS checking each level against the conditions they must satisfy.
    ///
    /// Time complexity: O(n) - BFS, we will visit each node.
    /// Space complexity: O(l) - The vectors will grow to the size of the levels they hold.
    ///
    /// Runtime 31 ms Beats 50%
    /// Memory 11.7 MB Beats 50%
    #[allow(dead_code)]
    pub fn is_even_odd_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut even_level = Vec::from([root.unwrap()]);
        let mut odd_level = vec![];
        let mut last_value: Option<i32>;
        loop {
            if even_level.is_empty() {
                return true;
            }
            last_value = None;
            odd_level.clear();
            // Even level: odd increasing values
            for rc in &even_level {
                let node = rc.borrow();
                if node.val % 2 == 0 {
                    return false;
                }
                if let Some(last) = last_value {
                    if last >= node.val {
                        return false;
                    }
                }
                last_value = Some(node.val);
                if let Some(left) = &node.left {
                    odd_level.push(left.clone());
                }
                if let Some(right) = &node.right {
                    odd_level.push(right.clone());
                }
            }
            if odd_level.is_empty() {
                return true;
            }
            last_value = None;
            even_level.clear();
            // Odd level: even decreasing values
            for rc in &odd_level {
                let node = rc.borrow();
                if node.val % 2 == 1 {
                    return false;
                }
                if let Some(last) = last_value {
                    if last <= node.val {
                        return false;
                    }
                }
                last_value = Some(node.val);
                if let Some(left) = &node.left {
                    even_level.push(left.clone());
                }
                if let Some(right) = &node.right {
                    even_level.push(right.clone());
                }
            }
        }
    }
}

// Tests.
fn main() {
    let tests = [(vec![0], 0)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
}
