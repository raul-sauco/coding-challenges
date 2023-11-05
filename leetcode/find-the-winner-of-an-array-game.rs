// 1535. Find the Winner of an Array Game
// 🟠 Medium
//
// https://leetcode.com/problems/find-the-winner-of-an-array-game/
//
// Tags: Array - Simulation


struct Solution;
impl Solution {
    /// Use a variable to store the current winner and the number of wins, if
    /// we get to k wins, return the current winner. If we get first to the end
    /// of the input array (n) also return the current winner, because we are
    /// guaranteed to have the array maximum, so it will win all next rounds.
    ///
    /// Time complexity: O(n) - We visit n elements and do constant time work
    /// for each.
    /// Space complexity: O(1) - We store to integers.
    ///
    /// Runtime 7 ms Beats 100%
    /// Memory 3.34 MB Beats 66.67%
    pub fn get_winner(arr: Vec<i32>, k: i32) -> i32 {
        let mut winner = [arr[0], 0];
        for num in arr.into_iter().skip(1) {
            if num > winner[0] {
                winner = [num, 0];
            }
            winner[1] += 1;
            if winner[1] == k {
                break;
            }
        }
        winner[0]
    }
}

// Tests.
fn main() {
    let tests = [(vec![2, 1, 3, 5, 4, 6, 7], 2, 5), (vec![3, 2, 1], 10, 3)];
    for t in tests {
        assert_eq!(Solution::get_winner(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
