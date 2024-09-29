// 432. All O`one Data Structure
// 🔴 Hard
//
// https://leetcode.com/problems/all-oone-data-structure/
//
// Tags: Hash Table - Linked List - Design - Doubly-Linked List

use std::collections::{BTreeSet, HashMap};

/// We need to be able to find an entry given only its key, while at the same time, being able to
/// preserve the ordering of the entries based on their count, the easiest way is to use two data
/// structures, a hashmap of key => count to find the count of an item given its key, then use the
/// pair as the keys in a structure that preserves ordering, like a BTreeSet. For each call, we
/// remove the item from the set update its count and reinsert it, to preserve the ordering.
///
/// Time complexity: O(nlog(n)) - Where n is the number of calls made to inc/dec, these calls
/// remove the entry from the BTreeSet and reinsert it, both at log(n) cost.
/// Space complexity: O(e) - Where e is the number of different keys that are in the all-o-one
/// structure at one given time, and it could be equal to the number of calls.
///
/// Runtime 22 ms Beats 93%
/// Memory 14.80 MB Beats 62%
#[derive(Ord, PartialOrd, Eq, PartialEq)]
struct Entry {
    count: usize,
    key: String,
}

#[derive(Default)]
struct AllOne {
    hm: HashMap<String, usize>,
    counts: BTreeSet<Entry>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AllOne {
    fn new() -> Self {
        Default::default()
    }

    fn inc(&mut self, key: String) {
        match self.hm.get_mut(&key) {
            Some(count) => {
                let mut e = Entry { key, count: *count };
                self.counts.remove(&e);
                *count += 1;
                e.count += 1;
                self.counts.insert(e);
            }
            None => {
                self.hm.insert(key.clone(), 1);
                self.counts.insert(Entry { key, count: 1 });
            }
        }
    }

    #[allow(dead_code)]
    fn dec(&mut self, key: String) {
        match self.hm.get_mut(&key) {
            Some(1) => {
                self.hm.remove(&key);
                self.counts.remove(&Entry { key, count: 1 });
            }
            Some(count) => {
                let mut e = Entry { key, count: *count };
                self.counts.remove(&e);
                *count -= 1;
                e.count -= 1;
                self.counts.insert(e);
            }
            None => unreachable!("No calling dec with missing key"),
        }
    }

    fn get_max_key(&self) -> String {
        match self.counts.last() {
            Some(e) => e.key.clone(),
            None => "".to_string(),
        }
    }

    fn get_min_key(&self) -> String {
        match self.counts.first() {
            Some(e) => e.key.clone(),
            None => "".to_string(),
        }
    }
}

// Tests.
fn main() {
    println!("\n\x1b[92m» Running tests...\x1b[0m");
    let mut success = 0;
    let mut all_one = AllOne::new();
    all_one.inc("hello".to_string());
    all_one.inc("hello".to_string());
    if all_one.get_max_key() == "hello" {
        println!("\x1b[92m✔\x1b[95m Test 1 passed!\x1b[0m");
        success += 1;
    }
    if all_one.get_min_key() == "hello" {
        println!("\x1b[92m✔\x1b[95m Test 2 passed!\x1b[0m");
        success += 1;
    }
    all_one.inc("leet".to_string());
    if all_one.get_max_key() == "hello" {
        println!("\x1b[92m✔\x1b[95m Test 3 passed!\x1b[0m");
        success += 1;
    }
    if all_one.get_min_key() == "leet" {
        println!("\x1b[92m✔\x1b[95m Test 4 passed!\x1b[0m");
        success += 1;
    }
    all_one.dec("hello".to_string());
    all_one.dec("hello".to_string());
    if all_one.get_max_key() == "leet" {
        println!("\x1b[92m✔\x1b[95m Test 5 passed!\x1b[0m");
        success += 1;
    }
    println!();
    if success == 5 {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!("\x1b[31mx\x1b[95m {} tests failed!\x1b[0m", 5 - success)
    }
}
