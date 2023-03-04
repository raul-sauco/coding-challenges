// 2444. Count Subarrays With Fixed Bounds
// 🔴 Hard
//
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
//
// Tags: Array - Queue - Sliding Window - Monotonic Queue

struct Solution;
impl Solution {
    // The key observation to make is that out of bounds elements cannot
    // belong to any subarray, we can split the input into subarrays that
    // could be subarrays with fixed bounds. If we keep track of the indexes
    // of the last time that we saw an out of bounds value, a max and a min
    // values, we can compute the number of subarrays in O(1) from any index.
    //
    // Time complexity: O(n) - We iterate over the elements one time and do
    // constant time work for each.
    // Space complexity: O(1) - The algorithm uses constant extra memory.
    //
    // Runtime 16 ms Beats 50%
    // Memory 3.2 MB Beats 50%
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        // Initialize the last max, min and out of bounds values seen.
        let (mut last_max, mut last_min, mut last_oob) = (-1, -1, -1);
        // Initialize the result.
        let mut res = 0;
        // An auxiliary variable used to cast the index once.
        let mut i;
        for (idx, num) in nums.iter().enumerate() {
            i = idx as i64;
            // Update the last seen values with the current value.
            if num < &min_k || num > &max_k {
                last_oob = i;
            }
            if num == &min_k {
                last_min = i;
            }
            if num == &max_k {
                last_max = i;
            }
            // How many valid arrays can we build that end at index i?
            // - We need to include one max and one min, the furthest
            //   right we can go is the furthest left between the last
            //   max and min: min(last_min, last_max)
            // - We cannot include any out of bounds values, the furthest
            //   left we can go in last_oob + 1
            // - We can pick any index between these values, that is
            //   min(last_min, last_max) - last_oob if that is a positive
            //   value, or 0 if the last out bounds is further left than
            //   one or both of last_max or last_min.
            res += 0.max(last_max.min(last_min) - last_oob);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 1, 1, 1], 1, 1, 10),
        (vec![1, 3, 5, 2, 7, 5], 1, 5, 2),
    ];
    for test in tests {
        assert_eq!(Solution::count_subarrays(test.0, test.1, test.2), test.3);
    }
    println!("All tests passed!")
}
