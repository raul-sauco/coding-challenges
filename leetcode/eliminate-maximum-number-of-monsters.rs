// 1921. Eliminate Maximum Number of Monsters
// 🟠 Medium
//
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
//
// Tags: Array - Greedy - Sorting

struct Solution;
impl Solution {
    /// Compute the monster arrival times and sort them. Then iterate over that
    /// vector "eliminating" one monster per minute, which is the equivalent of
    /// moving one position right at the same time that we "increment" the time
    /// by one unit. If any monster's arrival time at the city is lower than its
    /// position, we won't have time to eliminate it, and the result is the
    /// number of monsters that we have eliminated up to that point.
    ///
    /// Time complexity: O(n*log(n)) - The most efficient way to solve the problem
    /// is to first compute the arrival time of all monsters and sort them, then
    /// we can iterate over that vector and check if any monster arrival time is
    /// lower than its position. That is a valid way to find the result because
    /// we know that we can eliminate one monster per minute.
    /// Space complexity: O(n) - The vector with arrival times.
    ///
    /// Runtime 17 ms Beats 83.33%
    /// Memory 3.15 MB Beats 100%
    pub fn eliminate_maximum(dist: Vec<i32>, speed: Vec<i32>) -> i32 {
        let n = dist.len() as i32;
        let mut arrival_times = dist
            .into_iter()
            .zip(speed.into_iter())
            // Ceiling division tells us the first integer minute at which this
            // monster has already arrived at the city. No need for floats.
            .map(|(d, s)| (d + s - 1) / s)
            .collect::<Vec<i32>>();
        arrival_times.sort_unstable();
        for (i, t) in arrival_times.into_iter().enumerate() {
            // If this monster is already in the city, we have eliminated i.
            if t <= i as i32 {
                return i as i32;
            }
        }
        n
    }

    /// Compute the monster arrival times but, instead of sorting them, use
    /// counting sort, placing the monsters in buckets given the minute they
    /// arrive at, then iterating over the buckets until at some point we have
    /// accumulated more monsters in the buckets than the time we have had to
    /// eliminate them.
    ///
    /// Time complexity: O(n) - We iterate 3 times over n elements, for each
    /// iteration of any of these loops we do constant time work.
    /// Space complexity: O(n) - The vector with arrival times and the one with
    /// number of monsters at each minute.
    ///
    /// Runtime 11 ms Beats 100%
    /// Memory 3.39 MB Beats 100%
    pub fn eliminate_maximum_2(dist: Vec<i32>, speed: Vec<i32>) -> i32 {
        let n = dist.len();
        let arrival_times = dist
            .into_iter()
            .zip(speed.into_iter())
            // Ceiling division tells us the first integer minute at which this
            // monster has already arrived at the city. No need for floats.
            .map(|(d, s)| (d + s - 1) / s)
            .collect::<Vec<i32>>();
        let mut counts = vec![0; n];
        for arrival_time in arrival_times.iter().map(|&x| x as usize) {
            if arrival_time >= n {
                continue;
            }
            counts[arrival_time] += 1;
        }
        let mut eliminated_monsters = 0;
        for i in 1..n {
            eliminated_monsters += counts[i];
            if eliminated_monsters > i {
                return i as i32;
            }
        }
        n as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 3, 4], vec![1, 1, 1], 3),
        (vec![3, 2, 4], vec![5, 3, 2], 1),
        (vec![1, 1, 2, 3], vec![1, 1, 1, 1], 1),
        (vec![4, 3, 3, 3, 4], vec![1, 1, 1, 1, 4], 3),
    ];
    for t in tests {
        assert_eq!(Solution::eliminate_maximum(t.0.clone(), t.1.clone()), t.2);
        assert_eq!(Solution::eliminate_maximum_2(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
