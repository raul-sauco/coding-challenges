// 2275. Largest Combination With Bitwise AND Greater Than Zero
// 🟠 Medium
//
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
//
// Tags: Array - Hash Table - Bit Manipulation - Counting

struct Solution;
impl Solution {
    /// Iterate over the candidates keeping track of which bits are set using an array to keep
    /// count of how many candidates have the bit in each of the 24 possible possitons set, we
    /// will be able to AND these values.
    ///
    /// Time complexity: O(m*n) - Where m is the number of candidates and n is the log2 of the
    /// largest candidate, since it is limited to a max of 24, we can consider the total O(m).
    /// Space complexity: O(1) - We use an array of size 24.
    ///
    /// Runtime 24 ms Beats 100%
    /// Memory 3.52 MB Beats 9%
    #[allow(dead_code)]
    pub fn largest_combination_loop(candidates: Vec<i32>) -> i32 {
        // We get the maximum number of bits from the problem constrains. <= 10^7
        // let m = 10000000usize.ilog2() as usize + 1;
        // Use a fixed 24 value to be able to use an array instead of a vector.
        let mut bit_set_count = vec![0i32; 24];
        for candidate in candidates {
            for i in 0..24 {
                if candidate & 1 << i > 0 {
                    bit_set_count[i] += 1;
                }
            }
        }
        bit_set_count.into_iter().max().unwrap()
    }

    /// Same solution using an iterator.
    ///
    /// Runtime 22 ms Beats 100%
    /// Memory 3.52 MB Beats 9%
    pub fn largest_combination(candidates: Vec<i32>) -> i32 {
        candidates
            .into_iter()
            .fold([0i32; 24], |mut acc, c| {
                for i in 0..24 {
                    if c & 1 << i > 0 {
                        acc[i] += 1;
                    }
                }
                acc
            })
            .into_iter()
            .max()
            .unwrap()
    }
}

// Tests.
fn main() {
    let tests = [(vec![16, 17, 71, 62, 12, 24, 14], 4), (vec![8, 8], 2)];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::largest_combination(t.0.clone());
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
