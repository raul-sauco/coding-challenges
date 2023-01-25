// 909. Snakes and Ladders
// 🟠 Medium
//
// https://leetcode.com/problems/snakes-and-ladders/
//
// Tags: Array - Breadth-First Search - Matrix

struct Solution;
impl Solution {
    // We want to find the minimum distance to travel from a node to another
    // in an unweighted directed graph, each node has edges to the following
    // 6 nodes and some nodes have extra edges. BFS is a good option to
    // travel the unweighted graph because we move one edge at a time and
    // count the number of edges (rolls) we take until we land in the target.
    //
    // Time complexity: O(n^2) - Potentially, from each node we can reach
    // any other node but bfs will travel only one path because we only
    // enqueue a node the first time we see it. The board is n*n so n^2 cells.
    // Space complexity: O(n^2) - The dictionary could end up having one
    // entry per cell in the input, the queue can hold an entire level, which
    // could be more than half the board, for example in a 3x3 board.
    //
    // Runtime 7 ms Beats 33.33%
    // Memory 2.1 MB Beats 50%
    pub fn snakes_and_ladders(board: Vec<Vec<i32>>) -> i32 {
        use std::collections::{HashMap, VecDeque};
        let n = board.len();
        let target = n * n;
        let mut visited: HashMap<usize, usize> = HashMap::new();
        visited.insert(1, 0);
        let mut q = VecDeque::<usize>::new();
        q.push_back(1);
        while !q.is_empty() {
            let start_idx = q.pop_front().unwrap();
            for mut landing_idx in start_idx + 1..start_idx + 7 {
                let row = (landing_idx - 1) / n;
                let col = (landing_idx - 1) % n;
                let i = n - 1 - row;
                let j = if row % 2 == 0 { col } else { n - 1 - col };
                let cell_value = board[i][j];
                if cell_value != -1 {
                    landing_idx = cell_value as usize;
                }
                // landing_idx = landing_idx as usize;
                if landing_idx == target {
                    return (visited[&start_idx] + 1) as i32;
                }
                if !visited.contains_key(&landing_idx) {
                    visited.insert(landing_idx, visited[&start_idx] + 1);
                    q.push_back(landing_idx);
                }
            }
        }
        -1
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::snakes_and_ladders(vec![vec![-1, -1], vec![-1, 3]]),
        1
    );
    assert_eq!(
        Solution::snakes_and_ladders(vec![vec![1, 1, -1], vec![1, 1, 1], vec![-1, 1, 1]]),
        -1
    );
    assert_eq!(
        Solution::snakes_and_ladders(vec![
            vec![-1, -1, -1, -1, -1, -1],
            vec![-1, -1, -1, -1, -1, -1],
            vec![-1, -1, -1, -1, -1, -1],
            vec![-1, 35, -1, -1, 13, -1],
            vec![-1, -1, -1, -1, -1, -1],
            vec![-1, 15, -1, -1, -1, -1],
        ]),
        4
    );
    println!("All tests passed!")
}
