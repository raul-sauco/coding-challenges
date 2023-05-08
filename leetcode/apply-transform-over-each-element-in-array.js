// 2635. Apply Transform Over Each Element in Array
// 🟢 Easy
//
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/
//
// Tags: Javascript

// Use array.prototype.map since it does what the problem asks.
//
// Time complexity: O(n)
// Space complexity: O(n)
//
// Runtime 57 ms Beats 63.25%
// Memory 42.4 MB Beats 47.49%
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
const map = (arr, fn) => arr.map(fn);

// Use a for loop, to improve performance, we can use a typed array.
//
// Time complexity: O(n)
// Space complexity: O(n)
//
// Runtime 54 ms Beats 77.98%
// Memory 42.4 MB Beats 47.49%
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
const map2 = function (arr, fn) {
  let res = new Int32Array(arr.length);
  for (let i = 0; i < arr.length; ++i) {
    res[i] = fn(arr[i], i);
  }
  return res;
};
