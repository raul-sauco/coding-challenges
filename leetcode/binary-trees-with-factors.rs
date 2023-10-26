// 823. Binary Trees With Factors
// 🟠 Medium
//
// https://leetcode.com/problems/binary-trees-with-factors/
//
// Tags: Array - Hash Table - Dynamic Programming - Sorting

struct Solution;
impl Solution {
    /// Sort the entries, iterate over them using nested loops from smaller to
    /// greater while computing the number of trees rooted at each value, the
    /// inner loop uses the already computed number of trees rooted at the smaller
    /// values to compute the number of trees that we can construct using the
    /// bigger values.
    ///
    /// Time complexity: O(n^2) - We iterate over n values in both loops at most.
    /// Space complexity: O(n) - The copy of arr and the hash map both are size n.
    ///
    /// Runtime 82 ms Beats 14.29%
    /// Memory 2.28 MB Beats 14.29%
    pub fn num_factored_binary_trees(arr: Vec<i32>) -> i32 {
        let modu = 1_000_000_007;
        let mut arr = arr.into_iter().map(|x| x as usize).collect::<Vec<usize>>();
        arr.sort_unstable();
        let mut total_trees = 0;
        let mut dp = std::collections::HashMap::<usize, usize>::new();
        for (i, root) in arr.iter().enumerate() {
            // The value by itself is a subtree.
            dp.insert(*root, 1);
            for j in 0..i {
                let a = arr[j];
                let dp_a = *dp.get(&a).unwrap();
                if arr[i] % a == 0 {
                    let b = root / a;
                    if dp.contains_key(&b) {
                        let dp_b = *dp.get(&b).unwrap();
                        // dp[i] = (dp[i] + dp[a] * dp[b]) % modu;
                        dp.entry(*root)
                            .and_modify(|val| *val = (*val + dp_a * dp_b) % modu);
                    }
                }
            }
            total_trees = (total_trees + dp[&root]) % modu;
        }
        total_trees as i32
    }
}

// Tests.
fn main() {
    let tests = [(vec![2, 4], 3), (vec![2, 4, 5, 10], 7)];
    for t in tests {
        assert_eq!(Solution::num_factored_binary_trees(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
