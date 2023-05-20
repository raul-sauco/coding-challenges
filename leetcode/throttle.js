// 2676. Throttle
// 🟠 Medium
//
// https://leetcode.com/problems/throttle/
//
// Tags: Javascript

// Keep two nullable values, one with a timeout id and another one with call
// arguments. When we get a call, if a timeout is in curse, we overwrite the
// previous stored arguments with the last call's arguments, when the timeout
// concludes, we call the throttled function with these arguments. If a call
// comes when there is no timeout in place, call it immediately and create a
// timeout.
//
// Time complexity: O(1) - Each call is processed in O(1) if the caller has
// O(1) time complexity.
// Space complexity: O(1) - The function only stores a timeout id and args.
//
// Runtime 65 ms Beats 40.92%
// Memory 42.1 MB Beats 47.85%
/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function (fn, t) {
  let to = null;
  let storedArgs = null;
  const callback = () => {
    if (storedArgs) {
      fn(...storedArgs);
      storedArgs = null;
      to = setTimeout(callback, t);
    } else {
      to = null;
    }
  };
  return function (...args) {
    if (to === null) {
      fn(...args);
      to = setTimeout(callback, t);
    } else {
      storedArgs = args;
    }
  };
};
/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
