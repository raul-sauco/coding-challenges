// 2285. Maximum Total Importance of Roads
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-total-importance-of-roads/
//
// Tags: Greedy - Graph - Sorting - Heap (Priority Queue)

struct Solution;
impl Solution {
    /// Assign values in the range 1..=n to the cities based on the number of roads they are
    /// connected to, the more roads, the higher the value. Then use these values, and the hashmap
    /// with the number of connections per city, to compute the result.
    ///
    /// Time complexity: O(n*log(n))
    /// Space complexity: O(n)
    ///
    /// Runtime 55 ms Beats 11%
    /// Memory 5.72 MB Beats 11%
    pub fn maximum_importance(n: i32, roads: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let mut connections = vec![0; n];
        for road in roads {
            connections[road[0] as usize] += 1;
            connections[road[1] as usize] += 1;
        }
        let mut importance: Vec<_> = (0..n).collect();
        importance.sort_by(|a, b| connections[*b].cmp(&connections[*a]));
        println!("{:?}", importance);
        let mut res = 0;
        for i in 0..n {
            res += (n - i) * connections[importance[i]];
        }
        res as i64
    }
}

// Tests.
fn main() {
    let tests = [
        (
            5,
            vec![
                vec![0, 1],
                vec![1, 2],
                vec![2, 3],
                vec![0, 2],
                vec![1, 3],
                vec![2, 4],
            ],
            43,
        ),
        (5, vec![vec![0, 3], vec![2, 4], vec![1, 3]], 20),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_importance(t.0, t.1.clone());
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.2, res
            );
        }
    }
    println!();
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
