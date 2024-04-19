// 458. Poor Pigs
// 🔴 Hard
//
// https://leetcode.com/problems/poor-pigs/
//
// Tags: Math - Dynamic Programming - Combinatronics

struct Solution;
impl Solution {
    // We iterate voer x values until x satisfies (T+1)^x >= N, once the equation
    // is satisfied, x is the value we are looking for. Instead of calculating
    // iterations**x at every step, we remember the previous value
    // iterations^x-1 and we multiply once more by iterations.
    // It should be possible to optimize even further if we obtained the
    // most significant bit of iterations and used bit shifting with
    // multiplication by a smaller number in each iteration.
    //
    // Time complexity: O(log(n)) - Each iteration we check buckets against
    // the power of x.
    // Space complexity: O(1) - Constant extra space.
    //
    // Runtime 0 ms Beats 100%
    // Memory 2 MB Beats 100%
    pub fn poor_pigs(buckets: i32, minutes_to_die: i32, minutes_to_test: i32) -> i32 {
        if buckets < 2 {
            return 0;
        }
        let mut x = 1;
        let iterations = minutes_to_test / minutes_to_die + 1;
        let mut can_test = iterations;
        while can_test < buckets {
            can_test *= iterations;
            x += 1;
        }
        x
    }
}

// Tests.
fn main() {
    let tests = [(4, 15, 30, 2), (4, 15, 15, 2), (1000, 15, 60, 5)];
    for test in tests {
        assert_eq!(Solution::poor_pigs(test.0, test.1, test.2), test.3);
    }
    println!("All tests passed!")
}
