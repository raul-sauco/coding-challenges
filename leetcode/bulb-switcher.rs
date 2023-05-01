// 319. Bulb Switcher
// 🟠 Medium
//
// https://leetcode.com/problems/bulb-switcher/
//
// Tags: Math - Brain Teaser

struct Solution;
impl Solution {
    /// The perfect squares will remain on after n number of toggles, we can
    /// compute the number of perfect squares as the floor of the sqrt of n,
    /// which we can find using binary search, since the problem tells us that
    /// n <= 10^9, we can use its square root as the right boundary.
    ///
    /// Time complexity: O(1) - The loop can run a maximum of 16 times.
    /// Space complexity: O(1) - We use constant extra memory.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 100%
    pub fn bulb_switch(n: i32) -> i32 {
        let n = n as usize;
        let (mut l, mut r) = (0, 31622.min(n));
        while l <= r {
            let mid = (l + r) / 2;
            if mid * mid > n {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        r as i32
    }
}

// Tests.
fn main() {
    let tests = [(0, 0), (8, 2), (2147483647, 31622)];
    for t in tests {
        assert_eq!(Solution::bulb_switch(t.0), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m");
}
