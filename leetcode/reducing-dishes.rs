// 1402. Reducing Dishes
// 🔴 Hard
//
// https://leetcode.com/problems/reducing-dishes/
//
// Tags: Array - Dynamic Programming - Greedy - Sorting

struct Solution;
impl Solution {
    /// Solving the problem efficiently becomes easy once we make a few
    /// observations, it is always better to take all positive values, it is
    /// also always better to put greater values to the right, so we can start
    /// by taking all positive values sorted and multiplied by their indexes + 1
    /// Then, every time we add a negative value, it is better to pick the
    /// greater one (closer to zero) and try it on the furthest left index, 0.
    /// The result of adding that value will be adding the negative value * 1 to
    /// the result, and shifting all the previous values to the right one
    /// position, which we can compute as being equal to the current sum of
    /// values in the vector. If the result of adding this value is a gain, do
    /// it, otherwise, stop trying to add values and return the result.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the positive and negative values
    /// vectors has the highest complexity, everything else is O(n) we iterate
    /// over the values to split them into positive and negative, iterate over
    /// the positive values to create the initial sum and result and then
    /// iterate over the negative values checking if it is worth adding them in
    /// O(1) time.
    /// Space complexity: O(n) - The positive and negative vectors.
    ///
    /// Runtime 1 ms Beats 71.43%
    /// Memory 2.1 MB Beats 64.29%
    pub fn max_satisfaction(satisfaction: Vec<i32>) -> i32 {
        // Split positive and negative values into two arrays and sort them.
        let (mut pos, mut neg) = (vec![], vec![]);
        for val in satisfaction {
            if val < 0 {
                neg.push(val);
            } else {
                pos.push(val);
            }
        }
        neg.sort();
        pos.sort();
        let (mut res, mut current_sum) = (0, 0);
        for (i, val) in pos.iter().enumerate() {
            res += val * (i + 1) as i32;
            current_sum += val;
        }
        for val in neg.iter().rev() {
            // We want to add this value at index 0 and shift all other values,
            // it will decrease the result by its own value.
            // And we will shift all values to the right one index, that results
            // in multiplying the value by an integer 1 position greater than
            // we did before, we can easily do that computation by adding the
            // sum of values to the result, check if that is greater than the
            // value.
            if current_sum > -*val {
                res += current_sum + val;
                current_sum += val;
            } else {
                // Once the loss is greater than the gain, we can stop iterating
                // because the negative values to the left are smaller.
                break;
            }
        }
        res
    }

    /// A simplification of the previous solution where we sort all the values
    /// and remove the smallest ones while that results in a net gain.
    ///
    /// Time complexity: O(n*log(n)) - Sorting the positive and negative values
    /// vectors has the highest complexity, everything else is O(n) we iterate
    /// over the values to split them into positive and negative, iterate over
    /// the positive values to create the initial sum and result and then
    /// iterate over the negative values checking if it is worth adding them in
    /// O(1) time.
    /// Space complexity: O(n) - The positive and negative vectors.
    ///
    /// Runtime 1 ms Beats 71.43%
    /// Memory 2 MB Beats 92.86%
    pub fn max_satisfaction_one_loop(satisfaction: Vec<i32>) -> i32 {
        // Get a mutable local copy of the input and sort it. O(n*log(n)).
        let mut satisfaction = satisfaction;
        satisfaction.sort();
        let (mut current_sum, mut res) = (0, 0);
        for val in satisfaction.iter().rev() {
            if current_sum > -*val {
                res += current_sum + val;
                current_sum += val;
            } else {
                break;
            }
        }
        res
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![1], 1),
        (vec![4, 3, 2], 20),
        (vec![-1, -4, -5], 0),
        (vec![-1, -8, 0, 5, -9], 14),
    ];
    for t in tests {
        assert_eq!(Solution::max_satisfaction(t.0.clone()), t.1);
        assert_eq!(Solution::max_satisfaction_one_loop(t.0), t.1);
    }
    println!("All tests passed!")
}
