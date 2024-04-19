// 988. Smallest String Starting From Leaf
// 🟠 Medium
//
// https://leetcode.com/problems/smallest-string-starting-from-leaf/
//
// Tags: String - Tree - Depth-First Search - Binary Tree

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
    /// This solution does not work! But since I did not realize that until later, I kept it here,
    /// it may be a good base for some other problem. Afterwards I also realized that more people
    /// had also tried the top-down solution as well:
    /// https://leetcode.com/problems/smallest-string-starting-from-leaf/solutions/231102/bottom-up-vs-top-down/comments/240564
    ///
    /// Time complexity: O(nlog(n)) - We visit each node in the tree, for each node we push its char
    /// into the current path, then, before we return, we pop it, all of which is O(1) but when we
    /// are on each leave, we compare the current path with the minimal string that we have seen so
    /// far. This comparison could be as long as the height of the tree for each leave in the
    /// worst case, that is the justification why I think the complexity is O(nlog(n)) worst case,
    /// not O(n) like other solutions say.
    /// Space complexity: O(h) - Both the path and the res queues can grow to a max of the height
    /// of the tree, which is between log2(n) and n.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.88 MB Beats 50%
    #[allow(dead_code)]
    pub fn smallest_from_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn compare_lexicographical_order(
            vec1: &VecDeque<char>,
            vec2: &VecDeque<char>,
        ) -> std::cmp::Ordering {
            for (char1, char2) in vec1.iter().zip(vec2.iter()) {
                if char1 < char2 {
                    return std::cmp::Ordering::Less;
                } else if char1 > char2 {
                    return std::cmp::Ordering::Greater;
                }
            }
            vec1.len().cmp(&vec2.len())
        }
        let mut res = VecDeque::from(['~']);
        let mut path = VecDeque::new();
        fn dfs(
            opt: Option<&Rc<RefCell<TreeNode>>>,
            path: &mut VecDeque<char>,
            res: &mut VecDeque<char>,
        ) {
            if let Some(rc) = opt {
                let node = rc.borrow();
                let val = (node.val as u8 + b'a') as char;
                path.push_front(val);
                match (node.left.as_ref(), node.right.as_ref()) {
                    (None, None) => {
                        // A leaf, compare the strings.
                        match compare_lexicographical_order(&path, &res) {
                            std::cmp::Ordering::Less => *res = path.clone(),
                            std::cmp::Ordering::Equal | std::cmp::Ordering::Greater => (),
                        }
                    }
                    _ => {
                        dfs(node.left.as_ref(), path, res);
                        dfs(node.right.as_ref(), path, res);
                    }
                }
                path.pop_front();
            }
        }
        dfs(root.as_ref(), &mut path, &mut res);
        res.iter().collect()
    }

    /// This solution does not work! But since I did not realize that until later, I kept it here,
    /// it may be a good base for some other problem. Afterwards I also realized that more people
    /// had also tried the top-down solution as well:
    /// https://leetcode.com/problems/smallest-string-starting-from-leaf/solutions/231102/bottom-up-vs-top-down/comments/240564
    #[allow(dead_code)]
    pub fn smallest_from_leaf_nah(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn compare_lexicographical_order(vec1: &Vec<char>, vec2: &Vec<char>) -> std::cmp::Ordering {
            for (char1, char2) in vec1.iter().zip(vec2.iter()) {
                if char1 < char2 {
                    return std::cmp::Ordering::Less;
                } else if char1 > char2 {
                    return std::cmp::Ordering::Greater;
                }
            }
            vec1.len().cmp(&vec2.len())
        }
        fn dfs(opt: Option<&Rc<RefCell<TreeNode>>>) -> Option<Vec<char>> {
            match opt {
                Some(rc) => {
                    let node = rc.borrow();
                    let val = (node.val as u8 + b'a') as char;
                    match (dfs(node.left.as_ref()), dfs(node.right.as_ref())) {
                        (None, None) => Some(vec![val]),
                        (Some(mut v), None) | (None, Some(mut v)) => {
                            v.push(val);
                            Some(v)
                        }
                        (Some(mut l), Some(mut r)) => {
                            l.push(val);
                            r.push(val);
                            match compare_lexicographical_order(&l, &r) {
                                std::cmp::Ordering::Less | std::cmp::Ordering::Equal => Some(l),
                                std::cmp::Ordering::Greater => Some(r),
                            }
                        }
                    }
                }
                None => None,
            }
        }
        dfs(root.as_ref())
            .expect("At least one node")
            .iter()
            .collect()
        // If root could be None:
        // match dfs(root.as_ref()) {
        //     Some(v) => v.iter().collect(),
        //     None => "".to_string(),
        // }
    }
}

// Tests.
fn main() {
    println!("\n\x1b[92m» No tests in this file...\x1b[0m");
}
