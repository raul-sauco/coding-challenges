// 211. Design Add and Search Words Data Structure
// 🟠 Medium
//
// https://leetcode.com/problems/design-add-and-search-words-data-structure/
//
// Tags: String - Depth-First Search - Design - Trie

use std::collections::HashMap;

#[derive(Default)]
struct WordDictionary {
    children: HashMap<char, WordDictionary>,
    is_word_end: bool,
}

/**
 * Implement the word dictionary using plain hash maps to store the
 * children of each node. Inserting is exactly the same as with the
 * regular trie class and can be done in O(n), searching will need to
 * branch out to all the nodes' children when the current character is a
 * '.' wildcard and it could potentially take O(m*n) which is visiting
 * each node in the trie, even though usually would be faster.
 *
 * Time complexity: O(m*n) - For searching strings with wildcards, it
 * could potentially search the entire trie. O(n) for inserts, it will
 * perform one O(1) operation per character.
 * Space complexity: O(m*n) - Potentially, each character of each node
 * inserted could make its own node, in average it will be less than that
 * because words with common roots will share nodes.
 *
 * Runtime 732  ms Beats 60.71%
 * Memory 45.9 Beats 32.14%
 */
impl WordDictionary {
    /**
     *  Time complexity: O(1) - We create one empty HashMap instance.
     * Space complexity: O(1) - Constant space.
     */
    fn new() -> Self {
        Self {
            is_word_end: false,
            children: HashMap::new(),
        }
    }

    /**
     * Time complexity: O(1) - Word is limited to 25 chars, we may loop 25 times
     * and do O(1) work for each iteration.
     * Space complexity: O(1) - Constant space.
     */
    fn add_word(&mut self, word: String) {
        let mut node = self;
        for ch in word.chars() {
            node = node.children.entry(ch).or_default();
        }
        node.is_word_end = true;
    }

    /**
     * Time O(m*n) - Each wildcard will branch to all children, we may visit all
     * nodes in the word dictionary.
     * Space O(h) - The call stack can grow to the height of the tree, limited to
     * 20 so this is equivalent to O(1) in this case.
     */
    fn search(&self, word: String) -> bool {
        let chars: Vec<char> = word.chars().collect();
        self.search_from(&self, 0, &chars)
    }

    /**
     * Time O(m*n) - Each wildcard will branch to all children, we may visit all
     * nodes in the word dictionary.
     * Space O(h) - The call stack can grow to the height of the tree, limited to
     * 20 so this is equivalent to O(1) in this case.
     */
    fn search_from(&self, current: &WordDictionary, idx: usize, chars: &Vec<char>) -> bool {
        let mut node = current;
        let mut ch;
        for i in idx..chars.len() {
            ch = chars[i];
            match ch {
                // When we find a wildcard, we need to try all children.
                '.' => {
                    for (_, child) in node.children.iter() {
                        // If any children is a match return true.
                        if self.search_from(child, i + 1, chars) {
                            return true;
                        }
                    }
                    return false;
                }
                // If it is a regular character, match it.
                c => match node.children.get(&c) {
                    Some(child) => node = child,
                    None => return false,
                },
            }
        }
        // If we get to the end of the word.
        node.is_word_end
    }
}

// Tests.
fn main() {
    // Example test case.
    let mut wd = WordDictionary::new();
    wd.add_word(String::from("bad"));
    wd.add_word(String::from("dad"));
    wd.add_word(String::from("mad"));
    assert_eq!(wd.search(String::from("pad")), false);
    assert_eq!(wd.search(String::from("bad")), true);
    assert_eq!(wd.search(String::from(".ad")), true);
    assert_eq!(wd.search(String::from("b..")), true);

    wd = WordDictionary::new();
    wd.add_word(String::from("a"));
    wd.add_word(String::from("a"));
    assert_eq!(wd.search(String::from(".")), true);
    assert_eq!(wd.search(String::from("a")), true);
    assert_eq!(wd.search(String::from("aa")), false);
    assert_eq!(wd.search(String::from("a")), true);
    assert_eq!(wd.search(String::from(".a")), false);
    assert_eq!(wd.search(String::from("a.")), false);

    println!("All tests passed!")
}
