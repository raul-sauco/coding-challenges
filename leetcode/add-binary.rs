// 67. Add Binary
// 🟢 Easy
//
// https://leetcode.com/problems/add-binary/
//
// Tags: Math - String - Bit Manipulation - Simulation

struct Solution;
impl Solution {
    // Iterate over both strings from the bits of least weight to the bits of
    // most weight adding them into a result.
    //
    // Time complexity: O(max(m,n)) - Where m and n are the lengths of a and
    // b, we will iterate as many times as characters on the longest input
    // string.
    // Space complexity: O(max(m,n)) - The list of resulting bits will have
    // as many elements as digits on the longest input string plus possibly
    // one more.
    //
    // Runtime 2 ms Beats 62.23%
    // Memory 2 MB Beats 67.73%
    pub fn add_binary(a: String, b: String) -> String {
        // Bits in a and b.
        let mut a_bits: Vec<char> = a.chars().collect();
        let mut b_bits: Vec<char> = b.chars().collect();
        let mut carry = 0;
        let mut bits: Vec<char> = vec![];
        while a_bits.len() > 0 || b_bits.len() > 0 || carry != 0 {
            let mut res = carry;
            if a_bits.len() > 0 {
                match a_bits.pop() {
                    Some(c) => {
                        if c == '1' {
                            res += 1;
                        }
                    }
                    None => (),
                };
            }
            if b_bits.len() > 0 {
                match b_bits.pop() {
                    Some(c) => {
                        if c == '1' {
                            res += 1;
                        }
                    }
                    None => (),
                };
            }
            // Adjust the values for the next iteration.
            carry = if res > 1 { 1 } else { 0 };
            bits.push(if res == 1 || res == 3 { '1' } else { '0' });
        }
        bits.into_iter().rev().collect()
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::add_binary(String::from("11"), String::from("1")),
        String::from("100")
    );
    assert_eq!(
        Solution::add_binary(String::from("1010"), String::from("1011")),
        String::from("10101")
    );
    println!("All tests passed!")
}
