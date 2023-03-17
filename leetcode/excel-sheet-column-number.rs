// 171. Excel Sheet Column Number
// 🟢 Easy
//
// https://leetcode.com/problems/excel-sheet-column-number/
//
// Tags: Math - String

struct Solution;
impl Solution {
    // Convert from base 26 to base 10, pop characters from the end of the
    // input and convert them to the equivalent base 10 value adding it to
    // the result.
    //
    // Time complexity: O(n) - Where n is the number of characters in the
    // input.
    // Space complexity: O(n) - Where n is the number of characters in the
    // input.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2 MB Beats 96.34%
    pub fn title_to_number(column_title: String) -> i32 {
        // If the exponents of 26 were bigger, we could precompute and store
        // them in an array but they are only accessed once and go to 26^7 max.
        column_title
            .chars()
            .rev()
            .enumerate()
            .fold(0, |cur, (i, c)| {
                cur + (c as usize - 64) * 26_usize.pow(i as u32)
            }) as i32
    }
}

// Tests.
fn main() {
    let tests = [("A", 1), ("AB", 28), ("ZY", 701)];
    for test in tests {
        assert_eq!(Solution::title_to_number(String::from(test.0)), test.1);
    }
    println!("All tests passed!")
}
