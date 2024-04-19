// 1291. Sequential Digits
// 🟠 Medium
//
// https://leetcode.com/problems/sequential-digits/
//
// Tags: Enumeration

struct Solution;
impl Solution {
    /// Sometimes the easiest solution is to look at the constrains. In this case the result set is
    /// so small that it is worth hardcoding the values and filtering.
    ///
    /// Time complexity: O(1) - We iterate and filter values from an array of constant size.
    /// Space complexity: O(1) - We use an array of constant size of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.08 MB Beats 66.67%
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        [
            12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456,
            4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789, 12345678, 23456789, 123456789,
        ]
        .into_iter()
        // Leetcode is in an older Rust version, it needs this dereferencing.
        // .map(|x| *x)
        .filter(|&x| x >= low && x <= high)
        .collect::<Vec<_>>()
    }
}

// Tests.
fn main() {
    let tests = [
        (100, 300, vec![123, 234]),
        (1000, 13000, vec![1234, 2345, 3456, 4567, 5678, 6789, 12345]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::sequential_digits(t.0, t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
