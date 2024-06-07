// 648. Replace Words
// 🟠 Medium
//
// https://leetcode.com/problems/replace-words/
//
// Tags: Array - Hash Table - String - Trie

#[derive(Default)]
struct Trie {
    is_word_end: bool,
    children: [Option<Box<Trie>>; 26],
}

/**
 * A Trie implementation with an insert and a get_word_root methods.
 */
impl Trie {
    fn new() -> Self {
        Default::default()
        // Self {
        //     is_word_end: false,
        //     children: [None; 26],
        // }
    }

    fn insert(&mut self, word: String) {
        let mut node = self;
        for b in word.bytes() {
            node = node.children[(b - b'a') as usize].get_or_insert_with(|| Box::new(Trie::new()));
        }
        node.is_word_end = true;
    }

    fn get_word_root(&self, word: &str) -> Option<String> {
        let mut node = self;
        let mut path = String::new();
        for b in word.bytes() {
            match node.children[(b - b'a') as usize].as_ref() {
                Some(child) => node = child,
                None => return None,
            }
            path.push(b as char);
            if node.is_word_end {
                return Some(path);
            }
        }
        None
    }
}
struct Solution;
impl Solution {
    /// Use a Trie, insert the roots. Then iterate over the words in the sentence trying to find
    /// their root in the trie, if not found, use the word itself.
    ///
    /// Time complexity: O(m+n) - Where m is the number of characters in the dictionary and n is
    /// the number of characters in the sentence, we will visit each character and do O(1) work for
    /// each, in the worst case, for each character we may need to create a new Trie with a size 26
    /// array as their children.
    /// Space complexity: O(m) - In the worst case, each character in the dictionary results in a
    /// Trie, which would be O(26m) and can be simplified.
    ///
    /// Runtime 12 ms Beats 80%
    /// Memory 14.20 MB Beats 50%
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {
        let mut trie = Trie::new();
        for word in dictionary {
            trie.insert(word);
        }
        sentence
            .split_whitespace()
            .map(|word| trie.get_word_root(word).unwrap_or(word.to_string()))
            .collect::<Vec<String>>()
            .join(" ")
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec!["cat", "bat", "rat"],
            "the cattle was rattled by the battery",
            "the cat was rat by the bat",
        ),
        (
            vec!["a", "b", "c"],
            "aadsfasf absbs bbab cadsfafs",
            "a a b c",
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res =
            Solution::replace_words(t.0.iter().map(|s| s.to_string()).collect(), t.1.to_string());
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
