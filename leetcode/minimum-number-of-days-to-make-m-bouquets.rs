// 1482. Minimum Number of Days to Make m Bouquets
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    /// Binary search a number of days in which enough flowers have bloomed that we can make m
    /// bouquets of k flowers each.
    ///
    /// Time complexity: O(n*log(max(bloom_day))) - We binary search a number of days that we
    /// can use between 0 and the biggest value in bloom_day, each time that we test a value we
    /// iterate the entire input vector and we split the search space in two.
    /// Space complexity: O(1) - We store and pass around pointers and integers.
    ///
    /// Runtime 22 ms Beats 100%
    /// Memory 4.08 MB Beats 50%
    pub fn min_days(bloom_day: Vec<i32>, m: i32, k: i32) -> i32 {
        let n = bloom_day.len() as i32;
        if m * k > n {
            return -1;
        }
        fn can_make_m_bouquets_in_t_days(t: &i32, k: i32, m: i32, flowers: &Vec<i32>) -> bool {
            let mut total = 0;
            let mut cur = 0;
            for flower in flowers {
                if flower <= t {
                    cur += 1;
                    if cur == k {
                        total += 1;
                        cur = 0;
                        if total == m {
                            return true;
                        }
                    }
                } else {
                    cur = 0;
                }
            }
            false
        }
        // Worst case, we use all the flowers and take max(bloom_day) days.
        let (mut left, mut right) = (0, *bloom_day.iter().max().unwrap());
        let mut t;
        while left < right {
            t = (left + right) / 2;
            if can_make_m_bouquets_in_t_days(&t, k, m, &bloom_day) {
                right = t;
            } else {
                left = t + 1;
            }
        }
        left
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 10, 3, 10, 2], 3, 1, 3),
        (vec![1, 10, 3, 10, 2], 3, 2, -1),
        (vec![7, 7, 7, 7, 12, 7, 7], 2, 3, 12),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_days(t.0.clone(), t.1, t.2);
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
