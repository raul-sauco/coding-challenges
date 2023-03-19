// 4. Median of Two Sorted Arrays
// 🔴 Hard
//
// https://leetcode.com/problems/median-of-two-sorted-arrays/
//
// Tags: Array - Binary Search - Divide and Conquer

struct Solution;
impl Solution {
    /**
     * Use binary search, we choose the smaller input array, or either if the
     * same size, and do binary search for the edge of the partition, we try
     * positions and adjust the boundary left or right based on whether we
     * still have greater values on the left partition or lesser values on
     * the right partition than the values at the boundaries.
     *
     * Time complexity: O(log(min(m, n))) - We do binary search on the
     * smaller array.
     * Space complexity: O(1) - We use constant space.
     *
     * Runtime 0 ms Beats 100%
     * Memory 2.6 MB Beats 6.27%
     */
    pub fn find_median_sorted_arrays_bs(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        // To make it easy we binary search on the shorter array a.
        let (a, b) = if nums2.len() > nums1.len() {
            (&nums1, &nums2)
        } else {
            (&nums2, &nums1)
        };
        let (m, n) = (a.len() as i32, b.len() as i32);
        let half = (m + n) / 2;
        let (mut l, mut r) = (0, a.len() as i32 - 1);
        let mut mid: i32;
        let mut k;
        let mut la;
        let mut ra;
        let mut lb;
        let mut rb;
        loop {
            // TODO: Find a way to avoid depending on floor division, check the Python version
            // to see why this works. We should be able to implement the same logic using usize
            // and conditionals and avoiding all the, very hard to understand, casting.
            mid = ((l as f32 + r as f32) / 2.0).floor() as i32;
            k = half - mid - 2;
            la = if mid >= 0 && mid < m {
                a[mid as usize]
            } else {
                i32::MIN
            };
            ra = if mid + 1 < m {
                a[(mid + 1) as usize]
            } else {
                i32::MAX
            };
            lb = if k >= 0 { b[k as usize] } else { i32::MIN };
            rb = if k + 1 < n && k + 1 >= 0 {
                b[(k + 1) as usize]
            } else {
                i32::MAX
            };
            if lb > ra {
                l = mid + 1;
            } else if la > rb {
                r = mid - 1;
            } else {
                if (m + n) % 2 == 0 {
                    return (la.max(lb) as f64 + ra.min(rb) as f64) / 2.0;
                } else {
                    return ra.min(rb) as f64;
                }
            }
        }
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2], vec![], 2.0),
        (vec![], vec![2], 2.0),
        (vec![1, 3], vec![2], 2.0),
        (vec![0, 0], vec![0, 0], 0.0),
        (vec![1, 2], vec![3, 4], 2.5),
        (
            vec![1, 1, 2, 2, 3, 3, 5, 6],
            vec![4, 5, 8, 10, 12, 15, 18, 20, 21, 23, 24, 30],
            7.0,
        ),
    ];
    for test in tests {
        assert_eq!(
            Solution::find_median_sorted_arrays_bs(test.0, test.1),
            test.2
        );
    }
    println!("All tests passed!")
}
