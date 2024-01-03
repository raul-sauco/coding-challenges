// 2125. Number of Laser Beams in a Bank
// 🟠 Medium
//
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
//
// Tags: Array - Math - String - Matrix

use itertools::Itertools;

struct Solution;
impl Solution {
    /// Iterate over the rows counting ones, for each row that has one or more lasers, multiply the
    /// number of lasers by the number of lasers in the last row that had any, then use that value
    /// as the last row's count.
    ///
    /// Time complexity: O(n*m) - We visit each position in the m*n matrix once and do O(1) work
    /// for each.
    /// Space complexity: O(1) - We store two usize values.
    ///
    /// Runtime 3 ms Beats 90%
    /// Memory 2.85 MB Beats 30%
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        //     Leetcode solution, no Itertools there.
        //     let mut res = 0;
        //     let mut last_row_ones = 0;
        //     for s in bank {
        //         let ones = s.chars().filter(|&x| x == '1').count();
        //         if ones > 0 {
        //             res += last_row_ones * ones;
        //             last_row_ones = ones;
        //         }
        //     }
        //     res as i32

        // I like this solution with Itertools tuple_windows.
        bank.iter()
            .map(|row| row.bytes().filter(|&x| x == b'1').count())
            .filter(|count| *count != 0)
            .tuple_windows::<(_, _)>()
            .fold(0, |acc, (a, b)| acc + a * b) as i32

        // An idea that I had to pretend to iterate over windows using a tuple accumulator in
        // fold to keep the last row count as the second value in the accumulator. It would
        // probably look better using scan to collect the values and then fold to add them up.
        //     bank.iter()
        //         .map(|row| row.bytes().filter(|&x| x == b'1').count())
        //         .filter(|count| *count != 0)
        //         .fold((0, 0), |(acc, last), cur| {
        //             (acc + last * cur, cur)
        //         }).0 as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["011001", "000000", "010100", "001000"], 8),
        (vec!["000", "111", "000"], 0),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::number_of_beams(t.0.iter().map(|s| s.to_string()).collect::<Vec<_>>());
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
    println!("");
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
