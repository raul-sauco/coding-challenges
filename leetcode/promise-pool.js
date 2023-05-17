// 2636. Promise Pool
// 🟠 Medium
//
// https://leetcode.com/problems/promise-pool/
//
// Tags: Javascript

// Create a helper function that checks whethere we have run all the functions
// and, if we haven't yet, whether we have functions that we have not called
// yet and room in the pool, invoke the helper once from the main function and
// then once for each function that completes.
//
// Time complexity: O(1)? - Not sure about how to compute this but, I believe
// that it is O(1) because it just calls through the given functions.
// Space complexity: O(1) - The function itself only stores pointers.
//
// Runtime 64 ms Beats 52.8%
// Memory 42.6 MB Beats 15.32%
/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function (functions, n) {
  return new Promise((res) => {
    let nextIdx = 0;
    let running = 0;
    enque();
    function enque() {
      // Base case, we queued all the functions already.
      if (nextIdx === functions.length && running === 0) {
        res();
      }
      while (nextIdx < functions.length && running < n) {
        // Invoke the next function.
        functions[nextIdx++]().then(() => {
          running -= 1;
          enque();
        });
        running += 1;
      }
    }
  });
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */
