// 506. Relative Ranks
// 🟢 Easy
//
// https://leetcode.com/problems/relative-ranks/
//
// Tags: Array - Sorting - Heap (Priority Queue)

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Sort the input vector in reverse order and get a hashmap of index => value. Use that
    /// hashmap to return the input vector converted to their positions in the ranking.
    ///
    /// Time complexity: O(n*log(n)) - We sort the input vector. After that O(n)
    /// Space complexity: O(n) - The sorted vector and the hashmap.
    ///
    /// Runtime 3 ms Beats 95%
    /// Memory 2.53 MB Beats 39%
    pub fn find_relative_ranks(score: Vec<i32>) -> Vec<String> {
        let mut sc = score.clone();
        sc.sort_unstable_by(|a, b| b.cmp(a));
        let lookup = sc
            .iter()
            .enumerate()
            .map(|(i, &x)| (x, i))
            .collect::<HashMap<i32, usize>>();
        score
            .iter()
            .map(|x| match lookup.get(x) {
                Some(idx) => match idx {
                    0 => "Gold Medal".to_string(),
                    1 => "Silver Medal".to_string(),
                    2 => "Bronze Medal".to_string(),
                    _ => (idx + 1).to_string(),
                },
                None => unreachable!("Each entry should be in the hashmap"),
            })
            .collect()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![5], vec!["Gold Medal"]),
        (
            vec![5, 4, 3, 2, 1],
            vec!["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
        ),
        (
            vec![10, 3, 8, 9, 4],
            vec!["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_relative_ranks(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
