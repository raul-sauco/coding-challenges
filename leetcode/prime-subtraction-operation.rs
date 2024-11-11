// 2601. Prime Subtraction Operation
// 🟠 Medium
//
// https://leetcode.com/problems/prime-subtraction-operation/
//
// Tags: Array - Math - Binary Search - Greedy - Number Theory

struct Solution;
impl Solution {
    /// Iterate over the values from right to left, for each value, we try to find a prime we can
    /// subtract that makes the value less than the one to the right but still greater than 0.
    ///
    /// Time complexity: O(n) - We iterate over all the values in the input, for each, we try to
    /// find a prime number we can subtract iterating over a fixed number of elements.
    /// Space complexity: O(1) - Constant extra memory used.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.14 MB Beats 100%
    pub fn prime_sub_operation(nums: Vec<i32>) -> bool {
        fn doit(state: i32, x: i32) -> Option<i32> {
            let primes = [
                0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
                257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
                353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
                563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647,
                653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757,
                761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
                877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                991, 997,
            ];
            // State is the value to the right.
            for val in primes.into_iter().map(|prime| x - prime) {
                if val < state && val > 0 {
                    return Some(val);
                }
            }
            None
        }
        nums.into_iter().rev().try_fold(i32::MAX, doit).is_some()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![4, 9, 6, 10], true),
        (vec![6, 8, 11, 12], true),
        (vec![5, 8, 3], false),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::prime_sub_operation(t.0.clone());
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
