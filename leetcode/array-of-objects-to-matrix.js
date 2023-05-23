// 2675. Array of Objects to Matrix
// 🟠 Medium
//
// https://leetcode.com/problems/array-of-objects-to-matrix/
//
// Tags: Javascript

// Get all the keys and use them to generate the header row of the matrix, then
// go through each object checking its values and adding them to their
// matching columns.
//
// Time complexity: O(n) - We visit each key in the input array, top level and
// nested, at least once.
// Space complexity: O(n) - Even not counting the output data structure, the
// key set could, depending on the shape of the input, have the same size as
// the input.
//
// Runtime 377 ms Beats 82.6%
// Memory 91.6 MB Beats 94.35%
/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function (arr) {
  const keySet = new Set();
  // Get the keys for each object.
  for (const obj of arr) {
    getKeys(obj, "");
  }
  const keys = Array.from(keySet).sort();
  const res = [keys];

  for (const obj of arr) {
    const ktv = {};
    getValues(obj, "", ktv);
    const row = [];
    for (const key of keys) {
      if (key in ktv) {
        row.push(ktv[key]);
      } else {
        row.push("");
      }
    }
    res.push(row);
  }
  return res;
  /** Get all the keys */
  function getKeys(obj, path) {
    Object.keys(obj).forEach((key) => {
      const np = path ? `${path}.${key}` : key;
      if (obj[key] !== null && typeof obj[key] === "object") {
        getKeys(obj[key], np);
      } else {
        keySet.add(np);
      }
    });
  }
  /** Given all the values that will go in a row of the matrix */
  function getValues(obj, path, ktv) {
    Object.keys(obj).forEach((key) => {
      const np = path ? `${path}.${key}` : key;
      if (obj[key] !== null && typeof obj[key] === "object") {
        getValues(obj[key], np, ktv);
      } else {
        ktv[np] = obj[key];
      }
    });
  }
};
