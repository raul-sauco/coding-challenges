// 2090. K Radius Subarray Averages
// 🟠 Medium
//
// https://leetcode.com/problems/k-radius-subarray-averages/
//
// Tags: Array - Sliding Window

struct Solution;
impl Solution {
    /// Use a sliding window of size 2k+1, for each item, add the new value
    /// under the rightmost edge of the window and remove the value that was
    /// under the leftmost edge on the previous window, then divide by the
    /// window size.
    ///
    /// Time complexity: O(n) - We iterate over n-2k values and do O(1) for
    /// each on the main loop, previously we iterate over 2k values and compute
    /// their sum.
    /// Space complexity: O(1) - Constant space if we do not take the result
    /// vector, of size n, into account.
    ///
    /// Runtime 64 ms Beats 100%
    /// Memory 3.4 MB Beats 75%
    pub fn get_averages(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let n = nums.len();
        let mut res = vec![-1; n];
        let m = k * 2 + 1;
        if n < m {
            return res;
        }
        let mut sum: i64 = nums[..m].iter().map(|x| *x as i64).sum();
        let m = m as i64;
        for i in k..n - k {
            res[i] = (sum / m) as i32;
            if i + k + 1 < n {
                sum += nums[i + k + 1] as i64;
                sum -= nums[i - k] as i64;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![8], 100000, vec![-1]),
        (vec![100000], 0, vec![100000]),
        (
            vec![7, 4, 3, 9, 1, 8, 5, 2, 6],
            3,
            vec![-1, -1, -1, 5, 4, 4, -1, -1, -1],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::get_averages(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
