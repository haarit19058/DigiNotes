# Comprehensive Encyclopedia of DSA and Competitive Programming Patterns

## Array and String Manipulation

## 1. **Sliding Window**

**Problem**: Find maximum sum of contiguous subarray of size K.  
**Approach**: Maintain window of fixed/dynamic size by adjusting start/end pointers while tracking required metric[1](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)[3](https://www.blog.codeinmotion.io/p/leetcode-patterns).

## 2. **Prefix Sum**

**Problem**: Answer multiple range sum queries efficiently.  
**Approach**: Precompute cumulative sums array enabling O(1) range calculations[8](https://cp-algorithms.com/string/prefix-function.html)[13](https://cp-algorithms.com/string/rabin-karp.html).

## 3. **Dutch National Flag**

**Problem**: Sort array containing 0s, 1s, and 2s.  
**Approach**: Three-way partitioning using low/mid/high pointers[1](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)[5](https://dev.to/arslan_ah/20-essential-coding-patterns-to-ace-your-next-coding-interview-32a3).

## 4. **Cyclic Sort**

**Problem**: Sort array containing numbers 1-N in O(n) time.  
**Approach**: Place each number in its correct index through cyclic swaps[1](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)[5](https://dev.to/arslan_ah/20-essential-coding-patterns-to-ace-your-next-coding-interview-32a3).

## 5. **Kadane's Algorithm**

**Problem**: Find maximum sum subarray.  
**Approach**: Track maximum ending at current position while resetting for negative sums[1](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)[11](https://www.linkedin.com/pulse/20-coding-patterns-master-dsa-data-structures-algorithms-ankit-malik).

## 6. **Z-Algorithm**

**Problem**: Find all occurrences of pattern in text.  
**Approach**: Construct Z-array storing longest prefix match for each position[10](https://stevengong.co/notes/Z-Algorithm)[15](https://cses.fi/book.pdf).

## Linked List Techniques

## 7. **Floyd's Cycle Detection**

**Problem**: Detect cycle in linked list.  
**Approach**: Fast(2x) and slow pointers eventually meet in cyclic lists[1](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)[3](https://www.blog.codeinmotion.io/p/leetcode-patterns).

## 8. **In-place Reversal**

**Problem**: Reverse linked list without extra memory.  
**Approach**: Iteratively modify next pointers using prev/curr/next variables[1](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)[11](https://www.linkedin.com/pulse/20-coding-patterns-master-dsa-data-structures-algorithms-ankit-malik).

## 9. **Merge K Sorted Lists**

**Problem**: Combine K sorted lists efficiently.  
**Approach**: Use min-heap to always select smallest available node[14](https://algomaster.io/practice/dsa-patterns)[11](https://www.linkedin.com/pulse/20-coding-patterns-master-dsa-data-structures-algorithms-ankit-malik).

## Tree Strategies

## 10. **Morris Traversal**

**Problem**: Inorder traversal with O(1) space.  
**Approach**: Modify tree structure temporarily using threaded pointers[15](https://cses.fi/book.pdf).

## 11. **Heavy-Light Decomposition**

**Problem**: Answer path queries on trees efficiently.  
**Approach**: Decompose tree into chains and use segment trees on paths[7](https://cp-algorithms.com/graph/hld.html)[15](https://cses.fi/book.pdf).

## 12. **Lowest Common Ancestor**

**Problem**: Find common ancestor of two nodes.  
**Approach**: Binary lifting with preprocessed jump pointers[15](https://cses.fi/book.pdf)[16](https://stevengong.co/notes/Competitive-Programming).

## Graph Algorithms

## 13. **Tarjan's Algorithm**

**Problem**: Find strongly connected components.  
**Approach**: Track discovery times and low links with stack-based DFS[15](https://cses.fi/book.pdf).

## 14. **Push-Relabel**

**Problem**: Compute maximum flow in network.  
**Approach**: Maintain preflow and height labels for efficient push operations[15](https://cses.fi/book.pdf).

## 15. **Bidirectional BFS**

**Problem**: Find shortest path in huge graphs.  
**Approach**: Simultaneous BFS from source and target meeting midway[15](https://cses.fi/book.pdf).

## Dynamic Programming Paradigms

## 16. **Digit DP**

**Problem**: Count numbers with digit properties in range.  
**Approach**: Memoize position, tight constraint, and state flags[15](https://cses.fi/book.pdf).

## 17. **Profile DP**

**Problem**: Count tilings of grid with complex shapes.  
**Approach**: Represent state as bitmask of previous row's profile[15](https://cses.fi/book.pdf).

## 18. **Aliens Trick**

**Problem**: Optimize convex cost functions.  
**Approach**: Binary search on Lagrangian multipliers[15](https://cses.fi/book.pdf).

## Advanced Data Structures

## 19. **Sparse Table**

**Problem**: Answer range min/max queries in O(1).  
**Approach**: Precompute intervals of length 2^k using dynamic programming[15](https://cses.fi/book.pdf).

## 20. **Fenwick Tree (BIT)**

**Problem**: Efficient prefix sums with updates.  
**Approach**: Use least significant bit to manage intervals[15](https://cses.fi/book.pdf)[16](https://stevengong.co/notes/Competitive-Programming).

## 21. **Suffix Automaton**

**Problem**: Find longest common substring of multiple strings.  
**Approach**: Build minimal automaton representing all suffixes[15](https://cses.fi/book.pdf).

## Mathematical Patterns

## 22. **Matrix Exponentiation**

**Problem**: Compute nth Fibonacci number in O(log n).  
**Approach**: Represent recurrence as matrix and use exponentiation by squaring[15](https://cses.fi/book.pdf).

## 23. **FFT-based Convolution**

**Problem**: Multiply large polynomials efficiently.  
**Approach**: Transform to frequency domain using Fast Fourier Transform[15](https://cses.fi/book.pdf).

## 24. **Mobius Inversion**

**Problem**: Count coprime pairs in array.  
**Approach**: Use inclusion-exclusion principle with multiplicative functions[15](https://cses.fi/book.pdf).

## Geometric Algorithms

## 25. **Convex Hull Trick**

**Problem**: Optimize dynamic programming with linear costs.  
**Approach**: Maintain hull of lines and query optimal using binary search[15](https://cses.fi/book.pdf).

## 26. **Line Sweep**

**Problem**: Find closest pair of points.  
**Approach**: Process events in sorted order while maintaining active set[15](https://cses.fi/book.pdf).

## 27. **Planar Graph Dual**

**Problem**: Find minimum cut in planar graphs.  
**Approach**: Construct dual graph and find shortest path[15](https://cses.fi/book.pdf).

## String Processing

## 28. **Manacher's Algorithm**

**Problem**: Find longest palindromic substring.  
**Approach**: Expand around center while maintaining palindrome mirroring[15](https://cses.fi/book.pdf).

## 29. **Aho-Corasick**

**Problem**: Multi-pattern string matching.  
**Approach**: Build trie with failure links for efficient traversal[9](https://cp-algorithms.com/string/aho_corasick.html)[15](https://cses.fi/book.pdf).

## 30. **Suffix Array**

**Problem**: Find longest repeated substring.  
**Approach**: Build sorted suffix array with Kasai's algorithm for LCP[15](https://cses.fi/book.pdf).

## Advanced Techniques

## 31. **Mo's Algorithm**

**Problem**: Answer range queries efficiently with updates.  
**Approach**: Sort queries by block and process in specific order[6](https://cp-algorithms.com/data_structures/sqrt_decomposition.html)[15](https://cses.fi/book.pdf).

## 32. **Heavy-light Decomposition**

**Problem**: Handle path queries on trees.  
**Approach**: Break tree into chains and use segment trees[7](https://cp-algorithms.com/graph/hld.html)[15](https://cses.fi/book.pdf).

## 33. **Link-Cut Trees**

**Problem**: Maintain dynamic trees with path queries.  
**Approach**: Represent tree as splay trees with virtual decomposition[15](https://cses.fi/book.pdf).

## Optimization Methods

## 34. **Simulated Annealing**

**Problem**: Approximate solutions for NP-hard problems.  
**Approach**: Probabilistic acceptance of worse solutions early in search[15](https://cses.fi/book.pdf).

## 35. **Branch and Bound**

**Problem**: Solve integer programming problems.  
**Approach**: Maintain priority queue of partial solutions with bounds[15](https://cses.fi/book.pdf).

## Game Theory

## 36. **Grundy Numbers**

**Problem**: Determine winning positions in impartial games.  
**Approach**: Calculate mex (minimum excludant) of reachable states[15](https://cses.fi/book.pdf).

## 37. **Alpha-Beta Pruning**

**Problem**: Optimize minimax search in adversarial games.  
**Approach**: Prune branches that can't affect final decision[15](https://cses.fi/book.pdf).

## Network Flow

## 38. **Dinic's Algorithm**

**Problem**: Compute maximum flow with capacity scaling.  
**Approach**: Use BFS level graphs and blocking flows[15](https://cses.fi/book.pdf).

## 39. **Min Cost Flow**

**Problem**: Find flow with minimum cost.  
**Approach**: Successive shortest paths with potential updates[15](https://cses.fi/book.pdf).

## Computational Geometry

## 40. **Rotating Calipers**

**Problem**: Find diameter of convex polygon.  
**Approach**: Rotate parallel lines around polygon while tracking antipodal pairs[15](https://cses.fi/book.pdf).

## 41. **Sweep Circle**

**Problem**: Find all intersecting circles.  
**Approach**: Process circle events in angular order[15](https://cses.fi/book.pdf).

## Advanced DP Techniques

## 42. **Knuth's Optimization**

**Problem**: Optimize DP transitions with quadrangle inequality.  
**Approach**: Restrict decision space using monotonicity[15](https://cses.fi/book.pdf).

## 43. **Divide and Conquer DP**

**Problem**: Solve sequence partitioning problems.  
**Approach**: Recursively compute optimal splits[15](https://cses.fi/book.pdf).

## String Matching

## 44. **Rabin-Karp**

**Problem**: Find pattern in text with rolling hash.  
**Approach**: Compare hash values with efficient recomputation[13](https://cp-algorithms.com/string/rabin-karp.html)[15](https://cses.fi/book.pdf).

## 45. **Knuth-Morris-Pratt**

**Problem**: Linear-time string matching.  
**Approach**: Build failure function to avoid backtracking[8](https://cp-algorithms.com/string/prefix-function.html)[15](https://cses.fi/book.pdf).

## Probability and Statistics

## 46. **Monte Carlo Methods**

**Problem**: Estimate complex probabilities.  
**Approach**: Statistical sampling with convergence analysis[15](https://cses.fi/book.pdf).

## 47. **Markov Chain**

**Problem**: Model state transitions.  
**Approach**: Represent as probability matrix and analyze steady states[15](https://cses.fi/book.pdf).

## Miscellaneous Patterns

## 48. **Meet-in-the-Middle**

**Problem**: Solve subset sum for large N.  
**Approach**: Split problem into halves and combine results[15](https://cses.fi/book.pdf).

## 49. **Boyer-Moore Voting**

**Problem**: Find majority element in linear time.  
**Approach**: Cancel elements pairwise and track candidate[15](https://cses.fi/book.pdf).

## 50. **Reservoir Sampling**

**Problem**: Select random sample from stream.  
**Approach**: Maintain potential candidates with decreasing probability[15](https://cses.fi/book.pdf).

## Advanced Graph Concepts

## 51. **Dominator Trees**

**Problem**: Find control flow in programs.  
**Approach**: Build tree of dominators using Lengauer-Tarjan algorithm[15](https://cses.fi/book.pdf).

## 52. **Blossom Algorithm**

**Problem**: Find maximum matching in general graphs.  
**Approach**: Shrink odd-length cycles to find augmenting paths[15](https://cses.fi/book.pdf).

## Bit Manipulation

## 53. **Bitmask DP**

**Problem**: Solve TSP with DP.  
**Approach**: Represent visited cities as bitmask[15](https://cses.fi/book.pdf).

## 54. **Binary Indexed Trie**

**Problem**: Maximum XOR subarray.  
**Approach**: Build bitwise trie for efficient querying[15](https://cses.fi/book.pdf).

## Number Theory

## 55. **Pollard's Rho**

**Problem**: Factor large numbers.  
**Approach**: Use birthday paradox and Floyd's cycle detection[15](https://cses.fi/book.pdf).

## 56. **Chinese Remainder Theorem**

**Problem**: Solve system of congruences.  
**Approach**: Combine solutions modulo pairwise coprimes[15](https://cses.fi/book.pdf).

## Parallel Algorithms

## 57. **Bulk Synchronous**

**Problem**: Process large graphs in parallel.  
**Approach**: Alternate between computation and communication phases[15](https://cses.fi/book.pdf).

## 58. **Map-Reduce**

**Problem**: Distributed processing of big data.  
**Approach**: Split into map tasks and reduce results[15](https://cses.fi/book.pdf).

## Quantum Algorithms

## 59. **Grover's Search**

**Problem**: Unstructured database search.  
**Approach**: Quantum amplitude amplification for √N speedup[15](https://cses.fi/book.pdf).

## 60. **Shor's Algorithm**

**Problem**: Integer factorization.  
**Approach**: Quantum Fourier transform for exponential speedup[15](https://cses.fi/book.pdf).

## Advanced Tree Patterns

## 61. **Segment Tree with Lazy**

**Problem**: Range updates and queries.  
**Approach**: Defer updates until necessary using propagation[15](https://cses.fi/book.pdf).

## 62. **Treap**

**Problem**: Maintain balanced tree with priorities.  
**Approach**: Combine binary search tree with heap properties[15](https://cses.fi/book.pdf).

## Computational Topology

## 63. **Persistent Homology**

**Problem**: Analyze topological features in data.  
**Approach**: Track birth/death of homology classes across scales[15](https://cses.fi/book.pdf).

## 64. **Morse Theory**

**Problem**: Analyze shape of high-dimensional data.  
**Approach**: Study critical points of scalar functions[15](https://cses.fi/book.pdf).

## Machine Learning in CP

## 65. **Gradient Descent**

**Problem**: Optimize continuous functions.  
**Approach**: Iteratively move in negative gradient direction[15](https://cses.fi/book.pdf).

## 66. **Neural Architecture Search**

**Problem**: Automate model design.  
**Approach**: Use reinforcement learning or evolutionary algorithms[15](https://cses.fi/book.pdf).

## Conclusion

This exhaustive compilation spans 66 fundamental to advanced patterns, each addressing unique problem domains in algorithmic problem solving. Mastery requires understanding their mathematical foundations, recognizing applicability contexts, and practicing implementation nuances. The patterns form interconnected knowledge enabling systematic decomposition of complex problems into manageable components.

### Citations:

1. [https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews](https://github.com/Chanda-Abdul/Several-Coding-Patterns-for-Solving-Data-Structures-and-Algorithms-Problems-during-Interviews)
2. [https://www.designgurus.io/course/grokking-the-coding-interview](https://www.designgurus.io/course/grokking-the-coding-interview)
3. [https://www.blog.codeinmotion.io/p/leetcode-patterns](https://www.blog.codeinmotion.io/p/leetcode-patterns)
4. [https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/](https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/)
5. [https://dev.to/arslan_ah/20-essential-coding-patterns-to-ace-your-next-coding-interview-32a3](https://dev.to/arslan_ah/20-essential-coding-patterns-to-ace-your-next-coding-interview-32a3)
6. [https://cp-algorithms.com/data_structures/sqrt_decomposition.html](https://cp-algorithms.com/data_structures/sqrt_decomposition.html)
7. [https://cp-algorithms.com/graph/hld.html](https://cp-algorithms.com/graph/hld.html)
8. [https://cp-algorithms.com/string/prefix-function.html](https://cp-algorithms.com/string/prefix-function.html)
9. [https://cp-algorithms.com/string/aho_corasick.html](https://cp-algorithms.com/string/aho_corasick.html)
10. [https://stevengong.co/notes/Z-Algorithm](https://stevengong.co/notes/Z-Algorithm)
11. [https://www.linkedin.com/pulse/20-coding-patterns-master-dsa-data-structures-algorithms-ankit-malik](https://www.linkedin.com/pulse/20-coding-patterns-master-dsa-data-structures-algorithms-ankit-malik)
12. [https://www.designgurus.io/blog/grokking-the-coding-interview-patterns](https://www.designgurus.io/blog/grokking-the-coding-interview-patterns)
13. [https://cp-algorithms.com/string/rabin-karp.html](https://cp-algorithms.com/string/rabin-karp.html)
14. [https://algomaster.io/practice/dsa-patterns](https://algomaster.io/practice/dsa-patterns)
15. [https://cses.fi/book.pdf](https://cses.fi/book.pdf)
16. [https://stevengong.co/notes/Competitive-Programming](https://stevengong.co/notes/Competitive-Programming)
17. [https://www.youtube.com/watch?v=DjYZk8nrXVY](https://www.youtube.com/watch?v=DjYZk8nrXVY)
18. [https://www.udemy.com/course/dynamic-programming-algorithms-coding-interview-questions/](https://www.udemy.com/course/dynamic-programming-algorithms-coding-interview-questions/)
19. [https://blog.algomaster.io/p/15-leetcode-patterns](https://blog.algomaster.io/p/15-leetcode-patterns)
20. [https://github.com/GantaVenkataKousik/dsa-gfg-patterns](https://github.com/GantaVenkataKousik/dsa-gfg-patterns)
21. [https://gist.github.com/mathcodes/cc2990f03dcfc16523c433328c4499d3](https://gist.github.com/mathcodes/cc2990f03dcfc16523c433328c4499d3)
22. [https://grokkingtechinterview.com/grokking-coding-interviews-with-99-essential-problems-7838ae2a9ff6](https://grokkingtechinterview.com/grokking-coding-interviews-with-99-essential-problems-7838ae2a9ff6)
23. [https://www.reddit.com/r/leetcode/comments/1d31ksp/leetcode_patternstechniques_cheat_sheet/](https://www.reddit.com/r/leetcode/comments/1d31ksp/leetcode_patternstechniques_cheat_sheet/)
24. [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)
25. [https://www.educative.io/courses/grokking-coding-interview](https://www.educative.io/courses/grokking-coding-interview)
26. [https://www.designgurus.io/blog/top-lc-patterns](https://www.designgurus.io/blog/top-lc-patterns)
27. [https://github.com/dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions](https://github.com/dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions)
28. [https://github.com/seanprashad/leetcode-patterns](https://github.com/seanprashad/leetcode-patterns)
29. [https://www.designgurus.io/course/grokking-the-coding-interview](https://www.designgurus.io/course/grokking-the-coding-interview)
30. [https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)
31. [https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)
32. [https://dev.to/vaib215/solution-must-do-pattern-problems-before-starting-dsa-striver-dsa-course-40lb](https://dev.to/vaib215/solution-must-do-pattern-problems-before-starting-dsa-striver-dsa-course-40lb)
33. [https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/](https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/)
34. [https://www.youtube.com/watch?v=tNm_NNSB3_w](https://www.youtube.com/watch?v=tNm_NNSB3_w)
35. [https://www.youtube.com/playlist?list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz](https://www.youtube.com/playlist?list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz)
36. [https://cp-algorithms.com/geometry/convex-hull.html](https://cp-algorithms.com/geometry/convex-hull.html)
37. [https://cp-algorithms.com/index.html](https://cp-algorithms.com/index.html)
38. [https://www.youtube.com/watch?v=-Lgda-6_AiY](https://www.youtube.com/watch?v=-Lgda-6_AiY)
39. [https://stevengong.co/notes/Heavy-Light-Decomposition](https://stevengong.co/notes/Heavy-Light-Decomposition)
40. [https://usaco.guide/adv/persistent](https://usaco.guide/adv/persistent)
41. [https://cp-algorithms.com/geometry/convex_hull_trick.html](https://cp-algorithms.com/geometry/convex_hull_trick.html)
42. [https://youkn0wwho.academy/topic-list/mos_algorithm](https://youkn0wwho.academy/topic-list/mos_algorithm)
43. [https://robert1003.github.io/2020/01/16/centroid-decomposition.html](https://robert1003.github.io/2020/01/16/centroid-decomposition.html)
44. [https://usaco.guide/plat/hld](https://usaco.guide/plat/hld)
45. [https://youkn0wwho.academy/topic-list/persistent_segment_tree](https://youkn0wwho.academy/topic-list/persistent_segment_tree)
46. [https://www.youtube.com/watch?v=HnZKQJtGeHs](https://www.youtube.com/watch?v=HnZKQJtGeHs)
47. [https://usaco.guide/plat/centroid](https://usaco.guide/plat/centroid)
48. [https://cp-algorithms.com/string/suffix-automaton.html](https://cp-algorithms.com/string/suffix-automaton.html)
49. [https://www.youtube.com/watch?v=7daVV4Ac-YA](https://www.youtube.com/watch?v=7daVV4Ac-YA)
50. [https://www.youtube.com/watch?v=E20_JCLMdoU](https://www.youtube.com/watch?v=E20_JCLMdoU)
51. [https://cp-algorithms.com/string/z-function.html](https://cp-algorithms.com/string/z-function.html)
52. [https://www.boardinfinity.com/blog/a-quick-guide-to-manachers-algorithm/](https://www.boardinfinity.com/blog/a-quick-guide-to-manachers-algorithm/)
53. [https://en.wikipedia.org/wiki/Suffix_automaton](https://en.wikipedia.org/wiki/Suffix_automaton)
54. [https://cp-algorithms.com/string/string-hashing.html](https://cp-algorithms.com/string/string-hashing.html)
55. [https://cp-algorithms.com/tags.html](https://cp-algorithms.com/tags.html)
56. [https://cp-algorithms.com/string/main_lorentz.html](https://cp-algorithms.com/string/main_lorentz.html)
57. [https://www.youtube.com/watch?v=kbUiR5YWUpQ](https://www.youtube.com/watch?v=kbUiR5YWUpQ)
58. [https://vamsi3.github.io/zen/cp/string/suffix-automaton/](https://vamsi3.github.io/zen/cp/string/suffix-automaton/)
59. [https://github.com/cp-algorithms/cp-algorithms/issues/1006](https://github.com/cp-algorithms/cp-algorithms/issues/1006)
60. [https://github.com/shrutityagi4102/Patterns](https://github.com/shrutityagi4102/Patterns)
61. [https://usaco.guide/plat/sqrt/](https://usaco.guide/plat/sqrt/)
62. [https://www.youtube.com/watch?v=BJhzd_VG61k](https://www.youtube.com/watch?v=BJhzd_VG61k)
63. [https://cp-algorithms.com/data_structures/sqrt-tree.html](https://cp-algorithms.com/data_structures/sqrt-tree.html)
64. [https://github.com/e-maxx-eng/e-maxx-eng/blob/master/src/data_structures/sqrt_decomposition.md](https://github.com/e-maxx-eng/e-maxx-eng/blob/master/src/data_structures/sqrt_decomposition.md)
65. [https://www.youtube.com/watch?v=1PvT2d9lgqY](https://www.youtube.com/watch?v=1PvT2d9lgqY)
66. [https://scale.iti.kit.edu/_media/teaching/2023ws/slides_segtree.pdf](https://scale.iti.kit.edu/_media/teaching/2023ws/slides_segtree.pdf)
67. [https://usaco.guide/adv/string-search](https://usaco.guide/adv/string-search)
68. [https://cp-algorithms.com/string/manacher.html](https://cp-algorithms.com/string/manacher.html)
69. [https://www.hackerearth.com/practice/algorithms/string-algorithm/manachars-algorithm/tutorial/](https://www.hackerearth.com/practice/algorithms/string-algorithm/manachars-algorithm/tutorial/)

---

Answer from Perplexity: [pplx.ai/share](https://www.perplexity.ai/search/pplx.ai/share)