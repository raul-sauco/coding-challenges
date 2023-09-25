// 389. Find the Difference
// 🟢 Easy
//
// https://leetcode.com/problems/find-the-difference/
//
// Tags: Hash Table - String - Bit Manipulation - Sorting

struct Solution;
impl Solution {
    /// Iterate over s counting the frequency of each letter that we see, and
    /// storing that frequency in an auxiliary vector, then iterate over t
    /// subtracting the character frequencies that we see from the same vector
    /// when we see a letter for which the frequency is already 0, return it.
    ///
    /// Time complexity: O(n) - Where n is the size of either string, they
    /// differ only by one character, and it is limited to 1000.
    /// Space complexity: O(1) - We use a vector of size 26 of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 1.91 MB Beats 100%
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut freq = vec![0; 26];
        for c in s.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        let mut idx;
        for c in t.bytes() {
            idx = (c - b'a') as usize;
            if freq[idx] == 0 {
                return c as char;
            }
            freq[idx] -= 1;
        }
        unreachable!("The problem guarantees one result")
    }

    /// Return the sum of byte values in t minus the sum of byte values in s
    /// cast as a char.
    ///
    /// Time complexity: O(n) - Where n is the size of either string, they
    /// differ only by one character, and it is limited to 1000.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.08 MB Beats 80.92%
    pub fn find_the_difference_2(s: String, t: String) -> char {
        (t.bytes().map(|b| b as usize).sum::<usize>()
            - s.bytes().map(|b| b as usize).sum::<usize>()) as u8 as char
    }

    /// Return the sum of byte values in t minus the sum of byte values in s
    /// cast as a char.
    ///
    /// Time complexity: O(n) - Where n is the size of either string, they
    /// differ only by one character, and it is limited to 1000.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.10 MB Beats 80.92%
    pub fn find_the_difference_3(s: String, t: String) -> char {
        (s + &t).bytes().fold(0u8, |acc, b| acc ^ b) as char
    }
}

// Tests.
fn main() {
    let tests = [
        ("abcd".to_string(), "abcde".to_string(), 'e'),
        ("".to_string(), "y".to_string(), 'y'),
    ];
    for t in tests {
        assert_eq!(Solution::find_the_difference(t.0.clone(), t.1.clone()), t.2);
        assert_eq!(
            Solution::find_the_difference_2(t.0.clone(), t.1.clone()),
            t.2
        );
        assert_eq!(Solution::find_the_difference_3(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
