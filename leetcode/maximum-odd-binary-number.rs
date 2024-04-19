// 2864. Maximum Odd Binary Number
// 🟢 Easy
//
// https://leetcode.com/problems/maximum-odd-binary-number/
//
// Tags: Math - String - Greedy

struct Solution;
impl Solution {
    /// One solution is to use two pointers, move all 1s to the left and all 0s to the right, then
    /// swap the rightmost 1 with the zero at the last position of the vector.
    ///
    /// Time complexity: O(n) - Two pointers.
    /// Space complexity: O(n) - The vector that we use to access and swap by index.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.13 MB Beats 29.17%
    pub fn maximum_odd_binary_number(s: String) -> String {
        let n = s.len();
        let mut s = s.chars().collect::<Vec<_>>();
        let (mut l, mut r) = (0, n - 1);
        while l < r {
            match (s[l], s[r]) {
                ('1', '1') => l += 1,
                ('0', '0') => r -= 1,
                ('1', '0') => {
                    l += 1;
                    r -= 1;
                }
                _ => {
                    s.swap(l, r);
                    l += 1;
                    r -= 1;
                }
            }
        }
        if s[l] == '1' {
            s.swap(l, n - 1);
        } else {
            s.swap(l - 1, n - 1);
        }
        s.into_iter().collect::<String>()
    }
}

// Tests.
fn main() {
    let tests = [("1", "1"), ("010", "001"), ("0101", "1001")];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_odd_binary_number(t.0.to_string());
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
