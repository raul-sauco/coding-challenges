// 518. Coin Change II
// 🟠 Medium
//
// https://leetcode.com/problems/coin-change-ii/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /**
     * Use an array of the same size as amount plus one where each position
     * stores the number of different combinations that we have to build up
     * to that amount. We initialize the array with all zeroes except for
     * i == 0 that we initialize at 1 to represent that there is one way to
     * make up 0, not choose any coins. Then we iterate over the coins, for
     * each coin, we iterate over all the positions in dp from coin to the
     * end, the number of ways we can get there is the number of ways
     * currently plus the number of ways that we can get to i - coin, because
     * we can use one of these coins to get there from i - coin and we can do
     * that in as many different ways as we can get to i - coin.
     *
     * Time complexity: O(m*n) - We iterate over the number of coins and, in
     * the inner loop, over coin..amount.
     * Space complexity: O(n) - The size of the dp object.
     *
     * Runtime 0 ms Beats 100%
     * Memory 2 MB Beats 77.78%
     */
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        let n = amount as usize;
        let mut dp = vec![0; n + 1];
        // We have one way to come up with 0, not choosing any coin.
        dp[0] = 1;
        let mut c: usize;
        for coin in coins {
            c = coin as usize;
            for i in c..=n {
                dp[i] += dp[i - c];
            }
        }
        *dp.last().unwrap()
    }
}

// Tests.
fn main() {
    let tests = [
        (3, vec![2], 0),
        (10, vec![10], 1),
        (5, vec![1, 2, 5], 4),
        (500, vec![1, 2, 5], 12701),
    ];
    for test in tests {
        assert_eq!(Solution::change(test.0, test.1), test.2);
    }
    println!("All tests passed!")
}
