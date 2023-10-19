// 844. Backspace String Compare
// 🟢 Easy
//
// https://leetcode.com/problems/backspace-string-compare/
//
// Tags: Two Pointers - String - Stack - Simulation

struct Solution;
impl Solution {
    /// Use two stacks, push characters and pop when we see the '#' character,
    /// return true if the result of processing both strings is the same.
    ///
    /// Time complexity: O(m+n) - We process both strings.
    /// Space complexity: O(m+n) - We use an extra stack of memory for each string.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.11 MB Beats 27.91%
    pub fn backspace_compare(s: String, t: String) -> bool {
        let mut stack = [vec![], vec![]];
        let mut idx = 0;
        for char_iter in [s.chars(), t.chars()] {
            for c in char_iter {
                if c == '#' {
                    stack[idx].pop();
                } else {
                    stack[idx].push(c);
                }
            }
            idx += 1;
        }
        stack[0] == stack[1]
    }
}

// Tests.
fn main() {
    let tests = [
        ("ab#c".to_string(), "ad#c".to_string(), true),
        ("ab##".to_string(), "c#d#".to_string(), true),
        ("a#c".to_string(), "b".to_string(), false),
    ];
    for t in tests {
        assert_eq!(Solution::backspace_compare(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
