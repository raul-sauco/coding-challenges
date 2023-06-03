// 2101. Detonate the Maximum Bombs
// 🟠 Medium
//
// https://leetcode.com/problems/detonate-the-maximum-bombs/
//
// Tags: Array - Math - Depth-First Search - Breadth-First Search - Graph - Geometry

struct Solution {}
impl Solution {
    /// The bombs form a directed graph where they are the nodes and the edges
    /// are formed between them and any other bombs that are within the radius
    /// of their explosions and will be triggered in a chain reaction. We can
    /// start by constructing an adjacency list using O(n^2) then we can do a
    /// graph traversal starting at each node checking how many bombs will be
    /// triggered and return the maximum result.
    ///
    /// Time complexity: O(n^3) - We perform a DFS that could have a time
    /// complexity of O(n^2) for each node in the graph.
    /// Space complexity: O(n^2) - The adjacency 2D vector.
    ///
    /// Runtime 18 ms Beats 100%
    /// Memory 2.2 MB Beats 100%
    pub fn maximum_detonation(bombs: Vec<Vec<i32>>) -> i32 {
        let n = bombs.len();
        let mut res = 0;
        // Create an adjacency vector.
        let mut adj: Vec<Vec<usize>> = vec![vec![]; n];
        // Iterate over all pairs.
        for i in 0..n {
            let (x1, y1, r1) = (bombs[i][0], bombs[i][1], bombs[i][2]);
            for j in i + 1..n {
                let (x2, y2, r2) = (bombs[j][0], bombs[j][1], bombs[j][2]);
                let dist = i64::pow((x1 - x2) as i64, 2) + i64::pow((y1 - y2) as i64, 2);
                if dist <= i64::pow(r1 as i64, 2) {
                    // We can reach 2 from 1.
                    adj[i].push(j);
                }
                if dist <= i64::pow(r2 as i64, 2) {
                    adj[j].push(i);
                }
            }
        }
        fn dfs(i: usize, in_path: &mut Vec<bool>, adj: &Vec<Vec<usize>>) -> i32 {
            let mut count = 1;
            for nei in adj[i].iter() {
                let nei = *nei;
                if !in_path[nei] {
                    in_path[nei] = true;
                    count += dfs(nei, in_path, adj);
                }
            }
            count
        }
        let mut dp = vec![-1; n];
        // Pick start nodes to do a
        for i in 0..n {
            let mut in_path = vec![false; n];
            in_path[i] = true;
            dp[i] = dfs(i, &mut in_path, &adj);
            if dp[i] > res {
                res = dp[i];
            }
        }
        res
    }
}

fn main() {
    let tests = [
        (vec![vec![2, 1, 3], vec![6, 1, 4]], 2),
        (vec![vec![1, 1, 5], vec![10, 10, 5]], 1),
    ];
    for t in tests {
        assert_eq!(Solution::maximum_detonation(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
