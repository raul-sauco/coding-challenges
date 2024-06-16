// 330. Patching Array
// 🔴 Hard
//
// https://leetcode.com/problems/patching-array/
//
// Tags: Array - Greedy

struct Solution;
impl Solution {
    /// We need to make sure that we can set or unset each bit for the k bits of n. We can greedily
    /// make sure that we can construct each value checking that we don't have a gap bigger than
    /// the current sum of values + 1.
    ///
    /// Time complexity: O(n) - We iterate over the input and do constant time work for each
    /// element.
    /// Space complexity: O(1) - We use 2 integers of extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.14 MB Beats 50%
    #[allow(dead_code)]
    pub fn min_patches_it(nums: Vec<i32>, n: i32) -> i32 {
        let n = n as i64;
        let mut current_sum = 0;
        let mut patches = 0;
        for num in nums.into_iter().map(|x| x as i64).chain(std::iter::once(n)) {
            if current_sum >= n {
                break;
            }
            while num > current_sum + 1 && current_sum < n {
                patches += 1;
                current_sum += current_sum + 1;
            }
            current_sum += num;
        }
        patches
    }

    /// Similar logic to the previous solution but an attempt to avoid using the iterator. What I
    /// was really trying to do was to avoid using i64s and use saturating_add, but I didn't manage
    /// to do that, I prefer the previous solution.
    ///
    /// Time complexity: O(n) - We iterate over the input and do constant time work for each
    /// element.
    /// Space complexity: O(1) - We use 2 integers of extra memory.
    ///
    /// Runtime 1 ms Beats 50%
    /// Memory 2.12 MB Beats 50%
    pub fn min_patches(nums: Vec<i32>, n: i32) -> i32 {
        let (mut next, mut patches, mut i, n) = (1, 0, 0, n as i64);
        let nl = nums.len();
        while next <= n {
            if i < nl && nums[i] as i64 <= next {
                next += nums[i] as i64;
                i += 1;
            } else {
                patches += 1;
                next *= 2;
            }
        }
        patches
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 3], 6, 1),
        (vec![1, 2, 2], 5, 0),
        (vec![1, 5, 10], 20, 2),
        (vec![1, 2, 31, 33], 2147483647, 28),
        (
            vec![
                1, 2, 2, 6, 34, 38, 41, 44, 47, 47, 56, 59, 62, 73, 77, 83, 87, 89, 94,
            ],
            20,
            1,
        ),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::min_patches(t.0.clone(), t.1);
        if res == t.2 {
            success += 1;
            println!("\x1b[92m✔\x1b[95m Test {} passed!\x1b[0m", i);
        } else {
            println!(
                "\x1b[31mx\x1b[95m Test {} failed expected: {:?} but got {}!!\x1b[0m",
                i, t.2, res
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
