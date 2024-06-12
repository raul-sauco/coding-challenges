// 75. Sort Colors
// 🟠 Medium
//
// https://leetcode.com/problems/sort-colors/
//
// Tags: Array - Two Pointers - Sorting

struct Solution;
impl Solution {
    /// Use three pointers, two write pointers on the extremes for 0 and 2 elements, and one read
    /// pointer. Read elements and swap them to their position.
    ///
    /// Time complexity: O(n) - We iterate over the elements visiting each element once and pushing
    /// them left or right depending on their value.
    /// Space complexity: O(1) - Three pointers of extra memory.
    ///
    /// Runtime 1 ms Beats 56%
    /// Memory 2.16 MB Beats 13%
    pub fn sort_colors(nums: &mut Vec<i32>) {
        // Three pointers, push 0s and 2s to the side while iterating over the vector.
        let (mut left, mut i, mut right) = (0, 0, nums.len());
        while i < right {
            match nums[i] {
                0 => {
                    nums.swap(i, left);
                    left += 1;
                    i += 1;
                }
                1 => {
                    i += 1;
                }
                2 => {
                    right -= 1;
                    nums.swap(i, right);
                }
                _ => panic!("Unexpected element {}", nums[i]),
            }
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2], vec![2]),
        (vec![2, 0, 1], vec![0, 1, 2]),
        (vec![2, 0, 2, 1, 1, 0], vec![0, 0, 1, 1, 2, 2]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, mut t) in tests.clone().into_iter().enumerate() {
        Solution::sort_colors(&mut t.0);
        if t.0 == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.1, t.0
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
