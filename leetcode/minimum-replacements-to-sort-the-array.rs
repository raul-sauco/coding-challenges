// 2366. Minimum Replacements to Sort the Array
// 🔴 Hard
//
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
//
// Tags: Array - Math - Greedy

struct Solution;
impl Solution {
    /// Traverse the items from the right, each time that we find a value
    /// greater than the one to its right we need to split it into multiple
    /// values, the optimal way to do that is to maximize the minimum resulting
    /// value, that way we improve the maximum for values to the left.
    ///
    /// Time complexity: O(n) - We do one single traversal of the input.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 8 ms Beats 100%
    /// Memory 4.22 MB Beats 33.33%
    pub fn minimum_replacement(nums: Vec<i32>) -> i64 {
        let mut res = 0;
        let mut next = *nums.last().unwrap();
        for num in nums[..nums.len() - 1].iter().rev() {
            if num > &next {
                let splits = (num + next - 1) / next;
                res += (splits - 1) as i64;
                next = num / &splits;
            } else {
                next = *num;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![3, 9, 3], 2), (vec![1, 2, 3, 4, 5], 0)];
    for t in tests {
        assert_eq!(Solution::minimum_replacement(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
