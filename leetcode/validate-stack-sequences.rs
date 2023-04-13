// 946. Validate Stack Sequences
// 🟠 Medium
//
// https://leetcode.com/problems/validate-stack-sequences/
//
// Tags: String - Stack - Simulation

struct Solution;
impl Solution {
    /// Use an extra stack of memory and simulate the operations that took
    /// place, push the next element, then, while the top of the stack matches
    /// the next element that needs to be popped, pop it.
    ///
    /// Time complexity: O(n) - We visit each element on the pushed array and
    /// do amortized O(1) for each.
    /// Space complexity: O(n) - The stack can grow to the same size as the
    /// input.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.1 MB Beats 90%
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut stack = vec![];
        let mut pop_idx = 0;
        for val in pushed {
            stack.push(val);
            while !stack.is_empty() && *stack.last().unwrap() == popped[pop_idx] {
                stack.pop();
                pop_idx += 1;
            }
        }
        stack.is_empty()
    }
}

// Tests.
fn main() {
    let tests = [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], true),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], false),
    ];
    for t in tests {
        assert_eq!(
            Solution::validate_stack_sequences(Vec::from(t.0), Vec::from(t.1)),
            t.2
        );
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
