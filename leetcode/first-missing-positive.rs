// 41. First Missing Positive
// 🔴 Hard
//
// https://leetcode.com/problems/first-missing-positive/
//
// Tags: Array - Hash Table

struct Solution;
impl Solution {
    /// The input constraints mean that, either the input vector contains exactly the first n
    /// integers between 1..=n or one or more of them are missing, either way, we do not care
    /// about any values except one instance each of these integers, anything else we can ignore,
    /// for example duplicates, negative numbers, zero and anything bigger than n. We iterate over
    /// the input, each time we find a value x in the range 1..=n we move it to the index x-1,
    /// unless the value there is already x, once we complete that loop, each index i will contain
    /// the integer i+1 if it was found in the original input, we iterate over the mutated input
    /// vector and return the first nums[i] where the value is not i+1, if we get to the end of the
    /// vector without having returned anything, it means that it contains exactly the values 1..=n
    /// and we know that the first missing positive is n+1, we can return that value.
    ///
    /// Time complexity: O(n) - Even though we have a nested while loop inside the for loop, all it
    /// does is move a positive integer in the valid range to its position by index, each value
    /// is moved at most once so the inner loop runs n times, it could run multiple times for one
    /// iteration of the outer for, but that would mean that it does not need to run in the same
    /// number of other iterations of the for loop.
    /// Space complexity: O(1) - We use constant extra memory by using the input vector to mark
    /// elements seen.
    ///
    /// Runtime 6 ms Beats 63%
    /// Memory 2.88 MB Beats 99%
    pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut num;
        for i in 0..n {
            num = nums[i];
            while num > 0
                && num <= n as i32
                && num as usize - 1 != i
                && nums[i] != nums[num as usize - 1]
            {
                nums.swap(i, num as usize - 1);
                num = nums[i];
            }
        }
        for i in 0..n {
            if nums[i] != i as i32 + 1 {
                return i as i32 + 1;
            }
        }
        n as i32 + 1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 1, 1], 2),
        (vec![1, 2, 0], 3),
        (vec![1, 2, 3], 4),
        (vec![3, 4, -1, 1], 2),
        (vec![-3, -4, -1, 1], 2),
        (vec![7, 8, 9, 11, 12], 1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::first_missing_positive(t.0.clone());
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
