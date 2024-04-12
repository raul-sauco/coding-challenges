// 42. Trapping Rain Water
// 🔴 Hard
//
// https://leetcode.com/problems/trapping-rain-water/
//
// Tags: Array - Two Pointers - Dynamic Programming - Stack - Monotonic Stack

struct Solution;
impl Solution {
    /// Use two pointers, the minimum height between them is the maximum water that we will be able
    /// to collect if some of the bars between them have a lower height.
    ///
    /// Time complexity: O(n) - We visit each position in the input once and do O(1) work for each.
    /// Space complexity: O(1) - We store several integers.
    ///
    /// Runtime 2 ms Beats 72%
    /// Memory 2.22 MB Beats 57%
    #[allow(dead_code)]
    pub fn trap_if(height: Vec<i32>) -> i32 {
        let (mut water_trapped, mut l, mut r) = (0, 0, height.len() - 1);
        let (mut max_left, mut max_right) = (height[l], height[r]);
        while l + 1 < r {
            if max_left < max_right {
                l += 1;
                if height[l] > max_left {
                    max_left = height[l];
                } else if height[l] < max_left {
                    water_trapped += max_left - height[l];
                }
            } else {
                r -= 1;
                if height[r] > max_right {
                    max_right = height[r];
                } else if height[r] < max_right {
                    water_trapped += max_right - height[r];
                }
            }
        }
        water_trapped
    }

    /// Same solution but use cmp.
    ///
    /// Time complexity: O(n) - We visit each position in the input once and do O(1) work for each.
    /// Space complexity: O(1) - We store several integers.
    ///
    /// Runtime 2 ms Beats 72%
    /// Memory 2.22 MB Beats 57%
    pub fn trap(height: Vec<i32>) -> i32 {
        let (mut water_trapped, mut l, mut r) = (0, 0, height.len() - 1);
        let (mut max_left, mut max_right) = (height[l], height[r]);
        while l + 1 < r {
            if max_left < max_right {
                l += 1;
                match max_left.cmp(&height[l]) {
                    std::cmp::Ordering::Less => max_left = height[l],
                    std::cmp::Ordering::Equal => (),
                    std::cmp::Ordering::Greater => water_trapped += max_left - height[l],
                }
            } else {
                r -= 1;
                match max_right.cmp(&height[r]) {
                    std::cmp::Ordering::Less => max_right = height[r],
                    std::cmp::Ordering::Equal => (),
                    std::cmp::Ordering::Greater => water_trapped += max_right - height[r],
                }
            }
        }
        water_trapped
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0], 0),
        (vec![4, 2, 0, 3, 2, 5], 9),
        (vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::trap(t.0.clone());
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
