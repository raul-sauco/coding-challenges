// 1457. Pseudo-Palindromic Paths in a Binary Tree
// 🟠 Medium
//
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
//
// Tags: Bit Manipulation - Tree - Depth-First Search - Breadth-First Search - Binary Tree

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
    /// Use DFS to explore each path in the tree from root to leaf, for each path, keep track of
    /// the values that we see, depending on the use that we want to give the value count, we might
    /// need to use a hashmap as a counter, in this case, we only need to know if we have seen each
    /// value an even or uneven number of times, for that we can use a set, value is present for
    /// uneven number of times, not present for 0 or even number of times. This solution uses the
    /// same logic as the Python solution but iterative DFS and a bitmask instead of recursive DFS
    /// and a hashset to make it a little different.
    ///
    /// Time complexity: O(n) - We visit each value and do O(1) work for each.
    /// Space complexity: O(h) - The stack will grow to the height of the tree, which could be n.
    ///
    /// Runtime 26 ms Beats 100%
    /// Memory 12.12 MB Beats 87.50%
    pub fn pseudo_palindromic_paths(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        // A stack with the node and the values bitmask, we need at least 9 bits.
        let mut stack = vec![(root.unwrap(), 0u16)];
        let mut res = 0;
        while let Some((rc, mut seen)) = stack.pop() {
            let nr = rc.borrow();
            // Flip the bit for this value. Is guaranteed that 1 <= val <= 9.
            seen ^= 1 << nr.val;
            // Process the children
            match (nr.left.clone(), nr.right.clone()) {
                // No children, we are at a leaf, add 1 if the path values form a palindrome.
                (None, None) => {
                    if seen.count_ones() < 2 {
                        res += 1;
                    }
                }
                (None, Some(child)) | (Some(child), None) => stack.push((child, seen)),
                (Some(left), Some(right)) => {
                    stack.push((left, seen));
                    stack.push((right, seen));
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    //     let tests = [(vec![0], 0)];
    //     println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    //     let mut success = 0;
    //     for (i, t) in tests.iter().enumerate() {
    //         let res = Solution::pseudo_palindromic_paths(t.0.clone());
    //         if res == t.1 {
    //             success += 1;
    //             println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
    //         } else {
    //             println!(
    //                 "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
    //                 i, t.1, res
    //             );
    //         }
    //     }
    //     println!();
    //     if success == tests.len() {
    //         println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    //     } else if success == 0 {
    //         println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    //     } else {
    //         println!("\x1b[31mx\x1b[95m {} tests failed!\x1b[0m", tests.len() - success)
    //     }
}
