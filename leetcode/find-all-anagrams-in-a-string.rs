// 438. Find All Anagrams in a String
// 🟠 Medium
//
// https://leetcode.com/problems/find-all-anagrams-in-a-string/
//
// Tags: Hash Table - String - Sliding Window

struct Solution;
impl Solution {
    // A very similar problem to LeetCode 567. Permutation in String, create
    // an array of character frequencies in p, then start iterating over a
    // window of s of the same length as p using the hashmap to check if the
    // sliding window contains exactly the same characters, and in the same
    // frequency as p, to slide the window, we add the character to the right
    // and remove the one to the left from the frequencies array.
    //
    // Time complexity: O(n) - Where n is the number of characters in s.
    // Space complexity: O(1) - We use an array of size 26.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.2 MB Beats 91.49%
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        if p.len() > s.len() {
            return vec![];
        }
        // Convert the input strings to vec<char>
        let s_chars: Vec<char> = s.chars().collect();
        let p_chars: Vec<char> = p.chars().collect();
        let mut freq = vec![0; 26];
        let base = 'a' as usize;
        for i in 0..p.len() {
            freq[p_chars[i] as usize - base] -= 1;
            freq[s_chars[i] as usize - base] += 1;
        }
        // A vector to store the indexes at which the anagrams start.
        let mut result: Vec<i32> = if freq.iter().all(|&b| b == 0) {
            vec![0]
        } else {
            vec![]
        };
        // Explicit left pointer, the right pointer is implicit in the for loop.
        let mut left: usize = 0;
        for right in p.len()..s.len() {
            freq[s_chars[left] as usize - base] -= 1;
            left += 1;
            freq[s_chars[right] as usize - base] += 1;
            if freq.iter().all(|&b| b == 0) {
                result.push(left as i32);
            }
        }
        result
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::find_anagrams(String::from("abacbabc"), String::from("abc")),
        vec![1, 2, 3, 5]
    );

    println!("All tests passed!")
}
