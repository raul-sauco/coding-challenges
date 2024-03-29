// 2962. Count Subarrays Where Max Element Appears at Least K Times
// 🟠 Medium
//
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
//
// Tags: Array - Sliding Window

struct Solution;
impl Solution {
    /// Use a sliding window, move the right pointer until the count of the maximum element is
    /// equal to k, at that point, any slice that starts at the current start and ends at any
    /// element between the current end and the end of the input will be a valid subarray, there
    /// is one of them for each possible end, add n - end to the result. Then shrink the window
    /// from the left while the count is still equal to k. For each element that we remove, there
    /// are the same number of valid subarrays starting at the new start that we can add to the
    /// result.
    ///
    /// Time complexity: O(n) - Both pointers will visit each element in the input a maximum of one
    /// time.
    /// Space complexity: O(1) - We store pointers and integers.
    ///
    /// Runtime 17 ms Beats 50%
    /// Memory 3.17 MB Beats 100%
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let mut res = 0;
        let maximum = *nums.iter().max().expect("An i32");
        let n = nums.len();
        let mut count = 0;
        let mut start = 0;
        for end in 0..n {
            if nums[end] == maximum {
                count += 1;
            }
            // Any array starting at start and ending anywhere between end and n will have at
            // least k maximum elements.
            let valid_subarray_count = (n - end) as i64;
            while count == k {
                res += valid_subarray_count;
                // Then shift the left pointer.
                if nums[start] == maximum {
                    count -= 1;
                }
                start += 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], 1, 1),
        (vec![1, 1], 1, 3),
        (vec![1, 1], 2, 1),
        (vec![1, 4, 2, 1], 3, 0),
        (vec![1, 3, 2, 3, 3], 2, 6),
        (vec![3, 3, 3, 3, 3], 1, 15),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::count_subarrays(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.2, res
            );
        }
    }
    println!();
    if success == tests.len() {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
