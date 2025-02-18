// 2375. Construct Smallest Number From DI String
// 🟠 Medium
//
// https://leetcode.com/problems/construct-smallest-number-from-di-string/
//
// Tags: String - Backtracking - Stack - Greedy

struct Solution;
impl Solution {
    /// Use a backtracking approach, start trying the available digits from the smallest to
    /// greatest, that guarantees that the first solution we find will be the smallest
    /// lexicographically. Iterate over the available digits checking if they match the increasing
    /// or decreasing requirement, if they do, call the recursive function with that digit, return
    /// the first valid solution we find.
    ///
    /// Time  complexity: O(8^n) - Worst case scenario we will try each available digit in every
    /// level and the first match will be the last combination we try.
    /// Space complexity: O(1) - We store two vectors of size 8 for each level and have a max of 8
    /// levels in the call stack.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.33 MB Beats 33%
    pub fn smallest_number(pattern: String) -> String {
        fn bt(
            i: usize,
            cur: &Vec<char>,
            pattern: &Vec<char>,
            available: Vec<char>,
        ) -> Option<Vec<char>> {
            if i >= pattern.len() {
                return Some(cur.to_vec());
            }
            let mut next = cur.iter().map(|&c| c).collect::<Vec<_>>();
            for digit in available.iter() {
                match cur.last().unwrap().cmp(digit) {
                    std::cmp::Ordering::Less => {
                        if pattern[i] == 'D' {
                            continue;
                        }
                    }
                    std::cmp::Ordering::Equal => unreachable!(),
                    std::cmp::Ordering::Greater => {
                        if pattern[i] == 'I' {
                            continue;
                        }
                    }
                }
                // The digit complies with the requirements.
                next.push(*digit);
                match bt(
                    i + 1,
                    &next,
                    pattern,
                    available
                        .iter()
                        .filter(|&x| x != digit)
                        .map(|c| *c)
                        .collect::<Vec<_>>(),
                ) {
                    Some(v) => return Some(v),
                    None => (),
                }
                next.pop();
            }
            None
        }
        let digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
        let pattern = pattern.chars().collect::<Vec<_>>();
        for digit in digits.iter() {
            match bt(
                0,
                &vec![*digit],
                &pattern,
                digits
                    .iter()
                    .filter(|&x| x != digit)
                    .map(|c| *c)
                    .collect::<Vec<_>>(),
            ) {
                Some(v) => return v.iter().collect::<String>(),
                None => (),
            }
        }
        "".to_string()
    }
}

// Tests.
fn main() {
    let tests = [("IIIDIDDD", "123549876"), ("DDD", "4321")];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::smallest_number(t.0.to_string());
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
