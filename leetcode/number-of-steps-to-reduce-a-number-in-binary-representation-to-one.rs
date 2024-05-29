// 1404. Number of Steps to Reduce a Number in Binary Representation to One
// 🟠 Medium
//
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
//
// Tags: String - Bit Manipulation

struct Solution;
impl Solution {
    /// Iterate from the back simulating the addition operation, when we find the first one, the
    /// carry will become 1. When carry + the current digit result in an odd value, we need to do 2
    /// operations, otherwise we can just shift right, one operation.
    ///
    /// Time complexity: O(n) - Where n is the number of characters in the input.
    /// Space complexity: O(1) - Constant extra memory used, an array with 2 i32 values.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.13 MB Beats 100%
    pub fn num_steps(s: String) -> i32 {
        s[1..]
            .chars()
            .map(|c| if c == '1' { 1 } else { 0 })
            .rev()
            .fold([0, 0], |[res, carry], d| {
                // if (d ^ carry) & 1 == 1 {
                if (d + carry) % 2 == 1 {
                    [res + 2, 1]
                } else {
                    [res + 1, carry]
                }
            })
            .into_iter()
            .sum::<i32>()
    }
}

// Tests.
fn main() {
    let tests = [
        ("1", 0),
        ("10", 1),
        ("1101", 6),
        ("11111111111111111111111111", 27),
        ("111111111000001111111111110000011111", 47),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::num_steps(t.0.to_string());
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
