// 1700. Number of Students Unable to Eat Lunch
// 🟢 Easy
//
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
//
// Tags: Array - Stack - Queue - Simulation

struct Solution;
impl Solution {
    /// Count the number of zero and one students, then iterate over the sandwitches assigning
    /// sandwitches to students until we have a sandwitch type that we don't have students for.
    ///
    /// Time complexity: O(n) - Visit each element and do constant time work.
    /// Space complexity: O(1) - Store two i32 values.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.06 MB Beats 83%
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let (mut zeroes, mut ones) = students.iter().fold((0, 0), |acc, x| {
            if *x == 0 {
                (acc.0 + 1, acc.1)
            } else {
                (acc.0, acc.1 + 1)
            }
        });
        for i in 0..sandwiches.len() {
            if sandwiches[i] == 0 {
                if zeroes == 0 {
                    return (sandwiches.len() - i) as i32;
                } else {
                    zeroes -= 1;
                }
            } else {
                if ones == 0 {
                    return (sandwiches.len() - i) as i32;
                } else {
                    ones -= 1;
                }
            }
        }
        0
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 1, 0, 0], vec![0, 1, 0, 1], 0),
        (vec![1, 1, 1, 1], vec![0, 1, 0, 1], 4),
        (vec![1, 1, 1, 0, 0, 1], vec![1, 0, 0, 0, 1, 1], 3),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::count_students(t.0.clone(), t.1.clone());
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
