// 125. Valid Palindrome
// 🟢 Easy
//
// https://leetcode.com/problems/valid-palindrome/
//
// Tags: Two Pointers - String

struct Solution1;
impl Solution1 {
    // Two pointers, one from the start of the string and one from the end
    // keep looping until they meet, if the character under either pointer
    // is not alphanumeric, skip that character, when they both are, check
    // that they are the same character, independently of the case.
    //
    // Time complexity: O(n) - One pass to clean up the input and another to
    // check if the remaining characters form a palindrome.
    // Space complexity: O(1) - Only pointers stored in memory though maybe
    // join and filter may use extra memory.
    //
    // Runtime 2 ms Beats 62.8%
    // Memory 2.3 MB Beats 59.11%
    pub fn is_palindrome(s: String) -> bool {
        let mut l = 0;
        let mut r = s.len() - 1;
        let s = s.as_bytes();
        while l < r {
            let a = s[l] as char;
            if !a.is_alphanumeric() {
                l += 1;
                continue;
            }
            let b = s[r] as char;
            if !b.is_alphanumeric() {
                r -= 1;
                continue;
            }
            if a.to_lowercase().to_string() != b.to_lowercase().to_string() {
                return false;
            }
            l += 1;
            r -= 1;
        }
        true
    }
}
struct Solution;
impl Solution {
    // First clean the string, then iterate over the characters using a
    // pointer at the start and one at the end checking that the characters
    // at the same distance from the middle match.
    //
    // Time complexity: O(n) - One pass to clean up the input and another to
    // check if the remaining characters form a palindrome.
    // Space complexity: O(n) - s1 has the same size as the input string.
    //
    // Runtime 3 ms Beats 55.39%
    // Memory 2.6 MB Beats 29.74%
    pub fn is_palindrome(s: String) -> bool {
        // The idiomatic way to remove non alphanumerical characters in Rust.
        let s1: Vec<char> = s
            .chars()
            .filter(|c| c.is_alphanumeric())
            .map(|c| c.to_ascii_lowercase())
            .collect();
        if s1.len() == 0 {
            return true;
        }
        let mut l = 0;
        let mut r = s1.len() - 1;
        while l < r {
            if s1[l] != s1[r] {
                return false;
            }
            l += 1;
            r -= 1;
        }
        true
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::is_palindrome(String::from(" ")), true);
    assert_eq!(Solution1::is_palindrome(String::from(" ")), true);
    assert_eq!(Solution::is_palindrome(String::from(".,")), true);
    assert_eq!(Solution::is_palindrome(String::from("0P")), false);
    assert_eq!(Solution::is_palindrome(String::from("race a car")), false);
    assert_eq!(
        Solution::is_palindrome(String::from("A man, a plan, a canal: Panama")),
        true
    );
    assert_eq!(
        Solution1::is_palindrome(String::from("A man, a plan, a canal: Panama")),
        true
    );
    println!("All tests passed!")
}
