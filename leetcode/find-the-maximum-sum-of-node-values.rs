// 3068. Find the Maximum Sum of Node Values
// 🔴 Hard
//
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
//
// Tags: Array - Dynamic Programming - Greedy - Bit Manipulation - Tree - Sorting

struct Solution;
impl Solution {
    /// The main observation is that we can xor any pairs we choose by consecutively xor-ing all
    /// nodes between them. Once we deduce that, we can compute the gains that we can obtain from
    /// xor-ing any two nodes and xor any pairs that give us a positive gain.
    ///
    /// Time complexity: O(n*log(n)) - We visit each value to compute the gains that we can get
    /// from xor-ing that one value with k. Then we sort the gains vector.
    /// Space complexity: O(n) - We store a mutable copy of the nums to sort and go through.
    ///
    /// Runtime 29 ms Beats 100%
    /// Memory 3.72 MB Beats 100%
    pub fn maximum_value_sum(nums: Vec<i32>, k: i32, _edges: Vec<Vec<i32>>) -> i64 {
        let mut gains = nums.iter().map(|x| (x ^ k) - x).collect::<Vec<_>>();
        gains.sort_unstable_by(|a, b| b.cmp(&a));
        nums.iter().map(|&x| x as i64).sum::<i64>()
            + gains.chunks(2).fold(0, |acc, chunk| {
                if chunk.len() == 2 && chunk[0] + chunk[1] > 0 {
                    acc + (chunk[0] + chunk[1]) as i64
                } else {
                    acc
                }
            })
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 1], 3, vec![vec![0, 1], vec![0, 2]], 6),
        (vec![2, 3], 7, vec![vec![0, 1]], 9),
        (
            vec![7, 7, 7, 7, 7, 7],
            3,
            vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![0, 4], vec![0, 5]],
            42,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_value_sum(t.0.clone(), t.1, t.2.clone());
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
