// 1363. Largest Multiple of Three
// 🔴 Hard
//
// https://leetcode.com/problems/largest-multiple-of-three/
//
// Tags: Array - Dynamic Programming - Greedy

// use regex::Regex;

struct Solution;
impl Solution {
    /// Iterate over the input vector getting the count of each digit from 0 to 9, then compute
    /// their sum, if the sum is a multiple of 3, we can construct the result returning all the
    /// digits in decreasing order. Otherwise we need to remove digits, starting by the ones that
    /// have less weight, we use the module of the current sum to try and remove one digit only, if
    /// it is not possible, we can remove 2. A special case to handle is when the result is formed
    /// by multiple zeroes, we need to remove them and leave only one.
    ///
    /// Time complexity: O(n) - We iterate over all the digits to get their count. After that,
    /// getting the sum inside each time the loop runs is O(1) and the loop will run at most 2
    /// times.
    /// Space complexity: O(1) - For the version using regex, the version used in Leetcode uses
    /// O(n) because it stores the result string and it operates on it in case it is an all-zero
    /// string.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.27 MB Beats 33.33%
    pub fn largest_multiple_of_three(digits: Vec<i32>) -> String {
        let mut counts = [0; 10];
        for digit in digits {
            counts[digit as usize] += 1;
        }
        let mut sum: usize = counts.iter().enumerate().map(|(i, c)| i * c).sum();
        fn remove_one(counts: &mut [usize], module: usize) {
            let priorities = if module == 1 {
                [1, 4, 7, 2, 5, 8]
            } else {
                [2, 5, 8, 1, 4, 7]
            };
            for digit in priorities {
                if counts[digit] > 0 {
                    counts[digit] -= 1;
                    break;
                }
            }
        }
        loop {
            match sum % 3 {
                0 => break,
                1 => remove_one(&mut counts, 1),
                2 => remove_one(&mut counts, 2),
                _ => unreachable!(),
            }
            sum = counts.iter().enumerate().map(|(i, c)| i * c).sum();
        }
        // We could return this directly if we did not need to deal with all-zero strings.
        let res = counts
            .iter()
            .enumerate()
            .rev()
            .map(|(i, c)| {
                if c > &0 {
                    i.to_string().repeat(*c)
                } else {
                    "".to_string()
                }
            })
            .collect::<String>();
        if res == "".to_string() {
            return res;
        }
        if res.chars().next().unwrap() == '0' {
            "0".to_string()
        } else {
            res
        }
        // This does not work in Leetcode, no access to regex.
        // let re = Regex::new("^[0]+$").unwrap();
        // return re
        //     .replace(
        //         &counts
        //             .iter()
        //             .enumerate()
        //             .rev()
        //             .map(|(i, c)| {
        //                 if c > &0 {
        //                     i.to_string().repeat(*c)
        //                 } else {
        //                     "".to_string()
        //                 }
        //             })
        //             .collect::<String>(),
        //         "0",
        //     )
        //     .to_string();
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], ""),
        (vec![8, 1, 9], "981"),
        (vec![0, 0, 0, 1, 0], "0"),
        (vec![8, 6, 7, 1, 0], "8760"),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::largest_multiple_of_three(t.0.clone());
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
