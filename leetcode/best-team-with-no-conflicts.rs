// 1626. Best Team With No Conflicts
// 🟠 Medium
//
// https://leetcode.com/problems/best-team-with-no-conflicts/
//
// Tags: Array - Dynamic Programming - Sorting

struct Solution;
impl Solution {
    // Once we sort the players by score, this problem becomes obtaining the
    // sum of scores of players up to, and including, a given age that we
    // have seen already. That makes this problem similar to range sum
    // query mutable in that we need to efficiently update elements in an
    // array and query sum ranges at that point, before we add any player
    // with a higher score.
    //
    // Time complexity: O(n*log(a)) - Where n is the number of players and a
    // is the max age in the input and it is limited to a max a 1000.
    // Space complexity: O(n) - The sorted players array has the same size as
    // the input, the binary indexed tree has size max(ages).
    //
    // Runtime 5 ms Beats 100%
    // Memory 2.2 MB Beats 100%
    pub fn best_team_score(scores: Vec<i32>, ages: Vec<i32>) -> i32 {
        // Zip scores and ages together, using scores as the first element, we want the
        // binary indexed tree to be indexed by ages because they max out at an order
        // of magnitude lower than scores.$
        let mut sa = scores.iter().zip(ages.iter()).collect::<Vec<_>>();
        // Sort the tuples by score first then age.
        sa.sort_unstable();
        let mut bit = vec![0; (ages.iter().max().unwrap() + 1) as usize];
        // Define a function that updates the binary indexed tree with
        // the best score currently possible using players up to age age.
        fn update_bit(age: i32, score: i32, bit: &mut Vec<i32>) {
            let mut idx = age;
            while (idx as usize) < bit.len() {
                bit[idx as usize] = bit[idx as usize].max(score);
                idx += idx & (-idx);
            }
        }
        // Get the best score of a team composed of members up to, and including, age.
        fn query_bit(age: i32, bit: &mut Vec<i32>) -> i32 {
            let mut idx = age;
            let mut best = 0;
            while idx > 0 {
                let current = bit[idx as usize];
                if current > best {
                    best = current;
                }
                idx -= idx & (-idx);
            }
            best
        }
        let mut res = 0;
        for (score, age) in sa {
            let best_score = score + query_bit(*age, &mut bit);
            // Use the best possible score with this max age to update the bit.
            update_bit(*age, best_score, &mut bit);
            if best_score > res {
                res = best_score;
            }
        }
        res
    }
}

// Tests.
fn main() {
    assert_eq!(
        Solution::best_team_score(vec![4, 5, 6, 5], vec![2, 1, 2, 1]),
        16
    );
    assert_eq!(
        Solution::best_team_score(vec![1, 2, 3, 5], vec![8, 9, 10, 1]),
        6
    );
    assert_eq!(
        Solution::best_team_score(vec![1, 3, 5, 10, 15], vec![1, 2, 3, 4, 5]),
        34
    );
    println!("All tests passed!")
}
