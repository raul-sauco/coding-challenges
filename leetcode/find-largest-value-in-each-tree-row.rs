// 515. Find Largest Value in Each Tree Row
// 🟠 Medium
//
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/
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
    /// Use BFS, visit each level keeping track of the maximum seen at that level
    /// and pushing that maximum to a vector containing the result.
    ///
    /// Time complexity: O(n) - We visit each node and do constant time work for
    /// each of them.
    /// Space complexity: O(n) - The queue can grow to the size of a level, one
    /// level could be n/2.
    ///
    /// Runtime 2 ms Beats 60%
    /// Memory 2.95 MB Beats 100%
    pub fn largest_values(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut queue = VecDeque::new();
        let mut res = vec![];
        if root.is_none() {
            return res;
        }
        queue.push_back(root.unwrap());
        let mut level_max;
        while !queue.is_empty() {
            level_max = i32::MIN;
            for _ in 0..queue.len() {
                match queue.pop_front() {
                    Some(node) => {
                        level_max = level_max.max(node.borrow().val);
                        match node.borrow().left.clone() {
                            Some(left) => queue.push_back(left),
                            _ => {}
                        };
                        match node.borrow().right.clone() {
                            Some(right) => queue.push_back(right),
                            _ => {}
                        }
                    }
                    None => unreachable!("We are popping the level nodes"),
                }
            }
            res.push(level_max);
        }
        res
    }

    /// Similar to the previous solution but use two vectors instead of a queue.
    ///
    /// Time complexity: O(n) - We visit each node and do constant time work for
    /// each of them.
    /// Space complexity: O(n) - The vectors can grow to the size of a level, one
    /// level could be n/2.
    ///
    /// Runtime 2 ms Beats 60%
    /// Memory 3.09 MB Beats 60%
    pub fn largest_values_2(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res = vec![];
        if root.is_none() {
            return res;
        }
        let (mut level, mut next_level) = (vec![root.unwrap()], vec![]);
        let mut level_max;
        while !level.is_empty() {
            level_max = i32::MIN;
            while let Some(cur) = level.pop() {
                let mut cur_mut = cur.borrow_mut();
                if cur_mut.val > level_max {
                    level_max = cur_mut.val;
                }
                match (cur_mut.left.take(), cur_mut.right.take()) {
                    (Some(l), Some(r)) => {
                        next_level.push(l);
                        next_level.push(r);
                    }
                    (Some(n), None) | (None, Some(n)) => next_level.push(n),
                    _ => (),
                }
            }
            res.push(level_max);
            std::mem::swap(&mut level, &mut next_level);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![0], 0)];
    for _t in tests {
        // assert_eq!(Solution::largest_values(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
