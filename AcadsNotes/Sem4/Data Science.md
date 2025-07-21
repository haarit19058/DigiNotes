# Laplacian and connected components

Let's break down the concepts step by step with mathematical details.

---

## 1. Laplacian Matrix and Its Eigenvalues

For an undirected graph with nn nodes, the (unnormalized) Laplacian matrix is defined as

L=D−A,L = D - A,

where:

- DD is the degree matrix (a diagonal matrix with DiiD_{ii} equal to the degree of node ii).
- AA is the adjacency matrix of the graph.

An eigenvector vv and its eigenvalue λ\lambda satisfy:

Lv=λv.L v = \lambda v.

---

## 2. Zero Eigenvalues and Disconnected Components

### **A. Constant Vector is an Eigenvector**

Consider the constant vector 1=[1,1,…,1]T\mathbf{1} = [1, 1, \dots, 1]^T. Observe that for any node ii:

(L1)i=Dii⋅1−∑jAij⋅1.(L \mathbf{1})_i = D_{ii} \cdot 1 - \sum_{j} A_{ij} \cdot 1.

Since the degree DiiD_{ii} is defined as the sum of the weights of edges incident to ii (or simply the number of edges in the unweighted case), we have:

(L1)i=degree(i)−degree(i)=0.(L \mathbf{1})_i = \text{degree}(i) - \text{degree}(i) = 0.

Thus,

L1=0⋅1,L \mathbf{1} = 0 \cdot \mathbf{1},

which means the constant vector 1\mathbf{1} is an eigenvector corresponding to eigenvalue λ=0\lambda = 0.

---

### **B. Multiple Disconnected Components**

Suppose the graph has kk disconnected components, denoted by G1,G2,…,GkG_1, G_2, \dots, G_k. For each component GiG_i, define an indicator vector v(i)v^{(i)} as:

vj(i)={1if node j belongs to Gi,0otherwise.v^{(i)}_j = \begin{cases} 1 & \text{if node } j \text{ belongs to } G_i, \\ 0 & \text{otherwise}. \end{cases}

**Why is v(i)v^{(i)} an eigenvector with eigenvalue 0?**

- Within component GiG_i, each node is connected only to nodes in GiG_i and not to nodes outside GiG_i (because the graph is disconnected).
    
- For any node jj in GiG_i:
    
    (Lv(i))j=Djj⋅vj(i)−∑lAjlvl(i).(L v^{(i)})_j = D_{jj} \cdot v^{(i)}_j - \sum_{l} A_{jl} v^{(i)}_l.
    
    Since vj(i)=1v^{(i)}_j = 1 and vl(i)=1v^{(i)}_l = 1 if ll is in GiG_i (and 0 otherwise), the summation gives the degree of jj (only counting neighbors in GiG_i). Thus:
    
    (Lv(i))j=degree(j)−degree(j)=0.(L v^{(i)})_j = \text{degree}(j) - \text{degree}(j) = 0.
- For nodes not in GiG_i, v(i)v^{(i)} is 0, and the corresponding entries in Lv(i)L v^{(i)} are also 0 (since these nodes have no connection to GiG_i).
    

Thus, each v(i)v^{(i)} is an eigenvector with eigenvalue 0.

Since the kk indicator vectors are linearly independent, there are at least kk linearly independent eigenvectors with eigenvalue 0. This shows that if the graph has kk disconnected components, the Laplacian LL has exactly kk zero eigenvalues.

---

## 3. Algebraic Connectivity (The Second Smallest Eigenvalue)

Once we have accounted for the kk zero eigenvalues (in the case of disconnected components), for a **connected** graph (k=1k = 1), the smallest eigenvalue is 00 (with eigenvector 1\mathbf{1}), and the **second smallest eigenvalue** λ2\lambda_2 is positive. This eigenvalue is often called the **algebraic connectivity** or **Fiedler value**.

### **Mathematical Intuition Using the Rayleigh Quotient**

For any vector x∈Rnx \in \mathbb{R}^n, the Rayleigh quotient of LL is given by:

R(x)=xTLxxTx=∑(i,j)∈E(xi−xj)2∑ixi2.R(x) = \frac{x^T L x}{x^T x} = \frac{\sum_{(i,j) \in E} (x_i - x_j)^2}{\sum_{i} x_i^2}.

- The minimum of this quotient (subject to x≠0x \neq 0) is λ1=0\lambda_1 = 0, achieved by x=1x = \mathbf{1}.
- To find the second smallest eigenvalue, we minimize R(x)R(x) over all xx that are **orthogonal** to 1\mathbf{1} (i.e., ∑ixi=0\sum_i x_i = 0). The minimizer in this subspace is the eigenvector corresponding to λ2\lambda_2.

### **Why Does λ2\lambda_2 Measure Connectivity?**

- **If λ2\lambda_2 is very small (close to 0):**  
    There exists a non-constant vector xx (the Fiedler vector) such that the numerator
    
    ∑(i,j)∈E(xi−xj)2\sum_{(i,j) \in E} (x_i - x_j)^2
    
    is very small relative to ∑ixi2\sum_i x_i^2. This indicates that xx does not change much across edges, suggesting that the graph can be partitioned into two sets where the differences xi−xjx_i - x_j across the cut are small—i.e., there is a **sparse cut** separating the graph into two nearly disconnected parts.
    
- **If λ2\lambda_2 is larger:**  
    Any vector xx (orthogonal to 1\mathbf{1}) will have a relatively large value of
    
    ∑(i,j)∈E(xi−xj)2,\sum_{(i,j) \in E} (x_i - x_j)^2,
    
    implying that the graph does not have an obvious partition where the edge differences are minimal. Thus, the graph is more robustly connected.
    

### **Cheeger’s Inequality**

This intuition is formalized by **Cheeger’s inequality**, which relates the isoperimetric number (or Cheeger constant) h(G)h(G) of the graph to the algebraic connectivity λ2\lambda_2:

λ22≤h(G)≤2λ2Δ,\frac{\lambda_2}{2} \le h(G) \le \sqrt{2\lambda_2 \Delta},

where Δ\Delta is the maximum degree in the graph. A smaller λ2\lambda_2 implies a smaller Cheeger constant, meaning there exists a partition with relatively few crossing edges (a "weak link" in connectivity). Conversely, a larger λ2\lambda_2 suggests better connectivity.

---

## 4. Summary

- **kk Zero Eigenvalues:**  
    For a graph with kk disconnected components, one can construct kk independent indicator vectors (each supported on a different component), all of which are annihilated by the Laplacian LL. Hence, there are kk eigenvalues equal to zero.
    
- **Algebraic Connectivity λ2\lambda_2:**  
    In a connected graph (where k=1k=1), the smallest eigenvalue is 0 and the second smallest eigenvalue λ2\lambda_2 is positive. The value of λ2\lambda_2 (found via the Rayleigh quotient) measures how “tight” the connectivity of the graph is. A smaller λ2\lambda_2 indicates that the graph is closer to having a weak (or sparse) cut, meaning it could be partitioned into two almost disconnected components. A larger λ2\lambda_2 implies stronger connectivity.
    

This mathematical framework not only tells us about the number of connected components but also provides a quantitative measure of how well-connected the graph is through λ2\lambda_2 and the associated eigenvectors used in spectral clustering.




# hey This is the section where i will be making notes for mid sem exam...

Lets start from the first chapter..

It says to read chapter 3 and 4 from the mu book..

## What are tail bounds ??
Tail bounds are mathematical inequalities that provide an upper limit on the probability that a random variable deviates significantly from its expected value

Tail bounds formally quantify how quickly the probability decays as the random variable moves away from its average

## Moments
Moments in probability are numerical measures that summarize various aspects of a random variable's distribution by taking expectations of its powers. They provide a systematic way to capture key features of the distribution, including its center, spread, and shape.

## Definition

- **Raw Moments:** The nth raw moment of a random variable XXX is defined as
    
    E[Xn]E[X^n]E[Xn]
    
    where E[⋅]E[\cdot]E[⋅] denotes the expected value. The first raw moment is E[X]E[X]E[X], which is the mean of the distribution.[1](https://www.statisticshowto.com/calculus-definitions/moment-definition-examples-generating-function/)
    
- **Central Moments:** By centering the random variable around its mean, the nth central moment is given by
    
    E[(X−μ)n]E[(X - \mu)^n]E[(X−μ)n]
    
    where μ\muμ is the mean. For example, the second central moment is the variance, a measure of the distribution's spread.[4](https://en.wikipedia.org/wiki/Moment_\(mathematics\))
    

## Key Moments and Their Interpretations

|**Moment**|**Definition**|**Interpretation**|
|---|---|---|
|**First Moment**|E[X]E[X]E[X]|Mean or central tendency|
|**Second Moment**|E[X2]E[X^2]E[X2] (or variance via central moment E[(X−μ)2]E[(X-\mu)^2]E[(X−μ)2])|Variability or dispersion|
|**Third Moment**|E[(X−μ)3]E[(X-\mu)^3]E[(X−μ)3]|Skewness, indicating asymmetry of the distribution|
|**Fourth Moment**|E[(X−μ)4]E[(X-\mu)^4]E[(X−μ)4]|Kurtosis, reflecting the "peakedness" of the distribution|

## Applications

Moments are used in various fields to:

- Describe the overall shape of a probability distribution
    
- Analyze the convergence properties of sequences of random variables
    
- Serve as the foundation for techniques like the moment generating function (MGF), which uniquely represents a distribution if all moments exist
    
- Inform statistical methods such as parameter estimation and hypothesis testing
    

Moments are central to the study of probability and statistics because they condense complex distributional properties into concise, interpretable numbers, providing insight into both average behavior and variability in data.

This overview explains that a moment in probability is essentially the expected value of a power of a random variable, which, when computed for different powers, helps reveal characteristics like the mean, variance, skewness, and kurtosis of the distribution.




# Project 

## Introduction to Graph Sampling

Graph sampling is a statistical technique used to analyze large graphs by selecting a representative subset of nodes and edges. This method is essential for managing and understanding complex networks, such as social networks, biological networks, and web graphs, where full data collection is often impractical due to size and access constraints[1](http://user.informatik.uni-goettingen.de/~ychen/papers/graph_sampling_simplex11.pdf)[2](http://isi-iass.org/home/wp-content/uploads/Survey_Statistician_2021_January_N83_04.pdf).

## Key Elements of Graph Sampling

1. **Definition of Sample Graph**: A sample graph is a subgraph of the original graph, selected based on a specified sampling strategy. It aims to preserve key properties of the original graph, such as degree distribution and connectivity[2](http://isi-iass.org/home/wp-content/uploads/Survey_Statistician_2021_January_N83_04.pdf)[3](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/a_myakushina23.pdf).
    
2. **Sampling Strategies**: These can be broadly categorized into **node sampling** and **edge sampling**.
    
    - **Node Sampling**: Involves selecting nodes and retaining their connections. Techniques include Random Node Sampling, Random Degree Node Sampling, and Random PageRank Sampling[3](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/a_myakushina23.pdf).
        
    - **Edge Sampling**: Focuses on selecting edges and their incident nodes. Techniques like Random Edge Sampling are used[5](https://cs.stanford.edu/~jure/pubs/sampling-kdd06.pdf).
        
3. **Applications**: Graph sampling is used in various fields, including:
    
    - **Social Network Analysis**: To study network properties without crawling the entire network[1](http://user.informatik.uni-goettingen.de/~ychen/papers/graph_sampling_simplex11.pdf).
        
    - **Biological Networks**: For analyzing protein interactions or gene regulatory networks.
        
    - **Web Graphs**: To understand web structure and link dynamics.
        
    - **Machine Learning**: In frameworks like GraphSAGE for efficient graph processing[4](https://graphscope.io/docs/learning_engine/graph_sampling)[6](https://graph-learn17-zh.readthedocs.io/en/latest/en/gl/graph/graph_operator/graph_sampling.html).
        

## Detailed Explanation of Sampling Methods

## 1. **Random Selection Techniques**

- **Random Node (RN) Sampling**: Nodes are selected uniformly at random. This method is simple but may not capture complex graph structures well[3](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/a_myakushina23.pdf).
    
- **Random Degree Node (RDN) Sampling**: Nodes are selected with probabilities proportional to their degrees. This method biases towards high-degree nodes[3](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/a_myakushina23.pdf).
    
- **Random PageRank (RPN) Sampling**: Nodes are selected based on their PageRank scores, which reflect their importance in the graph[3](https://www.sas.rochester.edu/mth/undergraduate/honorspaperspdfs/a_myakushina23.pdf).
    

## 2. **Sampling by Exploration**

- **Breadth-First Sampling (BFS)**: Starts from a node and explores all its neighbors before moving further. It is widely used for its simplicity and effectiveness[1](http://user.informatik.uni-goettingen.de/~ychen/papers/graph_sampling_simplex11.pdf)[7](https://www.isi-next.org/conferences/graphsampling/).
    
- **Random Walk (RW) Sampling**: Involves traversing the graph by randomly selecting a neighbor of the current node. This method is effective for capturing temporal patterns in graphs[5](https://cs.stanford.edu/~jure/pubs/sampling-kdd06.pdf)[7](https://www.isi-next.org/conferences/graphsampling/).
    

## 3. **Deletion Methods**

These involve removing nodes or edges from the graph to reduce its size while preserving certain properties.

## Where Graph Sampling is Used

Graph sampling is applied in various domains:

- **Social Media Platforms**: To analyze user behavior and network structures without accessing the entire network[1](http://user.informatik.uni-goettingen.de/~ychen/papers/graph_sampling_simplex11.pdf).
    
- **Biological Research**: For studying protein-protein interaction networks or gene regulatory networks.
    
- **Web Search Engines**: To understand web link structures and improve search algorithms.
    
- **Machine Learning Frameworks**: Such as GraphSAGE, which uses sampling to efficiently process large graphs[4](https://graphscope.io/docs/learning_engine/graph_sampling)[6](https://graph-learn17-zh.readthedocs.io/en/latest/en/gl/graph/graph_operator/graph_sampling.html).
    

## Benefits of Graph Sampling

1. **Efficiency**: Reduces computational costs by handling smaller graphs.
    
2. **Preservation of Properties**: Maintains key graph characteristics, making it suitable for analysis and modeling.
    
3. **Scalability**: Enables the study of very large graphs that are otherwise impractical to analyze in full.
    

## Challenges in Graph Sampling

1. **Choosing the Right Sampling Method**: Different methods preserve different graph properties, so selecting the appropriate method is crucial.
    
2. **Sample Size Determination**: Deciding how small the sample can be while still accurately representing the original graph is a challenge.
    
3. **Preserving Temporal Patterns**: In dynamic graphs, maintaining temporal properties in the sample is essential for accurate analysis[5](https://cs.stanford.edu/~jure/pubs/sampling-kdd06.pdf).
    

In summary, graph sampling is a powerful tool for analyzing complex networks by reducing their size while maintaining essential properties. It is widely used across various fields to improve efficiency and scalability in network analysis.


## What is page rank ??

## What is PageRank?

PageRank is a link analysis algorithm developed by Google founders Larry Page and Sergey Brin to evaluate the importance and quality of web pages. It assigns a numerical score to each page based on the number and quality of links pointing to it, with higher scores indicating greater importance.

## How PageRank Works

1. **Link Analysis**: PageRank treats each incoming link as a vote for the page's importance. Pages with more high-quality links are considered more authoritative.
    
2. **Damping Factor**: The algorithm uses a damping factor (usually around 0.85) to simulate the probability that a user will continue clicking on links or jump to a random page.
    
3. **Iterative Calculation**: PageRank values are calculated iteratively until they converge to a stable distribution, reflecting the relative importance of each page in the web graph.
    

## Key Components of PageRank

- **Incoming Links**: The number and quality of links pointing to a page.
    
- **Damping Factor (d)**: Adjusts the probability of continuing to click on links.
    
- **PageRank Score**: A numerical value between 0 and 10, historically used to rank pages.
    

## Applications and Impact

- **Search Engine Optimization (SEO)**: PageRank influences how web pages are ranked in search results.
    
- **Webpage Authority**: Helps determine the authority and relevance of web pages.
    
- **Link Quality**: Encourages natural, high-quality backlinks and discourages manipulation.
    

## Current Status

While the public PageRank scores are no longer available (since 2016), the algorithm remains significant in Google's ranking process. Other metrics like Domain Authority and Page Authority have been developed by SEO tools to estimate page quality.

## Formula

The simplified PageRank formula is:  
PR(A)=1−dN+d(PR(B)LB+PR(C)LC+⋯ )PR(A) = \frac{1-d}{N} + d \left( \frac{PR(B)}{L_B} + \frac{PR(C)}{L_C} + \cdots \right)PR(A)=N1−d+d(LBPR(B)+LCPR(C)+⋯)  
where:

- PR(A)PR(A)PR(A) is the PageRank of page A,
    
- ddd is the damping factor,
    
- NNN is the total number of pages,
    
- PR(B),PR(C),…PR(B), PR(C), \ldotsPR(B),PR(C),… are the PageRanks of pages linking to A,
    
- LB,LC,…L_B, L_C, \ldotsLB,LC,… are the numbers of links from those pages[1](https://en.wikipedia.org/wiki/PageRank)[3](https://www.holisticseo.digital/theoretical-seo/pagerank/)[5](https://delante.co/definitions/pagerank/).
    



![[pasted file.png]]





