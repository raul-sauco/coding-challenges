// 1371. Find the Longest Substring Containing Vowels in Even Counts
// 🟠 Medium
//
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
//
// Tags: Hash Table - String - Bit Manipulation - Prefix Sum

struct Solution;
impl Solution {
    /// Use 5 bits to store even/uneven count of the 5 vowels we are interested on. For each one of
    /// the possible 32 (2^5) combinations of values, store in an array the first position at which
    /// we saw it. Initialize the array with the value 31 "11111" pointing to the position before
    /// the start of the array => -1. To simplify things, I will use 0 and then shift forward all
    /// the other indexes by 1.
    /// We then iterate over the characters in the input string, compute the current running xor
    /// and check if it has been seen before, if yes, the vowels are all in even pairs between any
    /// index we have seen the same xor at, we are only interested on the first one because it will
    /// give us the longest substring, and the current one, we max that value with the current max.
    /// If we have not seen this xor before, we store it pointing to its current position.
    /// I have used usize::MAX to flag uninitialized array elements, using Option<i32> set no None
    /// would have been better, and using i32 for the position would have let us use the non
    /// modified indexes, which would make the code more readable, but I choose this way to save on
    /// some casting to usize to use as indexes.
    ///
    /// Time complexity: O(n) - We visit each element and do O(1) work for each.
    /// Space complexity: O(1) - We store an array of 32 elements and 2 usizes, all in the stack.
    ///
    /// Runtime 3 ms Beats 100%
    /// Memory 3.04 MB Beats 92%
    pub fn find_the_longest_substring(s: String) -> i32 {
        let mut current_xor = usize::from_str_radix("11111", 2).expect("Wrong binary number");
        // There are only 32 possible values of current_xor.
        let mut lookup = [usize::MAX; 32];
        let mut res = 0;
        lookup[current_xor] = 0;
        for (pos, c) in s.chars().enumerate() {
            match c {
                'a' => current_xor ^= 1 << 4,
                'e' => current_xor ^= 1 << 3,
                'i' => current_xor ^= 1 << 2,
                'o' => current_xor ^= 1 << 1,
                'u' => current_xor ^= 1,
                _ => (),
            }
            // If we have seen it before, the xor between this two positions will be 31, all vowels
            // between them will be in even pairs.
            if lookup[current_xor] != usize::MAX {
                res = res.max(pos - lookup[current_xor] + 1);
                // let prev = lookup[current_xor];
                // let size = pos - lookup[current_xor];
                // println!(
                //     "{pos}:{c}:{current_xor:b} Matched prev position {prev}. Length is {size}"
                // );
            } else {
                // If this is the first time we see this XOR value, store it to match later.
                lookup[current_xor] = pos + 1;
                // println!("{pos}:{c}:{current_xor:b} Did not match. Inserting at {pos}");
            }
        }
        res as _
    }
}

// Tests.
fn main() {
    let tests = [
        ("c", 1),
        ("e", 0),
        ("ec", 1),
        ("aaaaaa", 6),
        ("bcbcbc", 6),
        ("leetcodeisgreat", 5),
        ("eleetminicoworoep", 13),
    ];
    println!("\n\x1b[92m» Running {} tests...\x1b[0m", tests.len());
    let mut success = 0;
    for (i, t) in tests.iter().enumerate() {
        let res = Solution::find_the_longest_substring(t.0.to_string());
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
