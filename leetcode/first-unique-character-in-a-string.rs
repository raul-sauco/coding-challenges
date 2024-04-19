// 387. First Unique Character in a String
// 🟢 Easy
//
// https://leetcode.com/problems/first-unique-character-in-a-string/
//
// Tags: Hash Table - String - Queue - Counting

struct Solution;
impl Solution {
    /// Iterate over the input characters saving the index of characters that we see only one time,
    /// use i32::MAX to indicate that we have not seen that character yet, -1 to indicate that we
    /// have seen that character more than one time, and the index if we have seen it only once.
    ///
    /// Time complexity: O(n) - We iterate over the input characters, then over the seen array.
    /// Space complexity: O(1) - We use an array of fixed size 26 of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.28 MB Beats 42.65%
    pub fn first_uniq_char(s: String) -> i32 {
        let mut seen = [i32::MAX; 26];
        let mut cp;
        for (i, ch) in (s.bytes().enumerate()).rev() {
            cp = (ch - b'a') as usize;
            seen[cp] = if seen[cp] == i32::MAX { i as i32 } else { -1 };
        }
        match seen.iter().filter(|&x| *x >= 0 && *x < i32::MAX).min() {
            Some(res) => *res,
            None => -1,
        }
    }
}

// Tests.
fn main() {
    let tests = [("leetcode", 0), ("loveleetcode", 2), ("aabb", -1)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::first_uniq_char(t.0.to_string());
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
