// 10. Regular Expression Matching
// 🔴 Hard
//
// https://leetcode.com/problems/regular-expression-matching/
//
// Tags: String - Dynamic Programming - Recursion

use std::iter::once;

struct Solution;
impl Solution {
    /// Use a recursive function and memoization. Starting from the back of both
    /// the pattern and the string makes handling '*' characters easier. We need
    /// to handle the base cases, when the characters don't match and when we
    /// reach the end of the inputs, besides that, we need to handle the expansion
    /// character, we need to check matching it to none, one and more than one
    /// instances of the character to its. We can handle none and one in the
    /// current call of the recursive function, and have successive calls do the
    /// same, that way we have the "multiple" handled for any number of instances.
    ///
    /// Time complexity: O(m*n) - Where m is the length of the string and n is the
    /// length of the pattern. At most, we can call dfs with every combination of
    /// each value in the two input strings.
    /// Space complexity: O(m*n) - The size of the cache 2D vector.
    ///
    /// Runtime 1 ms Beats 85%
    /// Memory 2.02 MB Beats 95.71%
    pub fn is_match(s: String, p: String) -> bool {
        let s = once('^').chain(s.chars()).collect::<Vec<char>>();
        let p = once('^').chain(p.chars()).collect::<Vec<char>>();
        let mut cache = vec![vec![None::<bool>; p.len()]; s.len()];
        fn dfs(
            si32: i32,
            pi: usize,
            s: &Vec<char>,
            p: &Vec<char>,
            cache: &mut Vec<Vec<Option<bool>>>,
        ) -> bool {
            if si32 < 0 {
                return false;
            }
            let si = si32 as usize;
            if let Some(res) = cache[si][pi] {
                return res;
            }
            // Base case, we have matched the entire string and consumed the pattern.
            if s[si] == '^' && p[pi] == '^' {
                cache[si][pi] = Some(true);
                return true;
            }
            // Base case, we have consumed one but not the other.
            if pi == 0 {
                cache[si][pi] = Some(false);
                return false;
            }
            // Easy case, the characters match, consume and move both pointers.
            if s[si] == p[pi] || p[pi] == '.' {
                let res = dfs(si32 - 1, pi - 1, s, p, cache);
                cache[si][pi] = Some(res);
                return res;
            }
            // Handle * wildcard.
            if p[pi] == '*' {
                let skip = dfs(si32, pi - 2, s, p, cache);
                let match_one =
                    (p[pi - 1] == '.' || s[si] == p[pi - 1]) && dfs(si32 - 1, pi - 2, s, p, cache);
                let keep_matching =
                    (p[pi - 1] == '.' || s[si] == p[pi - 1]) && dfs(si32 - 1, pi, s, p, cache);
                let res = skip || match_one || keep_matching;
                cache[si][pi] = Some(res);
                return res;
            }
            cache[si][pi] = Some(false);
            false
        }
        dfs(s.len() as i32 - 1, p.len() - 1, &s, &p, &mut cache)
    }
}

// Tests.
fn main() {
    let tests = [
        ("a".to_string(), "ab*".to_string(), true),
        ("aa".to_string(), "a".to_string(), false),
        ("a".to_string(), "a*a*".to_string(), true),
        ("aa".to_string(), "aa".to_string(), true),
        ("aa".to_string(), "a*".to_string(), true),
        ("ab".to_string(), ".*".to_string(), true),
        ("ab".to_string(), ".*c".to_string(), false),
        ("aab".to_string(), "c*a*b".to_string(), true),
        ("abcd".to_string(), "d*".to_string(), false),
        ("a".to_string(), ".*..a*".to_string(), false),
        ("ab".to_string(), ".*.*.*c*.*".to_string(), true),
        ("abbbbbcd".to_string(), "ab*.*d".to_string(), true),
        ("mississippi".to_string(), "miss*is*p*.".to_string(), false),
        (
            "aaaaaaaaaaaaab".to_string(),
            "a*a*a*a*a*a*a*a*a*a*a*a*b".to_string(),
            true,
        ),
        (
            "abababababababababab".to_string(),
            "a*b.*a*b.*a*b.*a*b.*".to_string(),
            true,
        ),
        (
            "abcdefghijklmnopqrstuvwxyz".to_string(),
            "abcdefghijklmnopqrstuvwxyz".to_string(),
            true,
        ),
        (
            "abcdefghijklmnopqrstuvwxyz".to_string(),
            "abcdefghijklmnopqrstuvwxya".to_string(),
            false,
        ),
        (
            "abcdefghijklmnopqrstuvwxyz".to_string(),
            "ab..efg.ijklmnopqr...vwxy.".to_string(),
            true,
        ),
    ];
    let mut success = true;
    for t in tests {
        let res = Solution::is_match(t.0.clone(), t.1.clone());
        if res != t.2 {
            println!("{} != {} for s: {} p: {}", res, t.2, t.0, t.1);
            success = false;
        }
        // assert_eq!(Solution::is_match(t.0, t.1), t.2);
    }
    if success {
        println!("\x1b[92m» All tests passed!\x1b[0m");
    }
}
