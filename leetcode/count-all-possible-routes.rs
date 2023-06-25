// 1575. Count All Possible Routes
// 🔴 Hard
//
// https://leetcode.com/problems/count-all-possible-routes/
//
// Tags: Array - Dynamic Programming - Memoization

struct Solution;
impl Solution {
    /// Use dynamic programming, dp[i][j] indicates the number of routes to i
    /// while having still j remaining fuel.
    ///
    /// Time complexity: O(n^2*m) - Three nested loops, two of them iterating
    /// over all the locations, the outer one over 0..fuel+1.
    /// Space complexity: O(m*n) - The size of the dp 2D array.
    ///
    /// Runtime 167 ms Beats 33.33%
    /// Memory 2.2 MB Beats 66.67%
    pub fn count_routes(locations: Vec<i32>, start: i32, finish: i32, fuel: i32) -> i32 {
        let n = locations.len();
        let m = fuel as usize + 1;
        let finish = finish as usize;
        let mut dp = vec![vec![0; m]; n];
        for i in 0..m {
            dp[finish][i] = 1;
            for j in 0..n {
                for k in 0..n {
                    if k == j {
                        continue;
                    }
                    let diff = (locations[j] - locations[k]).abs() as usize;
                    if diff <= i {
                        dp[j][i] += dp[k][i - diff];
                        dp[j][i] %= 1000000007;
                    }
                }
            }
        }
        dp[start as usize][fuel as usize]
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![4, 3, 1], 1, 0, 6, 5),
        (vec![5, 2, 1], 0, 2, 3, 0),
        (vec![2, 3, 6, 8, 4], 1, 3, 5, 4),
    ];
    for t in tests {
        assert_eq!(Solution::count_routes(t.0, t.1, t.2, t.3), t.4);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
