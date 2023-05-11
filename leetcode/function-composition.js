// 2629. Function Composition
// 🟢 Easy
//
// https://leetcode.com/problems/function-composition/
//
// Tags: Javascript

// Recursively call the functions from the back of the array until there are
// no function. We can use both a loop and recursion.
//
// Time complexity: O(n)
// Space complexity: O(1) - O(n) if we used recursion because each of the
// n calls would be stored in the call stack.
//
// Runtime 70 ms Beats 68.20%
// Memory 43.7 MB Beats 15.53%
/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
  return function (x) {
    while (functions.length > 0) {
      x = functions.pop()(x);
    }
    return x;
  };
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
