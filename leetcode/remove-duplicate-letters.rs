// 316. Remove Duplicate Letters
// 🟠 Medium
//
// https://leetcode.com/problems/remove-duplicate-letters/
//
// Tags: String - Stack - Greedy - Monotonic Stack

struct Solution;
impl Solution {
    /// First record the last index of each unique character, then iterate over
    /// the input characters using a monotonic stack, when we visit each
    /// character, we want to push it into the stack, before, we want to pop
    /// any greater characters that we find at the top of the stack, that we
    /// can replace by using another instance of the same character to the
    /// right of the current position.
    ///
    /// Time complexity: O(n) - We iterate over the input characters and do
    /// amortized constant work for them, we may pop several characters in the
    /// inner loop, but it is limited to a total of n pops.
    /// Space complexity: O(n) - The result stack could grow to the size of the
    /// input, everything else is size 26.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.3 MB Beats 25%
    pub fn remove_duplicate_letters(s: String) -> String {
        // Convert the characters in the input string into indexes for the
        // other data structures with a => 0, b => 1 ...
        let s: Vec<usize> = s.bytes().map(|c| (c - b'a') as usize).collect();
        let mut last_idx = vec![1000; 26];
        for i in 0..s.len() {
            last_idx[s[i]] = i;
        }
        let mut seen = vec![false; 26];
        let mut stack = vec![];
        for i in 0..s.len() {
            if !seen[s[i]] {
                // If we have not decided to keep this character before, keep
                // this one, to do that, pop any greater characters from the
                // stack if we know that there is another same character to
                // the right.
                while let Some(top) = stack.last() {
                    if *top > s[i]
                        && last_idx.get(*top) != Some(&1000)
                        && last_idx.get(*top) > Some(&i)
                    {
                        seen[stack.pop().unwrap()] = false;
                    } else {
                        break;
                    }
                }
                // Push the current character into the stack, it may be popped later.
                stack.push(s[i]);
                seen[s[i]] = true;
            }
        }
        stack
            .into_iter()
            .map(|u| (u as u8 + b'a') as char)
            .collect::<String>()
    }
}

// Tests.
fn main() {
    let tests = [
        ("bcabc".to_string(), "abc".to_string()),
        ("cbacdcbc".to_string(), "acdb".to_string()),
    ];
    for t in tests {
        assert_eq!(Solution::remove_duplicate_letters(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
