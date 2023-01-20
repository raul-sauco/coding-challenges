// 491. Non-decreasing Subsequences
// 🟠 Medium
//
// https://leetcode.com/problems/non-decreasing-subsequences/
//
// Tags: Array - Hash Table - Backtracking - Bit Manipulation

struct Solution;
impl Solution {
    // The classic backtracking solution to sub-sequence type problems. Start
    // at the first element of the array and split into two branches, one
    // that uses it and one that skips it, for each element after that, we
    // chose to skip it and keep building the sequence and, if its value does
    // not break the non-decreasing property of the sequence, we create
    // another branch that uses the element.
    //
    // Time complexity: O(n*2^n) - The decision tree splits in two at each
    // level and it has a max of n levels, for each of the 2^n possible
    // sequences, we iterate over all its elements, a max of n, to convert
    // them into a tuple hash them and add them to the hash set.
    // Space complexity: O(n*2^n) - The number of subsequences that could be
    // in the hash set.
    //
    // Runtime 19 ms Beats 100%
    // Memory 5.6 MB Beats 44.44%
    pub fn find_subsequences(nums: Vec<i32>) -> Vec<Vec<i32>> {
        use std::collections::HashSet;
        let mut res = HashSet::new();
        let mut cur = vec![];
        fn bt(idx: usize, cur: &mut Vec<i32>, res: &mut HashSet<Vec<i32>>, nums: &Vec<i32>) {
            if idx == nums.len() {
                // If the subsequence is not empty.
                if cur.len() > 1 {
                    res.insert(cur.to_vec());
                }
                return;
            }
            // Keep building the sequence that skips this number.
            bt(idx + 1, cur, res, nums);
            // Try to unpack the last value.
            if cur.is_empty() || cur[cur.len() - 1] <= nums[idx] {
                cur.push(nums[idx]);
                bt(idx + 1, cur, res, nums);
                cur.pop();
            }
        }
        bt(0, &mut cur, &mut res, &nums);
        res.into_iter().collect()
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::find_subsequences(vec![4, 4, 3, 2, 1]).sort(),
        vec![vec![4, 4]].sort()
    );
    assert_eq!(
        Solution::find_subsequences(vec![4, 6, 7, 7]).sort(),
        vec![
            vec![4, 6],
            vec![4, 6, 7],
            vec![4, 6, 7, 7],
            vec![4, 7],
            vec![4, 7, 7],
            vec![6, 7],
            vec![6, 7, 7],
            vec![7, 7],
        ]
        .sort()
    );
    println!("All tests passed!")
}
