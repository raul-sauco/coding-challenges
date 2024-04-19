// 442. Find All Duplicates in an Array
// 🟠 Medium
//
// https://leetcode.com/problems/find-all-duplicates-in-an-array/
//
// Tags: Array - Hash Table

struct Solution;
impl Solution {
    /// Because each element appears once or twice, and the values are in the range 1..=n, we can
    /// use the values as indexes. Iterate over the input array, for each value, use it as an index
    /// to mark the position at the given index by updating the value to be negative, if we find an
    /// index that contains a negative value, we have seen it already and can add it to the result.
    ///
    /// Time complexity: O(n) - We iterate over the input and do constant time work for each item.
    /// Space complexity: O(1) - Constant space but we mutate the input.
    ///
    /// Runtime 6 ms Beats 91%
    /// Memory 2.65 MB Beats 83%
    pub fn find_duplicates(mut nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![];
        let mut idx;
        for i in 0..nums.len() {
            idx = nums[i].abs() as usize - 1;
            if nums[idx] < 0 {
                res.push(nums[i].abs());
            } else {
                nums[idx] *= -1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![4, 3, 2, 7, 8, 2, 3, 1], vec![2, 3]),
        (vec![1, 1, 2], vec![1]),
        (vec![1], vec![]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_duplicates(t.0.clone());
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
