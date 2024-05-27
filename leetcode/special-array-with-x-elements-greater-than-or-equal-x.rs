// 1608. Special Array With X Elements Greater Than or Equal X
// 🟢 Easy
//
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
//
// Tags: Array - Binary Search - Sorting

use std::i32;

struct Solution;
impl Solution {
    /// Sort the input, after that iterate over the values looking for a spot where the current
    /// value is the first that is bigger than the number of items to its right.
    ///
    /// Time complexity: O(n*log(n)) - We sort the input, after that o(n)
    /// Space complexity: O(n) - The local sorted copy of the input.
    ///
    /// Runtime 1 ms Beats 72%
    /// Memory 2.21 MB Beats 27%
    #[allow(dead_code)]
    pub fn special_array_linear(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        nums.sort_unstable();
        let mut target;
        for i in 0..n {
            target = (n - i) as i32;
            if nums[i] >= target && (i == 0 || nums[i - 1] < target) {
                return target;
            }
        }
        -1
    }

    /// A clever solution, use the count of numbers greater or equal to a given index.
    ///
    /// Time complexity: O(n) - We use count sorting.
    /// Space complexity: O(n) - The frequency array.
    ///
    /// Runtime 1 ms Beats 72%
    /// Memory 2.09 MB Beats 81%
    #[allow(dead_code)]
    pub fn special_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut freqs = vec![0; n + 1];
        for num in nums {
            freqs[n.min(num as usize)] += 1;
        }
        let mut total = 0;
        for i in (1..=n).rev() {
            total += freqs[i];
            if i == total as usize {
                return total;
            }
        }
        -1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 5], 2),
        (vec![0, 0], -1),
        (vec![0, 4, 3, 0, 4], 3),
        (vec![3, 6, 7, 7, 0], -1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::special_array(t.0.clone());
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
