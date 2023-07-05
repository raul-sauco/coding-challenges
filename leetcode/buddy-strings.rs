// 859. Buddy Strings
// 🟢 Easy
//
// https://leetcode.com/problems/buddy-strings/
//
// Tags: Hash Table - String

struct Solution;
/// Check all the conditions required by the problem description. Strings must
/// have the same length, when we iterate over the characters of the strings,
/// they must either all match and there must be a character that appears more
/// than once, or there must be only two mismatches and the characters on them
/// must be the same in both strings but in the reverse position.
///
/// Time complexity: O(n) - We visit each character in both of the strings and
/// do O(1) work for each.
/// Space complexity: O(k+n) - The dp vector has size k, the call stack will
/// reach height n.
///
/// Runtime 1 ms Beats 81.18%
/// Memory 2.3 MB Beats 15.88%
impl Solution {
    pub fn buddy_strings(s: String, goal: String) -> bool {
        if s.len() != goal.len() {
            return false;
        }
        let mut seen = vec![false; 26];
        let mut repeated_char = false;
        let mut mismatch = (0, 0);
        let mut found_mismatch = false;
        let goal = goal.into_bytes();
        for (i, c) in s.into_bytes().into_iter().enumerate() {
            if c != goal[i] {
                if found_mismatch {
                    return false;
                }
                if mismatch == (0, 0) {
                    mismatch = (c, goal[i]);
                } else {
                    if (goal[i], c) == mismatch {
                        found_mismatch = true;
                    } else {
                        return false;
                    }
                }
            }
            let cp = (c - b'a') as usize;
            if seen[cp] {
                repeated_char = true;
            }
            seen[cp] = true;
        }
        found_mismatch || (mismatch == (0, 0) && repeated_char)
    }
}

// Tests.
fn main() {
    let tests = [
        (String::from("ab"), String::from("ba"), true),
        (String::from("ab"), String::from("ab"), false),
        (String::from("aa"), String::from("aa"), true),
        (String::from("abc"), String::from("acd"), false),
        (String::from("abac"), String::from("abad"), false),
    ];
    for t in tests {
        assert_eq!(Solution::buddy_strings(t.0, t.1), t.2);
    }
    println!("[92m» All tests passed![0m")
}
