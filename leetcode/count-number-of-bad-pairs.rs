// 2364. Count Number of Bad Pairs
// 🟠 Medium
//
// https://leetcode.com/problems/count-number-of-bad-pairs/
//
// Tags: Array - Hash Table - Math - Counting

use std::{collections::HashMap, fs::File, i64, io::Read};

use serde::{Deserialize, Serialize};

struct Solution;
impl Solution {
    /// Solution overview
    ///
    /// Time complexity: O() -
    /// Space complexity: O() -
    ///
    /// Runtime 16 ms Beats 50%
    /// Memory 6.75 MB Beats 100%
    pub fn count_bad_pairs(nums: Vec<i32>) -> i64 {
        let mut groups = HashMap::new();
        let mut res = 0i64;
        for (i, num) in nums.into_iter().enumerate() {
            let key = num - i as i32;
            if let Some(count) = groups.get_mut(&key) {
                // This entry makes a bad pair with any previous entries that does not make a good
                // pair with.
                res += (i - *count) as i64;
                *count += 1;
            } else {
                res += i as i64;
                groups.insert(key, 1);
            }
        }
        res
    }
}

#[derive(Debug, Serialize, Deserialize)]
struct Test {
    nums: Vec<i32>,
    expected: i64,
}

// Tests.
fn main() {
    let file = File::open("data/count-number-of-bad-pairs.json").expect("Unable to open file");
    let mut contents = String::new();
    file.take(u64::MAX)
        .read_to_string(&mut contents)
        .expect("Unable to read file");
    let tests: Vec<Test> = serde_json::from_str(&contents).expect("Unable to parse JSON");
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let start = std::time::Instant::now();
        let res = Solution::count_bad_pairs(t.nums.clone());
        if res == t.expected {
            success += 1;
            println!(
                "\x1b[92m✔\x1b[95m Test {} passed! Took {} mil\x1b[0m",
                i,
                start.elapsed().as_millis()
            );
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.expected, res
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
