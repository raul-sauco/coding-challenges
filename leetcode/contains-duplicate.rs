// 217. Contains Duplicate
// 🟢 Easy
//
// https://leetcode.com/problems/contains-duplicate/
//
// Tags: Array - Hash Table - Sorting

struct Solution;
impl Solution {
    // Use a hash table to store values that we have seen, if we see a value
    // that is already in the hash table, we have found a duplicate.
    //
    // Time complexity: O(n) - We could end up visiting each value, for each,
    // we do O(1) work.
    // Space complexity: O(n) - The hash set could grow to the size of the
    // input.
    //
    // Runtime 12 ms Beats 89.2%
    // Memory 3.8 MB Beats 40.87%
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        use std::collections::HashSet;
        let mut seen = HashSet::<i32>::new();
        for num in nums {
            if seen.contains(&num) {
                return true;
            }
            seen.insert(num);
        }
        false
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::contains_duplicate(vec![1, 2, 3, 1]), true);
    assert_eq!(Solution::contains_duplicate(vec![1, 2, 3, 4]), false);
    assert_eq!(
        Solution::contains_duplicate(vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2]),
        true
    );
    println!("All tests passed!")
}
