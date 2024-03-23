// 234. Palindrome Linked List
// 🟢 Easy
//
// https://leetcode.com/problems/palindrome-linked-list/
//
// Tags: Linked List - Two Pointers - Stack - Recursion

mod linked_list;
use linked_list::{LinkedList, ListNode};

struct Solution;
impl Solution {
    /// Reverse the first half of the linked list, iterate over the reverse front and regular back
    /// checking that the values in the nodes match. Handle uneven length lists by skipping one
    /// node in the back before starting to compare nodes. To reverse the first half I first
    /// iterated over the list once to get the node count. I could not figure out how to iterate
    /// using fast/slow pointers while reversing the nodes on the slow pointer side, the problem is
    /// the box references, I would have been able to do it if the ListNodes were wrapped in
    /// Rc<RefCell<_>>.
    ///
    /// Time complexity: O(n) - We iterate twice over the nodes in the list.
    /// Space complexity: O(1) - Constant extra space used, pointers.
    ///
    /// Runtime 53 ms Beats 30%
    /// Memory 7.47 MB Beats 57%
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut node_count = 0;
        let mut cur = &head;
        while let Some(node) = cur {
            cur = &node.next;
            node_count += 1;
        }
        // Reverse the first half of the linked list.
        let (mut prev, mut curr) = (None, head);
        let mut reverse_count = node_count / 2;
        while let Some(mut node) = curr {
            curr = node.next;
            node.next = prev;
            prev = Some(node);
            reverse_count -= 1;
            if reverse_count == 0 {
                break;
            }
        }
        if node_count == 1 {
            return true;
        }
        if node_count % 2 == 1 {
            curr = curr.unwrap().next;
        }
        let (mut f, mut b) = (&prev, &curr);
        while let (Some(front), Some(back)) = (f, b) {
            if &front.val != &back.val {
                return false;
            }
            f = &front.next;
            b = &back.next;
        }
        true
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], true),
        (vec![1, 2], false),
        (vec![1, 2, 2, 1], true),
        (vec![1, 2, 3, 2, 1], true),
        (vec![6, 2, 3, 9, 5, 9, 3, 2, 6], true),
        (vec![6, 1, 3, 9, 5, 9, 3, 2, 6], false),
        (vec![6, 1, 3, 9, 5, 5, 9, 3, 2, 6], false),
        (vec![6, 2, 3, 9, 5, 5, 9, 3, 2, 6], true),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let head = LinkedList::from_list(t.0.clone()).head;
        let res = Solution::is_palindrome(head);
        if res == t.1 {
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
