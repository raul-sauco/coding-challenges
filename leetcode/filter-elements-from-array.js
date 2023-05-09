// 2634. Filter Elements from Array
// 🟢 Easy
//
// https://leetcode.com/problems/filter-elements-from-array/
//
// Tags: Javascript

// Provide a filter function not using Array.prototype.filter.:
//
// Time complexity: O(1)
// Space complexity: O(1)
//
// Runtime 66 ms Beats 14.9%
// Memory 41.4 MB Beats 97.8%
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  const res = [];
  for (let i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      res.push(arr[i]);
    }
  }
  return res;
};
