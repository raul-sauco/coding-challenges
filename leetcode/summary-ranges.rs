// 228. Summary Ranges
// 🟢 Easy
//
// https://leetcode.com/problems/summary-ranges/
//
// Tags: Array

struct Solution;
impl Solution {
    /// Use the first value to create a tuple with 2 equal elements, iterate
    /// over the rest of the array, when the element is equal to the second
    /// element in the current range we are looking at plus 1, keep extending
    /// the range, otherwise, add it to the ranges result and start a new range.
    /// When we add a range to the ranges result, we check if its two elements
    /// are equal, if they are, we return a string with only that one integer,
    /// if they are not equal, we create a range formatted as requested by the
    /// problem description.
    ///
    /// Time complexity: O(n) - We visit each element in the array once and do
    /// constant work for each.
    /// Space complexity: O(n) - The result vector could grow to the same size
    /// as the input. If we don't take that into consideration, then O(1)
    /// because we only store one tuple with two integers and an iterator
    /// pointer at any given time.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 100%
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        if nums.len() == 0 {
            return vec![];
        }
        let mut ranges = vec![];
        let mut current_range = (nums[0], nums[0]);
        for num in nums[1..].into_iter() {
            if *num == current_range.1 + 1 {
                current_range = (current_range.0, *num);
            } else {
                if current_range.0 == current_range.1 {
                    ranges.push(current_range.0.to_string());
                } else {
                    ranges.push(format!("{}->{}", current_range.0, current_range.1));
                }
                current_range = (*num, *num);
            }
        }
        if current_range.0 == current_range.1 {
            ranges.push(current_range.0.to_string());
        } else {
            ranges.push(format!("{}->{}", current_range.0, current_range.1));
        }
        ranges
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![0, 1, 2, 4, 5, 7],
            vec!["0->2".to_string(), "4->5".to_string(), "7".to_string()],
        ),
        (
            vec![0, 2, 3, 4, 6, 8, 9],
            vec![
                "0".to_string(),
                "2->4".to_string(),
                "6".to_string(),
                "8->9".to_string(),
            ],
        ),
    ];
    for t in tests {
        assert_eq!(Solution::summary_ranges(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
