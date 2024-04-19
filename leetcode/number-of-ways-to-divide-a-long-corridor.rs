// 2147. Number of Ways to Divide a Long Corridor
// 🔴 Hard
//
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
//
// Tags: Math - String - Dynamic Programming

const MOD: i32 = 1_000_000_007;

struct Solution;
impl Solution {
    /// Travel through the chars in the input keeping track of how many seats we have in the
    /// current "section" that we are taking into consideration, for each index in each branch, if
    /// we already have two seats, if we land in another seat, we need to put a divider and move to
    /// the next index with one seat, if we land on a plant, we can decide to place or not place a
    /// divider, we return the sum of the ways to divide resulting in both these decisions. If we
    /// do not have 2 seats yet in the current section, we move onto the next index, adding one
    /// seat to the count if the current position is one.
    ///
    /// Time complexity: O(n) - The DFS function will get call a max of cache-size times.
    /// Space complexity: O(n) - The cache has a size of 3*n.
    ///
    /// Runtime 209 ms Beats 100%
    /// Memory 14.26 MB Beats 100%
    pub fn number_of_ways(corridor: String) -> i32 {
        fn dfs(i: usize, s: usize, corridor: &Vec<char>, cache: &mut Vec<Vec<i32>>) -> i32 {
            // Base cases: we are at the end of the corridor
            if i == corridor.len() {
                if s == 2 {
                    return 1;
                } else {
                    return 0;
                }
            }
            if cache[i][s] != -1 {
                return cache[i][s];
            }
            let res;
            if s == 2 {
                if corridor[i] == 'S' {
                    res = dfs(i + 1, 1, corridor, cache);
                } else {
                    res = (dfs(i + 1, 0, corridor, cache) + dfs(i + 1, 2, corridor, cache)) % MOD;
                }
            } else {
                res = dfs(
                    i + 1,
                    s + if corridor[i] == 'S' { 1 } else { 0 },
                    corridor,
                    cache,
                );
            }
            cache[i][s] = res;
            cache[i][s]
        }
        let n = corridor.len();
        let corridor = corridor.chars().collect::<Vec<_>>();
        let mut cache = vec![vec![-1; 3]; n];
        dfs(0, 0, &corridor, &mut cache)
    }

    /// The bottom-up version of the previous solution, same logic for the transitions.
    ///
    /// Time complexity: O(n) - We iterate over the characters in the input and do constant time
    /// work for each.
    /// Space complexity: O(1) - We only store a tuple with three i32.
    ///
    /// Runtime 21 ms Beats 100%
    /// Memory 2.32 MB Beats 100%
    pub fn number_of_ways_2(corridor: String) -> i32 {
        let mut dp = (1, 0, 0);
        for c in corridor.chars() {
            if c == 'S' {
                dp = (0, (dp.0 + dp.2) % MOD, dp.1);
            } else {
                dp = ((dp.0 + dp.2) % MOD, dp.1, dp.2);
            }
        }
        dp.2
    }
}

// Tests.
fn main() {
    let tests = [("SSPPSPS", 3), ("PPSPSP", 1), ("S", 0)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::number_of_ways_2(t.0.to_string());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.1, res
            );
        }
    }
    println!("");
    if success == tests.len() {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
