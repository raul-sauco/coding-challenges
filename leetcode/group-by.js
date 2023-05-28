// 2631. Group By
// 🟠 Medium
//
// https://leetcode.com/problems/group-by/
//
// Tags: Javascript

// Use the provided function to get the key that corresponds to each element
// of the `this` array, if the key does not exist in the result object, add it
// pointing to an empty array. Push the current element into the array of
// elements referenced by the current key.
//
// Time complexity: O(n) - One conditional check and one access by index.
// Space complexity: O(n) - If we take into consideration the output object, or
// O(1) if we do not.
//
// Runtime 149 ms Beats 48.77%
// Memory 65.8 MB Beats 29.54%
/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function (fn) {
  let result = {};
  this.forEach((item) => {
    const key = fn(item);
    if (!result.hasOwnProperty(key)) {
      result[key] = [];
    }
    result[key].push(item);
  });
  return result;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
