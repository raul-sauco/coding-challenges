// 344. Reverse String
// 🟢 Easy
//
// https://leetcode.com/problems/reverse-string/
//
// Tags: Two Pointers - String

struct Solution;
impl Solution {
    /// We can use slice.swap() to switch each character in the first half with its counterpart
    /// from the tail end.
    ///
    /// Time complexity: O(n) -
    /// Space complexity: O(1) -
    ///
    /// Runtime 8 ms Beats 87%
    /// Memory 5.45 MB Beats 41%
    pub fn reverse_string(s: &mut Vec<char>) {
        let j = s.len() - 1;
        for i in 0..s.len() / 2 {
            (s[i], s[j - i]) = (s[j - i], s[i]);
            // s.swap(i, j - i); // Also 8ms
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!['a', 'b', 'c', 'd'], vec!['d', 'c', 'b', 'a']),
        (vec!['h', 'e', 'l', 'l', 'o'], vec!['o', 'l', 'l', 'e', 'h']),
        (vec!['a', 'b', 'c', 'd', 'e'], vec!['e', 'd', 'c', 'b', 'a']),
        (
            vec!['H', 'a', 'n', 'n', 'a', 'h'],
            vec!['h', 'a', 'n', 'n', 'a', 'H'],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, mut t) in tests.clone().into_iter().enumerate() {
        Solution::reverse_string(&mut t.0);
        if t.0 == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.1, t.0
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
