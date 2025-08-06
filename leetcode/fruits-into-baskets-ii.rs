// 3477. Fruits Into Baskets II
// 🟢 Easy
//
// https://leetcode.com/problems/fruits-into-baskets-ii/
//
// Tags: Array - Binary Search - Segment Tree - Simulation - Ordered Set

struct Solution;
impl Solution {
    /// For each element in fruits, iterate baskets until we find a basket we can place the fruit
    /// in, or we run out of baskets.
    ///
    /// Time complexity: O(n^2) - For each element in fruits, we may iterate the entire baskets
    /// vector.
    /// Space complexity: O(n) - The available vector.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.10 MB Beats 100%
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, baskets: Vec<i32>) -> i32 {
        let n = fruits.len();
        let mut available = vec![true; n];
        let mut res = 0;
        let mut placed;
        for fruit in fruits {
            placed = false;
            for i in 0..n {
                if available[i] && fruit <= baskets[i] {
                    placed = true;
                    available[i] = false;
                    break;
                }
            }
            if !placed {
                res += 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![4, 2, 5], vec![3, 5, 4], 1),
        (vec![3, 6, 1], vec![6, 4, 7], 0),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::num_of_unplaced_fruits(t.0.clone(), t.1.clone());
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
