// 1011. Capacity To Ship Packages Within D Days
// 🟠 Medium
//
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    // Use binary search to determine the minimum size of ship that lets us
    // ship all the weights in the given amount of time. The binary search
    // uses an auxiliary function to determine whether shipping is feasible
    // given a ship size.
    //
    // Time complexity: O(n*log(n)) - Linear time over the number of weights
    // to determine whether a ship size is suitable and log(n) over the
    // ship sizes, bounded by the max weight on the bottom and the total
    // weights on top, which makes it equivalent to n.
    // Space complexity: O(1) - Constant extra space used.
    //
    // Runtime 10 ms Beats 71.43%
    // Memory 2.4 MB Beats 100%
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
        let mut l = weights.iter().max().unwrap().to_owned();
        let mut r: i32 = weights.iter().sum();
        // Binary search the minimum ship size.
        while l < r {
            // Both ints are bounded to 500, the addition cannot overflow.
            let mid = (l + r) / 2;
            let mut ships = 0;
            let mut remaining_capacity = 0;
            for weight in &weights {
                if &remaining_capacity < weight {
                    ships += 1;
                    remaining_capacity = mid;
                }
                remaining_capacity -= weight;
                if ships > days {
                    break;
                }
            }
            if ships > days {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        l
    }
}

// Tests.
fn main() {
    assert_eq!(Solution::ship_within_days(vec![1, 2, 3, 1, 1], 4), 3);
    assert_eq!(Solution::ship_within_days(vec![3, 2, 2, 4, 1, 4], 3), 6);
    assert_eq!(
        Solution::ship_within_days(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        15
    );
    println!("All tests passed!")
}
