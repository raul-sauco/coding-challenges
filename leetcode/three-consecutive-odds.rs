// 1550. Three Consecutive Odds
// 🟢 Easy
//
// https://leetcode.com/problems/three-consecutive-odds/
//
// Tags: Array

struct Solution;
impl Solution {
    /// Keep track of the number of consecutive odds that we see, if it ever reaches 3 return true,
    /// if we run out of elements, return false.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(1)
    ///
    /// Runtime 1 ms Beats 25%
    /// Memory 2.15 MB Beats 25%
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        let mut odds = 0;
        for num in arr {
            if num % 2 == 1 {
                odds += 1;
                if odds == 3 {
                    return true;
                }
            } else {
                odds = 0;
            }
        }
        false
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2, 6, 4, 1], false),
        (vec![1, 2, 34, 3, 4, 5, 7, 23, 12], true),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::three_consecutive_odds(t.0.clone());
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
