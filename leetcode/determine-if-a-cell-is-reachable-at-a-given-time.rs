// 2849. Determine if a Cell Is Reachable at a Given Time
// 🟠 Medium
//
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/
//
// Tags: Math

struct Solution;
impl Solution {
    /// Handle the edge case where start and end are the same and we only have one
    /// unit of time, then check that both the x and y distances are less or equal
    /// to the given amount of time.
    ///
    /// Time complexity: O(1)
    /// Space complexity: O(1)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.03 MB Beats 45.45%
    pub fn is_reachable_at_time(sx: i32, sy: i32, fx: i32, fy: i32, t: i32) -> bool {
        !(sx == fx && sy == fy && t == 1) && t >= (sx - fx).abs() && t >= (sy - fy).abs()
    }
}

// Tests.
fn main() {
    let tests = [
        (1, 2, 1, 2, 1, false),
        (1, 3, 5, 1, 3, false),
        (2, 4, 7, 7, 6, true),
        (3, 1, 7, 3, 3, false),
    ];
    for t in tests {
        assert_eq!(Solution::is_reachable_at_time(t.0, t.1, t.2, t.3, t.4), t.5);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
