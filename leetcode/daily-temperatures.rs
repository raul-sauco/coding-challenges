// 739. Daily Temperatures
// 🟠 Medium
//
// https://leetcode.com/problems/daily-temperatures/
//
// Tags: Array - Stack - Monotonic Stack

struct Solution;
impl Solution {
    /// Use a monotonic decreasing stack with the indexes of temperatures that we have seen
    /// already. Iterate over the input, for each element check its value against the top of the
    /// stack, while the temperature of the current element is greater than the temperature of the
    /// element at the top of the stack, pop it and update the result with the difference between
    /// the current index and the popped element index, since this is the first temperature after
    /// that one that was higher.
    ///
    /// Time complexity: O(n) - We visit each element, for each we do amortized O(1) work, we may
    /// need to pop n elements from the stack for one element, but that would mean that we did not
    /// pop any elements for any other.
    /// Space complexity: O(n) - The stack may grow to size n.
    ///
    /// Runtime 23 ms Beats 100%
    /// Memory 4.36 MB Beats 65.52%
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n = temperatures.len();
        let mut stack: Vec<usize> = vec![];
        let mut res = vec![0; n];
        for i in 0..n {
            while let Some(&top) = stack.last() {
                if temperatures[i] > temperatures[top] {
                    stack.pop();
                    res[top] = (i - top) as i32;
                } else {
                    break;
                }
            }
            stack.push(i);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![73, 74, 75, 71, 69, 72, 76, 73],
            vec![1, 1, 4, 2, 1, 1, 0, 0],
        ),
        (vec![30, 40, 50, 60], vec![1, 1, 1, 0]),
        (vec![30, 60, 90], vec![1, 1, 0]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::daily_temperatures(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
