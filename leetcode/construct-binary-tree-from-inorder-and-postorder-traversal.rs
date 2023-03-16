// 106. Construct Binary Tree from Inorder and Postorder Traversal
// 🟠 Medium
//
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
//
// Tags: Array - Hash Table - Divide and Conquer - Tree - Binary Tree

use std::cell::RefCell;
use std::collections::HashMap;
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
    // We know that the root of the tree is the value at the end of the
    // postorder array, we can use that value to find the root in the
    // inorder array, any value to its left belongs to the left sub-tree, any
    // value to the right, to the right sub-tree. Create a hashmap of
    // value => index on the inorder array, the root of the given tree is the
    // last value in the postorder array, use that to find the position in the
    // inorder array and divide the problem into left and right subtrees.
    //
    // Time complexity: O(n) - For each call, we access one value in a
    // hashmap and pop one value from the end of an array, all of them O(1).
    // Space complexity: O(h) - The call stack will have the same height as
    // the tree, best O(log(n)), worst O(n).
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.7 MB Beats 22.22%
    pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut d: HashMap<i32, usize> = HashMap::new();
        for (idx, val) in inorder.iter().enumerate() {
            d.insert(*val, idx);
        }
        let mut postorder = postorder.clone();
        fn helper(
            l: usize,
            r: usize,
            inorder: &Vec<i32>,
            postorder: &mut Vec<i32>,
            d: &HashMap<i32, usize>,
        ) -> Option<Rc<RefCell<TreeNode>>> {
            if l > r {
                return None;
            }
            match postorder.pop() {
                Some(val) => {
                    let idx = d.get(&val).unwrap();
                    // let right = helper(idx + 1, r, inorder, postorder, d);
                    // let left = helper(l, idx - 1, inorder, postorder, d);
                    Some(Rc::new(RefCell::new(TreeNode {
                        val,
                        right: helper(idx + 1, r, inorder, postorder, d),
                        left: helper(l, idx - 1, inorder, postorder, d),
                    })))
                }
                None => None,
            }
        }
        helper(0, inorder.len() - 1, &inorder, &mut postorder, &d)
    }
}

// Tests.
fn main() {
    let tests = [(vec![9, 3, 15, 20, 7], vec![9, 15, 7, 20, 3])];
    for t in tests {
        Solution::build_tree(t.0, t.1);
    }
    println!("No tests on this file!")
}
