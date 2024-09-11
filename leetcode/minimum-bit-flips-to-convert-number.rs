// 2220. Minimum Bit Flips to Convert Number
// 🟢 Easy
//
// https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
//
// Tags: Bit Manipulation

struct Solution;
impl Solution {
    /// One solution is to XOR the input numbers and return the number of 1 bits in the result.
    ///
    /// Time complexity: O(log2(max(m,n))) - The built-in count_ones function's complexity.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.08 MB Beats 84%
    #[allow(dead_code)]
    pub fn min_bit_flips_built_in(start: i32, goal: i32) -> i32 {
        (start ^ goal).count_ones() as _
    }

    /// A neat method using Brian Kernighan’s Algorithm, it counts one values skipping values that
    /// we are not interested on.
    ///
    /// Time complexity: O(log2(n)) - Where n is the result.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.19 MB Beats 15%
    #[allow(dead_code)]
    pub fn min_bit_flips(start: i32, goal: i32) -> i32 {
        let mut rem = start ^ goal;
        let mut res = 0;
        while rem > 0 {
            rem &= rem - 1;
            res += 1;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(10, 7, 3), (3, 4, 3)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_bit_flips(t.0, t.1);
        if res == t.2 {
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
