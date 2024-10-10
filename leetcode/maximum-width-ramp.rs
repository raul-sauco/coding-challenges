// 962. Maximum Width Ramp
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-width-ramp/
//
// Tags: Array - Stack - Monotonic Stack

struct Solution;
impl Solution {
    /// One pass using monotonic stack, but for each value iterate the monotonic stack back while
    /// the top of the stack is less or equal to the current value.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(n)
    ///
    /// Runtime 8 ms Beats 20%
    /// Memory 2.86 MB Beats 20%
    #[allow(dead_code)]
    pub fn max_width_ramp_one_pass(nums: Vec<i32>) -> i32 {
        let mut seen = vec![0];
        let mut res = 0;
        for i in 1..nums.len() {
            let mut seen_idx = seen.len() - 1;
            if nums[i] < nums[seen[seen_idx]] {
                seen.push(i);
            } else {
                while nums[i] >= nums[seen[seen_idx]] {
                    res = res.max(i - seen[seen_idx]);
                    if seen_idx == 0 {
                        break;
                    }
                    seen_idx -= 1;
                }
            }
        }
        res as _
    }

    /// Two passes, create a monotonic non-increasing stack on the first one, on the second pass,
    /// find indexes of the greatest ramp.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(n)
    ///
    /// Runtime 7 ms Beats 20%
    /// Memory 2.77 MB Beats 20%
    pub fn max_width_ramp(nums: Vec<i32>) -> i32 {
        let mut stack = vec![];
        for i in 0..nums.len() {
            if stack.is_empty() || nums[stack[stack.len() - 1]] > nums[i] {
                stack.push(i);
            }
        }
        let mut res = 0;
        for i in (0..nums.len()).rev() {
            while !stack.is_empty() && nums[*stack.last().unwrap()] <= nums[i] {
                res = res.max(i - stack.pop().unwrap());
            }
        }
        res as _
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![6, 2], 0),
        (vec![6, 0, 8, 2, 1, 5], 4),
        (vec![9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_width_ramp(t.0.clone());
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
