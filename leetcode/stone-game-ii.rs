// 1140. Stone Game II
// 🟠 Medium
//
// https://leetcode.com/problems/stone-game-ii/
//
// Tags: Array - Math - Dynamic Programming - Game Theory

struct Solution {}
impl Solution {
    /// From each position, the player whose turn is can choose anywhere
    /// between 1 and 2*number of stones taken in the last move, the maximum
    /// score comes from choosing the max score possible between any of these
    /// choices taking into account that the other player will also play
    /// optimally, which means the score obtained by taking that many stones
    /// minus the score obtained by the other player from playing optimally the
    /// remaining of the array. We can recursively compute this result caching
    /// intermediate results to avoid recalculating results for the same play,
    /// which would result in exponential time complexity.
    ///
    /// Time complexity: O(n^3) - We may call the dfs function for every
    /// possible combination of start and end values, for each call, we will
    /// iterate between 1 and the next "end", to represent that the player can
    /// choose to take anywhere between 1 and the current maximum of stones
    /// they are allowed to take.
    /// Space complexity: O(n^2) - The size of the cache, which is n*n. The
    /// call stack can grow to a depth of n.
    ///
    /// Runtime 6 ms Beats 66.25%
    /// Memory 2.2 MB Beats 83.75%
    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {
        let mut cache = vec![vec![-1; piles.len() + 1]; piles.len() + 1];
        fn dfs(start: usize, end: usize, cache: &mut Vec<Vec<i32>>, piles: &Vec<i32>) -> i32 {
            if cache[start][end] != -1 {
                return cache[start][end];
            }
            let mut res = 0;
            let slice_sum: i32 = piles[start..piles.len()].iter().sum();
            let boundary = (2 * end).min(piles.len() - start) + 1;
            for i in 1..boundary {
                let best = dfs(start + i, end.max(i), cache, piles);
                res = res.max(slice_sum - best);
            }
            cache[start][end] = res;
            res
        }
        dfs(0, 1, &mut cache, &piles)
    }
}

fn main() {
    let tests = [(vec![2, 7, 9, 4, 4], 10), (vec![1, 2, 3, 4, 5, 100], 104)];
    for t in tests {
        assert_eq!(Solution::stone_game_ii(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
