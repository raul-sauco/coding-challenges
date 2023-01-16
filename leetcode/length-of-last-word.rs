// 58. Length of Last Word
// 🟢 Easy
//
// https://leetcode.com/problems/length-of-last-word/
//
// Tags: String

struct Solution;
impl Solution {
    // Iterate over the characters in the input string in reverse order,
    // ignore any whitespace found before non-whitespace chars, then
    // count the non-whitespace chars until more whitespace is found or
    // we get to the beginning of the string.
    //
    // Time complexity: O(n) - We may iterate over all the input.
    // Space complexity: O(1) - We only use pointers.
    //
    // Runtime 1 ms Beats 71.17%
    // Memory 2.1 MB Beats 34.67%
    pub fn length_of_last_word(s: String) -> i32 {
        // Count of characters in the last word.
        let mut count = 0;
        for char in s.chars().rev() {
            if char == ' ' {
                if count == 0 {
                    continue;
                }
                return count;
            }
            count += 1;
        }
        // If we exit the loop is because the last word starts at index 0
        count
    }
}

// Tests.
fn main() {
    // This test is not necessary because the problem guarantees at least one word.
    assert_eq!(Solution::length_of_last_word(String::from(""),), 0,);
    assert_eq!(Solution::length_of_last_word(String::from("     "),), 0,);
    assert_eq!(Solution::length_of_last_word(String::from("l     "),), 1,);
    assert_eq!(
        Solution::length_of_last_word(String::from("Hello World"),),
        5,
    );
    assert_eq!(
        Solution::length_of_last_word(String::from("luffy is still joyboy"),),
        6,
    );
    assert_eq!(
        Solution::length_of_last_word(String::from("   fly me   to   the moon  "),),
        4,
    );
    println!("All tests passed!")
}
