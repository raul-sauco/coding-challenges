// 109. Convert Sorted List to Binary Search Tree
// 🟠 Medium
//
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
//
// Tags: Linked List - Divide and Conquer - Tree - Binary Search Tree - Binary Tree

// Definition for singly-linked list.
use std::cell::RefCell;
use std::rc::Rc;
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
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
    // Use a divide and conquer approach, use two pointers to find the middle
    // of the linked list, use the middle node as the root of the BST, then
    // use two recursive calls with the unused left and right linked lists to
    // generate the left and right subtrees. Solution inspired by:
    // https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solutions/3282679
    // Even though I find the two pointer solution more elegant, in Rust it
    // seems like converting to array and using the same logic as in 108
    // performs better.
    //
    // Time complexity: O(n) - Each node will be visited one, two or three
    // times.
    // Space complexity: O(log(n)) - The height of the call stack.
    //
    // Runtime 466 ms Beats 14.29%
    // Memory 4 MB Beats 42.86%
    pub fn sorted_list_to_bst(head: Option<Box<ListNode>>) -> Option<Rc<RefCell<TreeNode>>> {
        match head {
            Some(_) => Self::slice_to_bst(head.as_ref(), None),
            None => None,
        }
    }

    // An auxiliary function that converts a segment of a linked list to a BST
    // and returns the root.
    fn slice_to_bst(
        first: Option<&Box<ListNode>>,
        last: Option<&Box<ListNode>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        // If the segment is empty, return an empty tree.
        if first == last {
            return None;
        }
        // Use a fast and slow pointers.
        let (mut slow, mut fast) = (first, first);
        let mut fast_next: Option<&Box<ListNode>>;
        // Iterate over the list while fast is valid, i.e. not null or the last node
        // on the slice.
        while fast != last {
            // Move the auxiliary pointer one step and check if we could move another step.
            fast_next = fast.and_then(|node| node.next.as_ref());
            if fast_next == last {
                break;
            }
            // Move the slow pointer one step.
            slow = slow.and_then(|node| node.next.as_ref());
            // Fast needs to move two steps.
            fast = fast_next.and_then(|node| node.next.as_ref());
        }
        Some(Rc::new(RefCell::new(TreeNode {
            val: slow?.val,
            left: Self::slice_to_bst(first, slow),
            right: Self::slice_to_bst(slow?.next.as_ref(), last),
        })))
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3], 10, 1),
        (vec![3, 6, 7, 11], 8, 4),
        (vec![30, 11, 23, 4, 20], 5, 30),
        (vec![30, 11, 23, 4, 20], 6, 23),
        (
            vec![
                332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673,
                679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097,
                692137887, 718203285, 629455728, 941802184,
            ],
            823855818,
            14,
        ),
    ];
    for test in tests {
        unimplemented!();
    }
    println!("No tests for this file!")
}
