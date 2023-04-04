// 2405. Optimal Partition of String
// 🟠 Medium
//
// https://leetcode.com/problems/optimal-partition-of-string/
//
// Tags: Hash Table - String - Greedy

struct Solution;
impl Solution {
    /// Keep a hashmap, or a vector of indexes indexed by character, of the
    /// last position at which we have seen a given character, also
    /// save the start index of the current partition that we are building,
    /// then iterate over the characters in the input, if we see a character
    /// that is contained in the current partition, we need to start a new
    /// one.
    ///
    /// Time complexity: O(n) - We iterate over the characters in the input
    /// string and do constant time work for each.
    /// Space complexity: O(1) - We use constant extra space, pointers and a
    /// vector of size 26.
    ///
    /// Runtime 3 ms Beats 63.64%
    /// Memory 2.2 MB Beats 81.82%
    pub fn partition_string(s: String) -> i32 {
        let mut res = 1;
        // Use the start index of the partition that we are building and the
        // last indexes at which we saw a certain character to determine where
        // to split the input string, this is more efficient than keeping a
        // hash set and having to empty it to start a new partition.
        let mut start = 1;
        let mut last_seen = vec![0; 26];
        for (i, c) in s.bytes().enumerate() {
            let chr_idx = (c - b'a') as usize;
            // If the last time we saw this character is inside the substring
            // that we are considering, start a new one.
            if last_seen[chr_idx] >= start {
                res += 1;
                start = i + 1;
            }
            // Use one-indexed positions to be able to use a Vec<usize>
            // initialized at 0 for elements we have not seen yet.
            last_seen[chr_idx] = i + 1;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        ("abccba", 2),
        ("ssssss", 6),
        ("abacaba", 4),
        ("oygwwncfgewspmqvbez", 3),
    ];
    for t in tests {
        assert_eq!(Solution::partition_string(String::from(t.0)), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
