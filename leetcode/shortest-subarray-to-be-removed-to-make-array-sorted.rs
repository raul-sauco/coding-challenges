// 1574. Shortest Subarray to be Removed to Make Array Sorted
// 🟠 Medium
//
// https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
//
// Tags: Array - Two Pointers - Binary Search - Stack - Monotonic Stack

struct Solution;
impl Solution {
    /// Find the longest increasing subarrays from left and right and use a two pointer
    /// approach to grow the subarray on the left and shrink the one on the left to make sure
    /// we can concatenate them.
    ///
    /// Time complexity: O(n) - Two pointer approach.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 3.79 MB Beats 100%
    pub fn find_length_of_shortest_subarray(arr: Vec<i32>) -> i32 {
        let mut right = arr.len() - 1;
        while right > 0 && arr[right] >= arr[right - 1] {
            right -= 1;
        }
        let mut res = right;
        let mut left = 0;
        while left < right && (left == 0 || arr[left - 1] <= arr[left]) {
            while right < arr.len() && arr[left] > arr[right] {
                right += 1;
            }
            left += 1;
            res = res.min(right - left);
        }
        res as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 10, 4, 2, 3, 5], 3),
        (vec![5, 4, 3, 2, 1], 4),
        (vec![1, 2, 3], 0),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_length_of_shortest_subarray(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.1, res
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
