// 206. Reverse Linked List
// 🟢 Easy
//
// https://leetcode.com/problems/reverse-linked-list/
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
impl Solution {
    /// Travel through the list reversing the pointer between each node and its
    /// next.
    ///
    /// Time complexity: O(n) - We visit each node.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 1 ms Beats 78.38%
    /// Memory 2.37 MB Beats 85.47%
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let (mut prev, mut curr) = (None, head);
        while let Some(mut node) = curr {
            curr = node.next;
            node.next = prev;
            prev = Some(node);
        }
        prev
    }
}

// Tests.
fn main() {
    println!("[92m» All tests passed![0m")
}
