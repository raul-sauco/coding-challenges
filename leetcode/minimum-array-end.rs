// 3133. Minimum Array End
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-array-end/
//
// Tags: Bit Manipulation

struct Solution;
impl Solution {
    /// For n steps choose the smallest next number that me can use. Barely passes.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(1)
    ///
    /// Runtime 1735 ms Beats 100%
    /// Memory 2.16 MB Beats 100%
    #[allow(dead_code)]
    pub fn min_end_on(n: i32, x: i32) -> i64 {
        let x = x as i64;
        (0..n - 1).fold(x, |acc, _| (acc + 1) | x)
    }

    /// For n steps choose the smallest next number that me can use. Barely passes.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(1)
    ///
    /// Runtime 1735 ms Beats 100%
    /// Memory 2.16 MB Beats 100%
    pub fn min_end(n: i32, x: i32) -> i64 {
        let mut x = x as i64;
        let mut n = n as i64 - 1;
        let mut b = 1i64;
        for _ in 0..64i64 {
            if b & x == 0 {
                x |= (n & 1) * b;
                n >>= 1;
            }
            b <<= 1;
        }
        x
    }
}

// Tests.
fn main() {
    let tests = [(3, 4, 6), (2, 7, 15)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_end(t.0, t.1);
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
