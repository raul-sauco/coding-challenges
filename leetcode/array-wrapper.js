// 2695. Array Wrapper
// 🟢 Easy
//
// https://leetcode.com/problems/array-wrapper/
//
// Tags: Javascript

// The problem asks us to override the value and string implementations and
// provide our own as described.
//
// Time complexity: O(n) - Each call to any of the methods needs to iterate
// all elements in the input array.
// Space complexity: O(n) - It will store all the elements of the input array.
//
// Runtime 56 ms Beats 77.70%
// Memory 44.3 MB Beats 34.49%
/**
 * @param {number[]} nums
 */
var ArrayWrapper = function (nums) {
  this.nums = nums;
};

ArrayWrapper.prototype.valueOf = function () {
  return this.nums.reduce((num, acc) => num + acc, 0);
};

ArrayWrapper.prototype.toString = function () {
  return `[${this.nums}]`;
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
