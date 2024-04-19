// 977. Squares of a Sorted Array
// 🟢 Easy
//
// https://leetcode.com/problems/squares-of-a-sorted-array/
//
// Tags: Array - Two Pointers - Sorting

struct Solution;
impl Solution {
    /// Navive solution works. Get a vector of the squares and sort it.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the vector of length n.
    /// Space complexity: O(n) - The extra vector.
    ///
    /// Runtime 5 ms Beats 81.35%
    /// Memory 2.23 MB Beats 78.76%
    #[allow(dead_code)]
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let mut sq = nums.into_iter().map(|x| x.pow(2)).collect::<Vec<_>>();
        sq.sort_unstable();
        sq
    }

    /// Linear time solution, use two pointers from both ends of the array to find the next biggest
    /// square and place it in its position in the result.
    ///
    /// Time complexity: O(n) - We are using a two-pointer algorithm, we will visit each position
    /// once and do constant work for each.
    /// Space complexity: O(n) - The extra vector.
    ///
    /// Runtime 3 ms Beats 97.41%
    /// Memory 2.25 MB Beats 78.76%
    pub fn sorted_squares_tp(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        // if n == 1 || nums[0] >= 0 {
        //     return nums.into_iter().map(|x| x.pow(2)).collect();
        // }
        let mut sq = vec![0; n];
        let (mut l, mut r) = (0, n - 1);
        let mut sql = nums[l].pow(2);
        let mut sqr = nums[r].pow(2);
        loop {
            // Important to move l when equal, otherwise we could overflow r-1 when r==0.
            if sqr > sql {
                sq[r - l] = sqr;
                r -= 1;
                if l <= r {
                    sqr = nums[r].pow(2);
                } else {
                    break;
                }
            } else {
                sq[r - l] = sql;
                l += 1;
                if l <= r {
                    sql = nums[l].pow(2);
                } else {
                    break;
                }
            }
        }
        sq
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], vec![1]),
        (vec![-5, -3, -2, -1], vec![1, 4, 9, 25]),
        (vec![0, 3, 4, 6, 10], vec![0, 9, 16, 36, 100]),
        (vec![-4, -1, 0, 3, 10], vec![0, 1, 9, 16, 100]),
        (vec![-7, -3, 2, 3, 11], vec![4, 9, 9, 49, 121]),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::sorted_squares_tp(t.0.clone());
        if res == t.1 {
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
