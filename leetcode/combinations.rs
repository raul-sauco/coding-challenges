// 77. Combinations
// 🟠 Medium
//
// https://leetcode.com/problems/combinations/
//
// Tags: Backtracking

struct Solution;
impl Solution {
    /// Use an internal function that iterates over all digits between the last
    /// digit added plus one and n adding each of them and checking the length
    /// of the resulting vector, if the vector has length k, add it to the
    /// result, otherwise call itself to add the next digit.
    ///
    /// Time complexity: O(k^n) - We iterate over k digit, for each digit, the
    /// decision tree branches into n options.
    /// Space complexity: O(k^n) - Each call to add_digit will add a new digit
    /// to the result and we saw the number of calls in the time complexity.
    ///
    /// Runtime 7 ms Beats 85.74%
    /// Memory 2.83 MB Beats 72.88%
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let mut res = vec![];
        fn add_digit(cur: &mut Vec<i32>, res: &mut Vec<Vec<i32>>, l: usize, n: usize, k: usize) {
            for i in l..=n {
                cur.push(i as i32);
                if cur.len() == k {
                    res.push(cur.clone());
                } else {
                    add_digit(cur, res, i + 1, n, k);
                }
                cur.pop();
            }
        }
        let mut cur = vec![];
        add_digit(&mut cur, &mut res, 1, n as usize, k as usize);
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (
            4,
            2,
            vec![
                vec![1, 2],
                vec![1, 3],
                vec![1, 4],
                vec![2, 3],
                vec![2, 4],
                vec![3, 4],
            ],
        ),
        (1, 1, vec![vec![1]]),
    ];
    for t in tests {
        assert_eq!(Solution::combine(t.0, t.1), t.2);
    }
    println!("[92m» All tests passed![0m")
}
