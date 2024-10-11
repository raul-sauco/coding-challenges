// 1497. Check If Array Pairs Are Divisible by k
// 🟠 Medium
//
// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
//
// Tags: Array - Hash Table - Counting

struct Solution;
impl Solution {
    /// Solution overview
    ///
    /// Time complexity: O() -
    /// Space complexity: O() -
    ///
    /// Runtime  ms Beats %
    /// Memory  MB Beats %
    pub fn can_arrange(arr: Vec<i32>, k: i32) -> bool {
        let mut mods = vec![0; k as usize];
        for &num in &arr {
            mods[(((num % k) + k) % k) as usize] += 1;
        }
        if mods[0] % 2 != 0 {
            return false;
        }
        let k = k as usize;
        for i in 1..k / 2 + 1 {
            if mods[i] != mods[k - i] {
                return false;
            }
        }
        true
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![-1, -1, -1, -1, 2, 2, -2, -2], 3, false),
        (vec![-1, 1, -2, 2, -3, 3, -4, 4], 3, true),
        (vec![1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5, true),
        (vec![1, 2, 3, 4, 5, 6], 7, true),
        (vec![1, 2, 3, 4, 5, 6], 10, false),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::can_arrange(t.0.clone(), t.1);
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
