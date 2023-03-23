import java.util.ArrayList;
import java.util.HashSet;

// 1319. Number of Operations to Make Network Connected
// 🟠 Medium
//
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/
//
// Tags: Depth-First Search - Breadth-First Search - Union Find - Graph

class Solution {

  /**
   * Use union-find to compute the number of disjoint sets and the number of
   * redundant connections at the same time in O(e+v), the number of
   * connections that we need to make is equal to the number of disjoint sets
   * minus one, if the number of redundant connections is less than that, we
   * cannot connect the network, return -1.
   *
   * Time complexity: O(v+e) - We iterate over all existing connections e to
   * create the disjoint set structure, then iterate over all vertices v to
   * compute the number of unconnected components.
   * Space complexity: O(v) - We use two extra structures that are both of
   * size v.
   *
   * Runtime 22 ms Beats 35.41%
   * Memory 62.6 MB Beats 32.50%
   */
  public int makeConnected(int n, int[][] connections) {
    UnionFind uf = new UnionFind(n, connections);
    int setCount = uf.getNumberOfSets();
    int redundantConnections = uf.getRedundantConnectionCount();
    if (setCount - 1 > redundantConnections) {
      return -1;
    } else {
      return setCount - 1;
    }
  }
}

class UnionFind {

  ArrayList<Integer> parents;
  ArrayList<Integer> rank;
  int redundantConnections;

  UnionFind(int n, int[][] edges) {
    parents = new ArrayList<Integer>();
    parents.ensureCapacity(n);
    rank = new ArrayList<Integer>();
    rank.ensureCapacity(n);
    for (int i = 0; i < n; i++) {
      parents.add(i, i);
      rank.add(i, 1);
    }
    for (int[] edge : edges) {
      if (findParent(edge[0]) == findParent(edge[1])) {
        redundantConnections += 1;
      } else {
        union(edge[0], edge[1]);
      }
    }
  }

  int findParent(int a) {
    if (parents.get(a) != a) {
      parents.set(a, findParent(parents.get(a)));
    }
    return parents.get(a);
  }

  void union(int a, int b) {
    int pa = findParent(a);
    int pb = findParent(b);
    if (rank.get(pb) > rank.get(pa)) {
      union(b, a);
      return;
    }
    parents.set(pb, pa);
    rank.set(pa, rank.get(pa) + rank.get(pb));
  }

  int getNumberOfSets() {
    HashSet<Integer> sets = new HashSet<Integer>();
    for (int i = 0; i < parents.size(); i++) {
      if (!sets.contains(findParent(i))) {
        sets.add(findParent(i));
      }
    }
    return sets.size();
  }

  int getRedundantConnectionCount() {
    return redundantConnections;
  }
}
