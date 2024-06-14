// 945. Minimum Increment to Make Array Unique
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/
//
// Tags: Array - Greedy - Sorting - Counting

struct Solution;
impl Solution {
    /// Sort the input, use one variable to store the minimum value that the next element in the
    /// array can be. If the element is less than the expected minimum, add the difference to the
    /// result and +1 the minimum. Otherwise, update the minimum to the current value plus one.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the input has the highest time complexity.
    /// Space complexity: O(log(n)) - The sorting algorithm uses some extra space, otherwise O(1)
    ///
    /// Runtime 24 ms Beats 50%
    /// Memory 2.88 MB Beats 100%
    pub fn min_increment_for_unique(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut res = 0;
        let mut min = nums[0] + 1;
        for &num in nums[1..].into_iter() {
            if num < min {
                res += min - num;
                min += 1;
            } else {
                min = num + 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(vec![1, 2, 2], 1), (vec![3, 2, 1, 2, 1, 7], 6)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_increment_for_unique(t.0.clone());
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
