// 456. 132 Pattern
// 🟠 Medium
//
// https://leetcode.com/problems/132-pattern/
//
// Tags: Array - Binary Search - Stack - Monotonic Stack - Ordered Set

struct Solution;
impl Solution {
    /// Precompute an array of minimum prefix at each position, then iterate
    /// from the back of the input storing the biggest values seen to the right.
    /// At each position, we pop any values from the stack that are smaller than
    /// the minimum at the current point, since we won't be able to use them,
    /// then we check if the current value is a peak between the top of the
    /// stack and the minimum to the left, if it is, we return true, we found a
    /// 132 pattern, otherwise we push the value into the monotonic stack, where
    /// it will be the smallest value at the top, and keep searching.
    ///
    /// Time complexity: O(n) - We iterate twice over the input array, once
    /// forward and once backwards, we also may push and pop each element into
    /// the stack, but once at most.
    /// Space complexity: O(n) - The vector of minimums and the stack are O(n)
    ///
    /// Runtime 9 ms Beats 25.40%
    /// Memory 5.34 MB Beats 9.89%
    pub fn find132pattern(nums: Vec<i32>) -> bool {
        let mins = nums
            .iter()
            .scan(nums[0], |state, &x| {
                *state = x.min(*state);
                Some(*state)
            })
            .collect::<Vec<i32>>();
        // A monotonic stack with the biggest values seen to the right.
        let mut stack = vec![nums[nums.len() - 1]];
        for i in (0..nums.len() - 1).rev() {
            if nums[i] <= mins[i] {
                continue;
            }
            while !stack.is_empty() && *stack.last().unwrap() <= mins[i] {
                stack.pop();
            }
            if !stack.is_empty() && *stack.last().unwrap() < nums[i] {
                return true;
            }
            stack.push(nums[i]);
        }
        false
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 1, 4, 2], true),
        (vec![-1, 3, 2, 0], true),
        (vec![1, 2, 3, 4], false),
        (vec![3, 5, 0, 3, 4], true),
        (vec![1, 0, 1, -4, -3], false),
    ];
    for t in tests {
        assert_eq!(Solution::find132pattern(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
