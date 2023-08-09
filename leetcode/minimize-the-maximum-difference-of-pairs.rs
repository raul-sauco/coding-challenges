// 2616. Minimize the Maximum Difference of Pairs
// 🟠 Medium
//
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
//
// Tags: Array - Binary Search - Greedy

struct Solution;
impl Solution {
    /// Sort the input array to have the pairs with the minimum difference next
    /// to each other, we can then try to pick x pairs and determine if it is
    /// possible. To maximize the value of x, we can use binary search.
    ///
    /// Time complexity: O(n*log(n) + n*log(max(nums))) - Sorting the input
    /// array then doing binary search on the maximum number of pairs that we
    /// can obtain.
    /// Space complexity: O(n) - We need a local copy of the input array to be
    /// able to sort it. If the input nums was mutable, we could do it using
    /// O(log(n)) extra space, which would be required for the sorting. We
    /// could also try to use some in-place sorting and then use O(1)
    ///
    /// Runtime 16 ms Beats 100%
    /// Memory 3.74 MB Beats 100%
    pub fn minimize_max(nums: Vec<i32>, p: i32) -> i32 {
        let mut nums = nums.clone();
        nums.sort_unstable();
        let n = nums.len();
        fn count_valid_pairs(threshold: i32, n: &usize, nums: &Vec<i32>) -> i32 {
            let (mut index, mut count) = (0, 0);
            while index < n - 1 {
                if nums[index + 1] - nums[index] <= threshold {
                    count += 1;
                    index += 1;
                }
                index += 1;
            }
            count
        }
        let (mut l, mut r) = (0, (nums[n - 1] - nums[0]) as usize);
        while l < r {
            let mid = (l + r) / 2;
            if count_valid_pairs(mid as i32, &n, &nums) >= p {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        l as i32
    }
}

// Tests.
fn main() {
    let tests = [(vec![10, 1, 2, 7, 1, 3], 2, 1), (vec![4, 2, 1, 2], 1, 0)];
    for t in tests {
        assert_eq!(Solution::minimize_max(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
