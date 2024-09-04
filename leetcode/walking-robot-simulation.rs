// 874. Walking Robot Simulation
// 🟠 Medium
//
// https://leetcode.com/problems/walking-robot-simulation/
//
// Tags: Array - Hash Table - Simulation

use std::collections::HashSet;

struct Solution;
impl Solution {
    /// Simulate the robot movements, convert the obstacles vector to a hashset to check whether
    /// the next cell is an obstacle in constant time.
    ///
    /// Time complexity: O(o+n) - Where o is the number of obstacles and n is the number of
    /// commands, we execute the steps in each command one by one, but the number of steps is 1..9
    /// so the complexity is o*9n and can be simplified.
    /// Space complexity: O(o) - A hashset of the obstacles.
    ///
    /// Runtime 9 ms Beats 88%
    /// Memory 3.09 MB Beats 11%
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        let obstacles = obstacles
            .into_iter()
            .map(|v| (v[0], v[1]))
            .collect::<HashSet<(i32, i32)>>();
        let mut res = 0;
        let mut dir = (0, 1);
        let mut pos = (0, 0);
        let mut next;
        for command in commands {
            match command {
                -2 => {
                    dir = (-dir.1, dir.0);
                }
                -1 => {
                    dir = (dir.1, -dir.0);
                }
                x => {
                    for _ in 0..x {
                        next = (pos.0 + dir.0, pos.1 + dir.1);
                        if obstacles.contains(&next) {
                            continue;
                        }
                        pos = (next.0, next.1);
                        res = res.max(next.0 * next.0 + next.1 * next.1);
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
        (vec![4, -1, 3], vec![], 25),
        (vec![4, -1, 4, -2, 4], vec![vec![2, 4]], 65),
        (vec![6, -1, -1, 6], vec![], 36),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::robot_sim(t.0.clone(), t.1.clone());
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
