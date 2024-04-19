// 1846. Maximum Element After Decreasing and Rearranging
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
//
// Tags: Array - Greedy - Sorting

struct Solution;
impl Solution {
    /// Sort the input, then iterate through the elements, the maximum at each position will be the
    /// minimum between its value and the value computed for (arr[i-1] + 1) because we can, at
    /// most, increase the values by one each position.
    ///
    /// Time complexity: O(n*log(n)) - We are sorting the input.
    /// Space complexity: O(n) - The local copy.
    ///
    /// Runtime 5 ms Beats 33.33%
    /// Memory 3.84 MB Beats 33.33%
    pub fn maximum_element_after_decrementing_and_rearranging(arr: Vec<i32>) -> i32 {
        let mut arr = arr;
        arr.sort_unstable();
        arr.into_iter().fold(0, |acc, x| x.min(acc + 1))
    }

    /// Similar solution, but use counting sort.
    ///
    /// Time complexity: O(n) - We iterate over the elements 2 times.
    /// Space complexity: O(n) - The counting buckets.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 4.17 MB Beats 33.33%
    pub fn maximum_element_after_decrementing_and_rearranging_2(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut counts = vec![0; n + 1];
        for num in arr {
            counts[n.min(num as usize)] += 1;
        }
        let mut res = 1;
        for i in 2..=n {
            res = i.min(res + counts[i]);
        }
        res as i32
    }

    /// Similar solution, use counting sort, update the second loop to use an iterator.
    ///
    /// Time complexity: O(n) - We iterate over the elements 2 times.
    /// Space complexity: O(n) - The counting buckets.
    ///
    /// Runtime 8 ms Beats 33.33%
    /// Memory 3.88 MB Beats 33.33%
    pub fn maximum_element_after_decrementing_and_rearranging_3(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut counts = vec![0; n + 1];
        for num in arr {
            counts[n.min(num as usize)] += 1;
        }
        counts
            .into_iter()
            .enumerate()
            .skip(2)
            .fold(1, |acc, (idx, val)| idx.min(acc + val)) as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2, 2, 1, 2, 1], 2),
        (vec![100, 1, 1000], 3),
        (vec![1, 2, 3, 4, 5], 5),
    ];
    for t in tests {
        assert_eq!(
            Solution::maximum_element_after_decrementing_and_rearranging(t.0.clone()),
            t.1
        );
        assert_eq!(
            Solution::maximum_element_after_decrementing_and_rearranging_2(t.0.clone()),
            t.1
        );
        assert_eq!(
            Solution::maximum_element_after_decrementing_and_rearranging_3(t.0.clone()),
            t.1
        );
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
