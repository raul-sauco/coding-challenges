// 100. Same Tree
// 🟢 Easy
//
// https://leetcode.com/problems/same-tree/
//
// Tags: Tree - Depth-First Search - Breadth-First Search - Binary Tree

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
    /// Since TreeNode derives Eq, que can use the `==` operator.
    ///
    /// Time complexity: O(n) - We visit each value in the tree.
    /// Space complexity: O(h) - The call stack, could grow to size n if the tree was skeewed.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.18 MB Beats 61.98%
    #[allow(dead_code)]
    pub fn is_same_tree_use_eq_trait(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        p == q
    }

    /// We can use a recursive solution, if both nodes are null or both nodes have the same value
    /// and the result of recursively calling the function on their left and right subtrees is
    /// true, return true, otherwise false.
    ///
    /// Time complexity: O(n) - We visit each value in the tree.
    /// Space complexity: O(h) - The call stack, could grow to size n if the tree was skeewed.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.04 MB Beats 97.92%
    #[allow(dead_code)]
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (p, q) {
            (None, None) => true,
            (Some(_), None) | (None, Some(_)) => false,
            (Some(rca), Some(rcb)) => {
                rca.borrow().val == rcb.borrow().val
                    && Solution::is_same_tree(rca.borrow().left.clone(), rcb.borrow().left.clone())
                    && Solution::is_same_tree(
                        rca.borrow().right.clone(),
                        rcb.borrow().right.clone(),
                    )
            }
        }
    }

    /// Same logic but assign the RC borrows, easier to read.
    ///
    /// Time complexity: O(n) - We visit each value in the tree.
    /// Space complexity: O(h) - The call stack, could grow to size n if the tree was skeewed.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.15 MB Beats 61.98%
    #[allow(dead_code)]
    pub fn is_same_tree_assigned(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (p, q) {
            (None, None) => true,
            (Some(_), None) | (None, Some(_)) => false,
            (Some(rca), Some(rcb)) => {
                let a = rca.borrow();
                let b = rcb.borrow();
                a.val == b.val
                    && Solution::is_same_tree(a.left.clone(), b.left.clone())
                    && Solution::is_same_tree(a.right.clone(), b.right.clone())
            }
        }
    }
}

// Tests.
fn main() {
    let tests = [(vec![0], 0)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    // let mut success = 0;
    // for (i, t) in tests.iter().enumerate() {
    //     let res = Solution::is_same_tree(t.0.clone());
    //     if res == t.1 {
    //         success += 1;
    //         println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
    //     } else {
    //         println!(
    //             "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
    //             i, t.1, res
    //         );
    //     }
    // }
    // println!();
    // if success == tests.len() {
    //     println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    // } else if success == 0 {
    //     println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    // } else {
    //     println!(
    //         "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
    //         tests.len() - success
    //     )
    // }
}
