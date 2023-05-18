// 2622. Cache With Time Limit
// 🟠 Medium
//
// https://leetcode.com/problems/cache-with-time-limit/
//
// Tags: Javascript

// Use a map to store the values, the only customization is that, when we add a
// new value, we also set a timeout at the given duration to remove the value
// from the object. The timeout would not be necessary if we didn't have the
// `count` method, we could simply store a "good-before" value when we add to
// the map, if we read a vaule after its expire-by timestap, we return false
// the same as if the value was not present, but, since we need to provide the
// number of valid entries on when `count` is called, we need to remove values
// as they expire.
//
// Time complexity: O(1) - Each call is processed in O(1).
// Space complexity: O(n) - We could end up storing one value per call if none
// of the durations ellapse.
//
// Runtime 63 ms Beats 40.27%
// Memory 41.7 MB Beats 77.44%
class TimeLimitedCache {
  cache = new Map();

  /**
   * @param {number} key
   * @param {number} value
   * @param {number} time until expiration in ms
   * @return {boolean} if un-expired key already existed
   */
  set(key, value, duration) {
    const entry = this.cache.get(key);
    if (entry) {
      clearTimeout(entry.to);
    }
    this.cache.set(key, {
      value,
      to: setTimeout(() => {
        this.cache.delete(key);
      }, duration),
    });
    return Boolean(entry);
  }

  /**
   * @param {number} key
   * @return {number} value associated with key
   */
  get(key) {
    return this.cache.get(key)?.value || -1;
  }

  /**
   * @return {number} count of non-expired keys
   */
  count() {
    return this.cache.size;
  }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
