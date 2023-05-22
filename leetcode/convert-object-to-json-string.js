// 2633. Convert Object to JSON String
// 🟠 Medium
//
// https://leetcode.com/problems/convert-object-to-json-string/
//
// Tags: Javascript

// Check the type of the object and do a conversion based on that, for complex
// objects, split them into its components and deal with each recursively.
//
// Time complexity: O(n) - Each primary component will be processed in O(1).
// Space complexity: O(n) - Even not taking into account input and output, if
// we had a recursively, russian doll, style object, the call stack could grow
// to size n.
//
// Runtime 139 ms Beats 5.9%
// Memory 76.4 MB Beats 8.43%
/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function (object) {
  if (object === null || object === undefined) {
    return String(object);
  }
  if (Array.isArray(object)) {
    return `[${object.map((o) => jsonStringify(o)).join(",")}]`;
  }
  if (typeof object === "object") {
    return `{${Object.keys(object)
      .map((key) => `"${key}":${jsonStringify(object[key])}`)
      .join(",")}}`;
  }
  if (typeof object === "string") {
    return `"${String(object)}"`;
  }
  // Else it is a primitive.
  return String(object);
};

function main() {
  const objects = [
    { y: 1, x: 2 },
    { a: "str", b: -12, c: true, d: null },
    { key: { a: 1, b: [{}, null, "Hello"] } },
    true,
    null,
    undefined,
  ];
  objects.forEach((o) => {
    if (jsonStringify(o) !== JSON.stringify(o)) {
      console.log(`Failed to stringify ${JSON.stringify(o)}`);
    }
  });
}

main();
