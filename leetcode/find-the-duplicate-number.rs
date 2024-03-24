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
    /// Runtime 11 ms Beats 59%
    /// Memory 4 MB Beats 24%
    #[allow(dead_code)]
    pub fn find_duplicate_cast(nums: Vec<i32>) -> i32 {
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

    /// Same logic but do not modify the input vector to cast to usize.
    ///
    /// Time complexity: O(n) - Linear time complexity.
    /// Space complexity: O(1) - We use constant extra space.
    ///
    /// Runtime 12 ms Beats 57%
    /// Memory 3.10 MB Beats 83%
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let (mut slow, mut fast) = (nums[0], nums[nums[0] as usize]);
        while slow != fast {
            slow = nums[slow as usize];
            fast = nums[nums[fast as usize] as usize];
        }
        // Reuse one of the pointers, it can be either.
        fast = 0;
        while slow != fast {
            slow = nums[slow as usize];
            fast = nums[fast as usize];
        }
        fast as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 3, 4, 2, 2], 2),
        (vec![3, 1, 3, 4, 2], 3),
        (vec![3, 3, 3, 3, 3], 3),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_duplicate(t.0.clone());
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
