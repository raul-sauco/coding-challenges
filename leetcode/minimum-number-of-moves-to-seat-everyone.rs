// 2037. Minimum Number of Moves to Seat Everyone
// 🟢 Easy
//
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
//
// Tags: Array - Greedy - Sorting

struct Solution;
impl Solution {
    /// Sort both input strings, then compare the elements one to one and add the absolute
    /// difference between each pair of elements at the same indexes to the result.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the highest time complexity. O(n) after.
    /// Space complexity: O(n) - The local mutable copy of the input. If we are OK with mutating
    /// the input, which should be OK because we are taking ownership, then it would be whatever
    /// extra memory the sorting algorithm takes. Currently, `sort_unstable` uses a pattern
    /// defeating quicksort that uses O(log(n)) extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.07 MB Beats 80%
    pub fn min_moves_to_seat(seats: Vec<i32>, students: Vec<i32>) -> i32 {
        let mut seats = seats;
        let mut students = students;
        seats.sort_unstable();
        students.sort_unstable();
        seats
            .iter()
            .zip(students.iter())
            .map(|(x, y)| (x - y).abs())
            .sum::<i32>()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3, 1, 5], vec![2, 7, 4], 4),
        (vec![4, 1, 5, 9], vec![1, 3, 2, 6], 7),
        (vec![2, 2, 6, 6], vec![1, 3, 2, 6], 4),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_moves_to_seat(t.0.clone(), t.1.clone());
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
