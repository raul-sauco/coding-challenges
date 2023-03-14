// 129. Sum Root to Leaf Numbers
// 🟠 Medium
//
// https://leetcode.com/problems/sum-root-to-leaf-numbers/
//
// Tags: Tree - Depth-First Search - Binary Tree

use std::cell::RefCell;
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
    // Traverse the tree using preorder DFS, add the value of the current
    // node to the path sum, if the node is a leaf, return that value,
    // otherwise call the function for any non-null children.
    //
    // Time complexity: O(n) - We will visit every node in the tree and do
    // constant work for each.
    // Space complexity: O(h) - The height of the call stack will be the
    // height of the tree, worst O(n), best O(log(n)).
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.1 MB Beats 44.44%
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
}

// Tests.
fn main() {
    // let tests = [];
    // for test in tests {
    //     assert_eq!(Solution::four_sum(test.0, test.1), test.2);
    // }
    println!("No tests on this file!")
}
