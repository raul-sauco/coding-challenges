// 2649. Nested Array Generator
// 🟠 Medium
//
// https://leetcode.com/problems/nested-array-generator/
//
// Tags: Javascript

// A generator that returns values of a nested array as if produced by an
// inorder traversal.
//
// Time complexity: O(n) - Each call takes O(1), n calls will take O(n)
// Space complexity: O(n) - The call stack could grow to size n.
//
// Runtime 184 ms Beats 73.7%
// Memory 74 MB Beats 50.62%
/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function* (arr) {
  if (!Array.isArray(arr)) {
    yield arr;
    return;
  }
  for (let i = 0; i < arr.length; i++) {
    yield* inorderTraversal(arr[i]);
  }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
