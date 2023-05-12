// 2666. Allow One Function Call
// 🟢 Easy
//
// https://leetcode.com/problems/allow-one-function-call/
//
// Tags: Javascript

// Preserve one boolean value with internal state that determines whether the
// funcion has been called already once, when called, if it is the first call,
// return the result of calling fn with the given arguments, if it is not the
// first call, do not return anything, which is the same as explicitly
// returning undefined. Use `apply` to pass the caller's context to fn.
//
// Time complexity: O(1)
// Space complexity: O(1)
//
// Runtime 68 ms Beats 8.32%
// Memory 41.6 MB Beats 90.70%

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {
  let called = false;
  return function (...args) {
    if (!called) {
      called = true;
      // Preserve the caller's context.
      return fn.apply(this, args);
    }
  };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
