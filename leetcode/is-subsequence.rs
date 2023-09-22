// 392. Is Subsequence
// 🟢 Easy
//
// https://leetcode.com/problems/is-subsequence/
//
// Tags: Two Pointers - String - Dynamic Programming

struct Solution;
impl Solution {
    /// Create an iterator over the characters in t, iterate over the characters
    /// in s matching each one with a character in the iterator, if we can match
    /// them all, s is a subsequence of t, otherwise it isn't. The iterator
    /// consumes characters as it checks for matches, which guarantees that, if
    /// we match a character, it will be to the right of the previous match.
    ///
    /// Time complexity: O(m+n) - We may iterate over the characters in both
    /// strings, at a minimum, we iterate one of them, s if it is a subsequence
    /// or t if it isn't.
    /// Space complexity: O(1) - I im not sure of this, but I believe that the
    /// iterators do not store all characters in a separate memory position,
    /// instead they keep a pointer to the original String position that they
    /// have accessed last.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.19 MB Beats 36.74%
    pub fn is_subsequence(s: String, t: String) -> bool {
        let mut t_chars = t.chars();
        s.chars().all(|c| t_chars.any(|t_c| t_c == c))
    }

    /// Same logic as the previous solution but using nested for and while
    /// loops instead of iterator functions.
    ///
    /// Time complexity: O(m+n) - We may iterate over the characters in both
    /// strings, at a minimum, we iterate one of them, s if it is a subsequence
    /// or t if it isn't.
    /// Space complexity: O(1) - I im not sure of this, but I believe that the
    /// iterators do not store all characters in a separate memory position,
    /// instead they keep a pointer to the original String position that they
    /// have accessed last.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.08 MB Beats 67.42%
    pub fn is_subsequence_2(s: String, t: String) -> bool {
        let mut t_chars = t.chars();
        let mut found;
        for s_c in s.chars() {
            found = false;
            while let Some(t_c) = t_chars.next() {
                if s_c == t_c {
                    found = true;
                    break;
                }
            }
            if !found {
                return false;
            }
        }
        true
    }
}

// Tests.
fn main() {
    let tests = [
        ("abc".to_string(), "ahbgdc".to_string(), true),
        ("axc".to_string(), "ahbgdc".to_string(), false),
    ];
    for t in tests {
        assert_eq!(Solution::is_subsequence(t.0.clone(), t.1.clone()), t.2);
        assert_eq!(Solution::is_subsequence_2(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
