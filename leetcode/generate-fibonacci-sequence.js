// 2648. Generate Fibonacci Sequence
// 🟢 Easy
//
// https://leetcode.com/problems/generate-fibonacci-sequence/
//
// Tags: Javascript

// A generator that builds its next value as the sum of the previous two.
//
// Time complexity: O(n) - Each call takes O(1), n calls will take O(n)
// Space complexity: O(1) - The generator only stores two number values.
//
// Runtime 58 ms Beats 56.65%
// Memory 41.3 MB Beats 97.60%
/**
 * @return {Generator<number>}
 */
var fibGenerator = function* () {
  let cur = 0;
  let next = 1;
  while (true) {
    next = cur + next;
    cur = next - cur;
    yield next - cur;
  }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
