# Inequalities

Here is a list of common **probabilistic inequalities** used in probability theory and statistics:

---

### **1. Markov-Type Inequalities**

- **Markov's Inequality**  
    For a non-negative random variable XX:
    
    P(X≥a)≤E[X]a,a>0P(X \geq a) \leq \frac{\mathbb{E}[X]}{a}, \quad a > 0
- **Chebyshev's Inequality**  
    For a random variable XX with mean μ\mu and variance σ2\sigma^2:
    
    P(∣X−μ∣≥kσ)≤1k2,k>0P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}, \quad k > 0

---

### **2. Tail Inequalities**

- **Chernoff Bound**  
    For a sum of independent random variables:
    
    P(X≥(1+δ)μ)≤exp⁡(−δ2μ2+δ),δ>0P(X \geq (1 + \delta)\mu) \leq \exp\left(-\frac{\delta^2 \mu}{2 + \delta}\right), \quad \delta > 0
- **Hoeffding's Inequality**  
    For bounded independent random variables XiX_i in [ai,bi][a_i, b_i]:
    
    P(Sn−E[Sn]≥t)≤exp⁡(−2t2∑i=1n(bi−ai)2),P\left(S_n - \mathbb{E}[S_n] \geq t\right) \leq \exp\left(-\frac{2t^2}{\sum_{i=1}^n (b_i - a_i)^2}\right),
    
    where Sn=∑i=1nXiS_n = \sum_{i=1}^n X_i.
    
- **Azuma-Hoeffding Inequality**  
    For a martingale with bounded differences ∣Xi−Xi−1∣≤ci|X_i - X_{i-1}| \leq c_i:
    
    P(Xn−E[Xn]≥t)≤exp⁡(−t22∑i=1nci2).P(X_n - \mathbb{E}[X_n] \geq t) \leq \exp\left(-\frac{t^2}{2\sum_{i=1}^n c_i^2}\right).
- **Bennett's Inequality**  
    For independent random variables XiX_i with bounded differences:
    
    P(Sn−E[Sn]≥t)≤exp⁡(−nh(tnσ2)),P(S_n - \mathbb{E}[S_n] \geq t) \leq \exp\left(-n h\left(\frac{t}{n \sigma^2}\right)\right),
    
    where h(x)=(1+x)ln⁡(1+x)−xh(x) = (1 + x)\ln(1 + x) - x.
    

---

### **3. Law of Large Numbers-Type Inequalities**

- **Weak Law of Large Numbers Inequality**  
    If X1,X2,…,XnX_1, X_2, \ldots, X_n are i.i.d. random variables: P(∣1n∑i=1nXi−μ∣≥ϵ)≤σ2nϵ2.P\left(\left| \frac{1}{n} \sum_{i=1}^n X_i - \mu \right| \geq \epsilon\right) \leq \frac{\sigma^2}{n \epsilon^2}.

---

### **4. Logarithmic Sobolev Inequalities**

- **Pinsker's Inequality**  
    Relates the total variation distance and Kullback-Leibler divergence: ∥P−Q∥TV≤12DKL(P∥Q).\|P - Q\|_{TV} \leq \sqrt{\frac{1}{2} D_{KL}(P \| Q)}.

---

### **5. Large Deviation Inequalities**

- **Cramér-Chernoff Inequality**  
    For Sn=∑i=1nXiS_n = \sum_{i=1}^n X_i:
    
    P(Sn≥a)≤inf⁡λ>0e−λaE[eλSn].P(S_n \geq a) \leq \inf_{\lambda > 0} e^{-\lambda a} \mathbb{E}[e^{\lambda S_n}].
- **Bernstein's Inequality**  
    For bounded independent random variables:
    
    P(Sn−E[Sn]≥t)≤exp⁡(−t22(σ2+Mt/3)),P(S_n - \mathbb{E}[S_n] \geq t) \leq \exp\left(-\frac{t^2}{2(\sigma^2 + Mt/3)}\right),
    
    where MM is the maximum absolute value of XiX_i.
    

---

### **6. Concentration Inequalities**

- **McDiarmid's Inequality**  
    If X1,X2,…,XnX_1, X_2, \ldots, X_n are independent, and ff satisfies a bounded difference condition:
    
    P(f(X)−E[f(X)]≥t)≤exp⁡(−2t2∑i=1nci2).P(f(X) - \mathbb{E}[f(X)] \geq t) \leq \exp\left(-\frac{2t^2}{\sum_{i=1}^n c_i^2}\right).
- **Dobrushin's Inequality**  
    A concentration inequality for spin systems with bounded interactions.
    

---

### **7. Inequalities for Gaussian Distributions**

- **Gaussian Tail Bound**  
    For a standard normal random variable ZZ: P(Z≥t)≤12πte−t2/2,t>0.P(Z \geq t) \leq \frac{1}{\sqrt{2\pi}t} e^{-t^2/2}, \quad t > 0.

---

### **8. Other General Inequalities**

- **Jensen's Inequality**  
    For a convex function ϕ\phi:
    
    ϕ(E[X])≤E[ϕ(X)].\phi(\mathbb{E}[X]) \leq \mathbb{E}[\phi(X)].
- **Cauchy-Schwarz Inequality**  
    For random variables XX and YY:
    
    (E[XY])2≤E[X2]E[Y2].(\mathbb{E}[XY])^2 \leq \mathbb{E}[X^2] \mathbb{E}[Y^2].
- **Fano's Inequality**  
    Provides a lower bound on the probability of classification error.
    

---

Would you like detailed derivations or applications of any specific inequality?


# Law of Large numbers

The **Law of Large Numbers (LLN)** is a fundamental theorem in probability theory that describes the behavior of the average of a large number of independent and identically distributed (i.i.d.) random variables. It formalizes the idea that as the number of trials increases, the sample average converges to the expected value (or population mean).

---

### Types of LLN

There are two main versions of the Law of Large Numbers:

1. **Weak Law of Large Numbers (WLLN)**  
    The sample average converges to the expected value in **probability**. Formally:  
    If X1,X2,…,XnX_1, X_2, \ldots, X_n are i.i.d. random variables with E[Xi]=μ\mathbb{E}[X_i] = \mu, then for any ϵ>0\epsilon > 0:
    
    lim⁡n→∞P(∣1n∑i=1nXi−μ∣≥ϵ)=0.\lim_{n \to \infty} P\left(\left| \frac{1}{n} \sum_{i=1}^n X_i - \mu \right| \geq \epsilon\right) = 0.
    
    This means that the probability of the sample mean deviating from the population mean by more than ϵ\epsilon becomes arbitrarily small as nn grows.
    
2. **Strong Law of Large Numbers (SLLN)**  
    The sample average converges to the expected value **almost surely** (with probability 1). Formally:
    
    P(lim⁡n→∞1n∑i=1nXi=μ)=1.P\left(\lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^n X_i = \mu\right) = 1.
    
    This is a stronger result than the WLLN because it guarantees convergence for almost every sequence of random variables, not just in probability.
    

---

### Key Assumptions

- The random variables X1,X2,…,XnX_1, X_2, \ldots, X_n are **independent**.
- The random variables have the same distribution (i.i.d.), though some versions relax this condition.
- The expected value E[Xi]=μ\mathbb{E}[X_i] = \mu exists and is finite.

---

### Intuition

The LLN explains why averages tend to stabilize and become representative of the population mean as the number of observations increases. For example:

- In flipping a fair coin, the proportion of heads should approach 0.5 as the number of flips increases.
- In rolling a six-sided die, the average of the outcomes should approach 3.5 as the number of rolls increases.

---

### Applications

1. **Statistics**: Provides the theoretical justification for using sample means to estimate population means.
2. **Gambling**: Explains why casinos profit in the long run by relying on the expected value of bets.
3. **Quality Control**: Ensures that long-term averages of production measurements reflect expected quality levels.
4. **Machine Learning**: Forms the basis for empirical risk minimization in training models.

---

Would you like to see proofs, examples, or a specific application of the LLN?





# Distances

## Jaccard Distance

### Jaccard Similarity and Distance

The **Jaccard Similarity Index** and **Jaccard Distance** are measures used to compare the similarity and dissimilarity between two sets.

#### Jaccard Similarity Index

The **Jaccard Similarity Index** (also known as the **Jaccard Coefficient**) is a statistic used to measure the similarity between two sets. It is defined as the size of the intersection divided by the size of the union of the two sets.

Mathematically, for two sets AA and BB, the Jaccard similarity index is calculated as:
$$
J(A,B) = \frac{|A \cap B|}{|A \cup B|}
$$

Where:

- A∩BA \cap B is the intersection of sets AA and BB (elements common to both sets),
- A∪BA \cup B is the union of sets AA and BB (all unique elements from both sets),
- ∣A∣|A| and ∣B∣|B| are the sizes of the sets AA and BB respectively.

#### Jaccard Distance

The **Jaccard Distance** is a measure of the dissimilarity between two sets. It is defined as:

D(A,B)=1−J(A,B)D(A, B) = 1 - J(A, B)

Where J(A,B)J(A, B) is the Jaccard similarity index. Jaccard distance quantifies how different two sets are. The value of the Jaccard distance ranges from 0 (completely identical) to 1 (completely different).

### Uses of Jaccard Similarity and Distance

1. **Text Similarity**: Jaccard similarity is widely used in text mining for comparing documents or strings. For instance, in a document comparison task, Jaccard similarity can measure how similar two documents are based on the words they share.
    
2. **Clustering**: It is used in clustering algorithms, especially in the context of grouping sets or documents that share similar characteristics or features.
    
3. **Recommendation Systems**: Jaccard similarity can help in building recommendation systems, where it is used to find similarity between users or items based on common attributes, such as in collaborative filtering.
    
4. **Bioinformatics**: It is applied in genetics and bioinformatics to compare biological samples, sequences, or genes, where the similarity of sequences is crucial.
    
5. **Market Basket Analysis**: In data mining, Jaccard similarity is useful for association rule mining, such as finding the similarity of product sets bought together by customers.
    

### Important Properties

1. **Range**: The Jaccard similarity index lies between 0 and 1:
    
    - J(A,B)=1J(A, B) = 1 means the sets are identical.
    - J(A,B)=0J(A, B) = 0 means the sets have no common elements.
2. **Symmetry**: Jaccard similarity is symmetric, meaning:
    
    J(A,B)=J(B,A)J(A, B) = J(B, A)
    
    This implies the similarity measure does not depend on the order of the sets.
    
3. **Simplicity**: Jaccard similarity is easy to calculate and interprets the data as set-based, which can be useful for a wide variety of applications, particularly in comparing binary or categorical data.
    
4. **Does not account for frequency**: Jaccard similarity considers only the presence or absence of elements and does not account for how often an element appears in the sets. This is particularly useful for tasks involving sparse data, such as document or set comparison.
    
5. **Connection to Other Metrics**: Jaccard similarity can be connected to other measures like the **Cosine Similarity** and **Euclidean Distance** in specific contexts, but Jaccard focuses primarily on the presence of elements rather than their magnitudes or frequency.
    

In practice, Jaccard is often preferred when you are working with binary data or categorical data where the relationships between elements are set-based rather than based on quantity.


## Edit Distance

**Edit distance** (also known as **Levenshtein distance**) is a measure of the difference between two strings (e.g., words, sequences, or texts). It quantifies how many operations are required to transform one string into another. The operations are typically **insertions**, **deletions**, and **substitutions** of characters.

### Types of Edit Operations:

1. **Insertion**: Adding a character into the string.
2. **Deletion**: Removing a character from the string.
3. **Substitution**: Replacing one character with another.

The **edit distance** between two strings is the minimum number of these operations required to convert one string into the other.

### Example:

Consider the two strings:

- String 1: "kitten"
- String 2: "sitting"

The edit distance between them is 3, and here’s how we can transform "kitten" into "sitting":

1. Substitute "k" with "s" → "sitten"
2. Insert "i" → "sittin"
3. Insert "g" → "sitting"

So, it takes 3 operations to transform "kitten" into "sitting", and thus the edit distance is 3.

### Calculation:

The most common algorithm to calculate edit distance is **dynamic programming**, where you create a matrix that holds the intermediate results of subproblems. This matrix is filled based on the previous subproblem solutions.

For two strings s1s_1 and s2s_2, the edit distance can be calculated by considering the following:

- **If the characters match**: No operation is needed.
- **If the characters don't match**: Consider all possible operations (insertion, deletion, substitution) and choose the one that minimizes the total cost.

### Algorithm (Dynamic Programming Approach):

1. Create a matrix DD where D[i][j]D[i][j] represents the edit distance between the first ii characters of s1s_1 and the first jj characters of s2s_2.
    
2. Initialize the first row and column, representing the edit distance between substrings and the empty string.
    
3. For each character pair s1[i]s_1[i] and s2[j]s_2[j], compute the minimum cost from the following options:
    
    - Deletion: D[i−1][j]+1D[i-1][j] + 1
    - Insertion: D[i][j−1]+1D[i][j-1] + 1
    - Substitution: D[i−1][j−1]+1D[i-1][j-1] + 1 if s1[i]≠s2[j]s_1[i] \neq s_2[j], or D[i−1][j−1]D[i-1][j-1] if they are the same.
4. The value at D[m][n]D[m][n] will be the final edit distance, where mm and nn are the lengths of the two strings.
    

### Uses of Edit Distance:

1. **Spell Checking**: Used to suggest corrections by finding words with a small edit distance from the misspelled word.
2. **DNA Sequence Alignment**: In bioinformatics, it is used to measure how similar two DNA or RNA sequences are.
3. **Text Similarity**: Used to compare two texts, identify similarity, or find approximate string matches.
4. **Natural Language Processing (NLP)**: Helps in tasks like machine translation and text clustering.
5. **Version Control**: Used in software development to compute changes between different versions of files.

In summary, edit distance is a versatile metric for comparing strings, widely used in applications involving text correction, biological sequence alignment, and similarity measurement in general.



