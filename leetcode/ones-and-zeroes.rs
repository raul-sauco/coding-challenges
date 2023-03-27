// 474. Ones and Zeroes
// 🟠 Medium
//
// https://leetcode.com/problems/ones-and-zeroes/
//
// Tags: Array - String - Dynamic Programming

struct Solution;
impl Solution {
    /// We can use dynamic programming, this problem is similar to the classic
    /// coin change problem, we can keep a dp object where the entries
    /// dp(i,j)= x represent the maximum number of substrings that we can use
    /// while keeping a maximum of i zeroes and j ones. For each substring in
    /// the input array of substrings, we iterate over all the keys, a maximum
    /// of 1e4, checking if we could add the number of zeroes and ones to the
    /// current dictionary entry without going over the limits m and n.
    ///
    /// Time complexity: O(m*n*s) - Where s is the length of strs. We iterate
    /// over all strings s and, for each, we iterate all the existing keys in
    /// the dp dictionary. m and n are limited to 100, we could simplify to
    /// O(s*1e4) ≈ O(s) but, in the context of the problem is a big enough
    /// that I think it is more accurate to not simplify. We could go even
    /// further and, since len(strs) <= 600, and that is also a small value,
    /// O(100*100*600) ≈ O(1)
    /// Space complexity: O(m*n) - The dp dictionary.
    ///
    /// Runtime 21 ms Beats 100%
    /// Memory 2.3 MB Beats 100%
    pub fn find_max_form(strs: Vec<String>, m: i32, n: i32) -> i32 {
        let (m, n) = ((m + 1) as usize, (n + 1) as usize);
        let mut res = 0;
        let mut dp = vec![vec![-1; n]; m];
        dp[0][0] = 0;
        for s in strs {
            let (mut ones, mut zeroes) = (0, 0);
            for c in s.chars() {
                if c == '0' {
                    zeroes += 1;
                } else {
                    ones += 1;
                }
            }
            // Iterate over the dp matrix in reverse.
            for i in (0..m).rev() {
                for j in (0..n).rev() {
                    if zeroes > i || ones > j {
                        continue;
                    }
                    let (z, o) = (i - zeroes, j - ones);
                    if dp[z][o] != -1 {
                        dp[i][j] = dp[i][j].max(dp[z][o] + 1);
                        res = res.max(dp[i][j]);
                    }
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["10", "0", "1"], 1, 1, 2),
        (vec!["10", "0001", "111001", "1", "0"], 4, 3, 3),
        (vec!["10", "0001", "111001", "1", "0"], 5, 3, 4),
        (vec!["10", "0001", "111001", "1", "0"], 50, 50, 5),
    ];
    for t in tests {
        let strs =
            t.0.iter()
                .map(|&s| String::from(s))
                .collect::<Vec<String>>();
        assert_eq!(Solution::find_max_form(strs, t.1, t.2), t.3);
    }
    println!("All tests passed!")
}
