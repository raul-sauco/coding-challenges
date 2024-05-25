// 140. Word Break II
// 🔴 Hard
//
// https://leetcode.com/problems/word-break-ii/
//
// Tags: Array - Hash Table - String - Dynamic Programming - Backtracking - Trie - Memoization

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Backtrack solution. each call takes the index from which to match, it looks at the
    /// character at that position of the input and tries to match all input words that start with
    /// that character. If the match is possible, it adds that word to the result, and calls
    /// backtrack with the remainder of the input string. If we cannot match the word we ignore it,
    /// if we cannot match any words, that call to bt will not do anything. If we get to the end of
    /// the input string, we add the string constructed to the result vector.
    ///
    /// Time complexity: O(2^n) - Worst case, we can generate a word with each character in the
    /// input.
    /// Space complexity: O(2^n) - That is the number of combinations that may be generated.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.12 MB Beats 29%
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        let mut res = Vec::new();
        let mut cur = String::new();
        let mut hm = HashMap::new();
        for word in word_dict {
            let ch = word.chars().next().unwrap();
            hm.entry(ch).or_insert(vec![]).push(word);
        }
        let chars = s.chars().collect::<Vec<_>>();
        Self::bt(0, &chars, &hm, &mut cur, &mut res);
        res
    }

    fn bt(
        i: usize,
        s: &Vec<char>,
        word_dic: &HashMap<char, Vec<String>>,
        cur: &mut String,
        res: &mut Vec<String>,
    ) {
        if i == s.len() && cur.len() > 0 {
            let mut matches = cur.clone();
            // Remove the extra space at the end.
            matches.pop();
            res.push(matches);
            return;
        }
        // Find all words that start with the current character.
        if let Some(words) = word_dic.get(&s[i]) {
            for word in words {
                if Self::can_match(s, i, word) {
                    cur.push_str(word);
                    cur.push(' ');
                    Self::bt(i + word.len(), s, word_dic, cur, res);
                    for _ in 0..=word.len() {
                        cur.pop();
                    }
                }
            }
        }
    }

    fn can_match(s: &Vec<char>, i: usize, word: &String) -> bool {
        if word.len() + i > s.len() {
            return false;
        }
        let chars = word.chars().collect::<Vec<_>>();
        for idx in 0..chars.len() {
            if chars[idx] != s[i + idx] {
                return false;
            }
        }
        return true;
    }
}

// Tests.
fn main() {
    let tests = [
        (
            "catsanddog",
            vec!["cat", "cats", "and", "sand", "dog"],
            vec!["cats and dog", "cat sand dog"],
        ),
        (
            "pineapplepenapple",
            vec!["apple", "pen", "applepen", "pine", "pineapple"],
            vec![
                "pine apple pen apple",
                "pineapple pen apple",
                "pine applepen apple",
            ],
        ),
        (
            "catsandog",
            vec!["cats", "dog", "sand", "and", "cat"],
            vec![],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let mut res =
            Solution::word_break(t.0.to_string(), t.1.iter().map(|s| s.to_string()).collect());
        let mut expected = t.2.clone();
        res.sort_unstable();
        expected.sort_unstable();
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
