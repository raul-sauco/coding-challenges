// 2416. Sum of Prefix Scores of Strings
// 🔴 Hard
//
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
//
// Tags: Array - String - Trie - Counting

#[derive(Default)]
struct Trie {
    is_word_end: bool,
    // The children can only lowercase English letters.
    children: [Option<Box<Trie>>; 26],
    value: i32,
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
            node = node.children[(b - b'a') as usize].get_or_insert_with(|| Box::new(Trie::new()));
            node.value += 1;
        }
        node.is_word_end = true;
    }

    fn score(&self, word: &str) -> i32 {
        let mut node = self;
        let mut points = 0;
        for b in word.bytes() {
            match node.children[(b - b'a') as usize].as_ref() {
                Some(child) => {
                    node = child;
                    points += node.value
                }
                None => break,
            }
        }
        points
    }
}

struct Solution;
impl Solution {
    /// Use a trie, insert the words, adding 1 to the "value" of each node as we visit it for each
    /// character in each word in the input. Then iterate over all characters in the input again
    /// computing the total points we get from them.
    ///
    /// Time complexity: O(c) - Where c is the total count of characters in the input, we iterate
    /// over all characters twice, once to insert and once to compute points.
    /// Space complexity: O(c) - We store all input word characters in the trie.
    ///
    /// Runtime 197 ms Beats 38%
    /// Memory 221.51 MB Beats 53%
    pub fn sum_prefix_scores(words: Vec<String>) -> Vec<i32> {
        let mut trie = Trie::new();
        for word in words.iter() {
            trie.insert(word.to_owned());
        }
        words.iter().map(|word| trie.score(word)).collect()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec!["abc", "ab", "bc", "b"], vec![5, 4, 3, 2]),
        (vec!["abcd"], vec![4]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res =
            Solution::sum_prefix_scores(t.0.iter().map(|s| s.to_string()).collect::<Vec<_>>());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
