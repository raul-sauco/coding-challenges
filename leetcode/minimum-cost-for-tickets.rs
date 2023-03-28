// 983. Minimum Cost For Tickets
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-cost-for-tickets/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// The minimal cost at any given day when we need to travel will be the
    /// best between: the best 30 days past plus the cost of a 30 day ticket,
    /// the best 7 days past plus the cost of a 7 day ticket or the best 1 day
    /// past plus the cost of a 1 day ticket. If we don't need to travel, we
    /// can maintain the same best cost as the day before.
    ///
    /// Time complexity: O(n) - Where n is the last day we need to travel,
    /// days[-1] and it has an upper bound of 365, then O(n) ≈ O(1).
    /// Space complexity: O(n) - The dp array goes from 0 to days[-1].
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.1 MB Beats 89.66%
    pub fn mincost_tickets(days: Vec<i32>, costs: Vec<i32>) -> i32 {
        let n = *days.last().unwrap() as usize + 1;
        let mut dp = vec![0; n];
        let mut idx = 0;
        for i in 1..n {
            if i == days[idx] as usize {
                idx += 1;
                dp[i] = (dp[i - 1] + costs[0])
                    .min(costs[1] + if i >= 7 { dp[i - 7] } else { 0 })
                    .min(costs[2] + if i >= 30 { dp[i - 30] } else { 0 });
            } else {
                dp[i] = dp[i - 1];
            }
        }
        *dp.last().unwrap()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 4, 6, 7, 8, 20], vec![2, 7, 15], 11),
        (
            vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
            vec![2, 7, 15],
            17,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::mincost_tickets(t.0, t.1), t.2);
    }
    println!("All tests passed!")
}
