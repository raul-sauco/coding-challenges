// 543. Diameter of Binary Tree
// 🟢 Easy
//
// https://leetcode.com/problems/diameter-of-binary-tree/
//
// Tags: Tree - Depth-First Search - Binary Tree

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
    /// Recursive postorder with the recursive function returning two values, the length of the
    /// longest path between the subtree root and a leave, and the number of nodes in the subtree
    /// diameter, each node uses these two values in their left and right sub-tree to compute its
    /// own return values.
    ///
    /// Time complexity: O(n) - We visit each node in the tree using postorder DFS.
    /// Space complexity: O(h) - The call stack will grow to size h, which could be equal to n.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.72 MB Beats 65.15%
    #[allow(dead_code)]
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
            match node {
                None => (0, 0),
                Some(rc) => {
                    let l = dfs(rc.borrow().left.clone());
                    let r = dfs(rc.borrow().right.clone());
                    (1 + l.0.max(r.0), (1 + r.0 + l.0).max(r.1.max(l.1)))
                }
            }
        }
        dfs(root).1
    }
}

// Tests.
fn main() {
    let tests = [(vec![0], 0)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    // let mut success = 0;
    // for (i, t) in tests.iter().enumerate() {
    //     let res = Solution::diameter_of_binary_tree(t.0.clone());
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
    //     println!("\x1b[31mx\x1b[95m {} tests failed!\x1b[0m", tests.len() - success)
    // }
}
