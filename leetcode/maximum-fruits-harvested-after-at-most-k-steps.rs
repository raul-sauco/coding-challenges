// 2106. Maximum Fruits Harvested After at Most K Steps
// 🔴 Hard
//
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
//
// Tags: Array - Binary Search - Sliding Window - Prefix Sum

struct Solution;
impl Solution {
    /// We can precompute the prefix sums of going left and right, then use a sliding window to
    /// check the gains of taking x steps to the left and the available ones to the right and
    /// viceversa.
    ///
    /// Time complexity: O(n) - All the operations run in linear time.
    /// Space complexity: O(n) - The prefix sum vectors will have at most size n.
    ///
    /// Runtime 6 ms Beats 100%
    /// Memory 9.74 MB Beats 100%
    pub fn max_total_fruits(fruits: Vec<Vec<i32>>, start_pos: i32, k: i32) -> i32 {
        let n = fruits.len();
        let insert_index = match fruits.binary_search_by(|v| v[0].cmp(&start_pos)) {
            Ok(idx) => idx,
            Err(idx) => idx,
        };
        let mut prefix_sum_left = Vec::with_capacity(insert_index + 1);
        let mut total = 0;
        for i in 0..=insert_index {
            let fi = insert_index - i;
            if fi == n || fruits[fi][0] > start_pos {
                continue;
            }
            total += fruits[fi][1];
            let steps = start_pos - fruits[fi][0];
            if steps > k {
                break;
            }
            prefix_sum_left.push((steps, total));
        }
        let mut prefix_sum_right = Vec::with_capacity(n - insert_index);
        total = 0;
        for i in insert_index..n {
            total += fruits[i][1];
            let steps = fruits[i][0] - start_pos;
            if steps > k {
                break;
            }
            prefix_sum_right.push((steps, total));
        }
        // Account for double counting the fruit at the start position.
        let penalty = if insert_index < n && fruits[insert_index][0] == start_pos {
            fruits[insert_index][1]
        } else {
            0
        };
        let mut res = 0;
        // Check the options starting going left.
        let mut r = prefix_sum_right.len();
        if r > 0 {
            r -= 1;
        }
        for &(steps, gain) in prefix_sum_left.iter() {
            let steps_right = k - 2 * steps;
            while r > 0 && prefix_sum_right[r].0 > steps_right {
                r -= 1;
            }
            total = gain;
            if prefix_sum_right.len() > 0 && prefix_sum_right[r].0 <= steps_right {
                total += prefix_sum_right[r].1;
            }
            res = res.max(total - penalty);
        }
        // Check the options going right.
        let mut l = prefix_sum_left.len();
        if l > 0 {
            l -= 1;
        }
        for &(steps, gain) in prefix_sum_right.iter() {
            let steps_left = k - 2 * steps;
            while l > 0 && prefix_sum_left[l].0 > steps_left {
                l -= 1;
            }
            total = gain;
            if prefix_sum_left.len() > 0 && prefix_sum_left[l].0 <= steps_left {
                total += prefix_sum_left[l].1;
            }
            res = res.max(total - penalty);
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![[2, 8], [6, 3], [8, 6]], 5, 4, 9),
        (
            vec![[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]],
            5,
            4,
            14,
        ),
        (vec![[0, 3], [6, 4], [8, 5]], 3, 2, 0),
        (vec![[200000, 10000]], 0, 200000, 10000),
        (vec![[0, 10000]], 200000, 200000, 10000),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::max_total_fruits(t.0.iter().map(|a| a.to_vec()).collect(), t.1, t.2);
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
