// 303. Range Sum Query - Immutable
// 🟢 Easy
//
// https://leetcode.com/problems/range-sum-query-immutable/
//
// Tags: Array - Design - Prefix Sum

struct NumArray {
    prefix_sums: Vec<i32>,
}

/**
 * Create an array of sums. When a range sum is requested, fetch it from
 * prefix_sums(right - left).
 *
 * Time complexity: O(n) - To create the prefix sum array we iterate over
 * the entire input array, then O(1) for the sum_range method.
 * Space complexity: O(n) - We store an array of prefix sums of the same
 * size as the input array.
 *
 * Runtime 6 ms Beats 77.78%
 * Memory 8.4 MB Beats 90.48%
 */
impl NumArray {
    /**
     * The constructor creates a vector of prefix sums.
     */
    fn new(nums: Vec<i32>) -> Self {
        NumArray {
            prefix_sums: nums
                .iter()
                .scan(0, |state, &x| {
                    *state = *state + x;
                    Some(*state)
                })
                .collect(),
        }
    }

    /**
     * Use the prefix sums to compute the result in O(1)
     */
    fn sum_range(&self, left: i32, right: i32) -> i32 {
        self.prefix_sums[right as usize]
            - if left > 0 {
                self.prefix_sums[left as usize - 1]
            } else {
                0
            }
    }
}

// Tests.
fn main() {
    let num_array = NumArray::new(vec![-2, 0, 3, -5, 2, -1]);
    assert_eq!(num_array.sum_range(0, 2), 1);
    assert_eq!(num_array.sum_range(2, 5), -1);
    assert_eq!(num_array.sum_range(0, 5), -3);
    println!("All tests passed!")
}
