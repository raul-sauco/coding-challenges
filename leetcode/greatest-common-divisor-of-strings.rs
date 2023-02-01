// 1071. Greatest Common Divisor of Strings
// 🟢 Easy
//
// https://leetcode.com/problems/greatest-common-divisor-of-strings/
//
// Tags: Math - String

struct Solution;
impl Solution {
    // If both input strings are formed by concatenating the same substring,
    // then concatenating them should be an associative operation, we can
    // use that to check if they have a GCD string. Once we know that they do,
    // we know that the length of the GCD string will be the length of the
    // GCD of their respective lengths.
    //
    // Time complexity: O(m+n) - We need to iterate both input strings to
    // concatenate them and check if they have a GCD. The `gcd` function
    // takes O(log(m*n)) time.
    // Space complexity: O(m+n) - The concatenated strings use extra memory.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.1 MB Beats 66.67%
    pub fn gcd_of_strings(str1: String, str2: String) -> String {
        /// A function that computes the GCD between two given non-negative
        /// integers. There is a more efficient version in Wikipedia.
        /// https://en.wikipedia.org/wiki/Binary_GCD_algorithm
        fn gcd(mut a: usize, mut b: usize) -> usize {
            if a < b {
                (a, b) = (b, a);
                // The above works on rustc 1.66 but fails in v1.58
                // return gcd(b, a);
            }
            while b != 0 {
                (a, b) = (b, a % b);
                // The above works on rustc 1.66 but fails in v1.58
                // let tmp = a % b;
                // a = b;
                // b = tmp;
            }
            a
        }
        if str1.clone() + &str2.clone() != str2.clone() + &str1.clone() {
            String::from("")
        } else {
            str1[..gcd(str1.len(), str2.len())].to_owned()
        }
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::gcd_of_strings(String::from("LEET"), String::from("CODE")),
        ""
    );
    assert_eq!(
        Solution::gcd_of_strings(String::from("ABCABC"), String::from("ABC")),
        "ABC"
    );
    assert_eq!(
        Solution::gcd_of_strings(String::from("ABABAB"), String::from("ABAB")),
        "AB"
    );
    assert_eq!(
        Solution::gcd_of_strings(String::from("ABABABAB"), String::from("ABAB")),
        "ABAB"
    );
    assert_eq!(
        Solution::gcd_of_strings(String::from("ABBAABBA"), String::from("ABBA")),
        "ABBA"
    );
    println!("All tests passed!")
}
