// 880. Decoded String at Index
// 🟠 Medium
//
// https://leetcode.com/problems/decoded-string-at-index/
//
// Tags: String - Stack

struct Solution;
impl Solution {
    /// Simulate the decoding of the string without actually decoding it,
    /// use the values that we encounter to compute the length of the
    /// resulting decoded string, when it is long enough, travel back over
    /// the indexes to find the character that is at position k.
    ///
    /// Time complexity: O(n) - We iterate over all elements in the input String
    /// twice and do constant work for each both times.
    /// Space complexity: O(n) - We use an extra vector of the same length as
    /// the input string. We could do away with the vector using iterators but
    /// using a nested iterator inside the loops to access characters using
    /// their index requires iterating over that many characters and overall
    /// time complexity would then be O(n^2)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.09 MB Beats 100%
    pub fn decode_at_index(s: String, k: i32) -> String {
        let mut k = k as usize;
        let s: Vec<char> = s.chars().collect();
        let mut current_length = 0;
        let mut i = 0;
        let mut c;
        while current_length < k {
            c = s[i];
            if c.is_digit(10) {
                current_length *= c.to_digit(10).unwrap() as usize;
            } else {
                current_length += 1;
            }
            i += 1;
        }
        for j in (0..i).rev() {
            c = s[j];
            if c.is_digit(10) {
                current_length /= c.to_digit(10).unwrap() as usize;
                k %= current_length;
            } else {
                if k == 0 || k == current_length {
                    return c.to_string();
                }
                current_length -= 1;
            }
        }
        unreachable!()
    }
}

// Tests.
fn main() {
    let tests = [
        ("ha22".to_string(), 5, "h".to_string()),
        ("leet2code3".to_string(), 10, "o".to_string()),
        ("a2345678999999999999999".to_string(), 1, "a".to_string()),
    ];
    for t in tests {
        assert_eq!(Solution::decode_at_index(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
