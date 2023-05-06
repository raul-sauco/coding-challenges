// 2667. Create Hello World Function
// 🟢 Easy
//
// https://leetcode.com/problems/create-hello-world-function/
//
// Tags: Javascript

// Create a function that returns "Hello World" when called.
//
// Time complexity: O(1)
// Space complexity: O(1)
//
// Runtime 61 ms Beats 100%
// Memory 42.1 MB Beats 100%
/**
 * @return {Function}
 */
var createHelloWorld = function () {
  return function (...args) {
    return "Hello World";
  };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
