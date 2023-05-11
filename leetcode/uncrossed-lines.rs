// 1035. Uncrossed Lines
// 🟠 Medium
//
// https://leetcode.com/problems/uncrossed-lines/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// This problem can be solved finding the longest common subsequence
    /// between both input arrays.
    ///
    /// Time complexity: O(m*n) - Two nested loops, one runs m times, the other
    /// runs n times.
    /// Space complexity: O(min(m,n) - The size of the DP array will be the
    /// same as the smallest of the input arrays.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 100%
    pub fn max_uncrossed_lines(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        if nums1.len() > nums2.len() {
            return Self::max_uncrossed_lines(nums2, nums1);
        }
        let n = nums2.len();
        let (mut dp, mut tmp): (Vec<i32>, Vec<i32>) = (vec![0; n + 1], vec![0; n + 1]);
        for num in nums1 {
            for j in 1..=n {
                if num == nums2[j - 1] {
                    tmp[j] = dp[j - 1] + 1;
                } else {
                    tmp[j] = dp[j].max(tmp[j - 1]);
                }
            }
            dp = tmp.clone();
        }
        dp[n]
    }

    /// Similar to the previous solution but use alternate references to avoid
    /// the array copy after each iteration of the inner loop.
    ///
    /// Time complexity: O(m*n) - Two nested loops, one runs m times, the other
    /// runs n times.
    /// Space complexity: O(min(m,n) - The size of the DP array will be the
    /// same as the smallest of the input arrays.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 100%
    pub fn max_uncrossed_lines_2(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        if nums1.len() > nums2.len() {
            return Self::max_uncrossed_lines(nums2, nums1);
        }
        let n = nums2.len();
        let (mut evens, mut odds): (Vec<i32>, Vec<i32>) = (vec![0; n + 1], vec![0; n + 1]);
        let (mut src, mut dest);
        for (i, num) in nums1.iter().enumerate() {
            for j in 1..=n {
                // Alternate pointers to avoid copying.
                if i % 2 == 0 {
                    src = &mut evens;
                    dest = &mut odds;
                } else {
                    src = &mut odds;
                    dest = &mut evens;
                }
                dest[j] = if *num == nums2[j - 1] {
                    src[j - 1] + 1
                } else {
                    src[j].max(dest[j - 1])
                };
            }
            // dp = tmp.clone();
        }
        evens[n].max(odds[n])
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 4, 2], vec![1, 2, 4], 2),
        (vec![1, 3, 7, 1, 7, 5], vec![1, 9, 2, 5, 1], 2),
        (vec![2, 5, 1, 2, 5], vec![10, 5, 2, 1, 7, 2], 3),
    ];
    for t in tests {
        assert_eq!(Solution::max_uncrossed_lines(t.0.clone(), t.1.clone()), t.2);
        assert_eq!(Solution::max_uncrossed_lines_2(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
