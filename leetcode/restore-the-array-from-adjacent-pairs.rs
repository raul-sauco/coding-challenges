// 1743. Restore the Array From Adjacent Pairs
// 🟠 Medium
//
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
//
// Tags: Array - Hash Table

use std::collections::HashMap;

struct Solution;
impl Solution {
    /// Construct a hashmap with the adjacencies in the input, then the problem has been reduced to
    /// finding the first element, one of the two that only appears once in the input pairs, and
    /// following the links that we have created to reconstruct the array from which the pairs
    /// originally came.
    ///
    /// Time complexity: O(n) - We iterate several times over n elements, but we always do constant
    /// time work in all of them. We create the adjacency list, then iterate over the list to find
    /// an element that only appears once in the input pairs, then we use the hashmap to do a DFS
    /// on the graph and reconstruct the array from which the pairs came.
    /// Space complexity: O(n) - The adjacency hashmap has size n.
    ///
    /// Runtime 84 ms Beats 72.22%
    /// Memory 20.82 MB Beats 72.22%
    pub fn restore_array(adjacent_pairs: Vec<Vec<i32>>) -> Vec<i32> {
        // A hashmap of num => (index, boolean flagging left or right position in the pair)
        let mut hm: HashMap<i32, Vec<(usize, bool)>> = HashMap::new();
        let n = adjacent_pairs.len();
        for i in 0..n {
            hm.entry(adjacent_pairs[i][0])
                .and_modify(|p| p.push((i, true)))
                .or_insert(vec![(i, true)]);
            hm.entry(adjacent_pairs[i][1])
                .and_modify(|p| p.push((i, false)))
                .or_insert(vec![(i, false)]);
        }
        let mut res = Vec::with_capacity(n + 1);
        let mut next = (0, true);
        for (_, val) in hm.iter() {
            if val.len() == 1 {
                next = val[0];
                break;
            }
        }
        let (mut pair, mut idx, mut adj);
        for _ in 0..=n {
            // Next points to the next pair and value we want to insert.
            idx = next.0;
            pair = [adjacent_pairs[idx][0], adjacent_pairs[idx][1]];
            res.push(pair[if next.1 { 0 } else { 1 }]);
            adj = pair[if next.1 { 1 } else { 0 }];
            if let Some(e) = hm.get(&adj) {
                if e.len() == 1 {
                    next = e[0].clone();
                } else {
                    for (i, b) in e {
                        if *i != idx {
                            next = (*i, *b);
                        }
                    }
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![2, 1], vec![3, 4], vec![3, 2]], vec![1, 2, 3, 4]),
        (
            vec![vec![4, -2], vec![1, 4], vec![-3, 1]],
            vec![-2, 4, 1, -3],
        ),
        (vec![vec![100000, -100000]], vec![100000, -100000]),
    ];
    let n = tests.len();
    let mut failed = 0;
    for t in tests {
        let res = Solution::restore_array(t.0);
        let expected = t.1;
        let reversed = expected.iter().rev().cloned().collect::<Vec<_>>();
        if res != expected && res != reversed {
            failed += 1;
            println!(
                "\x1b[91m  » {:?} not {:?} or {:?}\x1b[0m",
                res, expected, reversed
            );
        }
    }
    if failed == 0 {
        println!("\x1b[92m» All tests passed!\x1b[0m");
    } else if failed == n {
        println!("\x1b[91m» All tests failed!\x1b[0m");
    } else {
        println!("\x1b[93m» {} tests failed!\x1b[0m", failed);
    }
}
