// 31. Next Permutation
// 🟠 Medium
//
// https://leetcode.com/problems/next-permutation/
//
// Tags: Array - Two Pointers

struct Solution;
impl Solution {
    /// Start traversing leftwards from the right until we find an element that
    /// is smaller than the element to its right at index i. Start moving right
    /// from i until we find the smallest element that is still greater than
    /// nums[i] and swap them. Then reverse the vector slice to the right of i.
    ///
    /// Time complexity: O(n) - We visit each element a maximum of three times.
    /// Space complexity: O(1) - We mutate the input array.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.25 MB Beats 10.53%
    pub fn next_permutation(nums: &mut Vec<i32>) {
        let mut i = nums.len() - 1;
        while i > 0 && nums[i - 1] >= nums[i] {
            i -= 1;
        }
        // If the vector is sorted.
        if i == 0 {
            nums.reverse();
            return;
        }
        // Otherwise point to the first non-increasing from the left.
        i = i - 1;
        let mut j = i + 1;
        while j < nums.len() - 1 && nums[j + 1] > nums[i] {
            j += 1;
        }
        nums.swap(i, j);
        nums[i + 1..].reverse();
    }

    #[allow(dead_code)]
    /// Nice solution found on Leetcode that uses some built-in functions.
    pub fn next_permutation_2(nums: &mut Vec<i32>) {
        let pivot = nums.windows(2).rposition(|w| w[1] > w[0]);
        if let Some(pivot) = pivot {
            let swap_with = nums.iter().rposition(|&n| n > nums[pivot]).unwrap();
            nums.swap(pivot, swap_with);
            nums[pivot + 1..].reverse();
        } else {
            nums.reverse();
        }
    }
}

// Tests.
fn main() {
    let mut tests = [
        (vec![1, 2, 3], vec![1, 3, 2]),
        (vec![1, 3, 2], vec![2, 1, 3]),
        (vec![2, 3, 1], vec![3, 1, 2]),
        (vec![3, 2, 1], vec![1, 2, 3]),
        (vec![1, 1, 5], vec![1, 5, 1]),
        (vec![5, 1, 1], vec![1, 1, 5]),
        (vec![3, 1, 7, 6, 5], vec![3, 5, 1, 6, 7]),
    ];
    for t in &mut tests {
        Solution::next_permutation(&mut t.0);
        assert_eq!(t.0, t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
