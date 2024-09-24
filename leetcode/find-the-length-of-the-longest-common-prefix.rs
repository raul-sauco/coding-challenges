// 3043. Find the Length of the Longest Common Prefix
// 🟠 Medium
//
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
//
// Tags: Array - Hash Table - String - Trie

#[derive(Default)]
struct Trie {
    is_word_end: bool,
    // The children can only be digits 0..9
    children: [Option<Box<Trie>>; 10],
}

/**
 * A Trie implementation with an insert and a get_longest_prefix_match methods.
 */
impl Trie {
    fn new() -> Self {
        Default::default()
    }

    fn insert(&mut self, word: String) {
        let mut node = self;
        for b in word.bytes() {
            node = node.children[(b - b'0') as usize].get_or_insert_with(|| Box::new(Trie::new()));
        }
        node.is_word_end = true;
    }

    fn get_prefix_match_size(&self, word: &str) -> i32 {
        let mut node = self;
        let mut count = 0;
        for b in word.bytes() {
            match node.children[(b - b'0') as usize].as_ref() {
                Some(child) => node = child,
                None => break,
            }
            count += 1;
        }
        count
    }
}

struct Solution;
impl Solution {
    /// Use a Trie, insert all the values in one of the input vectors, then iterate over the values
    /// in the other keeping the length of the longest prefix match.
    ///
    /// Time complexity: O(m+n) - We iterate over all the digits in both input vectors.
    /// Space complexity: O(min(m, n)) - We store all the digits in the shortest input vector into
    /// the Trie.
    ///
    /// Runtime 57 ms Beats 100%
    /// Memory 7.61 MB Beats 25%
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        // This didn't improve either runtime nor memory use.
        // if arr1.len() > arr2.len() {
        //     return Self::longest_common_prefix(arr2, arr1);
        // }
        let mut trie = Trie::new();
        for word in arr1.iter().map(|num| num.to_string()) {
            trie.insert(word);
        }
        arr2.iter()
            .map(|num| num.to_string())
            .fold(0, |acc, word| acc.max(trie.get_prefix_match_size(&word)))
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 10, 100], vec![1000], 3),
        (vec![1, 2, 3], vec![4, 4, 4], 0),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::longest_common_prefix(t.0.clone(), t.1.clone());
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
