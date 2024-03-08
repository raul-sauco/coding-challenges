// 3005. Count Elements With Maximum Frequency
// 🟢 Easy
//
// https://leetcode.com/problems/count-elements-with-maximum-frequency/
//
// Tags: Array - Hash Table - Counting

struct Res {
    freq: usize,
    count: usize,
}

struct Solution;
impl Solution {
    /// Use bucket sort while keeping track of the count of elements with maximum frequency.
    ///
    /// Time complexity: O(n) - We visit each element and then the 100 buckets, it can be seen as
    /// o(1) since it is limited to 100 values.
    /// Space complexity: O(n) - The buckets array, it can be seen as O(1) because size is fixed.
    ///
    /// Runtime 2 ms Beats 53.64%
    /// Memory 2.04 MB Beats 95.45%
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut buckets = [0; 101];
        let mut res = Res { freq: 0, count: 0 };
        let mut freq;
        for num in nums {
            buckets[num as usize] += 1;
            freq = buckets[num as usize];
            if freq > res.freq {
                res.freq = freq;
                res.count = freq;
            } else if freq == res.freq {
                res.count += freq;
            }
        }
        res.count as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 4, 5], 5),
        (vec![1, 2, 2, 3, 1, 4], 4),
        (vec![1, 1, 1, 1, 1, 1], 6),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_frequency_elements(t.0.clone());
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
