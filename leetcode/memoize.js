// 2623. Memoize
// 🟠 Medium
//
// https://leetcode.com/problems/memoize/
//
// Tags: Javascript

// Recursively call the functions from the back of the array until there are
// no function. We can use both a loop and recursion.
//
// Time complexity: O(n) - Where n is the number of calls, all calls are
// resolved in O(1) time.
// Space complexity: O(n) - Each call with new parameters adds one entry to the
// map.
//
// Runtime 328 ms Beats 94.41%
// Memory 101.7 MB Beats 28.16%
/**
 * @param {Function} fn
 */
function memoize(fn) {
  const cache = new Map();
  return function (...args) {
    // The code is guaranteed to run in the browser, we can use the JSON object.
    const k = JSON.stringify(args);
    if (!cache.has(k)) {
      cache.set(k, fn(...args));
    }
    return cache.get(k);
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
