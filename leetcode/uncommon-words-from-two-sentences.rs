// 884. Uncommon Words from Two Sentences
// 🟢 Easy
//
// https://leetcode.com/problems/uncommon-words-from-two-sentences/
//
// Tags: Hash Table - String - Counting

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// We can use a hashmap with the count of each word between both input strings. After we count
    /// them, we can use the hashmap to construct the result vector.
    ///
    /// Time complexity: O(n) - We visit each element and push it into the hashmap, then we visit
    /// each element in the hashmap.
    /// Space complexity: O(n) - The lookup hashmap.
    ///
    /// Runtime 1 ms Beats 87%
    /// Memory 2.22 MB Beats 62%
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut lookup: HashMap<&str, u8> = HashMap::new();
        let mut res = vec![];
        for word in s1.split_whitespace().chain(s2.split_whitespace()) {
            lookup
                .entry(word)
                .and_modify(|count| *count += 1)
                .or_insert(1);
        }
        for (k, v) in lookup {
            if v == 1 {
                res.push(k.to_string());
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            "this apple is sweet",
            "this apple is sour",
            vec!["sour", "sweet"],
        ),
        ("apple apple", "banana", vec!["banana"]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let mut res = Solution::uncommon_from_sentences(t.0.to_string(), t.1.to_string());
        let expected = t.2.iter().map(|s| s.to_string()).collect::<Vec<_>>();
        res.sort_unstable();
        if res == expected {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, expected, res
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
