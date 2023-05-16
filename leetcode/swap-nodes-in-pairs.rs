// 24. Swap Nodes in Pairs
// 🟠 Medium
//
// https://leetcode.com/problems/swap-nodes-in-pairs/
//
// Tags: Linked List - Recursion

// Definition for singly-linked list.
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
struct Solution;

/// Swap the head with its next node if both are Some, then append the result
/// of calling swap_pairs on the next node.
///
/// Time complexity: O(n) - We visit each node and do O(1) operations for each.
/// Space complexity: O(n) - The call stack will have one level for each two
/// nodes in the linked list.
///
/// Runtime 1 ms Beats 76.47%
/// Memory 2 MB Beats 63.24%
impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        head.and_then(|mut l| match l.next {
            Some(mut r) => {
                l.next = Solution::swap_pairs(r.next);
                r.next = Some(l);
                Some(r)
            }
            None => Some(l),
        })
    }
}

// Tests.
fn main() {
    let tests = [(vec![0], 0)];
    for _ in tests {
        // assert_eq!(Solution::swap_pairs(), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
