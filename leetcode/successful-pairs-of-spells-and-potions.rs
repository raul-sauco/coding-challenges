// 2300. Successful Pairs of Spells and Potions
// 🟠 Medium
//
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
//
// Tags: Array - Two Pointers - Binary Search - Sorting

struct Solution;
impl Solution {
    /// Sort the potions array, then iterate over the spells, for each spell,
    /// find the index of the first potion that we can combine with it to
    /// satisfy the success value.
    ///
    /// Time complexity: O(n*log(n)+m*log(n)) - Where m is the number of spells
    /// and n is the number of potions. We sort the potions array at nlog(n)
    /// cost, then iterate over the spells, for each spell, we binary search
    /// the number of potions that can be combined with the spell to result in
    /// a successful combination.
    /// Space complexity: O(m+n) - We make a copy of the potions array n and
    /// sort it, the result array has size m.
    ///
    /// Runtime 55 ms Beats 88.89%
    /// Memory 4 MB Beats 55.56%
    pub fn successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        // Sort the potions to be able to binary search the boundary.
        let mut potions = potions;
        potions.sort_unstable();
        let n = potions.len();
        let mut res = Vec::with_capacity(spells.len());
        for spell_force in spells {
            // Need to cast both before multiplying to avoid overflow.
            let spell_force = spell_force as i64;
            // Binary search the boundary.
            let (mut l, mut r) = (0, n);
            while l < r {
                let mid = (l + r) / 2;
                let combined_force = spell_force * potions[mid] as i64;
                if combined_force < success {
                    l = mid + 1;
                } else {
                    r = mid;
                }
            }
            // The number of successful combinations for this spell.
            res.push((n - l) as i32);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 1, 2], vec![8], 16, vec![1, 0, 1]),
        (vec![3, 1, 2], vec![8, 5, 8], 16, vec![2, 0, 2]),
        (vec![5, 1, 3], vec![1, 2, 3, 4, 5], 7, vec![4, 0, 3]),
    ];
    for t in tests {
        assert_eq!(Solution::successful_pairs(t.0, t.1, t.2), t.3);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
