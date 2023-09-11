// 1282. Group the People Given the Group Size They Belong To
// 🟠 Medium
//
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
//
// Tags: Array - Hash Table

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Insert all people in a map with their group size as the key and a vector
    /// of people with that group size as the value. Then iterate the hashmap
    /// grouping the people found in each entry in groups of the key size, push
    /// all these groups into a vector and return that.
    ///
    /// Time complexity: O(n) - We iterate over all the elements twice and do
    /// constant time work for each.
    /// Space complexity: O(n) - Both the hashmap and the result vector have the
    /// same number of entries as the input vector.
    ///
    /// Runtime 4 ms Beats 73.33%
    /// Memory 2.25 MB Beats 53.33%
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        let mut d: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..group_sizes.len() {
            d.entry(group_sizes[i])
                .and_modify(|v: &mut Vec<i32>| v.push(i as i32))
                .or_insert(vec![i as i32]);
        }
        let mut res: Vec<Vec<i32>> = vec![];
        for (key, elements) in d {
            for chunk in elements.chunks(key as usize) {
                res.push(chunk.to_vec());
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![3, 3, 3, 3, 3, 1, 3],
            vec![vec![0, 1, 2], vec![3, 4, 6], vec![5]],
        ),
        (
            vec![2, 1, 3, 3, 3, 2],
            vec![vec![1], vec![0, 5], vec![2, 3, 4]],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::group_the_people(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
