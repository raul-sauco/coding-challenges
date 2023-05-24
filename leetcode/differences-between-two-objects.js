// 2700. Differences Between Two Objects
// 🟠 Medium
//
// https://leetcode.com/problems/differences-between-two-objects/
//
// Tags: Javascript

// Check both parameters to see if they match, if they are objects, recursively
// call the function with the input keys.
//
// Time complexity: O(n) - We visit each key in the input array, top level and
// nested, at least once.
// Space complexity: O(n) - Even not counting the output data structure, the
// key set could, depending on the shape of the input, have the same size as
// the input.
//
// Runtime 61 ms Beats 66.67%
// Memory 43.9 MB Beats 40%
/**
 * @param {object} obj1
 * @param {object} obj2
 * @return {object}
 */
function objDiff(obj1, obj2) {
  if (obj1 === obj2) {
    return {};
  }
  if (
    obj1 === null ||
    obj2 === null ||
    typeof obj1 !== "object" ||
    typeof obj2 !== "object" ||
    Array.isArray(obj1) !== Array.isArray(obj2)
  ) {
    return [obj1, obj2];
  }
  const returnObject = {};
  for (const key in obj1) {
    if (key in obj2) {
      const subDiff = objDiff(obj1[key], obj2[key]);
      if (Object.keys(subDiff).length > 0) {
        returnObject[key] = subDiff;
      }
    }
  }
  return returnObject;
}
