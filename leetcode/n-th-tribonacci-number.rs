// 1137. N-th Tribonacci Number
// 🟢 Easy
//
// https://leetcode.com/problems/n-th-tribonacci-number/
//
// Tags: Math - Dynamic Programming - Memoization

struct Solution;
impl Solution {
    // Use three variables initialized to the three initial tribonacci values,
    // iterate over 3..n values computing the sum of the current three
    // variables, discarding the lowest one and adding the sum as the third
    // value. The result will be that sum at the last iteration.
    //
    // Time complexity: O(n) - The loop executes n-2 times.
    // Space complexity: O(1) - Constant space used.
    //
    // Runtime 1 ms Beats 80%
    // Memory 3.4 MB Beats 5.71%
    pub fn tribonacci_plain(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        let mut a = 0;
        let mut b = 1;
        let mut c = 1;
        for _ in 0..n - 2 {
            let tn = a + b + c;
            a = b;
            b = c;
            c = tn;
        }
        c
    }

    // One idiomatic way to solve this could be to use fold.
    //
    // Time complexity: O(n) - Fold executes n times.
    // Space complexity: O(1) - Constant space used.
    //
    // Runtime 1 ms Beats 80%
    // Memory 2 MB Beats 55.71%
    pub fn tribonacci(n: i32) -> i32 {
        (0..n).fold((0, 0, 1), |(a, b, c), _| (b + a + c, a, b)).0
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::tribonacci(0), 0);
    assert_eq!(Solution::tribonacci(1), 1);
    assert_eq!(Solution::tribonacci(2), 1);
    assert_eq!(Solution::tribonacci(3), 2);
    assert_eq!(Solution::tribonacci(25), 1389537);
    assert_eq!(Solution::tribonacci(37), 2082876103);
    assert_eq!(Solution::tribonacci_plain(37), 2082876103);
    println!("All tests passed!")
}
