// 1539. Kth Missing Positive Number
// 🟢 Easy
//
// https://leetcode.com/problems/kth-missing-positive-number/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    // Use binary search to find the index right before the index where the
    // kth missing value would be if found. Use the combination of index and
    // value to compute how many missing values there are before a given
    // element.
    //
    // Time complexity: O(log(n)) - Binary search over the elements in arr.
    // Space complexity: O(1) - Constant extra memory used.
    //
    // Runtime 1 ms Beats 77.78%
    // Memory 2.1 MB Beats 88.89%
    pub fn find_kth_positive(arr: Vec<i32>, k: i32) -> i32 {
        if k < arr[0] {
            return k;
        }
        let (mut l, mut r) = (0, arr.len());
        let (mut mid, mut umid);
        while l < r {
            umid = l + (r - l) / 2;
            mid = umid as i32;
            if arr[umid] - mid - 1 < k {
                l = umid + 1;
            } else {
                r = umid;
            }
        }
        k + l as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![142], 145, 146),
        (vec![1, 2, 3, 4], 2, 6),
        (vec![2, 3, 4, 7, 11], 5, 9),
        (vec![100_000], 100_009, 100_010),
    ];
    for test in tests {
        assert_eq!(Solution::find_kth_positive(test.0, test.1), test.2);
    }
    println!("All tests passed!")
}
