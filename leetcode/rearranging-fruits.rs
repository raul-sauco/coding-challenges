// 2561. Rearranging Fruits
// 🔴 Hard
//
// https://leetcode.com/problems/rearranging-fruits/
//
// Tags: Array - Hash Table - Greedy - Sort

use std::collections::{HashMap, HashSet};

struct Solution;
impl Solution {
    /// Get the counts of elements in both vectors, then iterate over all the values found in both
    /// vectors, for each check if the count is uneven, equal or even, if even but not equal, we
    /// will need to swap some elements from one vector to the other, save these to_swap elements.
    /// Once we have all elements that need to be swapped, for each element, check if swapping them
    /// directly is more efficient than doing two indirect swaps using the minimum value in both
    /// vectors and add the minimum between these two to the result.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the to_swap vectors in the worst case.
    /// Space complexity: O(n) - The hashmaps, the all_keys vector and the swap vectors.
    ///
    /// Runtime 26 ms Beats 20%
    /// Memory 7.62 MB Beats 20%
    pub fn min_cost(basket1: Vec<i32>, basket2: Vec<i32>) -> i64 {
        let n = basket1.len();
        let mut min = basket1[0];
        let mut counts1: HashMap<i32, usize> = HashMap::new();
        for &num in basket1.iter() {
            *counts1.entry(num).or_default() += 1;
        }
        let mut counts2: HashMap<i32, usize> = HashMap::new();
        for &num in basket2.iter() {
            *counts2.entry(num).or_default() += 1;
        }
        let all_keys: HashSet<_> = basket1.into_iter().chain(basket2).collect();
        let mut atob = Vec::with_capacity(n);
        let mut btoa = Vec::with_capacity(n);
        for key in all_keys.iter() {
            if *key < min {
                min = *key;
            }
            let mut c1 = *counts1.get(key).unwrap_or(&0);
            let mut c2 = *counts2.get(key).unwrap_or(&0);
            // println!("{key}: {c1} {c2}");
            if (c1 + c2) % 2 != 0 {
                return -1;
            }
            while c1 != c2 {
                if c1 > c2 {
                    atob.push(*key);
                    c1 -= 1;
                    c2 += 1;
                } else {
                    btoa.push(*key);
                    c2 -= 1;
                    c1 += 1;
                }
            }
            // println!("{:?} {:?}", atob, btoa);
        }
        atob.sort_unstable();
        btoa.sort_unstable();
        // println!("{:?} {:?}", atob, btoa);
        min *= 2;
        if atob.len() != btoa.len() {
            panic!("Move vectors of different size");
        }
        let (mut a, mut b, l, mut res) = (0, 0, atob.len(), 0i64);
        while a + b < l {
            if atob.get(a).unwrap_or(&i32::MAX) < btoa.get(b).unwrap_or(&i32::MAX) {
                res += (atob[a].min(min)) as i64;
                a += 1;
            } else {
                res += (btoa[b].min(min)) as i64;
                b += 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![4, 2, 2, 2], vec![1, 4, 1, 2], 1),
        (vec![2, 3, 4, 1], vec![3, 2, 5, 1], -1),
        (
            vec![84, 80, 43, 8, 80, 88, 43, 14, 100, 88],
            vec![32, 32, 42, 68, 68, 100, 42, 84, 14, 8],
            48,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_cost(t.0.clone(), t.1.clone());
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.2, res
            );
        }
    }
    println!();
    if success == tests.len() {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
