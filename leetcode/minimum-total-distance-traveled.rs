// 2463. Minimum Total Distance Traveled
// 🔴 Hard
//
// https://leetcode.com/problems/minimum-total-distance-traveled/
//
// Tags: Array - Dynamic Programming - Sorting

use std::{cmp::Reverse, collections::BinaryHeap};

struct Solution;
impl Solution {
    /// This solution does not work, I assumed that greedily choosing the closest factory would
    /// result in the most optimal result, but it is not the case, there is one test case that
    /// shows this.
    ///
    /// Time complexity: O(m*log(m)+m*log(n)) - First we sort the robots, then we process them in
    /// order, for each, we pick the closets factory that can fix robots in O(log(n))
    /// Space complexity: O(m) - The heaps.
    #[allow(dead_code)]
    pub fn minimum_total_distance_greedy_heaps(mut robot: Vec<i32>, factory: Vec<Vec<i32>>) -> i64 {
        robot.sort_unstable();
        // Two heaps to find the closest factory to any robot.
        let mut left = BinaryHeap::<(i32, i32)>::new();
        let mut right = factory
            .iter()
            .map(|v| (Reverse((v[0], v[1]))))
            .collect::<BinaryHeap<_>>();
        let mut res = 0;
        for r in robot {
            while let Some(&Reverse((position, _capacity))) = right.peek() {
                // Move factories to the left/same spot to the min heap.
                if position > r {
                    break;
                }
                left.push(right.pop().unwrap().0);
            }
            // Find out which factory is closer.
            let go_right = match (left.peek(), right.peek()) {
                (None, Some(_)) => true,
                (Some(_), None) => false,
                (Some(&(left_pos, _)), Some(&Reverse((right_pos, _)))) => {
                    // If the distance to the right factory is closer.
                    (r - left_pos).abs() > (right_pos - r).abs()
                }
                (None, None) => unreachable!("The problem guarantees enough factory capacity"),
            };
            if go_right {
                let (pos, capacity) = right.pop().unwrap().0;
                res += (pos - r).abs() as i64;
                // println!("Robot {} going right to {}. Total {}", r, pos, res);
                if capacity > 1 {
                    right.push(Reverse((pos, capacity - 1)));
                }
            } else {
                let (pos, capacity) = left.pop().unwrap();
                res += (r - pos).abs() as i64;
                // println!("Robot {} going left to {}. Total {}", r, pos, res);
                if capacity > 1 {
                    left.push((pos, capacity - 1));
                }
            }
        }
        res
    }

    /// Use dynamic programming. See the explanation on the problem editorial.
    ///
    /// Time complexity: O(m*n*k) - The nested loops.
    /// Space complexity: O(m) - The dp vector.
    ///
    /// Runtime 4 ms Beats 100%
    /// Memory 2.20 MB Beats 100%
    pub fn minimum_total_distance(mut robot: Vec<i32>, mut factory: Vec<Vec<i32>>) -> i64 {
        robot.sort_unstable();
        factory.sort_unstable();
        let (m, n) = (robot.len(), factory.len());
        let mut dp = vec![i64::MAX; m + 1];
        dp[m] = 0;
        for fidx in (0..n).rev() {
            for ridx in 0..m {
                let mut cur = 0;
                // The number of robots that this factory can fix min the number of robots needing
                // fixing still.
                for k in 1..=(factory[fidx][1] as usize).min(m - ridx) as usize {
                    cur += (robot[ridx + k - 1] - factory[fidx][0]).abs() as i64;
                    dp[ridx] = dp[ridx].min(if dp[ridx + k] == i64::MAX {
                        i64::MAX
                    } else {
                        dp[ridx + k] + cur
                    });
                }
                // println!("{:?}", dp);
            }
        }
        dp[0]
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0, 4, 6], vec![vec![2, 2], vec![6, 2]], 4),
        (vec![1, -1], vec![vec![-2, 1], vec![2, 1]], 2),
        // This test fails on the greedy/heap solution, it is better for 9 to go to 7 even though
        // it is further.
        (
            vec![9, 11, 99, 101],
            vec![
                vec![10, 1],
                vec![7, 1],
                vec![14, 1],
                vec![100, 1],
                vec![96, 1],
                vec![103, 1],
            ],
            6,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::minimum_total_distance(t.0.clone(), t.1.clone());
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
