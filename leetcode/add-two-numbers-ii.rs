// 445. Add Two Numbers II
// 🟠 Medium
//
// https://leetcode.com/problems/add-two-numbers-ii/
//
// Tags: Linked List - Math - Stack

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
    /// Use the solution to problems that have been solved previously as the
    /// base for solving this one, reverse the input lists and add them, then
    /// return the result in reverse.
    ///
    /// Time complexity: O(n) - We visit each node.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 3 ms Beats 87.50%
    /// Memory 2.21 MB Beats 50.00%
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        Self::reverse_list(Self::add_two_helper(
            Self::reverse_list(l1),
            Self::reverse_list(l2),
        ))
    }

    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let (mut prev, mut curr) = (None, head);
        while let Some(mut node) = curr {
            curr = node.next;
            node.next = prev;
            prev = Some(node);
        }
        prev
    }

    pub fn add_two_helper(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(-1));
        let mut curr = &mut dummy;
        let (mut a, mut b) = (&l1, &l2);
        let mut carry = 0;
        // let mut val = 0;
        while *a != None || *b != None || carry != 0 {
            if let Some(node) = a {
                carry += node.val;
                a = &node.next;
            }
            if let Some(node) = b {
                carry += node.val;
                b = &node.next;
            }
            curr.next = Some(Box::new(ListNode::new(carry % 10)));
            curr = curr.next.as_mut().unwrap();
            carry /= 10;
        }
        dummy.next
    }
}

// Tests.
fn main() {
    println!("[92m» All tests passed![0m")
}
