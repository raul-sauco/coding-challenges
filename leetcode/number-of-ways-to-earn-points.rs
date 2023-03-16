// 2585. Number of Ways to Earn Points
// 🔴 Hard
//
// https://leetcode.com/problems/number-of-ways-to-earn-points/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    // A very interesting solution from Lee215
    // https://leetcode.com/problems/number-of-ways-to-earn-points/solutions/3258120
    // It simplifies quite a bit the code and improves the runtime a lot.
    //
    // Time complexity: O(n*c*t) -  n: the number of questions * c: the
    // maximum value of count * t the possible values that the target can
    // take 0..t.
    // Space complexity: O(t) - The size of the DP array used.
    //
    // Runtime 52 ms Beats 33.33%
    // Memory 2.1 MB Beats 91.67%
    pub fn ways_to_reach_target(target: i32, types: Vec<Vec<i32>>) -> i32 {
        // Convert the types to facilitate working with them.
        let target = target as usize;
        let types: Vec<(usize, usize)> = types
            .iter()
            .map(|v| (v[0] as usize, v[1] as usize))
            .collect();
        let mut dp = vec![0; target + 1];
        dp[0] = 1;
        const MOD: i32 = 10_i32.pow(9) + 7;
        for (count, mark) in types {
            for i in (0..target + 1).rev() {
                for k in 1..count.min(i / mark) + 1 {
                    dp[i] = (dp[i] + dp[i - mark * k]) % MOD;
                }
            }
        }
        *dp.last().unwrap()
    }
}

// Tests.
fn main() {
    let tests = [
        (6, vec![vec![6, 1], vec![3, 2], vec![2, 3]], 7),
        (18, vec![vec![6, 1], vec![3, 2], vec![2, 3]], 1),
    ];
    for t in tests {
        assert_eq!(Solution::ways_to_reach_target(t.0, t.1), t.2);
    }
    println!("All tests passed!")
}
