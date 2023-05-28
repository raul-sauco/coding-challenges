// 1406. Stone Game III
// 🔴 Hard
//
// https://leetcode.com/problems/stone-game-iii/
//
// Tags: Array - Math - Dynamic Programming - Game Theory

struct Solution;

impl Solution {
    /// The problem is a zero-sum game where both Alice and Bob are getting as
    /// many points as they can in each turn, and the turns alternate. We can
    /// determine that, from each position, each player will pick one, of the
    /// three possible results, that gives them the maximum score. Since the
    /// game is a zero sum game, we can keep track of the point difference
    /// between the two players after each play, and we can compute that
    /// difference for play starting at index i as the points obtained from
    /// picking 1..=3 stones minus the point difference given by the rest of
    /// the array knowing that the other player will also play optimally.
    ///
    /// Time complexity: O(n) - We visit the values in the input array one time
    /// each, in reverse, and do O(1) work for each since we are caching the
    /// results in the dp array.
    /// Space complexity: O(1) - The dp array has a fixed size of 3, we are
    /// also using an array, instead of a vector, to optimize by storing it in
    /// the stack instead of being forced to use the heap.
    ///
    /// Runtime 38 ms Beats 66.67%
    /// Memory 2.4 MB Beats 100%
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        let mut dp = [0, 0, 0];
        for i in (0..stone_value.len()).rev() {
            let mut best = i32::MIN;
            for j in 1..=3 {
                if i + j <= stone_value.len() {
                    best = best.max(stone_value[i..i + j].iter().sum::<i32>() - dp[(i + j) % 3]);
                }
            }
            dp[i % 3] = best;
        }
        String::from(if dp[0] < 0 {
            "Bob"
        } else if dp[0] == 0 {
            "Tie"
        } else {
            "Alice"
        })
    }

    /// Same logic as the previous example but using iterators.
    ///
    /// Time complexity: O(n) - We visit the values in the input array one time
    /// each, in reverse, and do O(1) work for each since we are caching the
    /// results in the dp array.
    /// Space complexity: O(1) - The dp array has a fixed size of 3, we are
    /// also using an array, instead of a vector, to optimize by storing it in
    /// the stack instead of being forced to use the heap.
    ///
    /// Runtime 34 ms Beats 66.67%
    /// Memory 2.4 MB Beats 100%
    pub fn stone_game_iii_it(stone_value: Vec<i32>) -> String {
        match (0..stone_value.len()).rev().fold([0; 3], |dp, i| {
            let next_score = (0..3)
                .map(|j| stone_value[i..].iter().take(j + 1).sum::<i32>() - dp[j])
                .max()
                .unwrap();
            [next_score, dp[0], dp[1]]
        })[0]
        {
            0 => "Tie",
            score if score > 0 => "Alice",
            _ => "Bob",
        }
        .to_string()
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2, 3, 6], String::from("Tie")),
        (vec![1, 2, 3, 7], String::from("Bob")),
        (vec![1, 2, 3, -9], String::from("Alice")),
    ];
    for t in tests {
        assert_eq!(Solution::stone_game_iii(t.0.clone()), t.1);
        assert_eq!(Solution::stone_game_iii_it(t.0.clone()), t.1);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
