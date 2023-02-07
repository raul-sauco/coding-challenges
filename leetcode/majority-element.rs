a// 169. Majority Element
// 🟢 Easy
//
// https://leetcode.com/problems/majority-element/
//
// Tags: Array - Hash Table - Divide and Conquer - Sorting - Counting

struct Solution;
impl Solution {
    // For the follow-up we can use the Boyer-Moore majority vote algorithm
    // https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm
    //
    // Time complexity: O(n) - We visit each element once and do O(1) work.
    // Space complexity: O(1) - We only store two pointers.
    //
    // Runtime 3 ms Beats 83.14%
    // Memory 2.3 MB Beats 80.81%
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut candidate = 0;
        let mut count = 0;
        for num in nums {
            if count == 0 {
                candidate = num;
            }
            count = if candidate == num {
                count + 1
            } else {
                count - 1
            };
        }
        candidate
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::majority_element(vec![3, 2, 3]), 3);
    println!("All tests passed!")
}
