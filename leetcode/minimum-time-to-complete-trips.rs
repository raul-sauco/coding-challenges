// 2187. Minimum Time to Complete Trips
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-time-to-complete-trips/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    // Use binary search to take guesses on the time that it can be needed
    // for the n buses to complete k number of trips.
    //
    // Time complexity: O(n*log(k*t)) - Where n is the number of buses,
    // k is the total number of trips to be completed and t is the time
    // that the fastest bus needs to complete one trip.
    // Space complexity: O(1) - Only pointers used, unless the list
    // comprehension takes memory, in that case O(n) but it could be improved
    // to O(1) using sum directly instead of the list comprehension.
    //
    // Runtime 87 ms Beats 50%
    // Memory 3.5 MB Beats 87.50%
    pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {
        let tt = total_trips as i64;
        // Initialize two pointers for the binary search.
        let (mut l, mut r) = (1, tt * *time.iter().min().unwrap() as i64);
        let mut guess;
        // Binary search the answer.
        while l < r {
            guess = l + (r - l) / 2;
            if time.iter().map(|x| guess / *x as i64).sum::<i64>() >= tt {
                r = guess;
            } else {
                l = guess + 1;
            }
        }
        l
    }
}

// Tests.
fn main() {
    let tests = [(vec![2], 1, 2), (vec![1, 2, 3], 5, 3)];
    for test in tests {
        assert_eq!(Solution::minimum_time(test.0, test.1), test.2);
    }
    println!("All tests passed!")
}
