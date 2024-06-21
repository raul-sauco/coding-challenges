// 1552. Magnetic Force Between Two Balls
// 🟠 Medium
//
// https://leetcode.com/problems/magnetic-force-between-two-balls/
//
// Tags: Array - Binary Search - Sorting

struct Solution;
impl Solution {
    /// We need to test a distance to see if it works. Binary search the answer that works.
    ///
    /// Time complexity: O(n*log(n)) - Both sorting and the binary search where testing each guess
    /// requires iterating over the input vector.
    /// Space complexity: O(1)
    ///
    /// Runtime 30 ms Beats 30%
    /// Memory 3.89 MB Beats 69%
    pub fn max_distance(mut position: Vec<i32>, m: i32) -> i32 {
        let n = position.len();
        position.sort_unstable(); // O(nlog(n))
        let (mut low, mut high) = (0, position.last().unwrap() - position[0]);
        let (mut guess, mut pending, mut prev);
        while low < high {
            guess = (low + high + 1) / 2;
            pending = m - 1;
            prev = position[0];
            for i in 1..n {
                if position[i] - prev >= guess {
                    pending -= 1;
                    prev = position[i];
                    if pending == 0 {
                        break;
                    }
                }
            }
            if pending <= 0 {
                low = guess;
            } else {
                high = guess - 1;
            }
        }
        low
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 4, 7], 3, 3),
        (vec![5, 4, 3, 2, 1, 1000000000], 2, 999999999),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_distance(t.0.clone(), t.1);
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
