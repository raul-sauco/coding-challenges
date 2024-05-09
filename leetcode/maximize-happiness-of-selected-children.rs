// 3075. Maximize Happiness of Selected Children
// 🟠 Medium
//
// https://leetcode.com/problems/maximize-happiness-of-selected-children/
//
// Tags: Array - Greedy - Sorting

struct Solution;
impl Solution {
    /// Sort the input, then greedily start choosing the largest values all the while subtracting
    /// the number of values that we have chosen already to the result if not negative.
    ///
    /// Time complexity: O(n*log(n)) - We sort the input values, after that O(k)
    /// Space complexity: O(1) - We mutate the input.
    ///
    /// Runtime 19 ms Beats 97%
    /// Memory 5.11 MB Beats 86%
    pub fn maximum_happiness_sum(mut happiness: Vec<i32>, k: i32) -> i64 {
        happiness.sort_unstable_by(|a, b| b.cmp(a));
        happiness[..k as usize]
            .iter()
            .enumerate()
            .fold(0, |acc, (i, x)| acc + 0.max(*x as i64 - i as i64))
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![12, 1, 42], 3, 53),
        (vec![1, 2, 3], 2, 4),
        (vec![1, 1, 1, 1], 2, 1),
        (vec![2, 3, 4, 5], 1, 5),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_happiness_sum(t.0.clone(), t.1);
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
