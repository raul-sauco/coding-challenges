// 2971. Find Polygon With the Largest Perimeter
// 🟠 Medium
//
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
//
// Tags: Array - Greedy - Sorting - Prefix Sum

struct Solution;
impl Solution {
    /// Sort the input and get the total sum, compare the last value with the half of the total, if
    /// it is greater or equal, we won't be able to use it to form a polygon, pop it from the
    /// vector and subtract its value from the total sum. If after that we have more than 2 values,
    /// return the current sum, otherwise return -1.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the highest time complexity, after that
    /// comparing the last number with the sum of the previous ones is O(n) overall.
    /// Space complexity: O(n) - The sorted mutable copy of the input vector, if we are allowed to
    /// mutate the input, we can do it in O(1)
    ///
    /// Runtime 20 ms Beats 82.05%
    /// Memory 4.07 MB Beats 94.87%
    pub fn largest_perimeter(nums: Vec<i32>) -> i64 {
        let mut nums = nums;
        nums.sort_unstable();
        let mut total_sum: i64 = nums.iter().map(|x| *x as i64).sum();
        for x in nums.into_iter().skip(2).map(|x| x as i64).rev() {
            total_sum -= x;
            if total_sum > x {
                return total_sum + x;
            }
        }
        -1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 1, 1], 3),
        (vec![5, 5, 5], 15),
        (vec![5, 5, 50], -1),
        (vec![1, 12, 1, 2, 5, 50, 3], 12),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::largest_perimeter(t.0.clone());
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
