// 2448. Minimum Cost to Make Array Equal
// 🔴 Hard
//
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/
//
// Tags: Array - Binary Search - Greedy - Sorting - Prefix Sum

struct Solution;
impl Solution {
    /// Binary search the value that results in the minimum cost to update all
    /// other values to that one, as we get further away from that value, the
    /// total cost increases, we can use that property to try on different
    /// values using binary search instead of having to try them all.
    ///
    /// Time complexity: O(n*log(n)) - We binary search the optimal value in
    /// log(n) tries, each try requires going over the entire vector of values.
    /// Space complexity: O(n) - The num_cost array has size n.
    ///
    /// Runtime 6 ms Beats 100%
    /// Memory 4.3 MB Beats 100%
    pub fn min_cost(nums: Vec<i32>, cost: Vec<i32>) -> i64 {
        let num_cost = (0..nums.len())
            .into_iter()
            .map(|i| (nums[i] as i64, cost[i] as i64))
            .collect::<Vec<_>>();
        fn get_cost(val: i64, num_cost: &Vec<(i64, i64)>) -> i64 {
            num_cost
                .iter()
                .fold(0, |acc, (num, cost)| acc + (*num - val).abs() * *cost)
        }
        let (mut left, mut right) = (i64::MAX, i64::MIN);
        for num in nums.into_iter() {
            let num = num as i64;
            if num > right {
                right = num;
            }
            if num < left {
                left = num;
            }
        }
        let mut res = get_cost(num_cost[0].0, &num_cost);
        while left < right {
            let mid = (left + right) / 2;
            let cost_1 = get_cost(mid, &num_cost);
            let cost_2 = get_cost(mid + 1, &num_cost);
            res = cost_1.min(cost_2);
            if cost_1 > cost_2 {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 3, 5, 2], vec![2, 3, 1, 14], 8),
        (vec![2, 2, 2, 2, 2], vec![4, 2, 8, 1, 3], 0),
        (
            vec![
                735103, 366367, 132236, 133334, 808160, 113001, 49051, 735598, 686615, 665317,
                999793, 426087, 587000, 649989, 509946, 743518,
            ],
            vec![
                724182, 447415, 723725, 902336, 600863, 287644, 13836, 665183, 448859, 917248,
                397790, 898215, 790754, 320604, 468575, 825614,
            ],
            1907611126748,
        ),
    ];
    for t in tests {
        assert_eq!(Solution::min_cost(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
