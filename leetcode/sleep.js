// 2621. Sleep
// 🟢 Easy
//
// https://leetcode.com/problems/sleep/
//
// Tags: Javascript

// Return a new promise that resolves after the given time.
//
// Time complexity: O(1) - The code will wait millis second in a non-blocking
// way.
// Space complexity: O(1) - Each call only creates one timeout object.
//
// Runtime 60 ms Beats 53.69%
// Memory 41.5 MB Beats 86.74%
/**
 * @param {number} millis
 */
async function sleep(millis) {
  return Promise.new((resolve) => setTimeout(resolve, millis));
}

/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
