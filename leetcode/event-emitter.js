// 2694. Event Emitter
// 🟠 Medium
//
// https://leetcode.com/problems/event-emitter/
//
// Tags: Javascript

// Implement a simple pub-sub element. Store a map of events => subscriptors,
// when the event happens, emit the event by calling the functions with the
// given arguments.
//
// Time complexity: O(n) - Each call to subscribe is handled in constant time
// but the calls to emit need to iterate over all the subscriptions for the
// given event.
// Space complexity: O(n) - It will store all the subscriptors.
//
// Runtime 64 ms Beats 40%
// Memory 42.8 MB Beats 42.34%
class EventEmitter {
  events = new Map();
  subscribe(event, cb) {
    if (!this.events.has(event)) {
      this.events.set(event, new Set());
    }
    this.events.get(event).add(cb);
    return {
      unsubscribe: () => {
        this.events.get(event).delete(cb);
      },
    };
  }

  emit(event, args = []) {
    if (!this.events.has(event)) {
      return [];
    }
    const res = [];
    for (const fn of this.events.get(event).values()) {
      res.push(fn(...args));
    }
    return res;
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
