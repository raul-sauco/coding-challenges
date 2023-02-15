// 989. Add to Array-Form of Integer
// 🟢 Easy
//
// https://leetcode.com/problems/add-to-array-form-of-integer/
//
// Tags: Array - Math

struct Solution;
impl Solution {
    // Create an empty array that we will use to build the result, iterate
    // over the digits in num from right to left adding the current carry,
    // we use mod to compute the resulting digit and div // 10 to "consume"
    // the current carry digit.
    //
    // Time complexity: O(max(n, log(k))) - On each loop we consume one digit
    // of num and divide k by 10, the loops will keep going as long as we
    // have digits or k is not zero.
    // Space complexity: O(max(n, log(k))) - The number of digits in the
    // result is directly proportional to the longest between the number of
    // digits in num and k.
    //
    // Runtime 8 ms Beats 100%
    // Memory 2.3 MB Beats 53.33%
    pub fn add_to_array_form(num: Vec<i32>, k: i32) -> Vec<i32> {
        let mut res = num.clone();
        let mut carry = k;
        for i in (0..res.len()).rev() {
            carry += res[i];
            res[i] = carry % 10;
            carry /= 10;
        }
        // Handle the case when k is greater or there is a leftover carry.
        let mut c: Vec<i32> = vec![];
        while carry != 0 {
            c.push(carry % 10);
            carry /= 10;
        }
        c.into_iter().rev().chain(res.into_iter()).collect()
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::add_to_array_form(vec![2, 7, 4], 181),
        vec![4, 5, 5]
    );
    assert_eq!(
        Solution::add_to_array_form(vec![9], 9999),
        vec![1, 0, 0, 0, 8]
    );
    assert_eq!(
        Solution::add_to_array_form(vec![2, 1, 5], 806),
        vec![1, 0, 2, 1]
    );
    println!("All tests passed!")
}
