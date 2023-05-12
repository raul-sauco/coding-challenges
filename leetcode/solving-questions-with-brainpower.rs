// 2140. Solving Questions With Brainpower
// 🟠 Medium
//
// https://leetcode.com/problems/solving-questions-with-brainpower/
//
// Tags: Array - Dynamic Programming

struct Solution;
impl Solution {
    /// Top down solution, use a helper function that takes the index of the
    /// first element that we can use as a parameter, the function recursively
    /// calls itself with two different parameters, using and skipping the
    /// current element, and returns the max result between these two options.
    ///
    /// Time complexity: O(n) - The maximum number of times we will execute the
    /// code inside the helper function is equal to the size of the cache n.
    /// Space complexity: O(n) - The size of the cache that we are using, the
    /// call stack will be, at most, equal to the size of the cache.
    ///
    /// Runtime 47 ms Beats 18.18%
    /// Memory 15.7 MB Beats 27.27%
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
        // A function that picks the best option between using and skipping the
        // element at the current index.
        fn helper(idx: usize, q: &Vec<Vec<i32>>, c: &mut Vec<i64>) -> i64 {
            // Base case, we have consumed all elements.
            if idx >= q.len() {
                return 0;
            }
            if c[idx] == -1 {
                c[idx] = helper(idx + 1, q, c)
                    .max(helper(idx + q[idx][1] as usize + 1, q, c) + q[idx][0] as i64);
            }
            c[idx]
        }
        let mut cache: Vec<i64> = vec![-1; questions.len()];
        helper(0, &questions, &mut cache)
    }

    /// Dynamic programming version of the previous solution, we create a DP
    /// vector that we iterate backwards, for each position, the maximum points
    /// that we could have there will be the maximum between skipping and
    /// taking that question. Skipping can be computed as the max at dp[i+1],
    /// taking can be computed as dp[i+brain power+1] + points.
    ///
    /// Time complexity: O(n) - We iterate over all n indexes of dp and do O(1)
    /// work for each.
    /// Space complexity: O(n) - The size of the dp array.
    ///
    /// Runtime 33 ms Beats 81.82%
    /// Memory 9.2 MB Beats 63.64%
    pub fn most_points_2(questions: Vec<Vec<i32>>) -> i64 {
        let mut dp: Vec<i64> = vec![0; questions.len()];
        for (idx, q) in (questions.iter().enumerate()).rev() {
            let points = q[0] as i64;
            let bp = q[1] as usize;
            let skip = if idx + 1 < dp.len() { dp[idx + 1] } else { 0 };
            let take = if idx + bp + 1 < dp.len() {
                points + dp[idx + bp + 1]
            } else {
                points
            };
            dp[idx] = skip.max(take);
        }
        dp[0]
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![vec![3, 2], vec![4, 3], vec![4, 4], vec![2, 5]], 5),
        (
            vec![vec![1, 1], vec![2, 2], vec![3, 3], vec![4, 4], vec![5, 5]],
            7,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::most_points(t.0.clone()), t.1);
        assert_eq!(Solution::most_points_2(t.0.clone()), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
