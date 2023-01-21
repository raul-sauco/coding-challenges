// 2543. Check if Point Is Reachable
// 🔴 Hard
//
// https://leetcode.com/problems/check-if-point-is-reachable/
//
// Tags: Greedy - Dynamic Programming - Math

struct Solution;
impl Solution {
    // Simulate the movements that are allowed but in reverse, starting at
    // the target point and trying to reach (1, 1).
    //
    // Time complexity: O(log(max(m, n))) - At each step we divide by 2
    // approximately, if one of the values is not divisible one loop, it will
    // became divisible in the next loop.
    // Space complexity: O(1) - We only store two integers and one tuple with
    // two elements.
    //
    // Runtime 1 ms Beats 100%
    // Memory 2.2 MB Beats 100%
    pub fn is_reachable(target_x: i32, target_y: i32) -> bool {
        let mut last = (-1, -1);
        let mut x = target_x;
        let mut y = target_y;
        while (x, y) != last {
            if x == 1 && y == 1 {
                return true;
            }
            last = (x, y);
            while x % 2 == 0 {
                x /= 2;
            }
            while y % 2 == 0 {
                y /= 2;
            }
            if x > y {
                x -= y;
            }
            if y > x {
                y -= x
            }
        }
        false
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::is_reachable(6, 9), false);
    assert_eq!(Solution::is_reachable(4, 7), true);
    println!("All tests passed!")
}
