// 18. 4Sum
// 🟠 Medium
//
// https://leetcode.com/problems/4sum/
//
// Tags: Array - Two Pointers - Sorting

struct Solution;
impl Solution {
    // A general algorithm that efficiently picks the sum of k numbers that
    // adds up to a given target if found in an input array of numbers, the
    // function works by fixing k-2 values and using a two pointer technique
    // to find the remaining 2, improving the time complexity by one order
    // of magnitude n.
    //
    // Time complexity: O(n^3) - The time complexity is O(n^(k-1)) in the
    // current case, where k == 4, O(n^3).
    // Space complexity: O(k) - The height of the call stack will be k-1,
    // which can be simplified to O(k).
    //
    // Runtime 4 ms Beats 97.10%
    // Memory 2.1 MB Beats 53.62%
    pub fn four_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        // Sorting lets us skip same value in the same position later.
        let mut vals = nums.clone();
        vals.sort();
        let mut current: Vec<i32> = vec![];
        Self::k_sum(4, 0, &vals, target as i64, &mut current)
    }

    // This function picks the next number to try, then backtracks.
    fn k_sum(
        k: usize,
        start: usize,
        vals: &Vec<i32>,
        target: i64,
        current: &mut Vec<i32>,
    ) -> Vec<Vec<i32>> {
        let mut res = vec![];
        // If we want more elements than available, empty result set.
        if k > vals.len() {
            return res;
        }
        for i in start..(vals.len() + 1 - k) {
            // Avoid picking the same value in the same position.
            if i > start && vals[i] == vals[i - 1] {
                continue;
            }
            current.push(vals[i]);
            if k == 3 {
                res.append(&mut Self::two_sum(
                    i + 1,
                    vals,
                    target - vals[i] as i64,
                    current,
                ));
            } else {
                res.append(&mut Self::k_sum(
                    k - 1,
                    i + 1,
                    vals,
                    target - vals[i] as i64,
                    current,
                ));
            }
            // Backtrack.
            current.pop();
        }
        res
    }

    // Use two pointers to pick two values in a sorted array that sum to the
    // given target in O(n).
    fn two_sum(
        start: usize,
        vals: &Vec<i32>,
        target: i64,
        current: &mut Vec<i32>,
    ) -> Vec<Vec<i32>> {
        let mut res = vec![];
        let (mut l, mut r) = (start, vals.len() - 1);
        let mut s;
        while l < r {
            s = vals[l] as i64 + vals[r] as i64;
            if s < target {
                l += 1;
            } else if target < s {
                r -= 1
            // We found a match.
            } else {
                let mut c = current.clone();
                c.append(&mut vec![vals[l], vals[r]]);
                res.push(c);
                // Keep trying to find more matches with the
                // current prefix.
                l += 1;
                while l < r && vals[l] == vals[l - 1] {
                    l += 1;
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0], 0, vec![]),
        (vec![2, 2, 2, 2, 2], 8, vec![vec![2, 2, 2, 2]]),
        (
            vec![1, 0, -1, 0, -2, 2],
            0,
            vec![vec![-2, -1, 1, 2], vec![-2, 0, 0, 2], vec![-1, 0, 0, 1]],
        ),
        (
            vec![1000000000, 1000000000, 1000000000, 1000000000],
            -294967296,
            vec![],
        ),
    ];
    for test in tests {
        assert_eq!(Solution::four_sum(test.0, test.1), test.2);
    }
    println!("All tests passed!")
}
