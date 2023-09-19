// 287. Find the Duplicate Number
// 🟠 Medium
//
// https://leetcode.com/problems/find-the-duplicate-number/
//
// Tags: Array - Two Pointers - Binary Search - Bit Manipulation

struct Solution;
impl Solution {
    /// View the vector of values as pointers in a linked list. Each value will
    /// point to a node in the linked list, except for the two repeated values
    /// that will point to the same node, creating a cycle. Once we know that,
    /// we can use Floyd's cycle detection algorithm to solve the problem using
    /// linear time and constant memory.
    ///
    /// Time complexity: O(n) - Linear time complexity.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 16 ms Beats 21.90%
    /// Memory 4 MB Beats 20.95%
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let nums = nums.iter().map(|x| *x as usize).collect::<Vec<usize>>();
        let (mut slow, mut fast) = (nums[0], nums[nums[0]]);
        while slow != fast {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        // Reuse the slow pointer.
        slow = 0;
        while slow != fast {
            slow = nums[slow];
            fast = nums[fast];
        }
        slow as i32
    }
}

// Tests.
fn main() {
    let tests = [(vec![1, 3, 4, 2, 2], 2), (vec![3, 1, 3, 4, 2], 3)];
    for t in tests {
        assert_eq!(Solution::find_duplicate(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
