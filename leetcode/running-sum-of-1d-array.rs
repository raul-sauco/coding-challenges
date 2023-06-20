// 1480. Running Sum of 1d Array
// 🟢 Easy
//
// https://leetcode.com/problems/running-sum-of-1d-array/
//
// Tags: Array - Prefix Sum

struct Solution;
impl Solution {
    /// Iterate over the input computing the prefix sum adding each element to
    /// the previous sum.
    ///
    /// Time complexity: O(n) - We visit each element in the input and do O(1)
    /// work for each.
    /// Space complexity: O(1) - Constant space if we do not take the output
    /// vector into account, otherwise O(n)
    ///
    /// Runtime 1 ms Beats 73.74%
    /// Memory 2 MB Beats 73.30%
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        nums.iter()
            .scan(0, |sum, i| {
                *sum += i;
                Some(*sum)
            })
            .collect::<Vec<_>>()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 4], vec![1, 3, 6, 10]),
        (vec![1, 1, 1, 1, 1], vec![1, 2, 3, 4, 5]),
        (vec![3, 1, 2, 10, 1], vec![3, 4, 6, 16, 17]),
    ];
    for t in tests {
        assert_eq!(Solution::running_sum(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
