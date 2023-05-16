// 2637. Promise Time Limit
// 🟢 Easy
//
// https://leetcode.com/problems/promise-time-limit/
//
// Tags: Javascript

// Return a new promise, the promise sets a timeout that executes after time t
// and will reject with the required message. If the function is called before
// the timeout, it will be called and it will run normally, resolving if the
// call is succesful and rejecting if there is an error.
//
// Time complexity: O(1) - The code will wait millis second in a non-blocking
// way.
// Space complexity: O(1) - Each call only creates one timeout object.
//
// Runtime 57 ms Beats 75.67%
// Memory 41.6 MB Beats 86.14%
/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function (fn, t) {
  return async function (...args) {
    return new Promise(async (res, rej) => {
      // Weird bug makes window.setTimeout() fail, probably due to LeetCode
      // runtime env, if it actually isn't or emulates a browser, the window
      // object may not exist.
      const timeout = setTimeout(() => rej("Time Limit Exceeded"), t);
      try {
        const result = await fn(...args);
        res(result);
      } catch (err) {
        rej(err);
      } finally {
        clearTimeout(timeout);
      }
    });
  };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
