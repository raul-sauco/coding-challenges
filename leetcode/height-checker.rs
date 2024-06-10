// 1051. Height Checker
// 🟢 Easy
//
// https://leetcode.com/problems/height-checker/
//
// Tags: Array - Sorting - Counting Sort

struct Solution;
impl Solution {
    /// Solution overview
    ///
    /// Time complexity: O(n*log(n)) - Sorting the n elements in the input array, after that,
    /// comparing the original copy with the sorted copy is O(n)
    /// Space complexity: O(n) - The sorted copy of the input array.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.14 MB Beats 18%
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut sorted_heights = heights.clone();
        sorted_heights.sort_unstable();
        heights
            .iter()
            .zip(sorted_heights.iter())
            .map(|(x, y)| if x == y { 0 } else { 1 })
            .sum::<i32>()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 1, 4, 2, 1, 3], 3),
        (vec![5, 1, 2, 3, 4], 5),
        (vec![1, 2, 3, 4, 5], 0),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::height_checker(t.0.clone());
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
