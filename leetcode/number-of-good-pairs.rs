// 1512. Number of Good Pairs
// 🟢 Easy
//
// https://leetcode.com/problems/number-of-good-pairs/
//
// Tags: Array - Hash Table - Math - Counting

struct Solution;
impl Solution {
    /// Iterate over the input values, keep a vector that stores how many times
    /// we have seen a given value. For each number in the input vector, we
    /// can make one pair for each time we have seen the same value previously.
    ///
    /// Time complexity: O(n) - We visit each element in the input and do
    /// constant time work for each.
    /// Space complexity: O(1) - We use an integer and an array of size 101 of
    /// extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.02 MB Beats 66.10%
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut seen = [0; 101];
        let mut res = 0;
        let nums = nums.into_iter().map(|x| x as usize).collect::<Vec<usize>>();
        for num in nums {
            res += seen[num];
            seen[num] += 1;
        }
        res
    }

    /// Similar logic as the solution above but use iterators. Iterate once to
    /// count the number of times we see each item in an array, then iterate
    /// that array, the number of pairs we can construct with each value is
    /// x * (x-1) / 2 where x is the number of instances of that value.
    ///
    /// Time complexity: O(n) - We visit each element in the input and do
    /// constant time work for each.
    /// Space complexity: O(1?) - Not sure if the iterators use extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.02 MB Beats 66.10%
    pub fn num_identical_pairs_2(nums: Vec<i32>) -> i32 {
        nums.into_iter()
            .fold([0; 101], |mut acc, num| {
                acc[num as usize] += 1;
                acc
            })
            .iter()
            .fold(0, |acc, x| acc + x * (x - 1) / 2)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 1, 1, 3], 4),
        (vec![1, 1, 1, 1], 6),
        (vec![1, 2, 3], 0),
    ];
    for t in tests {
        assert_eq!(Solution::num_identical_pairs(t.0.clone()), t.1);
        assert_eq!(Solution::num_identical_pairs_2(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
