// 164. Maximum Gap
// 🟠 Medium
//
// https://leetcode.com/problems/maximum-gap/
//
// Tags: Array - Sorting - Bucket Sort - Radix Sort

#[derive(Clone, Debug)]
struct Bucket {
    min: i32,
    max: i32,
}

impl Bucket {
    fn new() -> Self {
        Bucket {
            min: i32::MAX,
            max: i32::MIN,
        }
    }

    fn add(&self, num: i32) -> Self {
        Bucket {
            min: self.min.min(num),
            max: self.max.max(num),
        }
    }

    fn get_diff(&self) -> i32 {
        self.max - self.min
    }

    fn is_empty(&self) -> bool {
        self.min == i32::MAX
    }
}

struct Solution;
impl Solution {
    /// Use bucket sort. If we have n numbers, we know that there will be n - 1 gaps between them,
    /// once we find the minimum and maximum values, we know that if we have n buckets, with their
    /// size being < max - min / n, then we can guarantee that there will be a gap between elements
    /// in different buckets greater than any gap between elements in the same bucket. Once we have
    /// made that observation, the algorithm is not hard to code. Split the elements into buckets
    /// keeping track of the minimum and maximum values in each bucket, then iterate over the
    /// non-empty buckets checking the difference between the current bucket minimum and the
    /// previous bucket maximum, store the greatest difference as the result.
    ///
    /// Time complexity: O(n) - Linear time complexity.
    /// Space complexity: O(n) - We use n buckets with 2 values each min and max.
    ///
    /// Runtime 12 ms Beats 91%
    /// Memory 3.92 MB Beats 20%
    pub fn maximum_gap(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let min_max_bucket = nums
            .iter()
            .fold(Bucket::new(), |bucket, &num| bucket.add(num));
        if min_max_bucket.get_diff() == 0 {
            return 0;
        }
        let mut buckets = vec![Bucket::new(); n];
        for num in nums {
            let idx = ((num - min_max_bucket.min) as usize) * (n - 1)
                / min_max_bucket.get_diff() as usize;
            buckets[idx] = buckets[idx].add(num);
        }
        let mut last_max = None;
        let mut res = 0;
        for bucket in buckets {
            // Ignore empty buckets.
            if !bucket.is_empty() {
                if let Some(last) = last_max {
                    res = res.max(bucket.min - last);
                }
                last_max = Some(bucket.max);
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![10], 0),
        (vec![2, 1], 1),
        (vec![3, 6, 9, 1], 3),
        (vec![29, 25, 3, 49, 9, 37, 21, 43], 12),
        (vec![999, 2000, 3000, 4000, 5000], 1001),
        (vec![1000, 2000, 3000, 4000, 5000], 1000),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::maximum_gap(t.0.clone());
        if res == t.1 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.1, res
            );
        }
    }
    println!();
    if success == tests.len() {
        println!("\x1b[30;42m✔ All tests passed!\x1b[0m")
    } else if success == 0 {
        println!("\x1b[31mx \x1b[41;37mAll tests failed!\x1b[0m")
    } else {
        println!(
            "\x1b[31mx\x1b[95m {} tests failed!\x1b[0m",
            tests.len() - success
        )
    }
}
