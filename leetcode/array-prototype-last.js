// 2619. Array Prototype Last
// 🟠 Medium
//
// https://leetcode.com/problems/array-prototype-last/
//
// Tags: Javascript

// Try to access the last element, if it results in null, return -1.
//
// Time complexity: O(1) - One conditional check and one access by index.
// Space complexity: O(n) - If we take into consideration the output array, or
// O(1) if we do not.
//
// Runtime 62 ms Beats 25%
// Memory 42 MB Beats 46.36%
Array.prototype.last = function () {
  return this.at(-1) ?? -1;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
