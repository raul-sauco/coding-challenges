// 2028. Find Missing Observations
// 🟠 Medium
//
// https://leetcode.com/problems/find-missing-observations/
//
// Tags: Array - Math - Simulation

struct Solution;
impl Solution {
    /// A recursive solution computes the sum of the missing values and explores all possible
    /// solutions trying the values 1..=6 for each of the missing positions, this is not very
    /// efficient but it still passes the tests, which actually I found a bit surprising.
    ///
    /// Time complexity: O(6^n) - We branch on 6 different possibilities at each level and we
    /// compute n missing values.
    /// Space complexity: O(n) - The depth of the call stack and also the result vector.
    ///
    /// Runtime 81 ms Beats 25%
    /// Memory 12.48 MB Beats 25%
    #[allow(dead_code)]
    pub fn missing_rolls_rec(rolls: Vec<i32>, mean: i32, n: i32) -> Vec<i32> {
        let n_sum = (rolls.len() as i32 + n) * mean - rolls.iter().sum::<i32>();
        if n_sum < n || n_sum > 6 * n {
            return vec![];
        }
        fn dfs(cur: &mut Vec<i32>, sum: i32, n: i32) -> Result<String, String> {
            if sum < n || sum > n * 6 || (n == 0 && sum != 0) {
                return Err(String::from("No solution for this branch"));
            }
            if n == 0 && sum == 0 {
                return Ok(String::from("Solution found"));
            }
            for t in 1..=6 {
                cur.push(t);
                match dfs(cur, sum - t, n - 1) {
                    Ok(msg) => return Ok(msg),
                    Err(_) => {
                        cur.pop();
                    }
                }
            }
            Err(String::from("No solution for this branch"))
        }
        let mut res = vec![];
        match dfs(&mut res, n_sum, n) {
            Ok(_) => res,
            Err(_) => vec![],
        }
    }

    /// A linear time solution, compute the missing sum and create a vector where each element is
    /// missing sum / n. We may have a remainder missing sum % n, spread that remainder between the
    /// result elements.
    ///
    /// Time complexity: O(n) - We create a vector of size n and maybe visit some of its elements.
    /// Space complexity: O(n) - The size of the result vector.
    ///
    /// Runtime 51 ms Beats 87%
    /// Memory 3.07 MB Beats 25%
    pub fn missing_rolls(rolls: Vec<i32>, mean: i32, n: i32) -> Vec<i32> {
        let n_sum = (rolls.len() as i32 + n) * mean - rolls.iter().sum::<i32>();
        if n_sum < n || n_sum > 6 * n {
            return vec![];
        }
        let mut res = vec![n_sum / n; n as usize];
        let rem = n_sum % n;
        for i in 0..rem as usize {
            res[i] += 1;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 2, 4, 3], 4, 2, vec![6, 6]),
        (vec![1, 5, 6], 3, 4, vec![3, 2, 2, 2]),
        (vec![1, 2, 3, 4], 6, 4, vec![]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::missing_rolls(t.0.clone(), t.1, t.2);
        if res == t.3 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.3, res
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
