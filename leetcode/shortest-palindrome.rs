// 214. Shortest Palindrome
// 🔴 Hard
//
// https://leetcode.com/problems/shortest-palindrome/
//
// Tags: String - Rolling Hash - String Matching - Hash Function

struct Solution;
impl Solution {
    /// Use a sliding window technique with the left pointer at the start of the string and the
    /// right pointer starting at the end and moving left one element for each iteration. For each
    /// sliding window, move the pointers one element at a time towards the center to check if we
    /// have a palindrome between 0..l, if we don't, store the current right character in a prefix
    /// string that we build and move onto the next left character, if we do, return the current
    /// prefix plus the input string.
    ///
    /// Time complexity: O(n^2) - For each character, we try to build a palindrome using the entire
    /// string at a cost of O(n)
    /// Space complexity: O(n) - The Vec<char> that we use to be able to index characters.
    ///
    /// Runtime 113 ms Beats 19%
    /// Memory 2.24 MB Beats 85%
    #[allow(dead_code)]
    pub fn shortest_palindrome_tp(s: String) -> String {
        let sv = s.chars().collect::<Vec<_>>();
        let mut res = String::new();
        let (mut l, mut r);
        for i in (0..sv.len()).rev() {
            if i == 0 {
                res.push_str(&s);
                return res;
            }
            (l, r) = (0, i);
            while l < r - 1 && sv[l] == sv[r] {
                l += 1;
                r -= 1;
            }
            if l == r || (l == r - 1 && sv[l] == sv[r]) {
                // We found a partial match.
                res.push_str(&s);
                break;
            } else {
                res.push(sv[i]);
            }
        }
        res
    }

    /// A more efficient implementation using a rolling hash.
    ///
    /// Time complexity: O(n) - We visit each character in the input string and do O(1) work.
    /// Space complexity: O(n) - The Vec<char> that we use to be able to index characters.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.31 MB Beats 66%
    pub fn shortest_palindrome(s: String) -> String {
        let (hash_base, mod_value, ord) = (29, 1_000_000_007, b'a' as usize);
        let (mut forward_hash, mut reverse_hash) = (0, 0);
        let (mut power_value, mut palindrome_end_index) = (1, -1);
        for (i, c) in s.bytes().map(|x| x as usize).enumerate() {
            forward_hash = (forward_hash * hash_base + (1 + c - ord)) % mod_value;
            reverse_hash = (reverse_hash + (1 + c - ord) * power_value) % mod_value;
            power_value = (power_value * hash_base) % mod_value;
            if forward_hash == reverse_hash {
                palindrome_end_index = i as i32;
            }
        }
        s[(palindrome_end_index + 1) as usize..]
            .chars()
            .rev()
            .chain(s.chars())
            .collect()
    }
}

// Tests.
fn main() {
    let tests = [
        ("", ""),
        ("abcd", "dcbabcd"),
        ("aacecaaa", "aaacecaaa"),
        ("aaceecaaa", "aaaceecaaa"),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::shortest_palindrome(t.0.to_string());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
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
