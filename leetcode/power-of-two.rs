// 231. Power of Two
// 🟢 Easy
//
// https://leetcode.com/problems/power-of-two/
//
// Tags: Math - Bit Manipulation - Recursion

struct Solution;
impl Solution {
    /// We can use a built-in method to count the set bits in the binary representation of n,
    /// powers of 2 will be one 1 followed by all 0s.
    ///
    /// Time complexity: O(log(n)) - The count ones method will look at each bit of n.
    /// Space complexity: O(1) - No extra space used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.10 MB Beats 90.29%
    #[allow(dead_code)]
    pub fn is_power_of_two_co(n: i32) -> bool {
        n >= 0 && n.count_ones() == 1
    }

    /// The binary representation of a power of two is one 1 followed by all 0s. If we subtract 1,
    /// the binary representation of that number will be all 1s and one bit shorter that n, we can
    /// use that fact to binary AND these two values, if the result is 0, n is a power of 2.
    ///
    /// Time complexity: O(log(n)) - The binary AND will compare each bit.
    /// Space complexity: O(1) - No extra space used.
    ///
    /// Runtime 3 ms Beats 25.24%
    /// Memory 2.18 MB Beats 25.24%
    pub fn is_power_of_two(n: i32) -> bool {
        n > 0 && (n & n - 1) == 0
    }
}

// Tests.
fn main() {
    let tests = [(0, false), (1, true), (16, true), (3, false)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::is_power_of_two(t.0.clone());
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
