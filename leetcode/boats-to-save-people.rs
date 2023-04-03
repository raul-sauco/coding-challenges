// 881. Boats to Save People
// 🟠 Medium
//
// https://leetcode.com/problems/boats-to-save-people/
//
// Tags: Array - Two Pointers - Greedy - Sorting

struct Solution;
impl Solution {
    /// Sort the weights of the people that we need to save, then use two
    /// pointers, one for the heaviest person that needs to be saved and one
    /// for the lightest, if we can put them together on a boat, do so and
    /// shift both pointers, otherwise put the heaviest person alone in a boat
    /// and move only that pointer. This works because if the heaviest person
    /// cannot go on the boat together with the current lightest person, we
    /// know that it cannot also go with any other.
    ///
    /// Time complexity: O(n*log(n)) - Sorting has the most complexity, then
    /// arranging people on boats we can do in O(n).
    /// Space complexity: O(log(n)) - Sorting memory complexity in Rust.
    ///
    /// Runtime 10 ms Beats 100%
    /// Memory 2.5 MB Beats 92.31%
    pub fn num_rescue_boats(people: Vec<i32>, limit: i32) -> i32 {
        let mut weights = people.clone();
        weights.sort_unstable();
        weights.reverse();
        let (mut l, mut r) = (0, people.len() - 1);
        while l <= r {
            if weights[l] + weights[r] <= limit {
                r -= 1;
            }
            l += 1;
        }
        l as i32
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1, 2], 3, 1),
        (vec![3, 1, 7], 7, 2),
        (vec![3, 2, 2, 1], 3, 3),
        (vec![3, 5, 3, 4], 5, 4),
    ];
    for t in tests {
        assert_eq!(Solution::num_rescue_boats(t.0, t.1), t.2);
    }
    println!("\x1b[92m» All tests passed!\x1b[0m")
}
