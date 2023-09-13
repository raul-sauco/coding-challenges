// 135. Candy
// 🔴 Hard
//
// https://leetcode.com/problems/candy/
//
// Tags: Array - Greedy

struct Solution;
impl Solution {
    /// Use an extra auxiliary vector of the same size as the input vector to
    /// store the candy assigned to each child initialized to 1 for each child.
    /// Iterate over the input array forward, for each child that has a higher
    /// rating that the one to its left, give it one more candy that the one to
    /// its left already has. Once we reach the end we traverse backwards, for
    /// each child that has a higher rating than the one to its right, if its it
    /// not already getting more candy than the one to its right is, we give it
    /// the amount of candy that that one gets plus 1. We return the sum of
    /// values in the assigned candy array.
    ///
    /// Time complexity: O(n) - We traverse over n elements twice.
    /// Space complexity: O(n) - We store an extra vector of size n in memory.
    ///
    /// Runtime 2 ms Beats 89.25%
    /// Memory 2.14 MB Beats 84.95%
    pub fn candy(ratings: Vec<i32>) -> i32 {
        let n = ratings.len();
        let mut assignments = vec![1; n];
        for i in 1..n {
            if ratings[i] > ratings[i - 1] {
                assignments[i] = assignments[i - 1] + 1;
            }
        }
        let mut res = assignments[n - 1];
        for i in (0..n - 1).rev() {
            if ratings[i] > ratings[i + 1] && assignments[i] <= assignments[i + 1] {
                assignments[i] = assignments[i + 1] + 1;
            }
            res += assignments[i];
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![1, 0, 2], 5), (vec![1, 2, 2], 4)];
    for t in tests {
        assert_eq!(Solution::candy(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
