###### the glorified recursion with caching

Equivalent for time command in unix
Measure-Command {start-process fibonacciDAG.exe -Wait}


- visualgo.net to see the graphical representation of the algos

- Recursion dag vs recursion in fibonacci




## Two key properties of
- Optimal Substructure
- Overlapping Subproblems

In the context of dynamic programming, "optimal substructure" is a key property that a problem must exhibit in order for dynamic programming to be applicable. It means that an optimal solution to the problem can be constructed efficiently from optimal solutions to its subproblems.

### Explanation

To explain this in detail:

1. **Subproblems**:
   - These are smaller instances of the original problem.
   - Solving the subproblems involves breaking down the main problem into these smaller, more manageable problems.

2. **Optimal Substructure**:
   - If the overall optimal solution to the problem can be obtained by combining the optimal solutions of its subproblems, then the problem has an optimal substructure.
   - This property allows you to recursively break down the problem and build up the solution from the solutions to the subproblems.

### Example: Fibonacci Sequence

Let's use the Fibonacci sequence as an example to illustrate optimal substructure:

1. **Problem Definition**:
   - Compute the nth Fibonacci number, where the Fibonacci sequence is defined as:
     - \( F(0) = 0 \)
     - \( F(1) = 1 \)
     - \( F(n) = F(n-1) + F(n-2) \) for \( n > 1 \)

2. **Subproblems**:
   - To compute \( F(n) \), we need to compute \( F(n-1) \) and \( F(n-2) \).

3. **Optimal Substructure**:
   - The optimal solution for \( F(n) \) (i.e., the nth Fibonacci number) is obtained by combining the solutions of the subproblems \( F(n-1) \) and \( F(n-2) \):
     - \( F(n) = F(n-1) + F(n-2) \)

Since the optimal solution for \( F(n) \) is directly derived from the optimal solutions for \( F(n-1) \) and \( F(n-2) \), the Fibonacci problem exhibits an optimal substructure.

### Example: Shortest Path in Graphs

Another common example is the shortest path problem in a graph, such as finding the shortest path from one vertex to another using algorithms like Dijkstra's or Bellman-Ford.

1. **Problem Definition**:
   - Find the shortest path from a source vertex to a destination vertex in a weighted graph.

2. **Subproblems**:
   - To find the shortest path from the source to the destination, consider the shortest path from the source to some intermediate vertex and then from that intermediate vertex to the destination.

3. **Optimal Substructure**:
   - If the shortest path from the source to the destination passes through some intermediate vertex \( u \), then the total length of this path is the sum of the shortest path from the source to \( u \) and the shortest path from \( u \) to the destination.
   - Thus, if \( \text{dist}(u, v) \) is the shortest distance between vertices \( u \) and \( v \), and \( \text{dist}(s, t) \) is the shortest distance from the source \( s \) to the destination \( t \), then:
     - \( \text{dist}(s, t) = \text{dist}(s, u) + \text{dist}(u, t) \)
   - This ensures that the problem has an optimal substructure.

### Conclusion

In summary, the property of optimal substructure allows dynamic programming to be used effectively because it ensures that solving larger problems can be done efficiently by combining solutions to smaller subproblems. This is a crucial aspect of designing dynamic programming algorithms.




Two ways of calculating DP - 
- Top-Down
- bottom-up




