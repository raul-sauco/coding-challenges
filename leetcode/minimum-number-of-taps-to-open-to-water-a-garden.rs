// 1326. Minimum Number of Taps to Open to Water a Garden
// 🔴 Hard
//
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
//
// Tags: Array - Dynamic Programming - Greedy

struct Solution;
impl Solution {
    /// Using an auxiliary vector that stores the max reach of each tap, we can
    /// convert this problem to jump game 2, then visit each position and check
    /// if we can reach it and if we need to add a "jump" to reach it.
    ///
    /// Time complexity: O(n) - We iterate twice over all elements of the input
    /// and, both times, we do constant time work for each.
    /// Space complexity: O(n) - The auxiliary max_reach vector has size n.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.44 MB Beats 20%
    pub fn min_taps(n: i32, ranges: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut max_reach = vec![0; n + 1];
        let (mut start, mut end);
        for i in 0..n + 1 {
            start = 0.max(i as i32 - ranges[i]) as usize;
            end = n.min(i + ranges[i] as usize);
            max_reach[start] = max_reach[start].max(end);
        }
        let mut taps = 0;
        let (mut curr_end, mut next_end) = (0, 0);
        for i in 0..n + 1 {
            if i > next_end {
                return -1;
            }
            if i > curr_end {
                taps += 1;
                curr_end = next_end;
            }
            next_end = next_end.max(max_reach[i]);
        }
        taps
    }
}

// Tests.
fn main() {
    let tests = [
        (3, vec![0, 0, 0, 0], -1),
        (5, vec![3, 4, 1, 1, 0, 0], 1),
        (7, vec![1, 2, 1, 0, 2, 1, 0, 1], 3),
    ];
    for t in tests {
        assert_eq!(Solution::min_taps(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
