// 791. Custom Sort String
// 🟠 Medium
//
// https://leetcode.com/problems/custom-sort-string/
//
// Tags: Hash Table - String - Sorting

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Use a hash map to get a count of the characters in s, then iterate over the order string,
    /// for each character in order, check if we had any occurrences of that character in s, if we
    /// did, put as many in the output string.
    ///
    /// Time complexity: O(m+n) - We will visit each character in both input strings, it can be
    /// also seen as O(1) since one of them m <= 26 and the other one n <= 200.
    /// Space complexity: O(m) - Where m <= 26, so maybe O(1) the size of the hashset with the
    /// counts of characters in s, the number of entries is limited by the number of lowercase
    /// English letters.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 1.97 MB Beats 100%
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut counts = HashMap::new();
        for c in s.chars() {
            *counts.entry(c).or_insert(0) += 1;
        }
        let mut res = vec![];
        for c in order.chars() {
            if let Some(&count) = counts.get(&c) {
                for _ in 0..count {
                    res.push(c);
                }
                counts.remove_entry(&c);
            }
        }
        for (c, count) in counts.into_iter() {
            for _ in 0..count {
                res.push(c);
            }
        }
        res.into_iter().collect()
    }

    /// Another approach is to get a hashmap of the order characters to their order value, then use
    /// that hashmap to sort the s string in O(n*log(n)).
    ///
    /// Time complexity: O(m+n*log(n)) - We iterate m to create the hashmap of orders, then sort s.
    /// Space complexity: O(m) - Where m <= 26, The hashmap of orders.
    ///
    /// Runtime 1 ms Beats 46.15%
    /// Memory 2.12 MB Beats 26.92%
    #[allow(dead_code)]
    pub fn custom_sort_string_sorting(order: String, s: String) -> String {
        let order =
            order
                .into_bytes()
                .into_iter()
                .enumerate()
                .fold(HashMap::new(), |mut map, (i, val)| {
                    map.insert(val, i);
                    map
                });
        let mut res = s.into_bytes();
        // A default of 27 puts non-sorted characters at the end of the result.
        res.sort_by_cached_key(|c| order.get(c).unwrap_or(&27));
        String::from_utf8(res).expect("A valid string")
    }
}

// Tests.
fn main() {
    let tests = [("cba", "abcd", "cbad"), ("bcafg", "abcd", "bcad")];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::custom_sort_string(t.0.to_string(), t.1.to_string());
        if res == t.2.to_string() {
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
