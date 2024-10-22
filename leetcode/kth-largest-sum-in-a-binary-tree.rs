// 2583. Kth Largest Sum in a Binary Tree
// 🟠 Medium
//
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
//
// Tags: Tree - Breadth-First Search - Sorting - Binary Tree

use std::cell::RefCell;
use std::collections::{BinaryHeap, VecDeque};
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
    /// Use BFS to process the tree by level, for each level, compute the sum of it's node
    /// values and store that, then return the kth sum, I use a heap for that, but we could
    /// also use other methods, for example a vector then sort it.
    ///
    /// Time complexity: O(nlog(n)) - We visit each node in the tree in linear time, but we
    /// push/pop them from the heap of size n.
    /// Space complexity: O(n) - The size of the heap. We push one i64 for each level, if the
    /// tree is skeewed, it could have as many levels as nodes.
    ///
    /// Runtime 8 ms Beats 100%
    /// Memory 11.84 MB Beats 33%
    pub fn kth_largest_level_sum(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i64 {
        let n = k as usize + 1;
        let mut heap = BinaryHeap::with_capacity(n);
        let mut queue = VecDeque::from([root.unwrap()]);
        let mut level_sum: i64;
        while !queue.is_empty() {
            level_sum = 0;
            for _ in 0..queue.len() {
                if let Some(rc) = queue.pop_front() {
                    let node = rc.borrow();
                    level_sum += node.val as i64;
                    if let Some(left) = node.left.clone() {
                        queue.push_back(left);
                    }
                    if let Some(right) = node.right.clone() {
                        queue.push_back(right);
                    }
                }
            }
            heap.push(level_sum);
        }
        for _ in 0..k - 1 {
            heap.pop();
        }
        *heap.peek().unwrap()
    }
}

// Tests.
fn main() {
    let tree1 = Some(Rc::new(RefCell::new(TreeNode {
        val: 5,
        left: Some(Rc::new(RefCell::new(TreeNode {
            val: 8,
            left: Some(Rc::new(RefCell::new(TreeNode {
                val: 2,
                left: Some(Rc::new(RefCell::new(TreeNode {
                    val: 4,
                    left: None,
                    right: None,
                }))),
                right: Some(Rc::new(RefCell::new(TreeNode {
                    val: 6,
                    left: None,
                    right: None,
                }))),
            }))),
            right: Some(Rc::new(RefCell::new(TreeNode {
                val: 1,
                left: None,
                right: None,
            }))),
        }))),
        right: Some(Rc::new(RefCell::new(TreeNode {
            val: 9,
            left: Some(Rc::new(RefCell::new(TreeNode {
                val: 3,
                left: None,
                right: None,
            }))),
            right: Some(Rc::new(RefCell::new(TreeNode {
                val: 7,
                left: None,
                right: None,
            }))),
        }))),
    })));
    let tree2 = Some(Rc::new(RefCell::new(TreeNode {
        val: 1,
        left: Some(Rc::new(RefCell::new(TreeNode {
            val: 2,
            left: Some(Rc::new(RefCell::new(TreeNode {
                val: 3,
                left: None,
                right: None,
            }))),
            right: None,
        }))),
        right: None,
    })));
    let tests = [(tree1, 2, 13), (tree2, 1, 3)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::kth_largest_level_sum(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.1, res
            );
        }
    }
    println!();
    if success == tests.len() {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
