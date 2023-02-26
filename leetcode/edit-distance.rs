// 72. Edit Distance
// 🔴 Hard
//
// https://leetcode.com/problems/edit-distance/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    // We can compute the edit distance of each substring of w1 from 0 to j
    // and each substring of w2 from 0 to i based on whether the characters
    // at w1[j] and w2[i] match. If they match, the edit distance will be the
    // same as for the substrings w1[j-1], w2[i-1] because we won't need to
    // edit the new character, if they don't match, the edit distance will be
    // the best between [w1[j-1], w2[i-1]], [w1[j], w2[i-1]] and [w1[j-1],
    // w2[i]] because we know that we can edit any of them to become w1[0..j],
    // w2[0..i] with one edit, either remove, add or replace.
    //
    // Time complexity: O(m*n) - We compute dp for each combination of
    // possible prefixes of the two input strings.
    // Space complexity: O(m) - The dp array has the length of word1 + 1.
    //
    // Runtime 3 ms Beats 77.27%
    // Memory 2 MB Beats 88.64%
    pub fn min_distance(word1: String, word2: String) -> i32 {
        use std::cmp::min;
        let (m, n) = (word1.len(), word2.len());
        let w1: Vec<char> = word1.chars().collect();
        let w2: Vec<char> = word2.chars().collect();
        let mut dp: Vec<usize> = (0..m + 1).collect();
        for i in 0..n {
            let mut temp = vec![0; m + 1];
            temp[0] = i + 1;
            for j in 0..m {
                temp[j + 1] = if w1[j] == w2[i] {
                    dp[j]
                } else {
                    min(temp[j], min(dp[j + 1], dp[j])) + 1
                };
            }
            dp = temp;
        }
        dp[dp.len() - 1] as i32
    }
}

// Tests.
fn main() {
    let tests = [
        ("", "", 0),
        ("a", "a", 0),
        ("horse", "ros", 3),
        ("aaaaa", "abaa", 2),
        ("intention", "execution", 5),
    ];
    for test in tests {
        assert_eq!(
            Solution::min_distance(String::from(test.0), String::from(test.1)),
            test.2
        );
    }
    println!("All tests passed!")
}
