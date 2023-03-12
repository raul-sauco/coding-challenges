// 23. Merge k Sorted Lists
// 🔴 Hard
//
// https://leetcode.com/problems/merge-k-sorted-lists/
//
// Tags: Linked List - Divide and Conquer - Heap (Priority Queue) -
// Merge Sort

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
    // A divide and conquer approach will merge lists two at a time, it will
    // result in m//2 number of lists of average double the length, we keep
    // doing this until we only have one list and return that list,
    // effectively reducing the problem to multiple instances of merge 2
    // sorted lists.
    //
    // Time complexity: O(n*log(m)) - With n the number of items and m the
    // initial number of lists, on each step we run over all the items in
    // two lists and we halve the number of lists at each step.
    // Space complexity: O(1) - If we don't take into account input/output
    // list nodes.
    //
    // Runtime 13 ms Beats 38.10%
    // Memory 4 MB Beats 5.95%
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        if lists.is_empty() {
            return None;
        }
        let mut lists = lists.clone();
        let mut merged_lists;
        while lists.len() > 1 {
            merged_lists = vec![];
            for i in (0..lists.len()).step_by(2) {
                merged_lists.push(Self::merge_two_lists(
                    lists[i].clone(),
                    if i + 1 < lists.len() {
                        lists[i + 1].clone()
                    } else {
                        None
                    },
                ));
            }
            lists = merged_lists
        }
        lists[0].to_owned()
    }

    pub fn merge_two_lists(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        match (list1, list2) {
            (Some(list1), None) => Some(list1),
            (None, Some(list2)) => Some(list2),
            (None, None) => None,
            (Some(l1), Some(l2)) => {
                if l1.val < l2.val {
                    return Some(Box::new(ListNode {
                        val: l1.val,
                        next: Solution::merge_two_lists(l1.next, Some(l2)),
                    }));
                } else {
                    return Some(Box::new(ListNode {
                        val: l2.val,
                        next: Solution::merge_two_lists(Some(l1), l2.next),
                    }));
                }
            }
        }
    }
}

struct Solution2;
impl Solution2 {
    // A naive solution, collect the values in an array, sort them and then
    // generate the result linked list, besides being simple, this solution
    // performs pretty well, credits to .
    // https://leetcode.com/problems/merge-k-sorted-lists/solutions/2406489/
    //
    // Time complexity: O(n*log(m)) - We iterate over all list nodes in O(n)
    // to collect their values, then sort them in O(n*log(n)) and then
    // iterate over the values in O(n) to create the result linked list.
    // Space complexity: O(n) - We use an array of values of size n.
    //
    // Runtime 5 ms Beats 79.76%
    // Memory 3.1 MB Beats 74.40%
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        if lists.is_empty() {
            return None;
        }
        // Collect all values into a vector.
        let mut vals = vec![];
        lists.iter().for_each(|list| {
            let mut node = list.as_ref();
            while node.is_some() {
                vals.push(node.unwrap().val);
                node = node.unwrap().next.as_ref();
            }
        });
        vals.sort_unstable();
        // Build the result linked list backwards starting by the tail.
        let mut head = None;
        vals.iter().rev().for_each(|&val| {
            head = Some(Box::new(ListNode {
                val,
                next: head.take(),
            }))
        });
        head
    }
}
// Tests.
fn main() {
    // let tests = [];
    // for test in tests {
    //     unimplemented!();
    // }
    println!("No tests for this file!")
}
