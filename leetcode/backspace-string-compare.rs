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

    /// Use two iterators, have a function that returns the next valid character
    /// on the iterator, skipping one character per each '#' found. Compare the
    /// characters of each of the strings, in reverse, one at a time, if any of
    /// them is different, return false, if we get to the end, return true.
    ///
    /// Time complexity: O(m+n) - We process both strings.
    /// Space complexity: O(m+n) - We use an iterator of extra memory for each string.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.11 MB Beats 24.56%
    pub fn backspace_compare_2(s: String, t: String) -> bool {
        let (mut sc, mut st);
        let (mut si, mut ti) = (s.chars().rev(), t.chars().rev());

        fn get_next_char(iter: &mut impl Iterator<Item = char>) -> char {
            let mut skip = 0;
            loop {
                if let Some(c) = iter.next() {
                    if c == '#' {
                        skip += 1;
                    } else {
                        if skip == 0 {
                            return c;
                        } else {
                            skip -= 1;
                        }
                    }
                } else {
                    return '$';
                }
            }
        }

        loop {
             sc = get_next_char(&mut si);
             st = get_next_char(&mut ti);
             if sc != st {
                 return false;
             }
             if sc == '$' {
                 return true;
             }
        }

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
        assert_eq!(Solution::backspace_compare(t.0.clone(), t.1.clone()), t.2);
        assert_eq!(Solution::backspace_compare_2(t.0.clone(), t.1.clone()), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
