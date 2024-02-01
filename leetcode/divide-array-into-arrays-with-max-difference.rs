// 2966. Divide Array Into Arrays With Max Difference
// 🟠 Medium
//
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
//
// Tags: Array - Greedy - Sorting

struct Solution;
impl Solution {
    /// Sort the input, then pick groups of three and check if the difference between the first and
    /// last element is equal or less than k.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the input array has the highest time complexity,
    /// after that preparatory sorting step, the algorithm runs in O(n)
    /// Space complexity: O(n) - The sorted copy of the input takes n space.
    ///
    /// Runtime 56 ms Beats 70.67%
    /// Memory 5.66 MB Beats 29.33%
    #[allow(dead_code)]
    pub fn divide_array_for(nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        if nums.len() % 3 != 0 {
            return vec![];
        }
        let mut nums = nums;
        nums.sort_unstable();
        let mut res = vec![];
        let mut i = 0;
        let mut slc;
        while i < nums.len() - 1 {
            slc = nums[i..i + 3].to_vec();
            if slc[2] - slc[0] > k {
                return vec![];
            }
            res.push(slc);
            i += 3;
        }
        res
    }

    /// Same logic but use iterators and a flag, this solution uses extra space, storing the result
    /// temporarily, to avoid having to iterate the input twice.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the input array has the highest time complexity,
    /// after that preparatory sorting step, the algorithm runs in O(n)
    /// Space complexity: O(n) - The sorted copy of the input takes n space.
    ///
    /// Runtime 56 ms Beats 70.67%
    /// Memory 5.28 MB Beats 81.33%
    #[allow(dead_code)]
    pub fn divide_array_flag(mut nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        let mut comply = true;
        let res = nums
            .chunks(3)
            .map(|c| {
                if c[2] - c[0] > k {
                    comply = false;
                }
                c.to_vec()
            })
            .collect();
        if comply {
            return res;
        }
        vec![]
    }

    /// Same logic again, two passes, one to check if the chunks satisfy the given condition, the
    /// second one to return the result if they do. Sacrifices time to save memory usage.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the input array has the highest time complexity,
    /// after that preparatory sorting step, the algorithm runs in O(n)
    /// Space complexity: O(n) - The sorted copy of the input takes n space.
    ///
    /// Runtime 57 ms Beats 69.33%
    /// Memory 5.07 MB Beats 98.67%
    pub fn divide_array(mut nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        if nums.chunks(3).any(|c| c[2] - c[0] > k) {
            return vec![];
        }
        nums.chunks(3).map(|c| c.to_vec()).collect()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 3, 3, 2, 7, 3], 3, vec![]),
        (
            vec![1, 3, 4, 8, 7, 9, 3, 5, 1],
            2,
            vec![vec![1, 1, 3], vec![3, 4, 5], vec![7, 8, 9]],
        ),
        (
            vec![
                15, 13, 12, 13, 12, 14, 12, 2, 3, 13, 12, 14, 14, 13, 5, 12, 12, 2, 13, 2, 2,
            ],
            2,
            vec![],
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::divide_array(t.0.clone(), t.1);
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
