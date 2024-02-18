// 2149. Rearrange Array Elements by Sign
// 🟠 Medium
//
// https://leetcode.com/problems/rearrange-array-elements-by-sign/
//
// Tags: Array - Two Pointers - Simulation

struct Solution;
impl Solution {
    /// Have two iterators iterate over the input generating positive and negative values, zip and
    /// collect them in a vector.
    ///
    /// Time complexity: O(n) - We use two iterators over the entire input.
    /// Space complexity: O(1) - I would say that using iterators is O(1) because the values are
    /// not stored in memory but this solution is not memory efficient.
    ///
    /// Runtime 66 ms Beats 22.11%
    /// Memory 5.67 MB Beats 21.40%
    #[allow(dead_code)]
    pub fn rearrange_array_it(nums: Vec<i32>) -> Vec<i32> {
        nums.iter()
            .filter(|&&x| x >= 0)
            .zip(nums.iter().filter(|&&x| x < 0))
            .flat_map(|(&x, &y)| [x, y])
            .collect::<Vec<_>>()
    }

    /// Create a result vector of size n, and two pointers, to the next positive and negative
    /// positions in res. Iterate over the input placing positive and negative values in their
    /// respective positions.
    ///
    /// Time complexity: O(n) - We iterate over every value in the input.
    /// Space complexity: O(n) - We create a result vector with intermediate results that we update
    /// as the algorithm runs.
    ///
    /// Runtime 56 ms Beats 85.77%
    /// Memory 5.42 MB Beats 43.78%
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        let (mut ni, mut pi) = (1, 0);
        let mut res = vec![0; nums.len()];
        for num in nums {
            if num >= 0 {
                res[pi] = num;
                pi += 2;
            } else {
                res[ni] = num;
                ni += 2;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 1, -2, -5, 2, -4], vec![3, -2, 1, -5, 2, -4]),
        (vec![-1, 1], vec![1, -1]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::rearrange_array(t.0.clone());
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
