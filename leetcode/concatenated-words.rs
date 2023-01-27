// 472. Concatenated Words
// 🔴 Hard
//
// https://leetcode.com/problems/concatenated-words/
//
// Tags: Array - String - Dynamic Programming - Depth-First Search - Trie

struct Solution;
impl Solution {
    // We can create a dictionary of words keyed by their lengths, then we
    // iterate over the input words, for any word that is long enough to be
    // a concatenation of other words, we try to build by checking all the
    // slices that are of a length that has an existing word, if the slice
    // is found in the dictionary, we continue building, if we get to the
    // end of the word, we have found that all its substrings are smaller
    // words in the input.
    //
    // Time complexity: O(n) - Where n is the number of characters in the
    // input. We have to read all the characters to create the initial
    // dictionary, then we sort the keys in O(k*log(k)) where k is the number
    // of unique word lengths in the input and it is guaranteed to be less
    // than n, then we iterate over all words taking slices and checking if
    // the slices can be found in the dictionary, this is also O(n).
    // Space complexity: O(n) - The dictionary holds all the characters in
    // the input words.
    //
    // Runtime 37 ms Beats 100%
    // Memory 3.4 MB Beats 40%
    pub fn find_all_concatenated_words_in_a_dict(words: Vec<String>) -> Vec<String> {
        use std::collections::{BTreeMap, HashSet};
        let mut d: BTreeMap<usize, HashSet<String>> = BTreeMap::new();
        let mut shortest_two = vec![31; 2];
        for w in words.iter() {
            let l = w.len();
            let words_of_length = d.entry(l).or_insert(HashSet::new());
            words_of_length.insert(w.to_string());
            if l < shortest_two[1] {
                shortest_two[1] = l;
                if shortest_two[1] < shortest_two[0] {
                    let tmp = shortest_two[0];
                    shortest_two[0] = shortest_two[1];
                    shortest_two[1] = tmp;
                }
            }
        }
        // The minimum length a word needs to be considered.
        let min_length_concat: usize = shortest_two.iter().sum();
        let mut res: HashSet<String> = HashSet::new();
        fn dfs(
            word: &String,
            idx: usize,
            d: &BTreeMap<usize, HashSet<String>>,
            shortest: usize,
            res: &mut HashSet<String>,
        ) {
            // Base case, we have built the given word using other words
            // in the input.
            if idx == word.len() {
                res.insert(word.to_string());
                return;
            }
            for (length, words_of_length) in d {
                if word.len() - shortest < *length || idx + *length > word.len() {
                    break;
                }
                let wanted = &word[idx..idx + length];
                if words_of_length.contains(wanted) {
                    dfs(word, idx + length, d, shortest, res);
                }
            }
        }
        for w in words {
            if w.len() >= min_length_concat {
                dfs(&w, 0, &d, shortest_two[0], &mut res);
            }
        }
        res.into_iter().collect()
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::find_all_concatenated_words_in_a_dict(vec![
            String::from("cat"),
            String::from("dog"),
            String::from("catdog")
        ]),
        vec!["catdog"]
    );
    let mut res = Solution::find_all_concatenated_words_in_a_dict(vec![
        String::from("cat"),
        String::from("cats"),
        String::from("catsdogcats"),
        String::from("dog"),
        String::from("dogcatsdog"),
        String::from("hippopotamuses"),
        String::from("rat"),
        String::from("ratcatdogcat"),
    ]);
    res.sort();
    assert_eq!(res, vec!["catsdogcats", "dogcatsdog", "ratcatdogcat",]);
    println!("All tests passed!")
}
