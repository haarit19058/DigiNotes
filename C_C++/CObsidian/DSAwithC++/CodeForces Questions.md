
# Promise Yourself that you will do at least 2 questions from codeforces everyday No Matter what are the circumstances......
# Promise Yourself Success



# 1999F-Expected Mean

## Problem Statement

Arul has a binary array∗ a of length n.

He will take all subsequences†† of length kk (kk is odd) of this array and find their median.

What is the sum of all these values?

[Link](https://codeforces.com/problemset/problem/1999/F)


## Solution

Suppose that there are x ones and y zeros. Then the cases where median is 1 occurs only when there are  at least \[k/2] + 1 ones in an array. 

Selecting i ones from x  *$^xC_{i}$*  and selecting k-i zeors from *$^yC_{k-1}$*  . The ans is sum of ones where the i is greater than \[k/2] +1  so summing over the multiplication of two terms representing all the possible permutations from \[k/2]+1 to x.

 Depending on your implementation, it can take O(nlogMOD)O(nlog⁡MOD) or O(n+logMOD)O(n+log⁡MOD) time.
 


## Code


``` cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5, mod = 1e9 + 7;
int64_t fact[N];

// Uses the formula of (axb)mod n = (amodn +bmodn)modn recursively
int64_t pw(int64_t a, int64_t b) {
	int64_t r = 1;
	while(b > 0) {
		if(b & 1) r = (r * a) % mod;
		b /= 2;
		a = (a * a) % mod; 
	}
	return r;
}

// Another logic used is the freds little rule that says that if p is prime number then a x ainv = 1 mod p then ainv = a^mod-2

int64_t C(int64_t n, int64_t k) {
	if(n < k) return 0LL;
	return (fact[n] * pw((fact[n - k] * fact[k]) % mod, mod - 2)) % mod;
}
int main() {
	int t; cin >> t;
	fact[0] = 1;
	for(int64_t i = 1; i < N; ++i) fact[i] = (fact[i - 1] * i) % mod;
	while(t--) {
		int n, k; cin >> n >> k;
		vector<int> a(n);
		int ones = 0;
		for(int i = 0; i < n; ++i) {
			cin >> a[i];
			ones += a[i];
		}
		//at least k/2+1 ones
		int64_t ans = 0;
		for(int cnt_ones = k / 2 + 1; cnt_ones <= min(ones, k); ++cnt_ones) {
			ans += C(ones, cnt_ones) * C(n - ones, k - cnt_ones) % mod;
			ans %= mod;
		}
		cout << ans << "\n";
	}
}
```



# Triple Operations
## Problem Statement
On the board Ivy wrote down all integers from ll to rr, inclusive.

In an operation, she does the following:

- pick two numbers xx and yy on the board, erase them, and in their place write the numbers 3x3x and ⌊y3⌋⌊y3⌋. (Here ⌊∙⌋⌊∙⌋ denotes rounding down to the nearest integer).

What is the minimum number of operations Ivy needs to make all numbers on the board equal 00? We have a proof that this is always possible.

[Link](https://codeforces.com/problemset/problem/1999/E)


## Solution 


## Code

```cpp

```




# Sum of Divisors
## Problem Statement
Given a positive integer **N**., The task is to find the value of **Σi from 1 to N** **F(i)** where function _**F(i)**_ for the number **i** is defined as the sum of all divisors of **i**.

[Link](https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1)

## Solution 
// Guys I will just try to give Idea here :

suppose we are given N = 5 ,

  Now we have to find factors of 1, 2,3,4,5 that will be 

  f1 = 1, f2 = 1 + 2 , f3 = 1 + 3, f4 = 1+2+4, f5 = 1+5, and then we try to sum them so ans will be 

   ans       =  f1 + f2 + f3 + f4 + f5 = 1 + (1 + 2) + (1 + 3) + (1 + 2 + 4) + (1 + 5)  // equals  21 now club alike terms
		= (1x5) + (2x2) + (3x1) + (4x1)+(5x1) // remains 21

  now this part does the main trick  and here I will do some rewriting as 
		= (1 x (5/1) ) + (2 x(5/2)) + (3x(5/3)) + (4 x (5/4)) +(5x(5/5))  //still remains 21

  here I am doing floor division so example 3/2 = 1 and 7/3 =2

You can See answer remains same so here is our pattern that for any N 

	  ans = (1 x (N/1)) + (2 x (N/2)) + (3x(N/3)) + ... + (Nx(N/N)) 

    apply this on some value of N and it may become more clear

## Code

```cpp
long long sumOfDivisors(int N) {
    
    long long sum = 0;
    for(int i = 1;i<=N;i++){
        sum+=(i*(N/i));
    }

    return sum;
}

};
```


# CF976A
## Problem Statement
You are given two integers nn and kk.

In one operation, you can subtract any power of kk from nn. Formally, in one operation, you can replace n by (n−k$^x$) for any non-negative integer xx.

Find the minimum number of operations required to make nn equal to 00.

Input

Each test contains multiple test cases. The first line contains the number of test cases tt (1≤t≤1041≤t≤104). The description of the test cases follows.

The only line of each test case contains two integers nn and kk (1≤n,k≤1091≤n,k≤109).

Output

For each test case, output the minimum number of operations on a new line.

[Link](https://codeforces.com/contest/2020/problem/A)

## Solution 

To solve the problem of finding the minimum number of operations required to reduce nnn to 000 by subtracting powers of kkk, we can use a greedy approach. The idea is to break down nnn in terms of the powers of kkk.

### Steps to Solve the Problem:

1. **Understanding Powers of kkk**:
    
    - We can subtract k0,k1,k2,…k^0, k^1, k^2, \ldotsk0,k1,k2,… until kxk^xkx exceeds nnn.
    - The maximum power of kkk that is relevant is determined by the largest xxx such that kx≤nk^x \leq nkx≤n.
2. **Counting Operations**:
    
    - The key observation is that the operation count corresponds to the number of non-zero digits in the base kkk representation of nnn.
    - Every non-zero digit means that you can subtract the respective power of kkk to reduce nnn.
3. **Convert nnn to Base kkk**:
    
    - By converting nnn into its representation in base kkk, we can count how many non-zero coefficients exist. Each non-zero coefficient indicates a power of kkk that can be subtracted.
## Code

```cpp
#include <iostream>

#include <cmath>

using namespace std;

  

int main() {

int t;

cin >> t;

while (t--) {

int n, k;

cin >> n >> k;

int itr = 0;

  

if (k == 1) {

cout<<n<<endl;

}

else{

  

while (n > 0) {

itr += n % k;

n /= k;

}

cout << itr << endl;

}

}

return 0;

}
```



# CF976B
## Problem Statement
magine you have nn light bulbs numbered 1,2,…,n1,2,…,n. Initially, all bulbs are on. To flip the state of a bulb means to turn it off if it used to be on, and to turn it on otherwise.

Next, you do the following:

- for each i=1,2,…,ni=1,2,…,n, flip the state of all bulbs jj such that jj is divisible by i†i†.

After performing all operations, there will be several bulbs that are still on. Your goal is to make this number exactly kk.

Find the smallest suitable nn such that after performing the operations there will be exactly kk bulbs on. We can show that an answer always exists.

†† An integer xx is divisible by yy if there exists an integer zz such that x=y⋅zx=y⋅z.

Input

Each test contains multiple test cases. The first line contains the number of test cases tt (1≤t≤1041≤t≤104). The description of the test cases follows.

The only line of each test case contains a single integer kk (1≤k≤10181≤k≤1018).

Output

For each test case, output nn — the minimum number of bulbs.
[Link](https://codeforces.com/problemset/problem/2020/B)


## Solution 

## Code

```cpp
#include <iostream>

#include <cmath>

using namespace std;

  

long long solve(long long k) {

// long long n = k;

// while (true) {

// long long sqr = sqrt(n);

// if (n - sqr == k) {

// return n;

// }

// n++;

// }

long long left = k, right = 2 * k; // Start search between k and 2k

long long result = 0;

  

while (left <= right) {

long long mid = left + (right - left) / 2;

long long perfect_squares = static_cast<long long>(sqrt(mid));

  

if (mid - perfect_squares < k) {

left = mid + 1; // Increase n

} else if (mid - perfect_squares > k) {

right = mid - 1; // Decrease n

} else {

result = mid; // Possible answer

right = mid - 1; // Try to find a smaller n

}

}

  

return result;

}

  

int main() {

int t;

cin >> t;

while (t--) {

long long k;

cin >> k;

  

// long double sqrt_part = sqrt(1.0 + 4.0 * k);

// long double n = (2.0 * k + 1.0 + sqrt_part) / 2.0;

  

cout << solve(k) << endl;

}

return 0;

}
```



# CF976C CF2020B

## Problem Statement
You are given three non-negative integers bb, cc, and dd.

Please find a non-negative integer a∈[0,261]a∈[0,261] such that (a|b)−(a&c)=d(a|b)−(a&c)=d, where || and && denote the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR) and the [bitwise AND operation](https://en.wikipedia.org/wiki/Bitwise_operation#AND), respectively.

If such an aa exists, print its value. If there is no solution, print a single integer −1−1. If there are multiple solutions, print any of them.

Input

Each test contains multiple test cases. The first line contains the number of test cases tt (1≤t≤1051≤t≤105). The description of the test cases follows.

The only line of each test case contains three positive integers bb, cc, and dd (0≤b,c,d≤10180≤b,c,d≤1018).

Output

For each test case, output the value of aa, or −1−1 if there is no solution. Please note that aa must be non-negative and cannot exceed 261261.
[Link](https://codeforces.com/problemset/problem/2020/C)

## Solution

bit by bit comparison is done using masking and bit maniputlations

## Code

```cpp
#include <iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--) {
        long long int b, c, d;
        cin >> b >> c >> d;

        long long mask = 1LL; // Initialize mask for bit positions
        long long a = 0;      // To hold the resulting value of a
        int flag = 0;         // Flag to check if valid a is found

        for(int i = 0; i < 62; i++) {
            flag = 0;   
            int bbit = (b >> i) & 1;
            int cbit = (c >> i) & 1;
            int dbit = (d >> i) & 1;

            // Case where a bit in a is set
            if(((1 | bbit) - (1 & cbit)) == dbit) {
                a |= mask; // Set the corresponding bit in a
                flag = 1;  // Mark flag true
            }

            else if(((0 | bbit) - (0 & cbit)) == dbit) {
            // No change in a (abit = 0)
                // Do nothing; a remains unchanged
                flag = 1; // Mark flag true
            }

            mask <<= 1; // Correctly shift mask left by 1
            if(flag == 0)break;
        }

        if(flag == 1) {
            cout << a << endl; // Output the resulting a
        } else {
            cout << -1 << endl; // Output -1 if no valid a found
        }
    }
    return 0;
}

```



# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```


# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```


# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

# CF975A

## Problem Statement
[Link](https://codeforces.com/problemset/problem/2020/B)

## Solution

## Code

```cpp

```

