// 350. Intersection of Two Arrays II
// 🟢 Easy
//
// https://leetcode.com/problems/intersection-of-two-arrays-ii/
//
// Tags: Array - Hash Table - Two Pointers - Binary Search - Sorting

struct Solution;
impl Solution {
    /// Count the elements in one ef the input vectors, then iterate over the other one, for each
    /// element, check if the count in the counter is greater than 0, if it is, add the element to
    /// the result and reduce the count by 1.
    ///
    /// Time complexity: O(m+n) - We visit each element in both the input vectors.
    /// Space complexity: O(1) - An array of size 1000.
    ///
    /// Runtime 1 ms Beats 70%
    /// Memory 2.02 MB Beats 93%
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut counts = [0; 1001];
        for num in nums1 {
            counts[num as usize] += 1;
        }
        let mut res = vec![];
        for num in nums2 {
            if counts[num as usize] > 0 {
                res.push(num);
                counts[num as usize] -= 1;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 2, 1], vec![2, 2], vec![2, 2]),
        (vec![4, 9, 5], vec![9, 4, 9, 8, 4], vec![9, 4]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::intersect(t.0.clone(), t.1.clone());
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
