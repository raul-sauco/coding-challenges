// 2693. Call Function with Custom Context
// 🟠 Medium
//
// https://leetcode.com/problems/call-function-with-custom-context/
//
// Tags: Javascript

// Use the `apply` function.
//
// Time complexity: O(1) - It just sets the context.
// Space complexity: O(1) - No extra memory used.
//
// Runtime 60 ms Beats 60.81%
// Memory 42 MB Beats 66.98%
/**
 * @param {Object} context
 * @param {any[]} args
 * @return {any}
 */
Function.prototype.callPolyfill = function (context, ...args) {
  return this.apply(context, args);
};

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
