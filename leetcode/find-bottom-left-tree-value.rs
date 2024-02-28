// 513. Find Bottom Left Tree Value
// 🟠 Medium
//
// https://leetcode.com/problems/find-bottom-left-tree-value/
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
    /// Use BFS, process level nodes left to right and assign the value of the first node found as
    /// the current result. Once we run out of nodes, return.
    ///
    /// Time complexity: O(n) -  We will push and pop each node to/from the queue in O(1) each.
    /// Space complexity: O(n) - The queue will grow to twice the size of the biggest level, which
    /// could be 2n.
    ///
    /// Runtime 2 ms Beats 71.43%
    /// Memory 3 MB Beats 100%
    #[allow(dead_code)]
    pub fn find_bottom_left_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = -1;
        let mut level_first;
        let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::from([root]);
        while !queue.is_empty() {
            level_first = None;
            for _ in 0..queue.len() {
                if let Some(rc) = queue.pop_front().expect("An Option<Rc>") {
                    let node = rc.borrow();
                    if level_first.is_none() {
                        level_first = Some(node.val);
                    }
                    queue.push_back(node.left.clone());
                    queue.push_back(node.right.clone());
                }
            }
            if let Some(val) = level_first {
                res = val;
            }
        }
        res
    }

    /// Same logic but easier to read code. Use a vector to contain each level and iterators to
    /// compute the next level from the current one. Using filter map to have a Vec<Rc> makes the
    /// code very clean.
    ///
    /// Time complexity: O(n) -  We will push and read each node to/from the vector in O(1) each.
    /// Space complexity: O(n) - The vector will grow to the size of the biggest level, which
    /// could be n.
    ///
    /// Runtime 2 ms Beats 71.43%
    /// Memory 2.90 MB Beats 100%
    #[allow(dead_code)]
    pub fn find_bottom_left_value_it(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut level = Vec::from([root.unwrap()]);
        let mut res = level[0].borrow().val;
        while !level.is_empty() {
            res = level[0].borrow().val;
            level = level
                .into_iter()
                .flat_map(|rc| [rc.borrow().left.clone(), rc.borrow().right.clone()])
                .filter_map(|rc| rc)
                .collect();
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![0], 0)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
}
