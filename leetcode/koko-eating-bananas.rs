// 875. Koko Eating Bananas
// 🟠 Medium
//
// https://leetcode.com/problems/koko-eating-bananas/
//
// Tags: Array - Binary Search

struct Solution;
impl Solution {
    // We need to take a guess of how many bananas Koko can eat in the given
    // amount of time and then check if the guess is correct, we can use
    // binary search to speed the process.
    //
    // Time complexity: O(p*log(b)) - Where p is the number of piles, we iterate
    // up to p piles every time we take a guess. and b is the number of bananas
    // in the biggest pile, we start with b as our right boundary and reduce the
    // search space in half at each guess.
    // Space complexity: O(1)
    //
    // Runtime 7 ms Beats 97.22%
    // Memory 2.3 MB Beats 88.89%
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        // Upper and lower k boundaries.
        let (mut l, mut r) = (1, *piles.iter().max().unwrap());
        // Declare a few variables outside the loop.
        let mut guess;
        while l < r {
            guess = l + (r - l) / 2;
            // If Koko can eat all the bananas in guess time shrink right.
            if piles.iter().fold(h, |acc, x| acc - (x + guess - 1) / guess) >= 0 {
                r = guess;
            } else {
                l = guess + 1;
            }
        }
        l
    }
}

// Tests.
fn main() {
    let tests = [
        (vec![3], 10, 1),
        (vec![3, 6, 7, 11], 8, 4),
        (vec![30, 11, 23, 4, 20], 5, 30),
        (vec![30, 11, 23, 4, 20], 6, 23),
        (
            vec![
                332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673,
                679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097,
                692137887, 718203285, 629455728, 941802184,
            ],
            823855818,
            14,
        ),
    ];
    for test in tests {
        assert_eq!(Solution::min_eating_speed(test.0, test.1), test.2);
    }
    println!("All tests passed!")
}
