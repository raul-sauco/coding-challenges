// 978. Longest Turbulent Subarray
// 🟠 Medium
//
// https://leetcode.com/problems/longest-turbulent-subarray/
//
// Tags: Array - Dynamic Programming - Sliding Window

struct Solution;
impl Solution {
    // Use a sliding window moving the right pointer forward while the sign
    // is the opposite sign than on the previous two elements, when the
    // condition fails, we adjust the left pointer to either, the current
    // element, if the element is equal to the previous one, or the previous
    // element if it is greater or smaller than the previous element, we
    // also keep a variable with the last sign that we have seen that we use
    // to check that the next one is the opposite sign.
    //
    // Time complexity: O(n) - We visit each element once and do O(1) work.
    // Space complexity: O(1) - Constant extra space used.
    //
    // Runtime 7 ms Beats 87.50%
    // Memory 2.4 MB Beats 100%
    pub fn max_turbulence_size(arr: Vec<i32>) -> i32 {
        if arr.len() == 1 {
            return 1;
        }
        // The pointer at which the current sequence starts.
        let mut l = 0;
        // The longest sequence found so far.
        let mut res = 1;
        // The sign that we need to maintain the sequence.
        let mut greater = arr[0] < arr[1];
        // Iterate over elements checking the sign with the previous element.
        for r in 1..arr.len() {
            // Two equal elements break any sequence and we need to start the
            // next sequence at the right element.
            if arr[r - 1] == arr[r] {
                l = r;
                if r < arr.len() - 1 {
                    greater = arr[r] < arr[r + 1];
                }
            // The wrong sign break the sequence but we can start the next one
            // using this pair of elements. Left pointer goes to left element.
            } else if greater != (arr[r - 1] < arr[r]) {
                l = r - 1;
                // The next comparison will be between the next pair, the sign
                // should be the opposite.
                greater = arr[r - 1] > arr[r];
            // The correct sign continues the sequence, check if it is the longest
            // sequence seen and update the flag for the next pair.
            } else {
                res = res.max(1 + r - l);
                greater = !greater;
            }
        }
        res as i32
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::max_turbulence_size(vec![100]), 1);
    assert_eq!(Solution::max_turbulence_size(vec![3, 3]), 1);
    assert_eq!(Solution::max_turbulence_size(vec![3, 4]), 2);
    assert_eq!(
        Solution::max_turbulence_size(vec![9, 4, 2, 10, 7, 8, 8, 1, 9]),
        5
    );
    assert_eq!(
        Solution::max_turbulence_size(vec![9, 4, 2, 1, 7, 8, 8, 1, 9, 7, 7]),
        4
    );
    println!("All tests passed!")
}
