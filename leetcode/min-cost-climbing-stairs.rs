// 746. Min Cost Climbing Stairs
// 🟢 Easy
//
// https://leetcode.com/problems/min-cost-climbing-stairs/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// Use two variables to compute the cost of reaching each step.
    ///
    /// Time complexity: O(n) - We visit each element and do constant time work
    /// for each.
    /// Space complexity: O(1) - We use two integers of extra memory.
    ///
    /// Runtime 1 ms Beats 67.24%
    /// Memory 2 MB Beats 91.38%
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let (mut a, mut b) = (0, 0);
        for i in 0..cost.len() {
            (a, b) = (b, cost[i] + a.min(b));
        }
        a.min(b)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![10, 15, 20], 15),
        (vec![1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ];
    for t in tests {
        assert_eq!(Solution::min_cost_climbing_stairs(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
