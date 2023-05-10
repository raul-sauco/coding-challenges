// 2626. Array reduce Transformation
// 🟢 Easy
//
// https://leetcode.com/problems/array-reduce-transformation/
//
// Tags: Javascript

// Use the function parameter as the inner variable that we will mutate as we
// compute the reduce of result. For each of the values in the input array,
// call the reduce function and assign the result to `init`.
//
// Time complexity: O(1)
// Space complexity: O(1)
//
// Runtime 67 ms Beats 24.80%
// Memory 44.2 MB Beats 18.41%
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function (nums, fn, init) {
  for (let num of nums) {
    init = fn(init, num);
  }
  return init;
};
