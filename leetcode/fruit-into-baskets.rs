// 904. Fruit Into Baskets
// 🟠 Medium
//
// https://leetcode.com/problems/fruit-into-baskets/
//
// Tags: Array - Hash Table - Sliding Window

struct Solution;
impl Solution {
    // Use a sliding window to add remove fruits from the baskets and a
    // hashmap to represent the baskets and how many fruits we have in them.
    //
    // Time complexity: O(n) - We visit each element once and do O(1) work.
    // Space complexity: O(1) - We use constant extra memory, two pointers
    // and a hashmap of max size == 3.
    //
    // Runtime 38 ms Beats 11.11%
    // Memory 2.5 MB Beats 55.56%
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut have = HashMap::<i32, usize>::new();
        let mut l = 0;
        let mut res = 0;
        for r in 0..fruits.len() {
            *have.entry(fruits[r]).or_insert(0) += 1;
            while have.len() > 2 {
                *have.get_mut(&fruits[l]).unwrap() -= 1;
                if *have.get(&fruits[l]).unwrap() == 0 {
                    have.remove(&fruits[l]);
                }
                l += 1;
            }
            if r - l + 1 > res {
                res = r - l + 1;
            }
        }
        res as i32
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::total_fruit(vec![1, 2, 1]), 3);
    assert_eq!(Solution::total_fruit(vec![0, 1, 2, 2]), 3);
    assert_eq!(Solution::total_fruit(vec![1, 2, 3, 2, 2]), 4);
    println!("All tests passed!")
}
