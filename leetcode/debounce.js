// 2627. Debounce
// 🟠 Medium
//
// https://leetcode.com/problems/debounce/
//
// Tags: Javascript

// Keep a variable with the current timeout, if any, when a new call comes, we
// cancel the previous timeout and create a new one, any timeout that executes
// will call the given function.
//
// Time complexity: O(1) - Each call is processed in O(1).
// Space complexity: O(1) - The function only stores a timeout id.
//
// Runtime 61 ms Beats 55.97%
// Memory 42.1 MB Beats 32.10%
/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function (fn, t) {
  let timeout = null;
  return function (...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => fn(...args), t);
  };
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
