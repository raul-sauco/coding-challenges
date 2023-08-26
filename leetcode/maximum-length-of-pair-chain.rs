// 646. Maximum Length of Pair Chain
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-length-of-pair-chain/
//
// Tags: Array - Dynamic Programming - Greedy - Sorting

struct Solution;
impl Solution {
    /// We can greedily pick the next interval that does not overlap the
    /// previous one and has the minimum right boundary, to do that in linear
    /// time, we can first sort the intervals, then visit them left to right,
    /// if the current interval does not overlap the previous one, we can add
    /// it to the result set and update the current boundary to its right
    /// value.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the highest time complexity,
    /// then checking the intervals can be done in O(n)
    /// Space complexity: O(n) - We need to copy the input vector to have the
    /// ability to sort it, some other languages may let us mutate and sort the
    /// input array without using any extra space.
    ///
    /// Runtime 6 ms Beats 83.33%
    /// Memory 2.09 MB Beats 100%
    pub fn find_longest_chain(pairs: Vec<Vec<i32>>) -> i32 {
        let mut pairs: Vec<(i32, i32)> = pairs.iter().map(|pair| (pair[0], pair[1])).collect();
        pairs.sort_by(|a, b| a.1.cmp(&b.1));
        let mut res = 1;
        let mut limit = pairs[0].1;
        for (l, r) in pairs.iter().skip(1) {
            if *l > limit {
                res += 1;
                limit = *r;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![1, 2], vec![2, 3], vec![3, 4]], 2),
        (vec![vec![1, 2], vec![7, 8], vec![4, 5]], 3),
    ];
    for t in tests {
        assert_eq!(Solution::find_longest_chain(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
