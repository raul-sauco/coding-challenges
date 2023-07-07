// 2024. Maximize the Confusion of an Exam
// 🟠 Medium
//
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
//
// Tags: String - Binary Search - Sliding Window - Prefix Sum

struct Solution;
impl Solution {
    /// Use a sliding window technique where we compute two max windows, in one
    /// we can have a maximum of k "T" values, in the other a maximum of k "F"
    /// values, we increase on the right, then shrink each window while the
    /// condition is not met, and then update the max window size if needed.
    ///
    /// Time complexity: O(n) - We visit each element and do O(1) work for each.
    /// Space complexity: O(n) - The chars vector has one element for each
    /// character in the input string. In another language where we could access
    /// the characters by index, we could use O(1) space.
    ///
    /// Runtime 9 ms Beats 80%
    /// Memory 2.3 MB Beats 20%
    pub fn max_consecutive_answers(answer_key: String, k: i32) -> i32 {
        let k = k as usize;
        let mut max_length = 0;
        let (mut true_left, mut false_left) = (0, 0);
        let (mut true_count, mut false_count) = (0, 0);
        let chars: Vec<_> = answer_key.chars().collect();
        let (mut true_window_size, mut false_window_size);
        for r in 0..chars.len() {
            if chars[r] == 'T' {
                true_count += 1;
            } else {
                false_count += 1;
            }
            while true_count > k {
                if chars[false_left] == 'T' {
                    true_count -= 1;
                }
                false_left += 1
            }
            false_window_size = r - false_left + 1;
            if false_window_size > max_length {
                max_length = false_window_size;
            }
            while false_count > k {
                if chars[true_left] == 'F' {
                    false_count -= 1;
                }
                true_left += 1;
            }
            true_window_size = r - true_left + 1;
            if true_window_size > max_length {
                max_length = true_window_size;
            }
        }
        max_length as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (String::from("TTFF"), 2, 4),
        (String::from("TFFT"), 1, 3),
        (String::from("TTFTTFTT"), 1, 5),
    ];
    for t in tests {
        assert_eq!(Solution::max_consecutive_answers(t.0, t.1), t.2);
    }
    println!("[92m» All tests passed![0m")
}
