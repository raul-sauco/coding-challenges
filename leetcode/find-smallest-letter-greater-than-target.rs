// 744. Find Smallest Letter Greater Than Target
// 🟢 Easy
//
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    /// Use binary search to find the first character bigger than the target. We
    /// can do that because the input array is guaranteed to be sorted.
    ///
    /// Time complexity: O(log(n)) - Binary search on the input array of size n.
    /// Space complexity: O(1) - We only store pointers.
    ///
    /// Runtime 3 ms Beats 77,78%
    /// Memory 2.7 MB Beats 91.67%
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        let t = target as u32;
        if (letters[0] as u32) > t || (letters[letters.len() - 1] as u32) < t {
            return letters[0];
        }
        let (mut l, mut r) = (0, letters.len() - 1);
        let mut mid: usize;
        while l <= r {
            mid = (r + l) / 2;
            if letters[mid] as u32 <= t {
                l = mid + 1;
            } else {
                // Prevent subtract overflow.
                if mid == 0 {
                    break;
                }
                r = mid - 1;
            }
        }
        if l == letters.len() {
            letters[0]
        } else {
            letters[l]
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!['c', 'f', 'j'], 'a', 'c'),
        (vec!['c', 'f', 'j'], 'c', 'f'),
        (vec!['x', 'x', 'y', 'y'], 'z', 'x'),
    ];
    for t in tests {
        assert_eq!(Solution::next_greatest_letter(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
