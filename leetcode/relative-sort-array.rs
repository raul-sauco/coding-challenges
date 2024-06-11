// 1122. Relative Sort Array
// 🟢 Easy
//
// https://leetcode.com/problems/relative-sort-array/
//
// Tags: Array - Hash Table - Sorting - Counting Sort

struct Solution;
impl Solution {
    /// Create a counts array with 1001 elements and count the frequency of elements in arr1, then
    /// iterate over the elements in arr2 using them to determine in which order to place the
    /// elements of arr1 in the result, we can get the count of each element from the counts array.
    /// Once we have placed all elements found in arr2, we iterate over all the indexes in counts
    /// in ascending order placing all the rest of the elements in the result vector.
    ///
    /// Time complexity: O(1) - We iterate over the elements in both arrays plus the 1000 elements
    /// in counts, m and n are capped at 1000 elements and counts has 1001 positions.
    /// Space complexity: O(1) - The counts array of size 1001;
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.06 MB Beats 100%
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        let n = arr1.len();
        let mut counts = [0; 1001];
        for num in arr1 {
            counts[num as usize] += 1;
        }
        let mut res = Vec::with_capacity(n);
        for num in arr2 {
            for _ in 0..counts[num as usize] {
                res.push(num);
            }
            counts[num as usize] = 0;
        }
        for (i, count) in counts.into_iter().enumerate() {
            for _ in 0..count {
                res.push(i as i32);
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
            vec![2, 1, 4, 3, 9, 6],
            vec![2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
        ),
        (
            vec![28, 6, 22, 8, 44, 17],
            vec![22, 28, 8, 6],
            vec![22, 28, 8, 6, 17, 44],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::relative_sort_array(t.0.clone(), t.1.clone());
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {:?}!!\x1b[0m",
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
