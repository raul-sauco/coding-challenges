// 1675. Minimize Deviation in Array
// 🔴 Hard
//
// https://leetcode.com/problems/minimize-deviation-in-array/
//
// Tags: Array - Greedy - Heap (Priority Queue) - Ordered Set

struct Solution;
impl Solution {
    // The problem lets us do two operations on the input array elements,
    // for even numbers, it lets us divide them by 2 as long as they remain
    // even, for odd numbers, we can multiply them by 2 once, then they
    // become even. To simplify the problem, we can start by multiplying all
    // odd values by 2, that way each element is at the maximum it can be,
    // and them pushing them all into a max heap after checking the value
    // of the smallest item in the heap. While we can make the biggest
    // current element smaller, that is while the top of the heap is even,
    // and we can divide it by 2, we will pop that element and compute the
    // current difference between it and the smallest element currently in
    // the heap, if the gap is the smallest seen so far, we will record it as
    // the temporary result, then we divide the value by 2 and push it back
    // into the heap. When we find an odd element as the top of the heap, we
    // know that we cannot make it any smaller and so we can stop iterating.
    //
    // Time complexity: O(n*log(n)) - We may pop and push all elements in the
    // input array a certain number of times t, t has a logarithmic relation
    // to the value of the element and its upper bound is 30 because of
    // log2(10^9), therefore time complexity is n*30*log(n) and we can
    // simplify it.
    // Space complexity: O(n) - The heap will have the same size as nums.
    //
    // Runtime 85 ms Beats 79%
    // Memory 3 MB Beats 46%
    pub fn minimum_deviation(nums: Vec<i32>) -> i32 {
        use std::{collections::BinaryHeap, i32::MAX};
        let vals: Vec<i32> = nums
            .iter()
            .map(|x| if x % 2 != 0 { x * 2 } else { *x })
            .collect();
        let mut smallest = *vals.iter().min().unwrap();
        let mut heap = BinaryHeap::from(vals);
        let mut res = MAX;
        while heap.peek().unwrap() % 2 == 0 {
            match heap.pop() {
                Some(val) => {
                    if val - smallest < res {
                        res = val - smallest;
                    }
                    let val = val / 2;
                    if val < smallest {
                        smallest = val;
                    }
                    heap.push(val);
                }
                None => unreachable!(),
            }
        }
        res.min(heap.peek().unwrap() - smallest)
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::minimum_deviation(vec![10, 4, 3]), 2);
    assert_eq!(Solution::minimum_deviation(vec![2, 10, 8]), 3);
    assert_eq!(Solution::minimum_deviation(vec![1, 2, 3, 4]), 1);
    assert_eq!(Solution::minimum_deviation(vec![4, 1, 5, 20, 3]), 3);
    println!("All tests passed!")
}
