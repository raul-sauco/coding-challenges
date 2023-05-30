// 705. Design HashSet
// 🟢 Easy
//
// https://leetcode.com/problems/design-hashset/
//
// Tags: Array - Hash Table - Linked List - Design - Hash Function

use std::ops::BitXor;

struct MyHashSet {
    size: usize,
    k: usize,
    values: Vec<Vec<i32>>,
}

/// The problem really is asking us to define a hash function and handle
/// collisions, here I use the simple FxHasher used in the Rust compiler.
/// https://github.com/rust-lang/rustc-hash/blob/5e09ea0a1c7ab7e4f9e27771f5a0e5a36c58d1bb/src/lib.rs
/// Each hash key points to a vector that we will use to handle collisions.
///
/// Time complexity: O(1) - In theory is possible that all elements end up in
/// the same bucket and the complexity is O(n) because we need to iterate a
/// vector of size n to check if the element is there, but the elements are
/// much more likely to end up somewhat evenly split between buckets.
/// Space complexity: O(n) - Each add call can add one element to the hash set.
///
/// - With a bucket of size 1000:
/// Runtime 11 ms Beats 100%
/// Memory 6.5 MB Beats 56.52%
///
/// - With a bucket of size 100:
/// Runtime 20 ms Beats 91.30%
/// Memory 6.4 MB Beats 82.61%
impl MyHashSet {
    fn new() -> Self {
        let size = 1000;
        MyHashSet {
            size,
            k: 0x517cc1b727220a95,
            values: vec![vec![]; size],
        }
    }

    fn add(&mut self, key: i32) {
        let hash = self.hash(key);
        if !self.values[hash].contains(&key) {
            self.values[hash].push(key);
        }
    }

    fn remove(&mut self, key: i32) {
        let hash = self.hash(key);
        self.values[hash].retain(|&x| x != key);
    }

    fn contains(&self, key: i32) -> bool {
        self.values[self.hash(key)].contains(&key)
    }

    fn hash(&self, val: i32) -> usize {
        let val = val as usize;
        val.rotate_left(5).bitxor(val).wrapping_mul(self.k) % self.size
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet::new();
 * obj.add(key);
 * obj.remove(key);
 * let ret_3: bool = obj.contains(key);
 */
fn main() {
    let mut my_hash_set = MyHashSet::new();
    my_hash_set.add(1);
    my_hash_set.add(2);
    assert_eq!(my_hash_set.contains(1), true);
    assert_eq!(my_hash_set.contains(3), false);
    my_hash_set.add(2);
    assert_eq!(my_hash_set.contains(2), true);
    my_hash_set.remove(2);
    assert_eq!(my_hash_set.contains(2), false);
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
