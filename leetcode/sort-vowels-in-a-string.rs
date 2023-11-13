// 2785. Sort Vowels in a String
// 🟠 Medium
//
// https://leetcode.com/problems/sort-vowels-in-a-string/
//
// Tags: String - Sorting

struct Solution;
impl Solution {
    /// Extract the vowels, sort them, and then use the sorted vowels to reconstruct the input.
    ///
    /// Time complexity: O(n*log(n)) - We first extract the vowels in O(n), then we sort the
    /// vowels, which could be the entire input of length n. in the worst case, then we iterate
    /// over the input again to replace the unsorted vowels with the sorted ones.
    /// Space complexity: O(n) - The vowels vector.
    ///
    /// Runtime 3 ms Beats 100%
    /// Memory 2.76 MB Beats 55.56%
    pub fn sort_vowels(s: String) -> String {
        fn is_vowel(c: &char) -> bool {
            match c {
                'a' | 'A' | 'e' | 'E' | 'i' | 'I' | 'o' | 'O' | 'u' | 'U' => true,
                _ => false,
            }
        }

        let mut vowels = s.chars().filter(|c| is_vowel(c)).collect::<Vec<_>>();
        vowels.sort_unstable_by(|a, b| b.cmp(a));
        s.chars()
            .map(|c| {
                if is_vowel(&c) {
                    vowels.pop().unwrap()
                } else {
                    c
                }
            })
            .collect::<String>()
    }
}

// Tests.
fn main() {
    let tests = [
        ("UEeuaOiAoI".to_string(), "AEIOUaeiou".to_string()),
        ("lYmpH".to_string(), "lYmpH".to_string()),
        ("lEetcOde".to_string(), "lEOtcede".to_string()),
    ];
    for t in tests {
        assert_eq!(Solution::sort_vowels(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
