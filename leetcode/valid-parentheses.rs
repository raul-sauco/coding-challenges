// 20. Valid Parentheses
// 🟢 Easy
//
// https://leetcode.com/problems/valid-parentheses/
//
// Tags: String - Stack

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Use a stack to push opening symbols that we see. Iterate over the input,
    /// if we see an opening symbol, push it into the stack, if we see a
    /// closing symbol, check that it matches the top of the stack, if it does,
    /// pop that symbol, if it doesn't return false. Once we run out of symbols,
    /// return whether the stack is empty.
    ///
    /// Time complexity: O(n) - We visit all characters in the input string and
    /// do O(1) work for each.
    /// Space complexity: O(n) - The stack grows in size linearly with the input.
    ///
    /// Runtime 1 ms Beats 75.94%
    /// Memory 2 MB Beats 99.77%
    pub fn is_valid(s: String) -> bool {
        let mut stack = vec![];
        for c in s.chars() {
            match c {
                '{' | '(' | '[' => stack.push(c),
                '}' => {
                    if stack.is_empty() || stack.pop().unwrap() != '{' {
                        return false;
                    }
                }
                ')' => {
                    if stack.is_empty() || stack.pop().unwrap() != '(' {
                        return false;
                    }
                }
                ']' => {
                    if stack.is_empty() || stack.pop().unwrap() != '[' {
                        return false;
                    }
                }
                _ => return false,
            }
        }
        stack.is_empty()
    }

    /// Similar to the previous solution but use a hashmap to make comparing
    /// symbols cleaner, it also makes the code more maintainable, if we want
    /// to match more symbols, we just need to add them to the hashmap.
    /// Use a stack to push opening symbols that we see. Iterate over the input,
    /// if we see an opening symbol, push it into the stack, if we see a
    /// closing symbol, check that it matches the top of the stack, if it does,
    /// pop that symbol, if it doesn't return false. Once we run out of symbols,
    /// return whether the stack is empty.
    ///
    /// Time complexity: O(n) - We visit all characters in the input string and
    /// do O(1) work for each.
    /// Space complexity: O(n) - The stack grows in size linearly with the input.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.1 MB Beats 81.98%
    pub fn is_valid_2(s: String) -> bool {
        let mut stack = vec![];
        let symbols = HashMap::from([(')', '('), ('}', '{'), (']', '[')]);
        for c in s.chars() {
            match c {
                '{' | '(' | '[' => stack.push(c),
                '}' | ')' | ']' => match stack.pop() {
                    Some(o) => match symbols.get(&c) {
                        Some(v) => {
                            if *v != o {
                                return false;
                            }
                        }
                        None => return false,
                    },
                    None => return false,
                },
                _ => return false,
            }
        }
        stack.is_empty()
    }
}

// Tests.
fn main() {
    let tests = [
        ("(", false),
        ("()", true),
        ("(]", false),
        ("{[]}", true),
        ("()[]{}", true),
    ];
    for t in tests {
        assert_eq!(Solution::is_valid(String::from(t.0)), t.1);
        assert_eq!(Solution::is_valid_2(String::from(t.0)), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
