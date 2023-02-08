// 45. Jump Game II
// 🟠 Medium
//
// https://leetcode.com/problems/jump-game-ii/
//
// Tags: Array - Dynamic Programming - Greedy

struct Solution;
impl Solution {
    // Visit each element of the array but do it in groups, we can see it as
    // treating each group as a level and the algorithm as BFS. For each
    // level, keep track of the farthest position we could jump to from this
    // level. When we get to the end of the level, add one to the number of
    // jumps that we have taken, and update the current level by updating the
    // last element we can explore to match the farthest element we can
    // reach from this level.
    // The algorithm repeatedly calculates the farthest point we can reach
    // from any of the positions that we can reach given the current number
    // of jumps, then "jump" once more and continue calculating. Each element
    // is only explored once.
    //
    // Time complexity: O(n) - Each element is visited once.
    // Space complexity: O(1) - Constant space.
    //
    // Runtime 2 ms Beats 80%
    // Memory 2.1 MB Beats 71.3%
    pub fn jump(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut jumps = 0;
        let mut reach = 0;
        let mut next_reach = 0;
        for i in 0..n - 1 {
            let current_jump = i + nums[i] as usize;
            if current_jump > next_reach {
                next_reach = current_jump;
            }
            if next_reach >= n - 1 {
                return 1 + jumps as i32;
            }
            if i == reach {
                jumps += 1;
                reach = next_reach;
            }
        }
        jumps as i32
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::jump(vec![0]), 0);
    assert_eq!(Solution::jump(vec![2, 3, 1, 1, 4]), 2);
    assert_eq!(Solution::jump(vec![2, 3, 0, 1, 4]), 2);
    assert_eq!(Solution::jump(vec![2, 3, 0, 1, 4, 0, 0, 0, 2, 8, 7, 3]), 5);
    println!("All tests passed!")
}
