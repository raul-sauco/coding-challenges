// 6. Zigzag Conversion
// 🟠 Medium
//
// https://leetcode.com/problems/zigzag-conversion/
//
// Tags: String

struct Solution;
impl Solution {
    // This solution improves on the above one realizing that we don't really
    // use the col position of the elements, we only care to know which row,
    // and after which character, they are on. Instead of using a matrix, we
    // can save time and space by using an array of strings as the matrix and
    // appending each character to the corresponding row-string.
    //
    // Time complexity: O(n) - We go over each character in the string once.
    // Space complexity: O(n) - We store all characters in the string in the
    // rows array
    //
    // Runtime 5 ms Beats 62.50%
    // Memory 2.2 MB Beats 85.12%
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 || num_rows as usize > s.len() {
            return s;
        }
        let mut rows: Vec<Vec<char>> = Vec::new();
        for _ in 0..num_rows {
            rows.push(Vec::<char>::new())
        }
        // Iterate over all the characters in s.
        let mut i: usize = 0;
        let mut down = true;
        for c in s.chars() {
            rows[i].push(c);
            if down {
                i += 1;
                if i + 1 == num_rows as usize {
                    down = false;
                }
            } else {
                i -= 1;
                if i == 0 {
                    down = true;
                }
            }
        }
        // Older versions of rustc do not have String::from_iter
        // String::from_iter(rows.into_iter().map(|v| String::from_iter(v)))
        rows.into_iter()
            .map(|v| v.into_iter().collect::<String>())
            .collect()
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::convert(String::from("AB"), 1), String::from("AB"));
    assert_eq!(
        Solution::convert(String::from("PAYPALISHIRING"), 3),
        String::from("PAHNAPLSIIGYIR")
    );
    println!("All tests passed!")
}
