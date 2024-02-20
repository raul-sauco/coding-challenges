// 268. Missing Number
// 🟢 Easy
//
// https://leetcode.com/problems/missing-number/
//
// Tags: Array - Hash Table - Math - Binary Search - Bit Manipulation - Sorting

struct Solution;
impl Solution {
    /// Get the sum of values in the input and compare that to what the sum of values in the
    /// inclusize range 1..=n should be, the difference is the missing number.
    ///
    /// Time complexity: O(n) - We visit every number in the input to get the sum of values.
    /// Space complexity: O(1) - Constant extra space used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.17 MB Beats 97.76%
    #[allow(dead_code)]
    pub fn missing_number_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        (n * (n + 1)) as i32 / 2 - nums.iter().sum::<i32>()
    }

    /// XOR the values that should be there with the ones actually there, the values that are
    /// present will annulate the index value that is equal, the only remaining value will be the
    /// index that we add that is not annulated by the missing value in the input.
    ///
    /// Time complexity: O(n) - We iterate all the values in the input.
    /// Space complexity: O(1) - Constant extra space used.
    ///
    /// Runtime 2 ms Beats 79.37%
    /// Memory 2.22 MB Beats 60.54%
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        nums.iter()
            .enumerate()
            .fold(0, |acc, (i, &num)| acc ^ (i as i32 + 1) ^ num)
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 0, 1], 2),
        (vec![0, 1], 2),
        (vec![9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::missing_number(t.0.clone());
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
