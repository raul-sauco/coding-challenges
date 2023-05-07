// 1964. Find the Longest Valid Obstacle Course at Each Position
// 🔴 Hard
//
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
//
// Tags: Array - Binary Search - Divide and Conquer - Binary Indexed Tree
// - Segment Tree - Merge Sort - Ordered Set

struct Solution;
impl Solution {
    /// Use dynamic programming, each subproblem can be seen as "the longest
    /// non-decreasing subsequence" but, if we use something similar to the
    /// LIS solution, it will run in O(n^2*log(n)), we can instead see that,
    /// for each index, we only need to find the longest sequence to the left
    /// where the last element is less than, or equal to the current element,
    /// because then we can append the current element. We could do this in
    /// O(n), resulting in O(n^2) overall time complexity, iterating over all
    /// the previous results but that can be optimized if we use an extra
    /// structure where we keep these previous results sorted and can binary
    /// search the insertion point.
    ///
    /// Time complexity: O(n*log(n)) - We iterate over all the elements, for
    /// each, we do a binary search over the previous results that could be up
    /// to n.
    /// Space complexity: O(n) - The dp array uses n extra memory.
    ///
    /// Runtime 112 ms Beats 100%
    /// Memory 3.7 MB Beats 100%
    pub fn longest_obstacle_course_at_each_position(obstacles: Vec<i32>) -> Vec<i32> {
        let mut dp = vec![std::i32::MAX; obstacles.len() + 1];
        let mut res = vec![0; obstacles.len()];
        let (mut l, mut mid, mut r);
        for (i, o) in obstacles.into_iter().enumerate() {
            (l, r) = (0, dp.len());
            while l < r {
                mid = l + (r - l) / 2;
                if dp[mid] <= o {
                    l = mid + 1;
                } else {
                    r = mid;
                }
            }
            res[i] = l as i32 + 1;
            dp[l] = o;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![2, 2, 1], vec![1, 2, 1]),
        (vec![1, 2, 3, 2], vec![1, 2, 3, 3]),
        (vec![3, 1, 5, 6, 4, 2], vec![1, 1, 2, 3, 2, 2]),
    ];
    for t in tests {
        assert_eq!(Solution::longest_obstacle_course_at_each_position(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
