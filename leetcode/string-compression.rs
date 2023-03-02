// 443. String Compression
// 🟠 Medium
//
// https://leetcode.com/problems/string-compression/
//
// Tags: Two Pointers - String

struct Solution;
impl Solution {
    // Use two pointers, one to read and one to write, iterate over all the
    // characters in the input reading characters while there are any and
    // they are the same as the current sequence's character, when we run out
    // of characters or find a new character, we write down the compressed
    // sequence and check if there are more characters to read.
    //
    // Time complexity: O(n) - We visit each character in the input once.
    // Space complexity: O(1) - We use pointers and create a new string of
    // the digits of count that can be at most of length 4.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.1 MB Beats 100%
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        let mut write = 0;
        let mut read = 0;
        let mut current: char;
        let mut count;
        while read < chars.len() {
            current = chars[read];
            count = 0;
            while read < chars.len() && current == chars[read] {
                read += 1;
                count += 1
            }
            // Write the compressed sequence.
            chars[write] = current;
            write += 1;
            if count > 1 {
                for digit in count.to_string().chars() {
                    chars[write] = digit;
                    write += 1;
                }
            }
        }
        write as i32
    }
}

// Tests.
fn main() {
    let tests = [("a", 1), ("aabbccc", 6), ("abbbbbbbbbbbb", 4)];
    for test in tests {
        let mut chars = String::from(test.0).chars().collect();
        assert_eq!(Solution::compress(&mut chars), test.1);
    }
    println!("All tests passed!")
}
