// 2360. Longest Cycle in a Graph
// 🔴 Hard
//
// https://leetcode.com/problems/longest-cycle-in-a-graph/
//
// Tags: Depth-First Search - Graph - Topological Sort

import java.util.HashMap;

public class Solution {

  /**
   * Use depth-first search starting from every node, keep visited nodes in
   * a set to make sure we only visit each node once. Keep also a hashmap
   * of sets that we have visited along the current path pointing to the
   * position along the path at which we saw them, if we see a node that we
   * already saw in the current path, we have found a cycle, the size of
   * the cycle is the difference between the two positions at which we
   * found the current node, if we get to a node that does not have any
   * outbound edges, we can return 0 because the path will not have any
   * cycles.
   *
   * Time complexity: O(n) - We visit each node once and do O(1) work,
   * once a node is visited along one path, we will not visit it from
   * another path, if a path leads to a node that was visited already, it
   * will stop there.
   * Space complexity: O(n) - The list of visited nodes and the dictionary
   * of nodes seen along the path can both be of size n.
   *
   * Runtime 99 ms Beats 39%
   * Memory 87.1 MB Beats 35.14%
   */
  public int longestCycle(int[] edges) {
    int n = edges.length;
    // https://stackoverflow.com/a/2364887/2557030
    boolean[] visited = new boolean[n];
    int res = 0;
    HashMap<Integer, Integer> path;
    for (int i = 0; i < n; i++) {
      if (!visited[i]) {
        path = new HashMap<Integer, Integer>();
        int cycle = dfs(i, 0, path, visited, edges);
        if (cycle > res) {
          res = cycle;
        }
      }
    }
    return res == 0 ? -1 : res;
  }

  int dfs(
    int node,
    int pos,
    HashMap<Integer, Integer> path,
    boolean[] visited,
    int[] edges
  ) {
    if (path.containsKey(node)) {
      return pos - path.get(node);
    }
    if (visited[node]) {
      return 0;
    }
    path.put(node, pos);
    visited[node] = true;
    if (edges[node] != -1) {
      return dfs(edges[node], pos + 1, path, visited, edges);
    }
    return 0;
  }
}
