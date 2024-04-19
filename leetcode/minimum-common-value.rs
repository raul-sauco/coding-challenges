// 2540. Minimum Common Value
// 🟢 Easy
//
// https://leetcode.com/problems/minimum-common-value/
//
// Tags: Array - Hash Table - Two Pointers - Binary Search

struct Solution;
impl Solution {
    /// Two pointers, start at index 0 in both vectors, compare the values and shift forwards the
    /// pointer that has the smaller value under it, if the values are the same at some point,
    /// return that value, if we get to the end of any of the vectors, return -1.
    ///
    /// Time complexity: O(m+n) - We will visit each element in both input vectors.
    /// Space complexity: O(1) - We only store two pointers.
    ///
    /// Runtime 7 ms Beats 80.95%
    /// Memory 3.92 MB Beats 52.38%
    #[allow(dead_code)]
    pub fn get_common_match(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let (m, n) = (nums1.len(), nums2.len());
        let (mut a, mut b) = (0, 0);
        while a < m && b < n {
            match nums1[a].cmp(&nums2[b]) {
                std::cmp::Ordering::Less => a += 1,
                std::cmp::Ordering::Equal => return nums1[a],
                std::cmp::Ordering::Greater => b += 1,
            }
        }
        -1
    }

    /// Exact same logic as the previous version, I expected this to run exactly the same as the
    /// previous solution but it runs faster, it would be interesting to look at the assembly to
    /// see why, in theory the match should be a zero cost abstraction.
    ///
    /// Time complexity: O(m+n) - We will visit each element in both input vectors.
    /// Space complexity: O(1) - We only store two pointers.
    ///
    /// Runtime 3 ms Beats 100%
    /// Memory 3.89 MB Beats 80.95%
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let (mut a, mut b) = (0, 0);
        while a < nums1.len() && b < nums2.len() {
            if nums1[a] == nums2[b] {
                return nums1[a];
            }
            if nums1[a] < nums2[b] {
                a += 1;
            } else {
                b += 1;
            }
        }
        -1
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3], vec![2, 4], 2),
        (vec![1, 2, 3], vec![20, 45], -1),
        (vec![1, 2, 3, 6], vec![2, 3, 4, 5], 2),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::get_common(t.0.clone(), t.1.clone());
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
