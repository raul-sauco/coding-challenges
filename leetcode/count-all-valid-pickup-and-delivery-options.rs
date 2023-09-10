// 1359. Count All Valid Pickup and Delivery Options
// 🔴 Hard
//
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
//
// Tags: Math - Dynamic Programming - Combinatorics

struct Solution;
impl Solution {
    /// There is only one way to position the pair elements when we only have
    /// one pair, that is the base case, then start computing how many ways we
    /// can insert the next pair in the existing elements, the pickup can be
    /// inserted in any of the 2n - 1 positions, the delivery in any of the 2n
    /// positions, but only after the pickup.
    ///
    /// Time complexity: O(n) - The loop runs n times, for each time we do
    /// constant time work.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 100%
    pub fn count_orders(n: i32) -> i32 {
        let mut res = 1;
        let m = 1_000_000_007;
        for i in 2..=n as usize {
            res = res * (i * 2 - 1) * i % m;
        }
        res as i32
    }

    /// Same logic as the solution above but using an iterator and fold.
    ///
    /// Time complexity: O(n) - The loop runs n times, for each time we do
    /// constant time work.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.01 MB Beats 100%
    pub fn count_orders_2(n: i32) -> i32 {
        (2..=n as usize).fold(1, |acc, i| acc * (i * 2 - 1) * i % 1000000007) as i32
    }

    /// Use combinatronics, the solution is (2n)!/(2^n)
    ///
    /// Time complexity: O(n) - The loop runs 2n times, for each time we do
    /// constant time work.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.05 MB Beats 100%
    pub fn count_orders_3(n: i32) -> i32 {
        let mut res = 1;
        for i in 2..=2 * n as usize {
            res *= i;
            res >>= (i - 1) % 2;
            res %= 1_000_000_007;
        }
        res as i32
    }

    /// Same as the previous version but use an iterator and fold.
    ///
    /// Time complexity: O(n) - The loop runs 2n times, for each time we do
    /// constant time work.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.23 MB Beats 50%
    pub fn count_orders_4(n: i32) -> i32 {
        (2..=2 * n as usize).fold(1, |acc, i| ((acc * i) >> ((i - 1) % 2)) % 1_000_000_007) as i32
    }
}

// Tests.
fn main() {
    let tests = [(1, 1), (2, 6), (3, 90), (500, 764678010)];
    for t in tests {
        assert_eq!(Solution::count_orders(t.0), t.1);
        assert_eq!(Solution::count_orders_2(t.0), t.1);
        assert_eq!(Solution::count_orders_3(t.0), t.1);
        assert_eq!(Solution::count_orders_4(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
