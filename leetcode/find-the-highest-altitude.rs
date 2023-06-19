// 1732. Find the Highest Altitude
// 🟢 Easy
//
// https://leetcode.com/problems/find-the-highest-altitude/
//
// Tags: Array - Prefix Sum

struct Solution;
impl Solution {
    /// Iterate over the input values keeping track of the sum up to the
    /// current value, return the highest value seen.
    ///
    /// Time complexity: O(n) - We visit each element of the input and do
    /// constant work for each.
    /// Space complexity: O(1) - We only store to i32 values.
    ///
    /// Runtime 1 ms Beats 83.50%
    /// Memory 2 MB Beats 94.17%
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut sum = 0;
        for g in gain {
            sum += g;
            if sum > res {
                res = sum;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![-5, 1, 5, 0, -7], 1),
        (vec![-4, -3, -2, -1, 4, 3, 2], 0),
    ];
    for t in tests {
        assert_eq!(Solution::largest_altitude(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
