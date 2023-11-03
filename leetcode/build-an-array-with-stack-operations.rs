// 1441. Build an Array With Stack Operations
// 🟠 Medium
//
// https://leetcode.com/problems/build-an-array-with-stack-operations/
//
// Tags: Array - Stack - Simulation

struct Solution;
impl Solution {
    /// Have an iterator over the values in target while keeping a reference to
    /// the last value that the stream n has produced, while the next value does
    /// not match the stream, push and pop, once it matches, push and move onto
    /// the next value in target.
    ///
    /// Time complexity: O(min(m,n)) - Where m is the size of target, we iterate
    /// over the values in target, the inner loop iterates over the values in 1..n
    /// until it finds the next match.
    /// Space complexity: O(1) - Constant space if we don't consider the output
    /// vector.
    ///
    /// Runtime 1 ms Beats 84.62%
    /// Memory 2.08 MB Beats 76.92%
    pub fn build_array(target: Vec<i32>, n: i32) -> Vec<String> {
        let mut res = vec![];
        let (push, pop) = ("Push", "Pop");
        let mut it = 1..=n;
        for num in target {
            while it.next().unwrap() < num {
                res.push(push.to_string());
                res.push(pop.to_string());
            }
            res.push(push.to_string());
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            vec![1, 3],
            3,
            vec![
                "Push".to_string(),
                "Push".to_string(),
                "Pop".to_string(),
                "Push".to_string(),
            ],
        ),
        (
            vec![1, 2, 3],
            3,
            vec!["Push".to_string(), "Push".to_string(), "Push".to_string()],
        ),
        (vec![1, 2], 4, vec!["Push".to_string(), "Push".to_string()]),
    ];
    for t in tests {
        assert_eq!(Solution::build_array(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
