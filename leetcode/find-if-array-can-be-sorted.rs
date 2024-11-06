// 3011. Find if Array Can Be Sorted
// 🟠 Medium
//
// https://leetcode.com/problems/find-if-array-can-be-sorted/
//
// Tags: Array - Bit Manipulation - Sorting

struct Solution;
impl Solution {
    /// Group the values by the number of set bits using `count_ones()` then check that each
    /// group's max is less than the next group's min.
    ///
    /// Time complexity: O(n) - We iterate over the values three times, once to group them, once to
    /// get the min and one to get the max.
    /// Space complexity: O(n) - The max memory used will be a chunk size, which could be n if all
    /// the values in the input had the same number of set bits, since n <= 100, we could call it
    /// constant space.
    ///
    /// Runtime 2 ms Beats 100%
    /// Memory 2.16 MB Beats 100%
    #[allow(dead_code)]
    pub fn can_sort_array_loop(nums: Vec<i32>) -> bool {
        let mut last_max = i32::MIN;
        for chunk in nums.chunk_by(|a, b| a.count_ones() == b.count_ones()) {
            if let Some(&cur_min) = chunk.iter().min() {
                if cur_min < last_max {
                    return false;
                }
                last_max = *chunk.iter().max().unwrap();
            }
        }
        true
    }

    /// Same solution but compress everything into one iterator chain, use `try_fold()` to break
    /// early when we find a pair of chunks that cannot be sorted.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.17 MB Beats 100%
    #[allow(dead_code)]
    pub fn can_sort_array(nums: Vec<i32>) -> bool {
        nums.chunk_by(|a, b| a.count_ones() == b.count_ones())
            .try_fold(i32::MIN, |last_max, chunk| {
                if *chunk.iter().min()? < last_max {
                    None
                } else {
                    Some(*chunk.iter().max()?)
                }
            })
            .is_some()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![8, 4, 2, 30, 15], true),
        (vec![1, 2, 3, 4, 5], true),
        (vec![3, 16, 8, 4, 2], false),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::can_sort_array(t.0.clone());
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
