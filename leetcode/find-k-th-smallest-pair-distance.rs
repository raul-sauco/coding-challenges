// 719. Find K-th Smallest Pair Distance
// 🔴 Hard
//
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/
//
// Tags: Array - Two Pointers - Binary Search - Sorting

struct Solution;
impl Solution {
    /// Use binary search to try different values of the difference, for each value, use a sliding
    /// window approach to count how many pairs' difference are below that value in linear time,
    /// then adjust the test value in the binary search according to the number of pairs.
    ///
    /// Time complexity: O(nlog(n)+nlog(m)) - Where m is the binary search space betwwen 0 and the greatest
    /// difference between elements in the input vector. For each try on the binary search, we call
    /// the count_pairs function that works in linear time. Sorting the input vector takes nlog(n).
    /// Space complexity: O(log(n)) - Unstable sorting in Rust takes log(n) with the current
    /// version. Everything else uses constant extra memory.
    ///
    /// Runtime 2 ms Beats 100%
    /// Memory 2.15 MB Beats 100%
    pub fn smallest_distance_pair(mut nums: Vec<i32>, k: i32) -> i32 {
        fn count_pairs(nums: &Vec<i32>, max_distance: i32) -> usize {
            let mut count = 0;
            let n = nums.len();
            let mut left = 0;
            for right in 0..n {
                while nums[right] - nums[left] > max_distance {
                    left += 1;
                }
                count += right - left;
            }
            count
        }
        let k = k as usize;
        nums.sort_unstable();
        let (mut low, mut high) = (0, *nums.last().expect("non empty vector") - nums[0]);
        let (mut mid, mut count);
        while low < high {
            mid = (low + high) / 2;
            count = count_pairs(&nums, mid);
            if count < k {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        low as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 3, 1], 1, 0),
        (vec![1, 1, 1], 2, 0),
        (vec![1, 6, 1], 3, 5),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::smallest_distance_pair(t.0.clone(), t.1);
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
