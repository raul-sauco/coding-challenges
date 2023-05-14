// 2632. Curry
// 🟠 Medium
//
// https://leetcode.com/problems/curry/
//
// Tags: Javascript

// Keep state inside the function, add the call arguments to an internal
// array until its size matches the number of parameters of the given function
// then call the function with the given parameters and return the result.
//
// Time complexity: O(n) - Where n is the number of calls, all calls are
// resolved in O(1) time, assuming that the function called is O(1) like in the
// examples given.
// Space complexity: O(n) - Each call with new parameters adds one, or multiple
// entries to the array.
//
// Runtime 79 ms Beats 19.80%
// Memory 49 MB Beats 12.4%
/**
 * @param {Function} fn
 * @return {Function}
 */
const curry = function (fn) {
  let params = [];
  return function curried(...args) {
    params = [...params, ...args];
    if (fn.length === params.length) {
      const res = fn(...params);
      params = [];
      return res;
    } else {
      return curried;
    }
  };
};

// Recursively call the curried function until the number of arguments and
// parameters match.
//
// Time complexity: O(n) - Where n is the number of calls, all calls are
// resolved in O(1) time, assuming that the function called is O(1) like in the
// examples given.
// Space complexity: O(n) - Each call with new parameters adds one entry to the
// call stack.
//
// Runtime 74 ms Beats 39.12%
// Memory 48.9 MB Beats 15.55%
/**
 * @param {Function} fn
 * @return {Function}
 */
const curry_2 = function (fn) {
  return function curried(...args) {
    return args.length >= fn.length
      ? fn(...args)
      : (...newArgs) => curried(...args, ...newArgs);
  };
};
/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
