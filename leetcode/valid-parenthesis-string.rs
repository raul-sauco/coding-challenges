// 678. Valid Parenthesis String
// 🟠 Medium
//
// https://leetcode.com/problems/valid-parenthesis-string/
//
// Tags: String - Dynamic Programming - Stack - Greedy

struct Solution;
impl Solution {
    /// Use memoized top-down dynamic programming, when we see a '*' character explore each of the
    /// three possibilities, '(', ')', and '*', if we see a ')' and don't have any characters in
    /// the stack, return false, if we get to the end of the input and the stack is empty, return
    /// true.
    ///
    /// Time complexity: O(n^2) - The dfs function can run at most n^2 times before having computed
    /// all possibilities.
    /// Space complexity: O(n^2) - The memo vector, the stack will grow to size n.
    ///
    /// Runtime 1 ms Beats 25%
    /// Memory 2.15 MB Beats 87%
    #[allow(dead_code)]
    pub fn check_valid_string_dp_memo(s: String) -> bool {
        let n = s.len();
        let s = s.chars().collect::<Vec<_>>();
        let mut memo: Vec<Vec<Option<bool>>> = vec![vec![None; n + 1]; n + 1];
        fn bt(i: usize, stack: usize, s: &Vec<char>, memo: &mut Vec<Vec<Option<bool>>>) -> bool {
            if let Some(res) = memo[i][stack] {
                return res;
            }
            if i == s.len() {
                memo[i][stack] = Some(stack == 0);
                return stack == 0;
            }
            match s[i] {
                '(' => {
                    memo[i][stack] = Some(bt(i + 1, stack + 1, s, memo));
                }
                ')' => {
                    if stack > 0 {
                        memo[i][stack] = Some(bt(i + 1, stack - 1, s, memo));
                    } else {
                        return false;
                    }
                }
                '*' => {
                    let open = bt(i + 1, stack + 1, s, memo);
                    let close = stack > 0 && bt(i + 1, stack - 1, s, memo);
                    let empty = bt(i + 1, stack, s, memo);
                    memo[i][stack] = Some(open || close || empty);
                }
                _ => unreachable!("Unexpected character"),
            }
            memo[i][stack].unwrap()
        }
        bt(0, 0, &s, &mut memo)
    }

    /// Count the range between the minimum and maximum close parentheses we can have for the
    /// string to be valid.
    ///
    /// Time complexity: O(n) - One pass, constant time per each character.
    /// Space complexity: O(1) - We only store two counters.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.12 MB Beats 87%
    pub fn check_valid_string(s: String) -> bool {
        let (mut max, mut min) = (0, 0);
        for c in s.chars() {
            max = if c == ')' { max - 1 } else { max + 1 };
            min = if c == '(' { min + 1 } else { 0.max(min - 1) };
            if max < 0 {
                return false;
            }
        }
        min == 0
    }
}

// Tests.
fn main() {
    let tests = [
        ("", true),
        ("(", false),
        (")", false),
        ("()", true),
        ("*)", true),
        ("(*)", true),
        ("(*(", false),
        ("(*))", true),
        ("**************************************************))))))))))))))))))))))))))))))))))))))))))))))))))", true),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::check_valid_string(t.0.to_string());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
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
