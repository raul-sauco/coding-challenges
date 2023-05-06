// 2620. Counter
// 🟢 Easy
//
// https://leetcode.com/problems/counter/
//
// Tags: Javascript

// Use the parameter as state, return and increment it in each call.
//
// Time complexity: O(1)
// Space complexity: O(1)
//
// Runtime 64 ms Beats 17.48%
// Memory 42 MB Beats 56.40%
/**
 * @param {number} n
 * @return {Function} counter
 */
const createCounter = (n) => () => n++;

/**
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
