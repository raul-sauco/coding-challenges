// 953. Verifying an Alien Dictionary
// 🟢 Easy
//
// https://leetcode.com/problems/verifying-an-alien-dictionary/
//
// Tags: Array - Hash Table - String

struct Solution;
impl Solution {
    // Create a hashmap with the characters pointing to the ordinal value,
    // then iterate over the words in the input using the hashmap to check
    // the words one character at a time until we find a tie-breaker.
    //
    // Time complexity: O(m+n) - Where m is the number of characters in order
    // and it is limited to 26, we iterate over them to create the o dict.
    // n is the combined number of characters in words, we could iterate over
    // all of them depending on the input. Equivalent to O(n) because m <= 26
    // Space complexity: O(m) ~ O(1) - The dictionary takes m space with
    // m <= 26.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2.2 MB Beats 57.14%
    pub fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
        use std::collections::HashMap;
        // Construct a hashmap to quickly check a characters order.
        let mut o = HashMap::<char, usize>::with_capacity(order.len());
        for (i, c) in order.chars().enumerate() {
            o.insert(c, i);
        }
        // Define a function that returns whether to words are ordered lexicographically
        // according to the given order.
        fn are_sorted(w1: &String, w2: &String, m: &HashMap<char, usize>) -> bool {
            let chs1: Vec<_> = w1.chars().collect();
            let chs2: Vec<_> = w2.chars().collect();
            for i in 0..w1.len().min(w2.len()) {
                let ord1 = m.get(&chs1[i]).unwrap();
                let ord2 = m.get(&chs2[i]).unwrap();
                if ord1 < ord2 {
                    return true;
                } else if ord1 > ord2 {
                    return false;
                }
            }
            // If the compared characters are all the same, we need to check string lengths.
            if w1.len() > w2.len() {
                false
            } else {
                true
            }
        }
        // Iterate over the input words checking that each contiguous pair is
        // lexicographically sorted.
        for i in 1..words.len() {
            if !are_sorted(&words[i - 1], &words[i], &o) {
                return false;
            }
        }
        true
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::is_alien_sorted(
            vec![String::from("apap"), String::from("app")],
            String::from("abcdefghijklmnopqrstuvwxyz")
        ),
        true
    );
    assert_eq!(
        Solution::is_alien_sorted(
            vec![String::from("apple"), String::from("app")],
            String::from("abcdefghijklmnopqrstuvwxyz")
        ),
        false
    );
    assert_eq!(
        Solution::is_alien_sorted(
            vec![String::from("hello"), String::from("leetcode")],
            String::from("hlabcdefgijkmnopqrstuvwxyz")
        ),
        true
    );
    println!("All tests passed!")
}
