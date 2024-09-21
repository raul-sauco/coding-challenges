// 386. Lexicographical Numbers
// 🟠 Medium
//
// https://leetcode.com/problems/lexicographical-numbers/
//
// Tags: Depth-First Search - Trie

struct Solution;
impl Solution {
    /// Generate the most significant digits first starting by 1, move to higher digits once the
    /// units reach 9 or we go over n.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(1)
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.76 MB Beats 18%
    pub fn lexical_order(n: i32) -> Vec<i32> {
        let n = n as usize;
        let mut num = 1;
        let mut res = vec![];
        for _ in 0..n {
            res.push(num as i32);
            if num * 10 <= n {
                num *= 10;
            } else {
                while num % 10 == 9 || num >= n {
                    num /= 10;
                }
                num += 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (2, vec![1, 2]),
        (13, vec![1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::lexical_order(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
                i, t.1, res
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
