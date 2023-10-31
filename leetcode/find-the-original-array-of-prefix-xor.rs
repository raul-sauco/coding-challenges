// 2433. Find The Original Array of Prefix Xor
// 🟠 Medium
//
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
//
// Tags: Array - Bit Manipulation

struct Solution;
impl Solution {
    /// Use the bitwise swap property; given A ^ B = C then A ^ C = B and B ^ C = A.
    /// Each value of the result can be computed as the xor of the values on the
    /// same index and the previous one in the input.
    ///
    /// Time complexity: O(n) - We visit each element and do O(1) work for each.
    /// Space complexity: O(1) - If we do not count the input and result vectors.
    ///
    /// Runtime 31 ms Beats 70.27%
    /// Memory 3.65 MB Beats 70.27%
    pub fn find_array(pref: Vec<i32>) -> Vec<i32> {
        let n = pref.len();
        let mut res = Vec::with_capacity(n);
        res.push(pref[0]);
        for i in 1..n {
            res.push(pref[i] ^ pref[i - 1]);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![5, 2, 0, 3, 1], vec![5, 7, 2, 3, 2])];
    for t in tests {
        assert_eq!(Solution::find_array(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
