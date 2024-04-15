// 129. Sum Root to Leaf Numbers
// 🟠 Medium
//
// https://leetcode.com/problems/sum-root-to-leaf-numbers/
//
// Tags: Tree - Depth-First Search - Binary Tree

use std::cell::RefCell;
use std::rc::Rc;

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
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
    // Traverse the tree using preorder DFS, add the value of the current node to the path sum, if
    // the node is a leaf, return that value, otherwise call the function for any non-null child.
    //
    // Time complexity: O(n) - We will visit every node in the tree and do constant work for each.
    // Space complexity: O(h) - The height of the call stack will be the height of the tree, worst
    // case O(n), best O(log(n)).
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.1 MB Beats 44.44%
    #[allow(dead_code)]
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Rc<RefCell<TreeNode>>, path_sum: i32) -> i32 {
            let path_sum = path_sum * 10 + node.borrow().val;
            match (node.borrow().left.clone(), node.borrow().right.clone()) {
                (None, None) => path_sum,
                (None, Some(child)) | (Some(child), None) => dfs(child, path_sum),
                (Some(left), Some(right)) => dfs(left, path_sum) + dfs(right, path_sum),
            }
        }
        match root {
            Some(root) => dfs(root, 0),
            None => 0,
        }
    }

    /// Same as the previous solution but use references and a match instead of cloning the Rc and
    /// using an if statement.
    ///
    /// Time complexity: O(n) - We visit every node and do O(1) work for each.
    /// Space complexity: O(h) - The call stack will grow to the size of the tree.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.17 MB Beats 19%
    #[allow(dead_code)]
    pub fn sum_numbers_ref(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(opt: Option<&Rc<RefCell<TreeNode>>>, path_sum: i32) -> i32 {
            match opt {
                Some(rc) => {
                    let node = rc.borrow();
                    let path_sum = path_sum * 10 + node.val;
                    match (&node.left, &node.right) {
                        (None, None) => path_sum,
                        _ => dfs(node.left.as_ref(), path_sum) + dfs(node.right.as_ref(), path_sum),
                    }
                }
                None => 0,
            }
        }
        dfs(root.as_ref(), 0)
    }
}

// Tests.
fn main() {
    println!("\n\x1b[92m» No tests in this file\x1b[0m");
}
