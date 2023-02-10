// 2306. Naming a Company
// 🔴 Hard
//
// https://leetcode.com/problems/naming-a-company/
//
// Tags: Array - Hash Table - String - Bit Manipulation - Enumeration

struct Solution;
impl Solution {
    // This solution is based in two observations, words with the same first
    // letters can never be combined amongst themselves, because they would
    // not change and therefore are guaranteed to be in the input, we can
    // put all words with the same characters into sets. Then we iterate over
    // each pair of sets, check how many word suffixes are common between
    // both sets, because they will also result in an existing word, and
    // compute the number of ways to combine suffixes that are not common
    // between themselves.
    //
    // Time complexity: O(n) - We visit each word to build the dictionary,
    // then iterate over the characters that we use as keys for the
    // dictionary using a nested loop at O(26^2)≈O(1). Inside each of the 26^2
    // loops we compute the intersection of sets, which overall can be at most
    // O(n) work because that is the number of words in the combined sets,
    // and do some math with the length of the sets and their intersection
    // at O(1).
    // Space complexity: O(n) - The dictionary contains all characters in the
    // input.
    //
    // Runtime 192 ms Beats 11.11%
    // Memory 9.7 MB Beats 22.22%
    pub fn distinct_names(ideas: Vec<String>) -> i64 {
        use std::collections::{HashMap, HashSet};
        let alpha = "abcdefghijklmnopqrstuvwxyz";
        let chars: Vec<char> = alpha.chars().collect();
        let mut d: HashMap<char, HashSet<String>> = HashMap::new();
        for c in alpha.chars() {
            d.insert(c, HashSet::new());
        }
        for idea in &ideas {
            let first_char: char = idea.chars().nth(0).unwrap();
            let suffix = idea[1..].to_owned();
            d.entry(first_char).or_default().insert(suffix);
        }
        let mut count = 0;
        for i in 0..alpha.len() - 1 {
            let w1 = match d.get(&chars[i]) {
                Some(w) => w,
                None => {
                    panic!("Expected key {} not found", &chars[i])
                }
            };
            if w1.len() == 0 {
                continue;
            }
            for j in i + 1..alpha.len() {
                let w2 = match d.get(&chars[j]) {
                    Some(w) => w,
                    None => {
                        panic!("Expected key {} not found", &chars[j])
                    }
                };
                // The count of elements common to both hash sets.
                let common = w1.intersection(w2).count();
                count += 2 * (w1.len() - common) * (w2.len() - common);
            }
        }
        count as i64
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::distinct_names(vec![String::from("lack"), String::from("back")]),
        0
    );
    println!("All tests passed!")
}
