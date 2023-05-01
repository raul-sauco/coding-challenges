// 1491. Average Salary Excluding the Minimum and Maximum Salary
// 🟢 Easy
//
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
//
// Tags: Array - Sorting

struct Solution;
impl Solution {
    /// Iterate over the input array keeping track of the minimum maximum and
    /// sum of elements, then subtract the max and min from the sum and divide
    /// it by the count of items minus 2. This is better than sorting and only
    /// iterating over the slice [1..n-1] because sorting is O(n*log(n)).
    ///
    /// Time complexity: O(n) - We iterate once over the items and do O(1) work
    /// for each.
    /// Space complexity: O(1) - We use 1*f64 and 3*i32 of extra memory.
    ///
    /// Runtime 1 ms Beats 75%
    /// Memory 2.1 MB Beats 73.15%
    pub fn average(salary: Vec<i32>) -> f64 {
        let item_count = (salary.len() - 2) as f64;
        let (mut sum, mut max, mut min) = (0, 0, i32::MAX);
        for item in salary {
            if item > max {
                max = item;
            }
            if item < min {
                min = item;
            }
            sum += item;
        }
        (sum - (min + max)) as f64 / item_count
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1000, 2000, 3000], 2000.0),
        (vec![4000, 3000, 1000, 2000], 2500.0),
    ];
    for t in tests {
        assert_eq!(Solution::average(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m");
}
