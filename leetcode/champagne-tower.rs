// 799. Champagne Tower
// 🟠 Medium
//
// https://leetcode.com/problems/champagne-tower/
//
// Tags: Dynamic Programming

struct Solution;
impl Solution {
    /// Iterate over n rows computing how much liquid falls into each glass and
    /// storing in a dp vector how much of it will overflow into the row below.
    ///
    /// Time complexity: O(n^2) - We iterate over n rows, each row has row_idx
    /// plus one items, for each item, we compute the amount that it overflows
    /// from it checking the two glasses above it.
    /// Space complexity: O(n) - We use two rows of length n of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.04 MB Beats 100%
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let n = query_row as usize;
        if n == 0 {
            return 1.min(0.max(poured)) as f64;
        }
        let mut dp = vec![0.0; n + 1];
        let mut prev = dp.clone();
        prev[0] = 0f64.max(poured as f64 - 1.0);
        // Check whether we have no overflows from the previous row and stop
        // iterating, the code passes the tests without this, but this flag
        // makes it faster.
        let mut no_overflows;
        // Compute overflows for all rows before the last one.
        for r in 1..n {
            no_overflows = true;
            dp[0] = 0f64.max((prev[0] / 2.0) - 1.0);
            if dp[0] > 0.0 {
                no_overflows = false;
            }
            for c in 1..r {
                dp[c] = 0f64.max((prev[c - 1] / 2.0 + prev[c] / 2.0) - 1.0);
                if dp[c] > 0.0 {
                    no_overflows = false;
                }
            }
            if no_overflows && r < n - 1 {
                return 0.0;
            }
            dp[r] = 0f64.max(prev[r - 1] / 2.0 - 1.0);
            std::mem::swap(&mut dp, &mut prev);
        }
        let glass = query_glass as usize;
        1f64.min(if glass == 0 {
            0f64.max(prev[glass] / 2.0)
        } else if glass == n {
            0f64.max(prev[glass - 1] / 2.0)
        } else {
            0f64.max(prev[glass - 1] / 2.0 + prev[glass] / 2.0)
        })
    }
}

// Tests.
fn main() {
    let tests = [
        (1, 0, 0, 1.0),
        (2, 1, 0, 0.5),
        (1, 1, 1, 0.0),
        (2, 1, 1, 0.5),
        (4, 2, 0, 0.25),
        (100000009, 33, 17, 1.0),
    ];
    for t in tests {
        assert_eq!(Solution::champagne_tower(t.0, t.1, t.2), t.3);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
