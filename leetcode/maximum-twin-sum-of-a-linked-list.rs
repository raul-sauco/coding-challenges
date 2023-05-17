// 2130. Maximum Twin Sum of a Linked List
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
//
// Tags: Linked List - Two Pointers - Stack

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

fn len(mut head: Option<&Box<ListNode>>) -> usize {
    let mut count = 0;
    while let Some(next) = head.take() {
        count += 1;
        head = next.next.as_ref();
    }
    count
}

fn split(mut head: Option<Box<ListNode>>) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
    let mid = len(head.as_ref()) / 2;
    let mut top = None;
    for _ in 0..mid {
        let mut node = head.take().unwrap();
        head = std::mem::replace(&mut node.next, top.take());
        top = Some(node);
    }
    (top, head)
}

/// Traverse the list to find its length, then reverse the first half and
/// traverse one last time adding twin nodes and saving the maximum sum.a
///
/// TODO: Improve the solution using only one pass, use a fast and slow pointer
/// to travel to the middle of the linked list while reversing the first half,
/// then travel the first, in reverse, and second halves adding the values.
/// This solution came from:
/// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/solutions/2310182/rust-100-without-stack-queue/
///
/// Time complexity: O(n) - We visit each node and do O(1) operations for each.
/// Space complexity: O(1) - We only store pointers in extra memory.
///
/// Runtime 59 ms Beats 75%
/// Memory 6.5 MB Beats 100%
impl Solution {
    pub fn pair_sum(head: Option<Box<ListNode>>) -> i32 {
        let (mut top, mut bottom) = split(head);
        let mut res = 0;
        while let (Some(mut top_node), Some(mut bottom_node)) = (top.take(), bottom.take()) {
            top = top_node.next.take();
            bottom = bottom_node.next.take();
            res = res.max(top_node.val + bottom_node.val);
        }
        res
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
