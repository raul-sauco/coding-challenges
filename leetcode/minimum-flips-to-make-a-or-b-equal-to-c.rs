// 1318. Minimum Flips to Make a OR b Equal to c
// 🟠 Medium
//
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
//
// Tags: Bit Manipulation

struct Solution;
impl Solution {
    /// Iterate over the least significant bit of the input values, check how
    /// many operations would take to make that bit in a or b == the bit in c,
    /// then right shift the three values by one and do it again.
    ///
    /// Time complexity: O(log(n)) - We iterate over the number of binary
    /// digits in the biggest value in the input, that is log2(n) where n is
    /// the largest value in the input.
    /// Space complexity: O(1) - We only store five integer values.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2 MB Beats 88.24%
    pub fn min_flips(a: i32, b: i32, c: i32) -> i32 {
        let mut res = 0;
        let (mut a, mut b, mut c) = (a, b, c);
        let (mut ab, mut bb, mut cb): (i32, i32, i32);
        while a != 0 || b != 0 || c != 0 {
            ab = a & 1;
            a >>= 1;
            bb = b & 1;
            b >>= 1;
            cb = c & 1;
            c >>= 1;
            match cb {
                1 => {
                    if ab == 0 && bb == 0 {
                        res += 1;
                    }
                }
                0 => {
                    res += ab + bb;
                }
                _ => unreachable!(),
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [(2, 6, 5, 3), (4, 2, 7, 1), (1, 2, 3, 0)];
    for t in tests {
        assert_eq!(Solution::min_flips(t.0, t.1, t.2), t.3);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
