// 168. Excel Sheet Column Title
// 🟢 Easy
//
// https://leetcode.com/problems/excel-sheet-column-title/
//
// Tags: Math - String

struct Solution;
impl Solution {
    // What the problem is asking is to convert from base 10 to base 26.
    //
    // Time complexity: O(log26(n)) - The loop will run until the value is 0
    // and on each iteration we divide by 26.
    // Space complexity: O(log26(n)) - We will have one character in the
    // result string for each iteration of the loop.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2 MB Beats 92.86%
    pub fn convert_to_title(column_number: i32) -> String {
        let mut res: Vec<char> = vec![];
        let mut val = column_number;
        const OFFSET: u8 = 'A' as u8;
        while val > 0 {
            val -= 1;
            res.push(((val % 26) as u8 + OFFSET) as char);
            val /= 26;
        }
        res.iter().rev().collect()
    }
}

// Tests.
fn main() {
    let tests = [("A", 1), ("AB", 28), ("ZY", 701)];
    for test in tests {
        assert_eq!(Solution::convert_to_title(test.1), String::from(test.0));
    }
    println!("All tests passed!")
}
