// 1561. Maximum Number of Coins You Can Get
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
//
// Tags: Array - Math - Greedy - Sorting - Game Theory

struct Solution;
impl Solution {
    /// We sort the input vector, then we iterate from the highest value taking every second
    /// value. The reasoning is that Alice will always keep the coin with the most value out of the
    /// remaining ones, since we want to maximize our total. To maximize the remaining total, we
    /// give Bob the smallest remaining coin. The easiest way to implement the algorithm is to sort
    /// the input, skip n/3 values that Bob will take, then take every second value, the result
    /// would be the same as if in each step we gave the highest to Alice, we took the next
    /// highest, and gave Bob the lowest.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the highest TC, linear time, once the vector is
    /// sorted, to collect every second highest value.
    /// Space complexity: O(n) - The local copy of the input that we sort.
    ///
    /// Runtime 18 ms Beats 75%
    /// Memory 3.33 MB Beats 25%
    pub fn max_coins(piles: Vec<i32>) -> i32 {
        let n = piles.len();
        let mut piles = piles;
        piles.sort_unstable();
        piles.into_iter().rev().skip(1).step_by(2).take(n / 3).sum()
    }

    /// Same logic as the previous solution, but mutate the input vector and iterate forward.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the highest TC, linear time, once the vector is
    /// sorted, to collect every second highest value.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 18 ms Beats 75%
    /// Memory 3.16 MB Beats 87.50%
    pub fn max_coins_2(mut piles: Vec<i32>) -> i32 {
        piles.sort_unstable();
        piles.iter().skip(piles.len() / 3).step_by(2).sum()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2, 4, 1, 2, 7, 8], 9),
        (vec![2, 4, 5], 4),
        (vec![9, 8, 7, 6, 5, 1, 2, 3, 4], 18),
    ];
    for t in tests {
        assert_eq!(Solution::max_coins(t.0.clone()), t.1);
        assert_eq!(Solution::max_coins_2(t.0.clone()), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
