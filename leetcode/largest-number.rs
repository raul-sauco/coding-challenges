// 179. Largest Number
// 🟠 Medium
//
// https://leetcode.com/problems/largest-number/
//
// Tags: Array - String - Greedy - Sorting

struct Solution;
impl Solution {
    /// Since the length of the string is fixed, we can greedily pick the number that is going to
    /// result in a highest value at the leftmost positions, we convert the numbers to string and
    /// sort them based on the result that we obtain combining them in pairs, for example, given 3,
    /// 34, we sort them based on "334" vs "343".
    ///
    /// Time complexity: O(nlog(n)) - Sorting the strings has the highest time complexity.
    /// Space complexity: O(n) - For the strings vector and the sorting algorithm.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.17 MB Beats 58%
    pub fn largest_number(nums: Vec<i32>) -> String {
        let mut nums = nums.iter().map(|x| x.to_string()).collect::<Vec<_>>();
        nums.sort_unstable_by(|a, b| format!("{b}{a}").cmp(&format!("{a}{b}")));
        if nums[0] == "0" {
            "0".to_string()
        } else {
            nums.join("")
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![0], "0"),
        (vec![0, 0], "0"),
        (vec![10, 2], "210"),
        (vec![3, 30, 34, 5, 9], "9534330"),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::largest_number(t.0.clone());
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
