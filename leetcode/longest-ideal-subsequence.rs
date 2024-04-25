// 2370. Longest Ideal Subsequence
// 🟠 Medium
//
// https://leetcode.com/problems/longest-ideal-subsequence/
//
// Tags: Hash Table - String - Dynamic Programming

struct Solution;
impl Solution {
    /// Iterate over the characters in the input. For each character, we will be able to append it
    /// to any previously existing sequence that ends in any character to which we can append the
    /// current character while keeping the sequence "ideal". We can keep a DP array of 26
    /// positions where the index is the character at the end of a sequence and the value is the
    /// length of the longest sequence that we have built so far that ends in that character. We
    /// check what is the longest sequence that we can obtain that ends in the current character,
    /// add one and store that in dp[i].
    ///
    /// Time complexity: O(n) - For each character in the input, we iterate over 2*k positions of
    /// DP, where k < 26.
    /// Space complexity: O(1) - We store an array of 26 i32 values.
    ///
    /// Runtime 10 ms Beats 100%
    /// Memory 2.26 MB Beats 90%
    #[allow(dead_code)]
    pub fn longest_ideal_string_easy_read(s: String, k: i32) -> i32 {
        let mut dp = [0; 26];
        for i in s.bytes().map(|b| b as usize - 97) {
            dp[i] = (0.max(i as i32 - k) as usize..=25.min(i + k as usize))
                .map(|idx| dp[idx])
                .max()
                .unwrap()
                + 1;
        }
        dp.into_iter().max().unwrap()
    }

    /// Same as the previous solution but compressed into one iterator.
    ///
    /// Time complexity: O(n) - For each character in the input, we iterate over 2*k positions of
    /// DP, where k < 26.
    /// Space complexity: O(1) - We store an array of 26 i32 values.
    ///
    /// Runtime 13 ms Beats 90%
    /// Memory 2.31 MB Beats 60%
    #[allow(dead_code)]
    pub fn longest_ideal_string_it(s: String, k: i32) -> i32 {
        s.bytes()
            .map(|b| b as usize - 97)
            .fold([0; 26], |mut dp, i| {
                dp[i] = (0.max(i as i32 - k) as usize..=25.min(i + k as usize))
                    .map(|idx| dp[idx])
                    .max()
                    .unwrap()
                    + 1;
                dp
            })
            .into_iter()
            .max()
            .unwrap()
    }

    /// Same as the previous solution but use a mutable reference to an array in the fold function.
    ///
    /// Time complexity: O(n) - For each character in the input, we iterate over 2*k positions of
    /// DP, where k < 26.
    /// Space complexity: O(1) - We store an array of 26 i32 values.
    ///
    /// Runtime 9 ms Beats 100%
    /// Memory 2.30 MB Beats 90%
    pub fn longest_ideal_string(s: String, k: i32) -> i32 {
        let mut dp = [0; 26];
        *s.bytes()
            .map(|b| b as usize - 97)
            .fold(&mut dp, |dp, i| {
                dp[i] = (0.max(i as i32 - k) as usize..=25.min(i + k as usize))
                    .map(|idx| dp[idx])
                    .max()
                    .unwrap()
                    + 1;
                dp
            })
            .iter()
            .max()
            .unwrap()
    }
}

// Tests.
fn main() {
    let tests = [("acfgbd", 2, 4), ("abcd", 3, 4), ("azaza", 25, 5)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::longest_ideal_string(t.0.to_string(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.2, res
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
