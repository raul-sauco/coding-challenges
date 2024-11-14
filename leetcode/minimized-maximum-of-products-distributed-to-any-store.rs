// 2064. Minimized Maximum of Products Distributed to Any Store
// 🟠 Medium
//
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    /// Use binary search to try the possible results and see if they work.
    ///
    /// Time complexity: O(log(max(q))*m) - We binary search the result, for each try, we
    /// iterate over all quantities spreading them between stores.
    /// Space complexity: O(1) - We use an outer while loop with three usize pointers and an
    /// inner iterator plus fold.
    ///
    /// Runtime 24 ms Beats 100%
    /// Memory 3.24 MB Beats 100%
    pub fn minimized_maximum(n: i32, quantities: Vec<i32>) -> i32 {
        let (mut left, mut right) = (1, *quantities.iter().max().unwrap());
        let mut mid;
        while left < right {
            mid = (left + right) / 2;
            // How many buckets do we need to spread this quantity at this spread rate?
            if quantities
                .iter()
                .fold(0, |acc, x| acc + ((x + mid - 1) / mid))
                > n
            {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        left as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (6, vec![11, 6], 3),
        (7, vec![15, 10, 10], 5),
        (1, vec![100000], 100000),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::minimized_maximum(t.0, t.1.clone());
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
