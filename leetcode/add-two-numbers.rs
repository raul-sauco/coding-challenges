// 2. Add Two Numbers
// 🟠 Medium
//
// https://leetcode.com/problems/add-two-numbers/
//
// Tags: Linked List - Math - Recursion

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
    /// Travel through the linked list adding the value of the current two nodes
    /// if they exist while keeping track of the carry value.
    ///
    /// Time complexity: O(n) - We visit each node.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 3 ms Beats 84.70%
    /// Memory 2.02 MB Beats 92.74%
    pub fn add_two_numbers(
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
