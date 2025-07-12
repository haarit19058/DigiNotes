# Segment Trees



# Interval Sheduling

## Problem
Given a set I of n customers each with a starting and ending time, find the maximum number of customers that a server can serve

Condition : Cannot serve two customers whose intervals overlap



# ProblemSet 1

## Question 1

You are given a list of intervals, where each interval represents the time during which a professor at IIT is teaching on a Monday. Each entry in the list is a tuple containing the starting and ending time of the lecture for each professor. Your task is to determine the time slot during which the maximum number of professors are simultaneously teaching. In other words, find the time at which the most professors are conducting their lectures concurrently.

### Approach

**Lemma 1.** The time at which the maximum number of professors are simultaneously teaching coincides with the start time of some lecture.

Proof. (Proof Sketch) Assume the time when the maximum number of professors are teaching is ℓ. Decrease this time until you reach the start of an interval, ensuring the number of professors teaching remains unchanged. With the above tool in hand, design an algorithm that counts the number of professors teaching at the start time of each
lecture.

### Proof

Let l be the time when maximum number of professors are teaching

Case 01 l is start time of some interval -> Proved
Case 02 $l$ is not the start time of the interval.
- Then we left shift $l$ till we get to some start time of professor
- During this left shif the number of professors remains same (why??)
- If we encounter some end time of interval before the start time then it means that there is some other interval which overlaps with these d intervals. So maximum number of professors teaching is d+1 which is not  possible.
- Then we will encounter only a start point by shifting leftwards and the number of overlapping intervals remains same


### Algorithm 
```pseudocode
intervals = [(s1,e1),(s2,e2),....(sn,en)]
filtered = []
for (si,ei) in intervals:
	filtered += (si,1)
	filtered += (ei,-1)

sort(filtered)
count  = 0
maxCount = 0;

for (si,ti) in filtered:
	count += ti
	maxCount = max(count,maxCount)

maxCount is the answer
```



## Question 2
You are given an array A of intervals, where each interval A[i] is represented as (si , ei ), indicating an interval starting at si and ending at ei . Implement a function to merge all overlapping intervals in A and return an array of non-overlapping intervals that cover all the intervals in the input array.

**How would you prove such a silly argument ??**

### Approach

We first sort the intervals based on their starting times and then we merge two comsecutive intervals if they overlaps.
### Proof
How do you prove that this algo is correct ??

We sorted the intervals based on start times. Therfore $si<si+1<ei+1$

There are two cases possible

Case 01 $ei<si+1$ 
- In this case si<ei<si+1<ei+1  So there is no overlap then we would add (si,ei) to the list and move to si+1
Case 02 $ei > si+1$
- In this case si<si+1<ei<ei+1. There is an overlap and the start of this overlap is si and end is ei+1. So we add (si,ei+1) to the list

Therfore the algorithm should compare last interval ith interval and i+1 for overlap if they do then update the start and the end of the interval adn move to next if they dont then we add that interval to out final answer

### Algorithm
```pseudocode
sort intervals based on their start times
start  = s1 
end = e1
i = 2
while i< n do
	if si<=end then
		end = ei
		i++
	else
		print(start,end)
		i++
		start = si
		end = ei
		i++
```

## Question 3
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
### Approach
We find the maximum number of non ovelapping intervals. Then subtracting them from total intervals we get minimum number of overlapping intervals that we need to remove. 

**Lemma**: same as the one discussed in the class to find the max overlapping intervals 

**Lemma2** k = n - l
### Proof
**Lemma 2**
By definittion l is the maximum number of non overlapping intervals.
n is the total number of intervals we need to remove
l is the 

Case 01 Suppose k < n - l
- It means thatt we need to remove \<n-l intervals to make the rest non overlapping. Then non overlapping intervals are >n - n + l  = >l This contradicts teh definition of l that l is the  max number of non overlapping intervals

Case 02 Suppose k > n -1
- We remove > n - l  intervals ot make rest maximum non overlapping then the remaining intervals are < l. Then there exist some interval in k such that adding it back wont affect the configuration.  Therefore k = n - l.

### Algorithm

Find max non overlapping intervals by sorting according to the end time. Then total - maxNon overlappinng intervals

## Question 4
In a cricket maidan in Mumbai, typically on Sunday, you will see hundered of matches being played simultaneously on the same maidan. Suppose you have the list of all the matches with the start and end times. Find out the total number of time units for which there is only one team playing in the maidan. If there are two teams with timings [(2,5),(3,8)], then the answer is 4.

### Approach


### Proof

### Algorithm



## Question 5
You are given two set of intervals A and B. An interval in a ∈ A, covers an interval b ∈ B, if a and b overlaps. Find the minimum number of intervals in A, that cover all intervals in B.
### Approach
Sort B according to start times. Then find interval in A that overlaps with bi and ends last.
while b intersects with a do b++;


In informal way take a interval in b, find a intervall in a such that it ends last and then while b intersects with increment b its like finding the max cover.

### Proof
Let a1,a2,...,ak be the intervals in out ans sorted on teh bases of end times and o1,o2,o3,..,ol be interval in optimum again sorted based on endtimes

**Lemma 3** endtime(o1)<endtime(a1)

o1 covers b1 and a1 also covers b1. So out algo will choose a1 such that it ends last. 

**Lemma 4** There is an optimal that starts with a1.

replace o1 with a1. Then there is an solution that starts with a1 and does not affect the optimality.

**Lemma 5** For all 1<=i<=k there is an optimum that starts with a1,a2,...,ai

for ith term suppose oi-1 = ai-1:
Now end(oi)<=end(ai)
ai overlaps all the intervals that oi does and it has max end time. So replace oi by ai.

Suppose optimal has k+1 soln and we have k soln.
Then end(ak) > end(ok)

It means that ak cannot cover the intervals that ok+1 can. Then we choose ak+1 as ok+1.

### Algorithm
```pseudocode
Input: A (list of intervals in A), B (list of intervals in B)
Output: Minimum number of intervals in A that cover all intervals in B

1. Sort B by their end times.
2. Initialize an empty list Ans to store the chosen intervals from A.
3. Set i = 0 (index for intervals in B).
4. While i < length(B):
   a. Let b = B[i] (current interval in B).
   b. Find the interval a ∈ A that overlaps with b and has the latest end time.
      - Initialize max_end = -∞.
      - For each interval a in A:
         i. If a overlaps with b (i.e., a.start <= b.end and b.start <= a.end):
            - Update max_end = max(max_end, a.end).
            - Store the interval a as the current candidate.
   c. Add the selected interval a to Ans.
   d. Increment i while B[i] overlaps with the selected interval a.
5. Return Ans.
```

## Question 6

### Approach
A village has n houses where each house i is built at the location (i, 0) from the origin. A telephone company has installed k towers on top of k houses to cover all the houses in the village. For each tower j, you know its location, say ℓj and a range, say rℓ . The tower

### Proof
bi is position of tower in our soln and oi is in optimal soln.
**Lemma** : For all 1<=i<=k, bi >= oi



### Algorithm
```pseudocode
Sort houses according to their x coordinate
ans = 0
i = 1
while i <= n do
	let x coordinate of house h[i] be ai
	let b be the house with largest x cordinate in range
	add b to ans
	i++
	while tower + k covers h[i]
		i++
```

## Question 12
You are given n task each with a duration and a deadline. The i task requires di duration and deadline ti . If you attempt the task then you need to work on it for di hours and complete it by time ti . You cannot work on two tasks simultaneously. Design an algorithm that finds the maximum number of tasks you can perform. For example, if the n tasks are \[(1, 5), (2, 4), (5, 5)], then you can finish the first task in one hour. Then you complete the second tasks by the third hour. Unfortunately, you will not be able to perform the last task. So, the answer to this instance is 2.

### Approach
Idea is to sort the tasks by increaseing order of thier deadline. Do the task that ends first.

### Proof

### Algorithm


# HomeWork 1

## Question 1
You are given an array A\[1, . . . , n] with the following specifications:
• Each element A\[i] is either a cop (‘c’) or a robber (‘r’).
• A cop can catch a robber within a distance of k units, but each cop can catch at most one robber.
Design and analyze an algorithm to find the maximum number of robbers that can be caught.
### Approach

### Proof
Let r1,r2,...rk be robbers caught in increasing order of their position
Let o1,o2,...,ok be the robbers caught in increasing order by optimal soln

**Lemma**    $ri<=oi$

For

### Algorithm

```pseudocode
R   //list of robbers  sorted
C   //list of cops sorted

i = 0 //pointer for cop
j = 0 // pointer for robber
count = 0 //number of robbers caught
while i<C.size and j<R.size:
	if(|ci - rj|<k) assign ci to rj
		i++
		j++
		count++;
	else if(ci > rj) j++
	else if (rj > ci) i++

```


# Challenge

Given points in a 2d plane how would you find the nearest points in better than O(NlogN).

# ProblemSet 2

## Question 1
Given a set of 2n integers, make n pairs (a1 , b1 ), (a2 , b2 ), . . . , (an , bn ) from these 2n integers such that the sum
SIgma (1 to n) max{ai , bi } is maximized. Design an algorithm that solves this problem in i=1
(a) (Easy) O(n log n) time
(b) (Medium) O(n) time

### Approach
For nlogn FIrst sort the array and then make pairs of first and last.

What about O(n) ??
Use partition using the partition in quick sort and do it till we get on the index >=n
Then simply sum up all the elements on right. Maybe n logn
### Proof
### Algorithm

## Question 2
You have landed a cracking job in Bangalore in a company named PpWaterballs. Fortunately, PpWaterballs has agreed to pay k rupees for your relocation to Bangalore. You have stored your belong- ing into n boxes where the box i contains box\[i] items. The cost of transporting each box is 1 rupee. Design an algorithm that will relocate the maximum number of items.

### Approach
Sort and pick the last k largest boxes. Can we do better than this ??

### Proof
### Algorithm

## Question 3
Given two numbers a and b, their absolute diﬀerence is |a − b|. Given an array of size n, design an algorithm to find two number in it with minimum absolute diﬀerence.
### Approach
### Proof
### Algorithm

## Question 4
At IIT Gandhinagar, students undertake a total of n + k courses as part of their B.Tech curriculum. Upon completion of their degree, students have the option to request the institute to convert the grades of k courses into a pass grade. This feature is thoughtfully designed to address situations where exceptionally bright
students may have encountered diﬃculties in a few courses, potentially due to personal preferences or other reasons. By utilising this option, the CPI (Cumulative Performance Index) of such bright students remains unaﬀected by a few challenging courses, ensuring a fair evaluation of their overall academic performance. In this problem, we will change the definition of CPI and ask you to maximise it. The courses are arranged in an arbitrary order, denoted as c1 , c2 , . . . , cn+k . Each course ci is assigned a grade gi , ranging from 0 to 9. The temporary CPI is represented by the concatenation of these grades: g1 g2 . . . gn+k . For
instance, if a student receives grades 1, 9, and 7 in courses 1, 2, and 3 respectively, their temporary CPI would be 197. The objective is to strategically select k courses from the transcript for removal, with the aim of improving the
grades in the remaining n courses. For example, if given the opportunity to remove one course from the transcript, the student would select course 1 in the aforementioned scenario. Consequently, their final CPI would be 97. Formally, students are provided with grades for n + k courses, and they must choose k grades for removal to maximise the remaining cumulative performance. An eﬃcient algorithm is required to accomplish this task.
### Approach

As the grades are in 0 - 9. Loop through the grades. First remove the grades that are 0 then 1 then 2 and so on . Track a counter k and decrement it at every cycle.
This will take O(9n) at worst time complexity

THis algo is very wrong can you spot it out why ??

What then what would you do ??
Take first k+1 numbers find the max and remove all numbers before it. Lets say it is l and then remove it. The check for another k-l+1 numbers and repeat the process.


Another approach ..
Delete gi if gi < gi+1.
Run the loop k times and if in any loop update is not done then break and remove remaining numbers from the right end of the string. KSG.

### Proof
**Lemma:** First Term is from teh first k+1 digits.
Suppose for contradiction it si not the case then we would have deleted teh first k+1 numbers. But we cannot do that.

**Lemma:** First digit in opt <= first digit in out soln.

Suppose first digit of optimal occurs before ours then our soln would alos have selected it.
If the first digit of optimal is after our first digit then by exchange argument we can change the optimal answer to ours without changing its optimality.

**Lemma:** There is an opt that starts with the firsst number in your ans.


what is the running time of this algo.
### Algorithm

```pseudocode
int k = k;
for(int i = 0;i<=9;i++){
	for(int j: grade string){
		if(grade[j] == i)k--;
	}
}
```


# ProblemSet 3

## Question 1
If all the edges in the graph have equal weights, then show that you can find the minimum spanning tree in O(m + n) time.
### Approach
Using BFS or DFS we can find in required time.
### Proof
### Algorithm



## Question 2
In the heart of New Delhi, esteemed mathematician Professor Gupta introduces a novel approach for computing minimum spanning trees, inspired by India’s rich mathematical heritage. His algorithm unfolds as follows: Given a graph G = (V, E), partition the vertex set V into two sets V1 and V2 such that |V1 | and |V2 | diﬀer
by at most 1. Let E1 be the set of edges incident solely on vertices in V1 , and E2 be the set of edges incident solely on vertices in V2 . Recursively solve the minimum spanning tree problem on the subgraphs G1 = (V1 , E1 ) and G2 = (V2 , E2 ). Finally, select the minimum-weight edge in E that crosses the cut V1 , V2 , and use this edge to unite the resulting two minimum spanning trees into a single spanning tree. Evaluate whether Professor Gupta’salgorithm correctly computes a minimum spanning tree of G, or provide a counterexample to demonstrate its
limitations. Either argue that the algorithm correctly computes a minimum spanning tree of G, or provide an example for
which the algorithm fails.
### Approach

Give an counter example a b c three vertices with a --1-- b -- 100--c--1-- a
### Proof
### Algorithm


## Question 3
You are given a graph G and its minimum spanning tree M. Design an eﬃcient algorithm that updates M when:
(a) A new edge e is added to the graph.
(b) An edge e is deleted from the graph.
### Approach
Because of the cycle property 
after adding an edge find the cycle that the edge is a part of. Then remove teh max edge from that cycle.

Do a dfs from one of the vertices of the edge and if you return to the same vertex then it is the cylce you wanted to know.

In this case there are n edges and n vertices so O(2 N) time.
Another method  is do bfs from one of the vertex of edge to another one and track the path. So now you also have a path and then include the edge.


Part B
if the edge deleted is from teh MST then there are two set of vertices S1 and S2.
FInd the minimum weighted edge from S1 to S2. It would take O(Vertices) time.

### Proof
### Algorithm


## Question 4
Show that if all the weight in the graph are distinct, then there is a unique minimum spanning tree in the graph.
### Approach
Suppose there are two MSTs. then S1 and S2 be the sum of those two msts then
Either S1>S2 or S2>S1 as all weights are unique.

### Proof
### Algorithm



# Problemset 5

## Question 1
Given an array A of integers, find indices i, j such that A\[i]+A\[i+1]+A\[i+2]+. . .+A\[j] is maximized. Design a divide-and-conquer algorithm for finding the indices i, j.
### Approach

### Proof
### Algorithm


## Question 1
### Approach

### Proof
### Algorithm


## Question 1
### Approach

### Proof
### Algorithm




# PS8 6

## Step 1 Convert the instance of problem A into instance of problem b

We formulate the graph H as follows
1) Add m nodes representing each friend and name them fi for all i belongs  to 1,m
2) Add n nodes for topics and name them ti for i belongs to 1,n
3) Add a source S and sink T
4) Add directed edges of capacity 3 from \ Source to each fi
5) Add directed edges of capacity k from each ti to T
6) Add capacity of 1 from  fi to ti if ti is in Si.

## Step 2 Solve instace of problem b

Find teh max flow in graph H using ford fulkerson algorithm
	Time complexity = E * max{O(3* m), O(k * n)}
Edges (E) = n + m + nm
Time complexity  = O(nm * max{O(3* m), O(k * n)})

## Step 3 Using solution of problem b recover solution of problem a

Lemma: there is a flow of size k * n  in graph H iff it is possible to make such an arrangement

## Step4 Proving the correctness of answer

Lemma If there is a flow of size k * n  then such an arrangement is possible.

Suppose that there is  a flow of size k * n. Now for each edge from fi to ti haveing a capacity of 1 gives us the required arrangement. If the edges has flow 1 then that friend would ask a question for that topic ti. For each topic the incoming and outgoing flow is equal to k. So k friends are assigned to that topic. For each friend incoming flow is 3 and outgoing flow is also three so at most questions asked by any friend is 3. F


Lemma If there is such an arrangement there is a flow of size n * k.



