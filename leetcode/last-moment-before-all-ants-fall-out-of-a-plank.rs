// 1503. Last Moment Before All Ants Fall Out of a Plank
// 🟠 Medium
//
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
//
// Tags: Array - Brainteaser - Simulation

struct Solution;
impl Solution {
    /// When ants collide, they turn around but, if we ignore their labels, it
    /// is effectively the same as ignoring each other, the result of a collision
    /// is still one ant going in each direction at the same speed, and with the
    /// same position as before the collision. We just need to find how long it
    /// takes the leftmost and to fall off the right edge, and how long it takes
    /// the rightmost and to fall off the left edge, and return the max between
    /// these two values. We iterate both input vectors to find the maximum value
    /// in left and the minimum value in right. If the input vectors were sorted
    /// we could just pick the last and first and return the result in O(1)
    ///
    /// Time complexity: O(m+n) - Visit each element in both vectors to find
    /// the maximum of left and minimum of right.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.14 MB Beats 100%
    pub fn get_last_moment(n: i32, left: Vec<i32>, right: Vec<i32>) -> i32 {
        left.into_iter()
            .max()
            .unwrap_or(0)
            .max(n - right.into_iter().min().unwrap_or(n))
    }
}

// Tests.
fn main() {
    let tests = [
        (10, vec![], vec![], 0),
        (4, vec![4, 3], vec![0, 1], 4),
        (7, vec![], vec![0, 1, 2, 3, 4, 5, 6, 7], 7),
        (7, vec![0, 1, 2, 3, 4, 5, 6, 7], vec![], 7),
    ];
    for t in tests {
        assert_eq!(Solution::get_last_moment(t.0, t.1, t.2), t.3);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
