// 1376. Time Needed to Inform All Employees
// 🟠 Medium
//
// https://leetcode.com/problems/time-needed-to-inform-all-employees/
//
// Tags: Tree - Depth-First Search - Breadth-First Search

use std::collections::VecDeque;

struct Solution {}
impl Solution {
    /// Reconstruct the tree, in this solution done creating an adjacency list
    /// in O(n), then use the tree to travel from the root to all the tree nodes
    /// keeping track of the time used. Return the maximum time to reach any node.
    ///
    /// Time complexity: O(n) - Recreate the tree, we could use tree nodes, but
    /// in Rust is quite verbose so I opted for an adjacency list instead, once
    /// we have a way to navigate from parents to children, the problem becomes
    /// a simple tree traversal, we can use BFS or DFS while keeping track of
    /// the time required to reach every employee, and return the maximum.
    /// Space complexity: O(n) - The subordinates vector is a 2D vector, but it
    /// will only have a total of n entries because each node is limited to
    /// having only one parent, we know the total number of edges = n-1.
    ///
    /// Runtime 39 ms Beats 86.67%
    /// Memory 8.7 MB Beats 33.33%
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        let n = n as usize;
        let head_id = head_id as usize;
        let manager = manager
            .into_iter()
            .map(|x| x as usize)
            .collect::<Vec<usize>>();
        let mut subordinates = vec![vec![]; n];
        for employee in 0..n {
            if employee != head_id {
                subordinates[manager[employee]].push(employee);
            }
        }
        let mut res = 0;
        // BFS the time needed to inform all employees.
        let mut queue = VecDeque::from([(head_id, 0)]);
        while !queue.is_empty() {
            let (current_employee, current_time) = queue.pop_front().unwrap();
            let time_to_informed = current_time + inform_time[current_employee];
            if time_to_informed > res {
                res = time_to_informed;
            }
            for subordinate in subordinates[current_employee].iter() {
                queue.push_back((*subordinate, time_to_informed));
            }
        }
        res
    }
}

fn main() {
    let tests = [
        (1, 0, vec![-1], vec![0], 0),
        (6, 2, vec![2, 2, -1, 2, 2, 2], vec![0, 0, 1, 0, 0, 0], 1),
    ];
    for t in tests {
        assert_eq!(Solution::num_of_minutes(t.0, t.1, t.2, t.3), t.4);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
