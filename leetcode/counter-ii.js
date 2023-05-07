// 2665. Counter II
// 🟢 Easy
//
// https://leetcode.com/problems/counter-ii/
//
// Tags: Javascript

// Use the parameter as state inside the closure and add another variable
// initialized with the same value, return an object with the three functions
// that the problem asks for.
//
// Time complexity: O(1)
// Space complexity: O(1)
//
// Runtime 69 ms Beats 46.34%
// Memory 44.9 MB Beats 40.38%
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
  let n = init;
  return {
    increment: () => ++n,
    decrement: () => --n,
    reset: () => (n = init),
  };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
