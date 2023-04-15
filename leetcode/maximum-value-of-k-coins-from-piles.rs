// 2218. Maximum Value of K Coins From Piles
// 🔴 Hard
//
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
//
// Tags: Array - Dynamic Programming - Prefix Sum

struct Solution;
impl Solution {
    /// Use an array of size k+1 to store computed results, iterate over each
    /// pile and each value i in the range k..0, dp[i] represents the best
    /// way we have found to pick i coins at the current pile, we can update
    /// dp[i] as the best way to pick between 0 and k coins from the current
    /// pile, or between 0 and all the coins if len(pile) < k.
    ///
    /// Time complexity: O(m*min(n,k)*k) - Where m is the number of piles, n
    /// is the max number of coins in any pile and k is the number of coins
    /// that we can pick in total.
    /// Space complexity: O(max(n,k)) - The dp array has size k+1, we also
    /// use an array of prefix sums for each pile with a max size of n.
    ///
    /// Runtime 45 ms Beats 42.86%
    /// Memory 2.2 MB Beats 100%
    pub fn max_value_of_coins(piles: Vec<Vec<i32>>, k: i32) -> i32 {
        let k = k as usize;
        let mut dp = vec![0; k + 1];
        for pile in piles {
            let sums = [
                vec![0],
                pile.iter()
                    .scan(0, |sum, i| {
                        *sum += i;
                        Some(*sum)
                    })
                    .collect(),
            ]
            .concat();
            for i in (1..=k).rev() {
                for j in 0..(i + 1).min(sums.len()) {
                    let current = sums[j] + dp[i - j];
                    if current > dp[i] {
                        dp[i] = current;
                    }
                }
            }
        }
        *dp.last().unwrap()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1, 100, 3], vec![7, 8, 9]], 2, 101),
        (
            vec![
                vec![1, 10, 3],
                vec![7, 8, 9],
                vec![8, 20, 10],
                vec![50, 25, 18],
            ],
            3,
            93,
        ),
        (
            vec![
                vec![100],
                vec![100],
                vec![100],
                vec![100],
                vec![100],
                vec![100],
                vec![1, 1, 1, 1, 1, 1, 700],
            ],
            7,
            706,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::max_value_of_coins(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
