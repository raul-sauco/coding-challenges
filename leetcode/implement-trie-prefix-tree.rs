// 208. Implement Trie (Prefix Tree)
// 🟠 Medium
//
// https://leetcode.com/problems/implement-trie-prefix-tree/
//
// Tags: Hash Table - String - Design - Trie

// NOTE: This file contains two different implementations, one using an extra
// TrieNode class and one that directly uses the Trie class and HashMaps to
// construct the structure, scroll down to see the second one.

// A TrieNode implementation that only supports english lowercase letters.
#[derive(Clone)]
struct TrieNode {
    children: Vec<Option<Box<TrieNode>>>,
    is_word_end: bool,
}

impl TrieNode {
    fn new() -> Self {
        TrieNode {
            children: vec![None; 26],
            is_word_end: false,
        }
    }
}

// A trie implementation that internally uses TrieNodes, each TrieNode contains
// a vector of size 26 in which each element is an Option<Box<TrieNode>>. We
// use the char points of the input search and prefix words to index the next
// character in the Trie and determine if the prefix is found in the trie.
// Each TrieNode also has a boolean that lets us know if it is the last
// character in one of the words found in the Trie that we can use to match
// entire words besides prefixes.
//
// Runtime 19 ms Beats 91.25%
// Memory 15.2 MB Beats 25%
struct Trie {
    root: TrieNode,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {
    // Time complexity: O(1) - We create one TrieNode that contains a vector of
    // size 26 and a boolean value.
    // Space complexity: O(1) - Constant space.
    fn new() -> Self {
        Trie {
            root: TrieNode::new(),
        }
    }

    // Time complexity: O(2000*26) - The worst case would be inserting a 2000
    // character word in which all characters are not found in the Trie, that
    // means inserting 2000 new TrieNodes each with a 26 element vector.
    // Space complexity: O(2000*26) - Same as the time complexity.
    fn insert(&mut self, word: String) {
        let mut node = &mut self.root;
        for ch in word.chars() {
            let idx = ch as usize - 'a' as usize;
            if node.children[idx].is_none() {
                node.children[idx] = Some(Box::new(TrieNode::new()));
            }
            node = node.children[idx].as_mut().unwrap();
        }
        // We have the last character's node mark it as the end of a word.
        node.is_word_end = true;
    }

    // Time complexity: O(2000) ~ O(1) - The worst case would be searching a
    // 2000 character word found in the Trie, 2000 O(1) operations is still O(1)
    // Space complexity: O(1) - We only store a pointer to a TrieNode.
    fn search(&self, word: String) -> bool {
        let mut node = &self.root;
        for ch in word.chars() {
            let idx = ch as usize - 'a' as usize;
            if node.children[idx].is_none() {
                return false;
            }
            node = node.children[idx].as_ref().unwrap();
        }
        node.is_word_end
    }

    // Time complexity: O(2000) ~ O(1) - The worst case would be searching a
    // 2000 character word found in the Trie, 2000 O(1) operations is still O(1)
    // Space complexity: O(1) - We only store a pointer to a TrieNode.
    fn starts_with(&self, prefix: String) -> bool {
        let mut node = &self.root;
        for ch in prefix.chars() {
            let idx = ch as usize - 'a' as usize;
            if node.children[idx].is_none() {
                return false;
            }
            node = node.children[idx].as_ref().unwrap();
        }
        true
    }
}

// Another version that avoids creating a separate TrieNode class.

use std::collections::HashMap;

#[derive(Default)]
struct Trie2 {
    is_word_end: bool,
    children: HashMap<char, Trie2>,
}

/**
 * A Trie implementation in which each trie is a trie node and we keep a
 * reference to the root trie as the structure itself.
 *
 * Runtime 20 ms Beats 86.25%
 * Memory 14.3 MB Beats 48.75%
 */
impl Trie2 {
    /**
     *  Time complexity: O(1) - We create one Trie instance.
     * Space complexity: O(1) - Constant space.
     */
    fn new() -> Self {
        Self {
            is_word_end: false,
            children: HashMap::new(),
        }
    }

    /**
     * Time complexity: O(2000) - The worst case would be inserting a 2000
     * character word in which all characters are not found in the Trie, that
     * means inserting 2000 new Trie each in O(1).
     * Space complexity: O(2000) - Same as the time complexity.
     */
    fn insert(&mut self, word: String) {
        let mut node = self;
        for ch in word.chars() {
            node = node.children.entry(ch).or_default();
        }
        // We have the last character's node mark it as the end of a word.
        node.is_word_end = true;
    }

    /**
     * Time complexity: O(2000) ~ O(1) - The worst case would be searching a
     * 2000 character word found in the Trie, 2000 O(1) operations is still O(1)
     * Space complexity: O(1) - We only store a pointer to a TrieNode.
     */
    fn search(&self, word: String) -> bool {
        match self.get_last_node(word) {
            Some(node) => node.is_word_end,
            None => false,
        }
    }

    /**
     * Time complexity: O(2000) ~ O(1) - The worst case would be searching a
     * 2000 character word found in the Trie, 2000 O(1) operations is still O(1)
     * Space complexity: O(1) - We only store a pointer to a TrieNode.
     */
    fn starts_with(&self, prefix: String) -> bool {
        match self.get_last_node(prefix) {
            Some(_) => true,
            None => false,
        }
    }

    /**
     * A helper method that extracts the common logic of navigating trie levels
     * to get to the last node.
     */
    fn get_last_node(&self, word: String) -> Option<&Trie2> {
        let mut node = self;
        for ch in word.chars() {
            match node.children.get(&ch) {
                Some(child) => node = child,
                None => return None,
            }
        }
        Some(node)
    }
}

// Tests.
fn main() {
    // Test the version using TrieNode.
    let mut trie = Trie::new();
    trie.insert(String::from("apple"));
    assert_eq!(trie.search(String::from("apple")), true);
    assert_eq!(trie.search(String::from("app")), false);
    assert_eq!(trie.starts_with(String::from("app")), true);
    trie.insert(String::from("app"));
    assert_eq!(trie.search(String::from("app")), true);

    // Test the version using Trie and HashMap.
    let mut trie = Trie2::new();
    trie.insert(String::from("apple"));
    assert_eq!(trie.search(String::from("apple")), true);
    assert_eq!(trie.search(String::from("app")), false);
    assert_eq!(trie.starts_with(String::from("app")), true);
    trie.insert(String::from("app"));
    assert_eq!(trie.search(String::from("app")), true);
    println!("All tests passed!")
}
