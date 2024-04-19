// 1930. Unique Length-3 Palindromic Subsequences
// 🟠 Medium
//
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
//
// Tags: Hash Table - String - Prefix Sum

#[derive(Debug, Copy, Clone, PartialEq, PartialOrd)]
enum PalindromeState {
    Empty,
    TwoChars,
    Complete,
}

struct Solution;
impl Solution {
    /// We can use an array of size 26 with characters that we have seen already, and a lookup
    /// table of size 26x26 with the state of palindromes that we are building, each three letter
    /// palindrome only has two distinct letters, the outer one and the inner one, which can be the
    /// same letter, we can use that fact to identify the palindromes with two char sequences, for
    /// example 'xy', if we record the current state of each palindrome, that gives us a quick way
    /// to access and modify palindromes. First we check any palindromes that have the current
    /// character as the outer character, if any of them are in the "two character" state, we can
    /// close them and complete them. Then we can use characters that we have seen to mark
    /// palindromes that we have not started building yet as "Two Char", we have the first and
    /// second character, but are missing the closing one.
    ///
    /// Time complexity: O(n) - For each character in the input of size n, we iterate over two
    /// vectors of size 26, one of them is a row, and another a column, in the lookup table.
    /// Space complexity: O(1) - We use an array of size 26 and a 2D array of size 26x26.
    ///
    /// Runtime 24 ms Beats 100%
    /// Memory 2.39 MB Beats 100%
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        const K: usize = 26;
        // Store the palindromes, key is the outer char, values are the inner ones.
        let mut palindromes = [[PalindromeState::Empty; K]; K];
        let mut seen = [false; 26];
        let mut c_idx;
        let mut res = 0;
        for c in s.bytes() {
            c_idx = (c - b'a') as usize;
            // Check for any open palindromes that we could close with this char.
            for j in 0..K {
                if palindromes[c_idx][j] == PalindromeState::TwoChars {
                    palindromes[c_idx][j] = PalindromeState::Complete;
                    res += 1;
                }
            }
            // Construct two char sequences.
            for i in 0..K {
                if seen[i] && palindromes[i][c_idx] == PalindromeState::Empty {
                    palindromes[i][c_idx] = PalindromeState::TwoChars;
                }
            }
            // And last, mark this as seen, easier to not check if it was true already.
            seen[c_idx] = true;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        ("aabca".to_string(), 3),
        ("adc".to_string(), 0),
        ("bbcbaba".to_string(), 4),
    ];
    for t in tests {
        assert_eq!(Solution::count_palindromic_subsequence(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
