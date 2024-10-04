// 2491. Divide Players Into Teams of Equal Skill
// 🟠 Medium
//
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
//
// Tags: Array - Hash Table - Two Pointers - Sorting

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Neat version of two-sum. Find the value the teams need to have to be valid, then create
    /// the teams.
    ///
    /// Time complexity: O(n) - Constant time work for each player in the input vector.
    /// Space complexity: O(n) - The lookup hashmap.
    ///
    /// Runtime 10 ms Beats 66%
    /// Memory 2.94 MB Beats 66%
    pub fn divide_players(skill: Vec<i32>) -> i64 {
        let (total, team_count) = (
            skill.iter().map(|x| *x as i64).sum::<i64>(),
            skill.len() as i64 / 2,
        );
        if total % team_count != 0 {
            return -1;
        }
        let target = total / team_count;
        let mut lookup: HashMap<i64, usize> = HashMap::new();
        let mut res = 0i64;
        for player in skill.iter().map(|x| *x as i64) {
            let team_mate = target - player;
            if let Some(count) = lookup.get_mut(&team_mate) {
                *count -= 1;
                res += player * team_mate;
                if *count == 0 {
                    lookup.remove(&team_mate);
                }
            } else {
                if let Some(player_count) = lookup.get_mut(&player) {
                    *player_count += 1;
                } else {
                    lookup.insert(player, 1);
                }
            }
        }
        if lookup.len() == 0 {
            return res;
        }
        -1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 2, 5, 1, 3, 4], 22),
        (vec![3, 4], 12),
        (vec![1, 1, 2, 3], -1),
        (vec![2, 3, 4, 2, 5, 5], 32),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::divide_players(t.0.clone());
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
