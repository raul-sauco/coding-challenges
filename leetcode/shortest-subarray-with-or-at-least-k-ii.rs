// 3097. Shortest Subarray With OR at Least K II
// 🟠 Medium
//
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/
//
// Tags: Array - Bit Manipulation - Sliding Window

struct Solution;
impl Solution {
    /// A nice variation of the sliding window problem where we need to figure out how to remove
    /// digits from the left when shrinking the window. To do it, we need to keep track of the
    /// number of times that we have seen a bit in values inside the window, when we pop a value,
    /// we need to remove one from that bit count, when we get to 0, that bit will not be set in
    /// the current value of the window's OR.
    ///
    /// Time complexity: O(n) - We visit each value in the input twice, for each, we iterate over
    /// the set bits in constant time because they max at 30.
    /// Space complexity: O(1) - One array of size 32 and a few integers.
    ///
    /// Runtime 23 ms Beats 100%
    /// Memory 4.06 MB Beats 66%
    pub fn minimum_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut l = 0;
        let mut res = usize::MAX;
        let mut bits = [0; 32];
        let mut mask;
        let mut int_val = 0;
        for (r, &num) in nums.iter().enumerate() {
            // Print integer as binary digits.
            // println!("num: {:#032b} - {}", num, num);
            for i in 0..32 {
                mask = 1 << i;
                // If this bit is set in the current num.
                if num & mask > 0 {
                    // Update the count of numbers with this bit set.
                    bits[i] += 1;
                    // If we go from 0 to 1, update the int value.
                    if bits[i] == 1 {
                        int_val += mask;
                    }
                }
            }
            // Now shrink the window as much as we can.
            while int_val >= k && l <= r {
                res = res.min(1 + r - l);
                for i in 0..32 {
                    mask = 1 << i;
                    if nums[l] & mask > 0 {
                        bits[i] -= 1;
                        if bits[i] == 0 {
                            int_val -= mask;
                        }
                    }
                }
                l += 1;
            }
        }
        if res == usize::MAX {
            -1
        } else {
            res as i32
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2], 0, 1),
        (vec![1, 2, 3], 2, 1),
        (vec![2, 1, 8], 10, 3),
        (vec![1, 2, 32, 21], 55, 3),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::minimum_subarray_length(t.0.clone(), t.1);
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
