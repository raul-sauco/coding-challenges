// 1431. Kids With the Greatest Number of Candies
//🟢 Easy
//
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
//
// Tags: Array

struct Solution;
impl Solution {
    /// Find the boundary for a kid's candies to be the maximum after we give
    /// them the extra candies as the maximum of the array minus the extra
    /// candies, then iterate checking if the value at each position plus the
    /// extra candies would be greater than the original greatest.
    ///
    /// Time complexity: O(n) - Two passes of the input array.
    /// Space complexity: O(1) - Or, O(n) if we take into account the output
    /// array.
    ///
    /// Runtime 1 ms Beats 76.67%
    /// Memory 2.1 MB Beats 83.33%
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let boundary = candies.iter().max().unwrap() - extra_candies;
        candies.iter().map(|x| x >= &boundary).collect()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2, 3, 5, 1, 3], 3, vec![true, true, true, false, true]),
        (
            vec![4, 2, 1, 1, 2],
            1,
            vec![true, false, false, false, false],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::kids_with_candies(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
