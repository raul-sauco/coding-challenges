// 260. Single Number III
// 🟠 Medium
//
// https://leetcode.com/problems/single-number-iii/
//
// Tags: Array - Bit Manipulation

struct Solution;
impl Solution {
    /// Xor all values in the input to find the xor of the two unique values, any of the set bits
    /// means a position where the bits in these two values are different. Use that differentiating
    /// bit to xor all values in two groups, the ones where the bit is set and the ones where it is
    /// not, each unique number is guaranteed to end up in one of the groups with all the other
    /// values being present twice, that means that once we run through all the values, the value
    /// of each group will be one of the unique values that we are looking for.
    ///
    /// Time complexity: O() - We iterate twice over the input nums and do constant time work for
    /// each value.
    /// Space complexity: O(1) - Constant extra memory.
    ///
    /// Runtime 1 ms Beats 77%
    /// Memory 2.26 MB Beats 77%
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let xor = nums.iter().fold(0, |acc, &num| acc ^ num);
        let bit = xor & (-xor);
        nums.iter().fold(vec![0, 0], |mut acc, &num| {
            if bit & num == 0 {
                acc[0] ^= num;
            } else {
                acc[1] ^= num;
            }
            acc
        })
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 1, 3, 2, 5], vec![5, 3]),
        (vec![-1, 0], vec![0, -1]),
        (vec![0, 1], vec![0, 1]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::single_number(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
