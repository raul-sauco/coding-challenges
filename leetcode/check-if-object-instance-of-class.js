// 2618. Check if Object Instance of Class
// 🟠 Medium
//
// https://leetcode.com/problems/check-if-object-instance-of-class/
//
// Tags: Javascript

// Get the provided object prototype and check if that matches the given class,
// keep going up the prototype chain until we find one that it matches or
// the chain ends.
//
// Time complexity: O(n) - It can go up the entire prototype chain or until it
// finds a class that matches.
// Space complexity: O(1) - The iterative version uses constant extra memory,
// we could use a recursive version with similar logic, but it would require
// extra memory.
//
// Runtime 115 ms Beats 27.90%
// Memory 51.1 MB Beats 95.40%
/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function (obj, classFunction) {
  if (
    obj === null ||
    obj === undefined ||
    typeof classFunction !== "function"
  ) {
    return false;
  }
  let prot = Object.getPrototypeOf(obj);
  while (prot !== null) {
    if (prot === classFunction.prototype) {
      return true;
    }
    prot = Object.getPrototypeOf(prot);
  }
  return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
