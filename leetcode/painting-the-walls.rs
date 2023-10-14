// 2742. Painting the Walls
// 🔴 Hard
//
// https://leetcode.com/problems/painting-the-walls/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// Use memoization, we can explore a recursive tree from the point of view
    /// of the paid painter, at each step, we can choose to paint or skip the
    /// current wall, then move to the next one. If we paint the current wall i,
    /// the free painter can use that time to paint time[i] walls, but we need
    /// to pay cost[i]. We can keep track of the current index and the number
    /// of remaining walls.
    ///
    /// Time complexity: O(n^2) - Since we are using memoization, the number of
    /// times dfs can run is the number of entries that we can have in our cache,
    /// which is equal to n^2 which are the combinations of values that i and
    /// remaining can take.
    /// Space complexity: O(n^2) - The size of our cache.
    ///
    /// Runtime 41 ms Beats 100%
    /// Memory 3.06 MB Beats 100%
    pub fn paint_walls(cost: Vec<i32>, time: Vec<i32>) -> i32 {
        let n = cost.len();
        let mut cache = vec![vec![i32::MAX; n + 1]; n];
        // A recursive function that explores the possible options from the paid
        // painter point of view and a given index.
        fn dfs(
            i: usize,
            remaining: i32,
            cache: &mut Vec<Vec<i32>>,
            cost: &Vec<i32>,
            time: &Vec<i32>,
        ) -> i32 {
            // We have painted all the houses.
            if remaining <= 0 {
                return 0;
            }
            // We have arrived at the end of the walls but missing some.
            if i == cost.len() {
                return i32::MAX / 2;
            }
            let rem = remaining as usize;
            if cache[i][rem] != i32::MAX {
                return cache[i][rem];
            }
            // Otherwise, keep exploring.
            cache[i][rem] = std::cmp::min(
                dfs(i + 1, remaining, cache, cost, time),
                dfs(i + 1, remaining - 1 - time[i], cache, cost, time) + cost[i],
            );
            cache[i][rem]
        }
        dfs(0, n as i32, &mut cache, &cost, &time)
    }

    /// Bottom-up dp version of the previous solution, use a vector to cache
    /// intermediate results and traverse back through the possibilities.
    ///
    /// Time complexity: O(n^2) - The nested loops can each run through n
    /// iterations.
    /// Space complexity: O(n^2) - The size of our cache, we could keep only the
    /// previous row of dp and reduce space complexity to O(n).
    ///
    /// Runtime 14 ms Beats 100%
    /// Memory 3.12 MB Beats 100%
    pub fn paint_walls_2(cost: Vec<i32>, time: Vec<i32>) -> i32 {
        let n = cost.len();
        let time = time.iter().map(|&x| x as usize).collect::<Vec<usize>>();
        let mut dp = vec![vec![0; n + 1]; n + 1];
        for i in 1..=n {
            dp[n][i] = i32::MAX / 2;
        }
        for i in (0..n).rev() {
            for remain in 1..=n {
                dp[i][remain] = std::cmp::min(
                    cost[i]
                        + dp[i + 1][if remain >= 1 + time[i] {
                            remain - 1 - time[i]
                        } else {
                            0
                        }],
                    dp[i + 1][remain],
                );
            }
        }
        dp[0][n]
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 2], vec![1, 2, 3, 2], 3),
        (vec![2, 3, 4, 2], vec![1, 1, 1, 1], 4),
    ];
    for t in tests {
        assert_eq!(Solution::paint_walls(t.0.clone(), t.1.clone()), t.2);
        assert_eq!(Solution::paint_walls_2(t.0.clone(), t.1.clone()), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
