// 2677. Chunk Array
// 🟠 Medium
//
// https://leetcode.com/problems/chunk-array/
//
// Tags: Javascript

// Iterate over the input array creating chunks of the given size and adding
// them to the result one at a time.
//
// Time complexity: O(n) - We will push every element of the input into the
// output array.
// Space complexity: O(n) - If we take into consideration the output array, or
// O(1) if we do not.
//
// Runtime 62 ms Beats 66.87%
// Memory 44.8 MB Beats 28.33%
/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function (arr, size) {
  let res = [];
  let i = 0;
  while (i < arr.length) {
    let cur = [];
    while (cur.length < size && i < arr.length) {
      cur.push(arr[i]);
      i++;
    }
    res.push(cur);
  }
  return res;
};
