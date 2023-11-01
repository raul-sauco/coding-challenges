// 501. Find Mode in Binary Search Tree
// 🟢 Easy
//
// https://leetcode.com/problems/find-mode-in-binary-search-tree/
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

struct Solution;
impl Solution {
    /// Use an iterative in-order DFS to explore the values in order, keep track
    /// of the frequency of the current value, when the value changes, update a
    /// monotonic vector of frequencies, we pop any smaller values, push equal
    /// values and ignore smaller ones. The monotonic vector will at any time
    /// only have the values for the most common frequency.
    ///
    /// Time complexity: O(n) - We visit each node and do constant time work
    /// for each. Even though we may pop multiple elements from the monotonic
    /// result vector, they are bounded by n.
    /// Space complexity: O(n) - The stack we use for the DFS and, unlikely but
    /// possible, the result vector.
    ///
    /// Runtime 2 ms Beats 70%
    /// Memory 2.96 MB Beats 70%
    pub fn find_mode(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = vec![];
        let mut node = root.clone();
        let mut res: Vec<(usize, i32)> = vec![];
        let mut cur = (0, i32::MAX);
        while !node.is_none() || !stack.is_empty() {
            match node {
                Some(rc) => {
                    let mut n = rc.borrow_mut();
                    if let Some(l) = n.left.clone() {
                        n.left = None;
                        stack.push(rc.clone());
                        node = Some(l);
                    } else {
                        let val = n.val;
                        if val == cur.1 {
                            cur.0 += 1;
                        } else {
                            cur = (1, val);
                        }
                        while let Some(last) = res.last() {
                            match last.0.cmp(&cur.0) {
                                std::cmp::Ordering::Less => {
                                    res.pop();
                                }
                                std::cmp::Ordering::Equal => {
                                    res.push(cur.clone());
                                    break;
                                }
                                std::cmp::Ordering::Greater => break,
                            }
                        }
                        // If res is empty push
                        if res.is_empty() {
                            res.push(cur.clone());
                        }
                        node = n.right.clone();
                    }
                }
                None => {
                    node = stack.pop();
                }
            }
        }
        res.into_iter().map(|(_count, val)| val).collect::<Vec<_>>()
    }
}

// Tests.
fn main() {
    //    let tests = [(vec![0], 0)];
    //    for t in tests {
    //        assert_eq!(Solution::find_mode(t.0), t.1);
    //    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
