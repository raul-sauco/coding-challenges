// 1759. Count Number of Homogeneous Substrings
// 🟠 Medium
//
// https://leetcode.com/problems/count-number-of-homogenous-substrings/
//
// Tags: Math - String

struct Solution;
impl Solution {
    /// Iterate over the characters in the input string keeping track of the last
    /// character seen and the length of the current sequence. For each sequence,
    /// add the current length to the number of substrings that we can build.
    ///
    /// Time complexity: O(n) - We visit each character in the input and do constant
    /// time work for each.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 5 ms Beats 100%
    /// Memory 2.22 MB Beats 100%
    pub fn count_homogeneous(s: String) -> i32 {
        let m = 1_000_000_007;
        let mut total = 0;
        // let s = s.chars().collect::<Vec<char>>();
        let (mut current_combinations, mut current_length) = (0, 0);
        let mut last_char = '^';
        for c in s.chars() {
            if c == last_char {
                current_length += 1;
                current_combinations = (current_length + current_combinations) % m;
            } else {
                total = (total + current_combinations) % m;
                current_combinations = 1;
                current_length = 1;
                last_char = c;
            }
        }
        (total + current_combinations) % m
    }
}

// Tests.
fn main() {
    let tests = [
        ("abbcccaa".to_string(), 13),
        ("xy".to_string(), 2),
        ("zzzzz".to_string(), 15),
    ];
    let n = tests.len();
    let mut failed = 0;
    for t in tests {
        let res = Solution::count_homogeneous(t.0);
        let expected = t.1;
        if res != expected {
            failed += 1;
            println!("\x1b[91m  » {:?} not {:?}\x1b[0m", res, expected);
        }
    }
    if failed == 0 {
        println!("\x1b[92m» All tests passed!\x1b[0m");
    } else if failed == n {
        println!("\x1b[91m» All tests failed!\x1b[0m");
    } else {
        println!("\x1b[93m» {} tests failed!\x1b[0m", failed);
    }
}
