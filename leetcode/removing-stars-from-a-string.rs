// 2390. Removing Stars From a String
// 🟠 Medium
//
// https://leetcode.com/problems/removing-stars-from-a-string/
//
// Tags: String - Stack - Simulation

struct Solution;
impl Solution {
    /// Use a stack to build the result, iterate over the characters in the
    /// input, when we see a '*', pop the last character from the stack, any
    /// other character, we push into the stack. Since Strings in Rust are
    /// mutable, we can use a String as our stack and return that directly.
    ///
    /// Time complexity: O(n) - We visit all characters in the input string and
    /// do O(1) work for each.
    /// Space complexity: O(n) - The stack grows in size linearly with the input.
    ///
    /// Runtime 3 ms Beats 100%
    /// Memory 2.3 MB Beats 100%
    pub fn remove_stars(s: String) -> String {
        let mut res = String::with_capacity(s.len());
        for c in s.chars() {
            if c == '*' {
                res.pop();
            } else {
                res.push(c);
            }
        }
        res
    }

    /// Use an iterator and the fold operator to pop characters from the result
    /// that we are building.
    ///
    /// Time complexity: O(n) - We visit all characters in the input string and
    /// do O(1) work for each.
    /// Space complexity: O(n) - The stack grows in size linearly with the input.
    ///
    /// Runtime 7 ms Beats 100%
    /// Memory 2.3 MB Beats 100%
    pub fn remove_stars_2(s: String) -> String {
        s.chars().fold(String::new(), |mut res, c| {
            match c {
                '*' => {
                    res.pop();
                }
                _ => res.push(c),
            };
            res
        })
    }

    /// Iterate in reverse over the characters in the input keeping count of how
    /// many skips we are due, when we see a '*' we increase the count of skips,
    /// when we see a character, if the count of skips is greater than 0, we
    /// decrease, if it is 0, we push the character to the result
    ///
    /// Time complexity: O(n) - We visit all characters in the input string and
    /// do O(1) work for each.
    /// Space complexity: O(n) - The stack grows in size linearly with the input.
    ///
    /// Runtime 6 ms Beats 100%
    /// Memory 2.4 MB Beats 100%
    pub fn remove_stars_3(s: String) -> String {
        let mut res = String::with_capacity(s.len());
        // Needs to be at least 32 bit for the 10^5 max value.
        let mut skip = 0;
        for c in s.chars().rev() {
            if c == '*' {
                skip += 1;
            } else {
                if skip > 0 {
                    skip -= 1;
                } else {
                    res.push(c);
                }
            }
        }
        res.chars().rev().collect()
    }
}

// Tests.
fn main() {
    let tests = [("leet**cod*e", "lecoe"), ("erase*****", "")];
    for t in tests {
        assert_eq!(Solution::remove_stars(String::from(t.0)), String::from(t.1));
        assert_eq!(
            Solution::remove_stars_2(String::from(t.0)),
            String::from(t.1)
        );
        assert_eq!(
            Solution::remove_stars_3(String::from(t.0)),
            String::from(t.1)
        );
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
