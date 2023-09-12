// 1647. Minimum Deletions to Make Character Frequencies Unique
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
//
// Tags: Hash Table - String - Greedy - Sorting

use std::collections::HashSet;

struct Solution;
impl Solution {
    /// Count the character frequencies in the input string, then iterate over
    /// them while keeping a hashset of frequencies that we have seen. For each
    /// character, while its frequency is greater than 0 and the current frequency
    /// has been used, it is in the frequency set, delete one occurrence. Once
    /// we find a free frequency count, store it in the set to avoid having
    /// another character use it.
    ///
    /// Time complexity: O(n) - We iterate once over the input string, then we
    /// iterate over the frequencies, even though there are nested loops, the
    /// inner loop can only iterate over a maximum of 26 values because we only
    /// have 26 possible frequencies, one for each lowercase character.
    /// Space complexity: O(1) - The frequency array and the hash set both have
    /// a maximum size of 26 elements.
    ///
    /// Runtime 2 ms Beats 83.33%
    /// Memory 2.28 MB Beats 100%
    pub fn min_deletions(s: String) -> i32 {
        let mut freqs = [0; 26];
        for b in s.bytes() {
            freqs[(b - b'a') as usize] += 1;
        }
        let mut freq_set: HashSet<usize> = HashSet::with_capacity(26);
        let mut res = 0;
        for mut freq in freqs {
            while freq > 0 && freq_set.contains(&freq) {
                freq -= 1;
                res += 1;
            }
            freq_set.insert(freq);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (String::from("aab"), 0),
        (String::from("aaabbbcc"), 2),
        (String::from("ceabaacb"), 2),
    ];
    for t in tests {
        assert_eq!(Solution::min_deletions(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
