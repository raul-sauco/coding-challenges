// 1980. Find Unique Binary String
// 🟠 Medium
//
// https://leetcode.com/problems/find-unique-binary-string/
//
// Tags: Array - String - Backtracking

struct Solution;
impl Solution {
    /// Create a vector of size 2^n that flags which elements we have seen using them as the index
    /// for a position in the vector. After we mark all input nums as seen, we iterate over the
    /// flags vector and return the first false index as a padded binary string.
    ///
    /// Time complexity: O(n^2) - We iterate over n digits of n strings.
    /// Space complexity: O(n) - We use an extra vector of size n.
    ///
    /// Runtime 1 ms Beats 66.67%
    /// Memory 2.32 MB Beats 33.33%
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        let m = nums.len();
        let n = 2u32.pow(m as u32) as usize;
        let mut seen = vec![false; n];
        let mut num;
        for num_str in nums {
            num = usize::from_str_radix(&num_str, 2).ok().unwrap();
            seen[num] = true;
        }
        for i in 0..n {
            if !seen[i] {
                return format!("{:0width$b}", i, width = m);
            }
        }
        unreachable!()
    }

    /// The number of strings that we cannot use is much smaller than the pool of strings that we
    /// can use, simply start trying strings until we find one that we can use. We could generate
    /// them randomly as well and, if the pool was bigger, in this problem is limited to 16, we
    /// could use a hashset to check contains.
    ///
    /// Time complexity: O(n^2) - We iterate over n digits of n strings.
    /// Space complexity: O(n) - We use an extra vector of size n.
    ///
    /// Runtime 1 ms Beats 66.67%
    /// Memory 2.22 MB Beats 33.33%
    pub fn find_different_binary_string_random(nums: Vec<String>) -> String {
        let m = nums.len();
        let n = 2u32.pow(m as u32) as usize;
        let ints = nums
            .into_iter()
            .map(|x| usize::from_str_radix(&x, 2).ok().unwrap())
            .collect::<Vec<_>>();
        for i in 0..n {
            if !ints.contains(&i) {
                return format!("{:0width$b}", i, width = m);
            }
        }
        unreachable!()
    }

    /// Very neat idea, iterate over the input numbers, for each number, only consider one digit,
    /// for example the digit at the same index as the number in the input string, set the digit in
    /// the result at the same index to the opossite as that number, that way we guarantee that at
    /// least one digit in the result will be different to one digit in any of the input numbers.
    ///
    /// Time complexity: O(n^2) - We iterate over n digits of n strings. In other languages that
    /// allow for index access to strings, we could directly access one digit and use O(n) time.
    /// Space complexity: O(n) - We use an extra vector of size n.
    ///
    /// Runtime 0 ms Beats 100%
    /// Memory 2.04 MB Beats 66.67%
    pub fn find_different_binary_string_cantors(nums: Vec<String>) -> String {
        let n = nums.len();
        let mut res = String::with_capacity(n);
        for i in 0..n {
            for (j, c) in nums[i].chars().enumerate() {
                if i == j {
                    res.push(if c == '0' { '1' } else { '0' });
                    break;
                }
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        vec!["01", "10"],
        vec!["00", "01"],
        vec!["111", "011", "001"],
    ];
    for t in tests {
        assert!(!t.contains(
            &Solution::find_different_binary_string(t.iter().map(|x| x.to_string()).collect())
                .as_str()
        ));
        assert!(!t.contains(
            &Solution::find_different_binary_string_random(
                t.iter().map(|x| x.to_string()).collect()
            )
            .as_str()
        ));
        assert!(!t.contains(
            &Solution::find_different_binary_string_cantors(
                t.iter().map(|x| x.to_string()).collect()
            )
            .as_str()
        ));
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
