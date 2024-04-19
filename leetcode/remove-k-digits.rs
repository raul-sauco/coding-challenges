// 402. Remove K Digits
// 🟠 Medium
//
// https://leetcode.com/problems/remove-k-digits/
//
// Tags: String - Stack - Greedy - Monotonic Stack

struct Solution;
impl Solution {
    /// We need to make the most significant digits as small as possible, we can use a
    /// non-decreasing monotonic stack, before pushing each digit into the stack, pop anything that
    /// is greater, that guarantees that the most significant positions are minimized. We need to
    /// handle leading zeroes, we could do it by converting to int then back to string or skipping
    /// any leading zeroes before we return. We also need to handle empty results to return "0"
    /// instead of "".
    ///
    /// Time complexity: O(n) - We visit each position once and do amortized O(1) work for each.
    /// Space complexity: O(n) - The monotonic stack.
    ///
    /// Runtime 1 ms Beats 81%
    /// Memory 2.37 MB Beats 63%
    #[allow(dead_code)]
    pub fn remove_kdigits_stack(num: String, k: i32) -> String {
        let n = num.len();
        let mut k = k as usize;
        if k >= n {
            return "0".to_string();
        }
        let mut stack = Vec::with_capacity(n);
        for c in num.chars() {
            while k > 0 && !stack.is_empty() && c < *stack.last().unwrap() {
                stack.pop();
                k -= 1;
            }
            stack.push(c);
        }
        while k > 0 {
            if stack.is_empty() {
                return "0".to_string();
            }
            stack.pop();
            k -= 1;
        }
        let mut i = 0;
        while stack[i] == '0' && i < stack.len() - 1 {
            i += 1;
        }
        stack.into_iter().skip(i).collect::<String>()
    }

    /// Same logic but use the fact that Strings are mutable to construct the result directly.
    ///
    /// Time complexity: O(n) - We visit each position once and do amortized O(1) work for each.
    /// Space complexity: O(n) - The monotonic stack.
    ///
    /// Runtime 1 ms Beats 81%
    /// Memory 2.63 MB Beats 63%
    #[allow(dead_code)]
    pub fn remove_kdigits_string(num: String, k: i32) -> String {
        let n = num.len();
        let mut k = k as usize;
        if k >= n {
            return "0".to_string();
        }
        if k == 0 {
            return num;
        }
        let mut res = String::with_capacity(n);
        for c in num.chars() {
            while k > 0 && !res.is_empty() && c < res.chars().last().unwrap() {
                res.pop();
                k -= 1;
            }
            // Avoid pushing leading zeroes.
            if res.is_empty() && c == '0' {
                continue;
            }
            res.push(c);
        }
        for _ in 0..k {
            res.pop();
        }
        if res.is_empty() {
            res.push('0');
        }
        res
    }

    /// Neat idea but if fails in LeetCode because of the size of the tests inputs. The biggest
    /// integer value in the Rust std is u128 and the tests have, at least, 2500 positions.
    #[allow(dead_code)]
    pub fn remove_kdigits(num: String, k: i32) -> String {
        let (res, k) = num
            .chars()
            .map(|d| d.to_digit(10).unwrap())
            .fold((0, k), |(acc, k), d| {
                let mut k = k;
                let mut acc = acc;
                while k > 0 && d < acc % 10 {
                    acc /= 10;
                    k -= 1;
                }
                (acc * 10 + d, k)
            });
        (res / if k > 0 { 10u32.pow(k as u32) } else { 1 }).to_string()
    }
}

// Tests.
fn main() {
    let tests = [
        ("10", 2, "0"),
        ("10200", 2, "0"),
        ("10200", 1, "200"),
        ("1432219", 5, "11"),
        ("1432219", 3, "1219"),
        ("1111111", 3, "1111"),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::remove_kdigits(t.0.to_string(), t.1);
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
