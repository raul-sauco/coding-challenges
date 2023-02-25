// 121. Best Time to Buy and Sell Stock
// 🟢 Easy
//
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    // The max profit will come from buying at the lowest price possible and
    // selling at the highest possible price after that lowest price. We can
    // keep a variable with the lowest price that we have seen so far, for
    // each element, first we check if its value is less than the current
    // lowest price, if it is, we update lowest price and move to the next
    // element, if it isn't, we check if the profit of buying at the current
    // lowest price and selling at this price is better than the current
    // maximum profit, if it is, we update it. Once we iterate over all
    // prices, we return the maximum profit found.
    //
    // Time complexity: O(n) - We visit each price once and do O(1) work.
    // Space complexity: O(1) - We use constant extra memory.
    //
    // Runtime 10 ms Beats 90.12%
    // Memory 2.9 MB Beats 97.27%
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut lowest_price = prices[0];
        let mut max_profit = 0;
        for price in prices {
            if price < lowest_price {
                lowest_price = price;
            } else {
                max_profit = max_profit.max(price - lowest_price);
            }
        }
        max_profit
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0);
    assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
    println!("All tests passed!")
}
