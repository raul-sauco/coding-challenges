// 948. Bag of Tokens
// 🟠 Medium
//
// https://leetcode.com/problems/bag-of-tokens/
//
// Tags: Array - Two Pointers - Greedy - Sorting

struct Solution;
impl Solution {
    /// Sort the input, after that greedily iterate over the tokens checking the token at both ends
    /// of the vector, if we have enough remaining power to play the token on the left, do it and
    /// gain one point, otherwise play the token on the right and gain that much power. On each
    /// loop, we check if there are remaining tokens and if our score has gone negative. Return the
    /// maximum amount of points seen.
    ///
    /// Time complexity: O(n*log(n)) - We need to sort the input, after that, O(n)
    /// Space complexity: O(n) - Sorting the input vector and the local copy.
    ///
    /// Runtime 1 ms Beats 100%
    /// Memory 2.08 MB Beats 100%
    pub fn bag_of_tokens_score(mut tokens: Vec<i32>, power: i32) -> i32 {
        let n = tokens.len() as i32;
        tokens.sort_unstable();
        let mut power = power;
        let mut points = 0;
        let mut res = 0;
        let (mut l, mut r) = (0, n - 1);
        while l <= r && points >= 0 {
            if tokens[l as usize] <= power {
                points += 1;
                power -= tokens[l as usize];
                l += 1;
            } else {
                points -= 1;
                power += tokens[r as usize];
                r -= 1;
            }
            res = res.max(points);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![100], 50, 0),
        (vec![200, 100], 150, 1),
        (vec![71, 55, 82], 54, 0),
        (vec![100, 200, 300, 400], 200, 2),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::bag_of_tokens_score(t.0.clone(), t.1);
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
