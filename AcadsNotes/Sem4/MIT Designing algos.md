
# Lecture2 : Divide and Conquer

Paradigm
- You can break up a problem into smaller parts and somehow compose the solution in the smaller parts.
- Given a problem of size n we will divide it into a subproblems of size n/b a>=1 ; b > 1
- Solve each subproblem rexursively and once the subproblem becomes relatively small it is quite easy to solve them.
- Combine all the solutions of the subproblems not needed for all type of divide problems.
- Write a recurrence thata associates with the problem
- T(n) = a T(n/b) + \[Work for merging the solutions]
- All reccurences need not to be of same sizes. Strassens algo
- Master theorem

## Convex Hull
Problem : Two dimensional problem with a bunch of points. We can do it for multiple dimensions as well. We are finding an envelope or a hull with two dimensional points that encloses all of the given points. FInd an algorithm to find the convex hull (segments that are a part of the convex HULL).

Formal statement: given n points in a plane
S = {(xi,yi) | i = 1,2,3,....,n}

Assume that no two have the same x coordinate and no two have teh same y coordinate and no three in  a line.

Convex Hull itself is hte smallest convex polygon containing all points in S CH(S)

Aim is to get sequence of all the points on the boundary in clockwise order as doubly linked list. 

### What would be the brute force method ??

Draw a line and check all the points. If all teh points are on the same side of the line then it is a segment of convex hull.

