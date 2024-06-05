// 1002. Find Common Characters
// 🟢 Easy
//
// https://leetcode.com/problems/find-common-characters/
//
// Tags: Array - Hash Table - String

struct Solution;
impl Solution {
    /// Iterate over all characters in the input, for each word, get a character count, return the
    /// minimum count for each character in each word.
    ///
    /// Time complexity: O(n) - Where n is the number of characters in all words in the input
    /// combined. We iterate over every input character and do constant time work for each.
    /// Space complexity: O(1) - Use size 26 arrays of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.08 MB Beats 100%
    pub fn common_chars(words: Vec<String>) -> Vec<String> {
        if words.len() == 0 {
            return vec![];
        }
        const N: usize = 26;
        let mut seen = [usize::MAX; N];
        let a = b'a' as usize;
        let mut char_count = [0; N];
        for w in words.iter() {
            char_count.fill(0);
            for b in w.bytes() {
                char_count[b as usize - a] += 1;
            }
            for i in 0..N {
                seen[i] = seen[i].min(char_count[i]);
            }
        }
        let mut res = vec![];
        for i in 0..N {
            for _ in 0..seen[i] {
                res.push((((i + a) as u8) as char).to_string());
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["cool", "lock", "cook"], vec!["c", "o"]),
        (vec!["bella", "label", "roller"], vec!["e", "l", "l"]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::common_chars(t.0.iter().map(|s| s.to_string()).collect());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
