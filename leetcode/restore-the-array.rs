// 1416. Restore The Array
//🔴 Hard
//
// https://leetcode.com/problems/restore-the-array/
//
// Tags: String - Dynamic Programming

struct Solution;
impl Solution {
    /// Iterate over possible combinations of left and right indexes checking
    /// if the resulting substring is a valid substring. We can improve the
    /// performance using dynamic programming, storing the number of
    /// valid combinations up to and including s[l] and adding that number to
    /// s[r+1] every time we find a valid substring s[l:r].
    ///
    /// Time complexity: O(log(k) * n) - We iterate over all n start positions
    /// in s, for each, we iterate over a maximum of log(k) values until the
    /// integer formed by the digits s[l:r] goes over k and we break.
    /// Space complexity: O(log(k)) - The dp array has length log(k).
    ///
    /// Runtime 20 ms Beats 100%
    /// Memory 2.7 MB Beats 100%
    pub fn number_of_arrays(s: String, k: i32) -> i32 {
        let (m, n) = (k.to_string().len() + 1, s.len());
        let mut dp = vec![0; m];
        dp[0] = 1;
        let (mut dpl, mut dpr, mut num);
        let s: Vec<char> = s.chars().collect();
        let k = k as usize;
        for l in 0..n {
            dpl = l % m;
            if s[l] == '0' {
                dp[dpl] = 0;
                continue;
            }
            num = 0;
            for r in l..n {
                num = num * 10 + s[r].to_digit(10).unwrap() as usize;
                if num <= k {
                    dpr = (r + 1) % m;
                    dp[dpr] = (dp[dpr] + dp[dpl]) % 1_000_000_007
                } else {
                    break;
                }
            }
            // Reset, this is dp[dpr] for the next iteration.
            dp[dpl] = 0;
        }
        dp[n % m]
    }
}

// Tests.
fn main() {
    let tests = [
        ("1000", 10, 0),
        ("1000", 1000, 1),
        ("1317", 2000, 8),
        ("13171317", 20, 16),
    ];
    for t in tests {
        assert_eq!(Solution::number_of_arrays(String::from(t.0), t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m");
}
