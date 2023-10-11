// 2251. Number of Flowers in Full Bloom
// 🔴 Hard
//
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/
//
// Tags: Array - Hash Table - Binary Search - Sorting - Prefix Sum - Ordered Set

struct Solution;
impl Solution {
    /// Create auxiliary data structures, one each for the sorted start and end
    /// times of the flowers blooming, and one for the time at which people visit.
    /// Iterate over the visit times sliding two pointers, one on the starts and
    /// another one on the ends vectors. When we move passed the visit time, the
    /// number of flowers in bloom equals the number of flowers that have started
    /// blooming s_idx, minus the number of flowers that have finished blooming,
    /// e_idx.
    ///
    /// Time complexity: O(m*log(m)+n*log(n)) - We need to sort both the flowers
    /// vector (m) and the people vector (n). After that, the algorithm uses a
    /// sliding window technique and runs in O(m+n) we iterate over the n people
    /// and advance the pointer to the sorted flowers start and end vectors while
    /// the values under the pointers are smaller than the visit time.
    /// Space complexity: O(m+n) - We create extra vectors to sort the input
    /// data, both for the flowers and people input vectors.
    ///
    /// Runtime 34 ms Beats 100%
    /// Memory 6.83 MB Beats 45.45%
    pub fn full_bloom_flowers(flowers: Vec<Vec<i32>>, people: Vec<i32>) -> Vec<i32> {
        let mut starts = flowers.iter().map(|v| v[0]).collect::<Vec<i32>>();
        let mut ends = flowers.iter().map(|v| v[1]).collect::<Vec<i32>>();
        starts.sort_unstable();
        ends.sort_unstable();
        let mut sorted_people = people
            .iter()
            .enumerate()
            .map(|(idx, item)| (*item, idx))
            .collect::<Vec<(i32, usize)>>();
        sorted_people.sort_unstable();
        let mut res = vec![0; people.len()];
        let (mut s_idx, mut e_idx) = (0, 0);
        for (visit_time, idx) in sorted_people {
            while s_idx < starts.len() && starts[s_idx] <= visit_time {
                s_idx += 1;
            }
            while e_idx < ends.len() && ends[e_idx] < visit_time {
                e_idx += 1;
            }
            res[idx] = (s_idx - e_idx) as i32;
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![vec![1, 6], vec![3, 7], vec![9, 12], vec![4, 13]],
            vec![2, 3, 7, 11],
            vec![1, 2, 2, 2],
        ),
        (vec![vec![1, 10], vec![3, 3]], vec![3, 3, 2], vec![2, 2, 1]),
    ];
    for t in tests {
        assert_eq!(Solution::full_bloom_flowers(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
