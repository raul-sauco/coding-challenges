// 974. Subarray Sums Divisible by K
// 🟠 Medium
//
// https://leetcode.com/problems/subarray-sums-divisible-by-k/
//
// Tags: Array - Hash Table - Prefix Sum

struct Solution;
impl Solution {
    // Create an array with the count of times we have obtained a certain
    // remainder in the input array up to that point when we have computed
    // prefix_sum % k, the subarray between two equal results will always be
    // divisible by k.
    //
    // Time complexity: O(n+k) - We visit each element of the input array and
    // do O(1) operations. We also iterate over k elements to create the
    // count array.
    // Space complexity: O(k) - We use an array of size k of extra memory.
    //
    // Runtime 1 ms Beats 84.8%
    // Memory 2 MB Beats 92.36%
    pub fn subarrays_div_by_k(nums: Vec<i32>, k: i32) -> i32 {
        let (mut res, mut prefix) = (0, 0);
        let mut count = vec![0; k as usize + 1];
        count[0] = 1;
        for num in nums {
            // The modulus of the prefix sum up to this index and k.
            prefix = (prefix + num) % k;
            // The remainder of the modulus operation.
            let idx = if prefix < 0 {
                (k + prefix) as usize
            } else {
                prefix as usize
            };
            // If we have seen the same modulus result before, the sum of
            // the subarray between the current index and any of these
            // indexes will be divisible by k.
            res += count[idx];
            // Record the current remainder.
            count[idx] += 1;
        }
        res
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::subarrays_div_by_k(vec![5], 9), 0);
    assert_eq!(Solution::subarrays_div_by_k(vec![4, 5, 0, -2, -3, 1], 5), 7);
    println!("All tests passed!")
}
