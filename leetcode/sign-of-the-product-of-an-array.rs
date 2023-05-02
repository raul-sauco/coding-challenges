// 1822. Sign of the Product of an Array
// 🟢 Easy
//
// https://leetcode.com/problems/sign-of-the-product-of-an-array/
//
// Tags: Array - Math

struct Solution;
impl Solution {
    /// Iterate over the input values counting the number of negative numbers,
    /// if we find a zero, return 0 immediately, otherwise, once we have visited
    /// all values, return -1 if the number of negative values is uneven, or 1
    /// if it is even.
    ///
    /// Time complexity: O(n) - We iterate over all values and do O(1) work.
    /// Space complexity: O(1) - We use one i32 of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.1 MB Beats 70%
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut neg_count = 0;
        for num in nums {
            if num == 0 {
                return 0;
            }
            if num < 0 {
                neg_count += 1;
            }
        }
        if neg_count % 2 == 0 {
            1
        } else {
            -1
        }
    }

    /// Same as above but use an iterator and fold.
    ///
    /// Time complexity: O(n) - We iterate over all values and do O(1) work.
    /// Space complexity: O(1) - We use one i32 of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.1 MB Beats 70%
    pub fn array_sign_iter(nums: Vec<i32>) -> i32 {
        nums.into_iter().fold(1, |acc, x| {
            if x == 0 {
                return 0;
            }
            if x < 0 {
                return acc * -1;
            }
            acc
        })
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 5, 0, 2, -3], 0),
        (vec![-1, 1, -1, 1, -1], -1),
        (vec![-1, -2, -3, -4, 3, 2, 1], 1),
    ];
    for t in tests {
        assert_eq!(Solution::array_sign(t.0.clone()), t.1);
        assert_eq!(Solution::array_sign_iter(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
