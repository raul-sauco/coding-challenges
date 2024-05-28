// 1208. Get Equal Substrings Within Budget
// 🟠 Medium
//
// https://leetcode.com/problems/get-equal-substrings-within-budget/
//
// Tags: String - Binary Search - Sliding Window - Prefix Sum

struct Solution;
impl Solution {
    /// Get a vector of the cost of converting each character, after that use a sliding window,
    /// since we are looking for the largest window, we can only allow the window to grow, not
    /// shrink, and only update the max length when the window does grow.
    ///
    /// Time complexity: O(n) - We visit each element and do constant time work, both constructing
    /// the vector of sums and during the sliding window.
    /// Space complexity: O(n) - The sums vector. Since in Rust we cannot access string characters
    /// by index, I am not too sure how we could do it in O(1)
    ///
    /// Runtime 1 ms Beats 100%
    /// Memory 2.64 MB Beats 44%
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        let mut l = 0;
        let sums = s
            .bytes()
            .zip(t.bytes())
            .map(|(x, y)| (x as i32 - y as i32).abs())
            .collect::<Vec<_>>();
        let mut cost = 0;
        let mut max_length = 0;
        for r in 0..sums.len() {
            cost += sums[r];
            if cost > max_cost {
                cost -= sums[l];
                l += 1;
            } else {
                max_length = r - l + 1;
            }
        }
        max_length as i32
    }
}

// Tests.
fn main() {
    let tests = [
        ("abcd", "bcdf", 3, 3),
        ("abcd", "cdef", 3, 1),
        ("abcd", "acde", 0, 1),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::equal_substring(t.0.to_string(), t.1.to_string(), t.2);
        if res == t.3 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.3, res
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
