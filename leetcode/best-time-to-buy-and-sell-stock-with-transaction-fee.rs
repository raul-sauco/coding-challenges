// 714. Best Time to Buy and Sell Stock with Transaction Fee
// 🟠 Medium
//
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
//
// Tags: Array - Dynamic Programming - Greedy

struct Dp {
    holding: i32,
    not_holding: i32,
}

struct Solution;
impl Solution {
    /// Iterate over the prices keeping track of the
    /// max profit at each index both holding and not holding stock. Recompute
    /// the maximums, holding will be the max of holding at the previous index
    /// or not holding at the previous index but buying stock at this index.
    /// Not holding will be the max of not holding at the previous index or
    /// holding at the previous index plus the gain from selling at the current
    /// price minus the fee.
    ///
    /// Time complexity: O(n) - We visit each price and do O(1) work for each.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 10 ms Beats 94.29%
    /// Memory 2.7 MB Beats 62.86%

    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        let mut prev = Dp {
            holding: -prices[0],
            not_holding: 0,
        };
        let mut next = Dp {
            holding: 0,
            not_holding: 0,
        };
        for price in prices[1..].iter() {
            // max profit holding stock
            next.holding = prev.holding.max(prev.not_holding - price);
            next.not_holding = prev.not_holding.max(prev.holding + price - fee);
            std::mem::swap(&mut prev, &mut next);
        }
        prev.holding.max(prev.not_holding)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 3, 2, 8, 4, 9], 2, 8),
        (vec![1, 3, 7, 5, 10, 3], 3, 6),
    ];
    for t in tests {
        assert_eq!(Solution::max_profit(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
