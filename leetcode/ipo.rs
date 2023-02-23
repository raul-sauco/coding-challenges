// 502. IPO
// 🔴 Hard
//
// https://leetcode.com/problems/ipo/
//
// Tags: Array - Greedy - Sorting - Heap (Priority Queue)

struct Solution;
impl Solution {
    // We want to greedily pick the job that gives us the maximum gain out of
    // the jobs that are available to us. We can use a heap to keep a list of
    // jobs sorted in reversed order by capital and a heap with the top
    // element being the one that gives us the maximum profit, after we
    // complete each job we update our current capital and iterate over the
    // jobs adding any available jobs to the heap, then pick the top job from
    // the heap in O(log(h)).
    //
    // Time complexity: O(n*log(n)) - Sorting n jobs has a O(n*log(n))
    // complexity, then we iterate k times on which we pop elements from the
    // sorted list in O(1) and append them to the heap in O(log(h)) where h
    // is the current size of the heap and has an upper bound of n. Then we
    // pop from the heap in O(log(h)), it would seem that the complexity is
    // then O(k*n*log(n)) but, since any of the n jobs will be popped from the
    // list and added to the heap a maximum of 1 time, we know that the limit
    // of O(log(h)) insertions is n, since h is also bound to n, the time
    // complexity of both sections of the algorithm is the same, O(n*log(n)).
    // Space complexity: O(n) - Both the sorted list and the heap can grow to
    // a size of n.
    //
    // Runtime 47 ms Beats 50%
    // Memory 5.2 MB Beats 16.67%
    pub fn find_maximized_capital(k: i32, w: i32, profits: Vec<i32>, capital: Vec<i32>) -> i32 {
        use std::collections::BinaryHeap;
        let mut sorted_jobs: Vec<(i32, i32)> = (0..profits.len())
            .map(|i| (capital[i], profits[i]))
            .collect();
        sorted_jobs.sort();
        sorted_jobs.reverse();
        let mut heap = BinaryHeap::<i32>::new();
        // The current capital.
        let mut cap = w;
        for _ in 0..k {
            while sorted_jobs.len() > 0 && sorted_jobs[sorted_jobs.len() - 1].0 <= cap {
                match sorted_jobs.pop() {
                    Some((_, p)) => heap.push(p),
                    None => panic!("We checked that there were jobs already!"),
                }
            }
            match heap.pop() {
                Some(v) => cap += v,
                None => break,
            }
        }
        cap
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::find_maximized_capital(1, 0, vec![1, 2, 3], vec![1, 1, 2]),
        0
    );
    assert_eq!(
        Solution::find_maximized_capital(2, 0, vec![1, 2, 3], vec![0, 1, 1]),
        4
    );
    assert_eq!(
        Solution::find_maximized_capital(3, 0, vec![1, 2, 3], vec![0, 1, 2]),
        6
    );
    println!("All tests passed!")
}
