// 1456. Maximum Number of Vowels in a Substring of Given Length
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
//
// Tags: String - Sliding Window

struct Solution;
impl Solution {
    /// Use two pointers to iterate over a substring of size k, when the right
    /// pointer reads a vowel, it increases the count of vowels in the substring
    /// by one, when the left pointer does, it decreases it by one, we return
    /// the max count of vowels that we have seen.
    ///
    /// Time complexity: O(n) - We visit once each character in the input and
    /// do O(1) work for each.
    /// Space complexity: O(n) - We use a vector of chars of the same size as
    /// the input. This is the easiest way of iterating over the characters
    /// since Rust won't let us index a String type.
    ///
    /// Runtime 10 ms Beats 50%
    /// Memory 2.6 MB Beats 50%
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let k = k as usize;
        let chars: Vec<char> = s.chars().collect();
        let (mut best, mut cur) = (0, 0);
        for r in 0..s.len() {
            match chars[r] {
                'a' | 'e' | 'i' | 'o' | 'u' => cur += 1,
                _ => {}
            };
            if r >= k {
                match chars[r - k] {
                    'a' | 'e' | 'i' | 'o' | 'u' => cur -= 1,
                    _ => {}
                }
            }
            if cur > best {
                best = cur;
            }
        }
        best as i32
    }
}

// Tests.
fn main() {
    let tests = [
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
        ("thlslsswprdwlthpvt", 4, 0),
    ];
    for t in tests {
        assert_eq!(Solution::max_vowels(String::from(t.0), t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
