// 1052. Grumpy Bookstore Owner
// 🟠 Medium
//
// https://leetcode.com/problems/grumpy-bookstore-owner/
//
// Tags: Array - Sliding Window

struct Solution;
impl Solution {
    /// Use a sliding window that counts the extra safisfied customers we can have using the boost
    /// during a given window. Return the sum of happy customers we get from the minutes the owner
    /// is not grumpy plus the extra gain from the "artificially happy" window.
    ///
    /// Time complexity: O(n)
    /// Space complexity: O(1)
    ///
    /// Runtime 2 ms Beats 100%
    /// Memory 2.33 MB Beats 50%
    pub fn max_satisfied(customers: Vec<i32>, grumpy: Vec<i32>, minutes: i32) -> i32 {
        let (m, n) = (minutes as usize, customers.len());
        let mut max_gain: i32 = (0..m)
            .map(|i| if grumpy[i] == 1 { customers[i] } else { 0 })
            .sum();
        // let mut max_gain = customers
        //     .iter()
        //     .zip(grumpy.iter())
        //     .take(m)
        //     .fold(0, |acc, (c, g)| if *g == 1 { acc + c } else { acc });
        let mut gain = max_gain;
        let mut left;
        for right in m..n {
            left = right - m;
            if grumpy[right] == 1 {
                gain += customers[right];
            }
            if grumpy[left] == 1 {
                gain -= customers[left];
            }
            max_gain = max_gain.max(gain);
        }
        customers
            .iter()
            .zip(grumpy.iter())
            .map(|(c, g)| if *g == 0 { *c } else { 0 })
            .sum::<i32>()
            + max_gain
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], vec![0], 1, 1),
        (
            vec![1, 0, 1, 2, 1, 1, 7, 5],
            vec![0, 1, 0, 1, 0, 1, 0, 1],
            3,
            16,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_satisfied(t.0.clone(), t.1.clone(), t.2);
        if res == t.3 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.3, res
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
