// 837. New 21 Game
// 🟠 Medium
//
// https://leetcode.com/problems/new-21-game/
//
// Tags: Math - Dynamic Programming - Sliding Window - Probability and Statistics

struct Solution {}
impl Solution {
    /// From each position, we can spread the possibilities that we have to end
    /// up having these many points into the max_pts different moves that we
    /// could make next. If we try to compute each forward position value, we
    /// will end up with O(mp*n) time complexity, instead, we can use a sliding
    /// window technique were we store the last max_pts (mp) elements' sum, at
    /// each position, we compute the probability of ending with that exact
    /// number of points as the sum of the sliding window, the preceding mp
    /// values, divided by the size of the sliding window.
    ///
    /// Time complexity: O(n) - We visit each position 1..=n and do O(1) work
    /// for each.
    /// Space complexity: O(n) - The size of the dp vector. If it was likely
    /// for max_pts to be much smaller than n, we could instead use a double
    /// ended queue as our dp object and pop the left elements as we iterate,
    /// that would let us use a max_pts-sized dp element.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.1 MB Beats 100%
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        let (n, k, mp, window_size) = (n as usize, k as usize, max_pts as usize, max_pts as f64);
        if k == 0 || n >= k + mp {
            return 1.0;
        }
        // We could use a double ended queue but both n and k <= 10^4.
        let mut dp = vec![0.0; n + 1];
        // We are certain to visit position 0.
        dp[0] = 1.0;
        let mut window_sum = 1.0;
        for i in 1..=n {
            dp[i] = window_sum / window_size;
            if i < k {
                window_sum += dp[i];
            }
            if i >= mp {
                window_sum -= dp[i - mp];
            }
        }
        dp[k..dp.len()].iter().sum()
    }
}

fn main() {
    let tests = [
        (1, 0, 2, 1.0),
        (6, 1, 10, 0.6),
        (10, 1, 10, 1.0),
        (21, 17, 10, 0.73278),
    ];
    for t in tests {
        assert_eq!(
            (Solution::new21_game(t.0, t.1, t.2) - t.3).abs() < 0.00001,
            true
        );
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
