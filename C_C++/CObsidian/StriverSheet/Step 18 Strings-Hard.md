# Minimum number of bracket reversals needed to make an expression balanced



Approach:

- We can keep track of the balance of parentheses using two variables: open and close.

- Traverse through the string, and for each character:

- If it's an opening parenthesis '(', increment the open count.

- If it's a closing parenthesis ')':

- If there are open parentheses available (open > 0), decrement the open count.

- Otherwise, increment the close count.

- The total number of moves required to make the string valid would be equal to open + close.

```cpp
int minAddToMakeValid(string s) {
    int open = 0, close = 0;
    for(char c : s) {
        if(c == '(') {
            open++;
        } else {
            if(open > 0) {
                open--; // balance it with an open parenthesis
            } else {
                close++;
            }
        }
    }
    return open + close; // total moves required
}
```

# Count and Say

```cpp
class Solution {
public:
    string countAndSay(int n) {
        if(n == 1) return "1";

        string s = countAndSay(n - 1);
        string ans;
        int count = 1;

        for(int i = 1; i < s.size(); i++) {
            if(s[i] == s[i - 1]) {
                count++;
            } else {
                ans += to_string(count) + s[i - 1];
                count = 1;
            }
        }
        // Add the last group
        ans += to_string(count) + s.back();

        return ans;
    }
};

```


# Rabin Karp

The idea is that when matching pattern in strings it takes O(n) time which is very large if we have too many strings.
Therefore instead of matching by characters we will calculate the hash of the string that we want to compare. Thereby reducing the comparision time to O(1) if we choose suitable hash function.

## Rabin-Karp Algorithm — Overview
**Rabin-Karp** is a string-searching (pattern matching) algorithm that uses hashing to find a pattern in a text efficiently.
### What problem does it solve?

Given a **text** and a **pattern**, find all occurrences of the pattern in the text.
### Naive approach

Check every substring of text of length equal to pattern length — compare character by character.  
Time complexity: **O((N - M + 1) * M)**, where
- N = length of text
- M = length of pattern
This is inefficient for large texts and patterns.

## Rabin-Karp idea:
- Instead of checking each substring character by character, **hash** the substring and pattern.
- If the hash of a substring matches the pattern's hash, then do a character-by-character check (to avoid hash collisions).
- Use a rolling hash technique to efficiently compute hashes for substrings.
## How it works:
1. Calculate hash of the pattern.
2. Calculate hash of the first substring of the text with the same length as the pattern.
3. Slide over the text one character at a time, updating the hash (rolling hash).
4. If hash of current substring == hash of pattern:
    - Check substring characters to confirm.
    - If match, report occurrence.
5. Continue until end of the text.
# Key points:
- Use **rolling hash** to update substring hash in O(1) time.
- Hash function often uses a **prime base** and a **modulus** to avoid overflow.
- To reduce collisions, modulus is a large prime.
## Rolling Hash Formula:
Suppose the text is `t[0..n-1]`, pattern length is `m`, and base is `b`.
- Hash of substring `t[i..i+m-1]` is:

$$ H_i = (t[i] * b^{m-1} + t[i+1] * b^{m-2} + \dots + t[i+m-1] * b^0) \mod M $$

To get the next hash $H_{i+1}$, remove the leftmost character and add the new character:

$$ H_{i+1} = \left( (H_i - t[i] * b^{m-1}) * b + t[i+m] \right) \mod M $$
# Simple C++ implementation

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;
const ll base = 31;
const ll mod = 1e9 + 7;

ll modExp(ll base, int exp, ll mod) {
    ll result = 1;
    ll cur = base;
    while(exp > 0) {
        if(exp & 1) result = (result * cur) % mod;
        cur = (cur * cur) % mod;
        exp >>= 1;
    }
    return result;
}

vector<int> rabinKarp(const string& text, const string& pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> occurrences;

    if(m > n) return occurrences;

    ll patternHash = 0, textHash = 0;
    ll power = modExp(base, m - 1, mod); // b^(m-1)

    // Calculate initial hash for pattern and first substring of text
    for(int i = 0; i < m; i++) {
        patternHash = (patternHash * base + pattern[i]) % mod;
        textHash = (textHash * base + text[i]) % mod;
    }

    for(int i = 0; i <= n - m; i++) {
        if(patternHash == textHash) {
            // Check character by character to avoid collision
            if(text.substr(i, m) == pattern) {
                occurrences.push_back(i);
            }
        }

        // Calculate hash for next substring
        if(i < n - m) {
            textHash = (textHash - text[i] * power % mod + mod) % mod; // remove left char
            textHash = (textHash * base + text[i + m]) % mod;          // add new char
        }
    }
    return occurrences;
}

int main() {
    string text = "abracadabra";
    string pattern = "abra";

    vector<int> positions = rabinKarp(text, pattern);
    for(int pos : positions) {
        cout << "Pattern found at index: " << pos << "\n";
    }

    return 0;
}
```


# KMP algorithm


## What is KMP?
Given:
* A **text** string `T` of length `n`
* A **pattern** string `P` of length `m`
**Goal:** Find all occurrences of `P` in `T` efficiently.
## Why KMP?
* Naive search compares the pattern at every position in text, possibly re-checking characters unnecessarily.
* Worst-case time complexity for naive is **O(n\*m)**.
* KMP improves it to **O(n + m)** by avoiding redundant comparisons using preprocessing.

## Intuition Behind KMP
When a mismatch happens at some position in the pattern, KMP uses previously matched information to skip unnecessary comparisons, instead of restarting from scratch.

## The Core Idea: The LPS Array (Longest Prefix Suffix)
* **LPS array** stores, for every position in the pattern, the length of the longest proper prefix of the pattern substring that is also a suffix of the substring.

**Proper prefix:** prefix not equal to the whole string.

Example:
Pattern = `"ABABAC"`

| Index | Substring | LPS value explanation             | LPS value |
| ----- | --------- | --------------------------------- | --------- |
| 0     | A         | No proper prefix and suffix match | 0         |
| 1     | AB        | No match                          | 0         |
| 2     | ABA       | "A" is both prefix and suffix     | 1         |
| 3     | ABAB      | "AB" is prefix and suffix         | 2         |
| 4     | ABABA     | "ABA" is prefix and suffix        | 3         |
| 5     | ABABAC    | No prefix = suffix match          | 0         |

---

## How to compute LPS?

For each index `i` in pattern, find the length of the longest prefix suffix of the substring `P[0...i]`.
**Algorithm:**
```pseudo
lps[0] = 0
length = 0  // length of previous longest prefix suffix

for i = 1 to m-1:
    while length > 0 and P[i] != P[length]:
        length = lps[length - 1]

    if P[i] == P[length]:
        length += 1
        lps[i] = length
    else:
        lps[i] = 0
```

---

## KMP Search Algorithm Using LPS

1. Initialize two pointers:
   * `i` for text (0 to n-1)
   * `j` for pattern (0 to m-1)

1. Compare `T[i]` and `P[j]`
   * If match, increment both `i` and `j`
   * If `j` reaches `m` (pattern length), a full match is found at `i-j`

1. If mismatch:
   * If `j != 0`, reset `j = lps[j-1]`
   * Else increment `i`

## Complete Example in C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Compute LPS array
vector<int> computeLPS(string &pattern) {
    int m = pattern.size();
    vector<int> lps(m, 0);
    int length = 0; // length of previous longest prefix suffix
    int i = 1;

    while (i < m) {
        if (pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        }
        else {
            if (length != 0) {
                length = lps[length - 1];
            }
            else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

// KMP search
void KMPSearch(string &text, string &pattern) {
    int n = text.size();
    int m = pattern.size();
    vector<int> lps = computeLPS(pattern);

    int i = 0; // index for text
    int j = 0; // index for pattern

    while (i < n) {
        if (text[i] == pattern[j]) {
            i++; j++;
        }

        if (j == m) {
            cout << "Pattern found at index " << i - j << "\n";
            j = lps[j - 1];
        }
        else if (i < n && text[i] != pattern[j]) {
            if (j != 0)
                j = lps[j - 1];
            else
                i++;
        }
    }
}

int main() {
    string text = "ABABDABACDABABCABAB";
    string pattern = "ABABCABAB";
    KMPSearch(text, pattern);
    return 0;
}
```

## Summary
* **Preprocessing:** Build LPS array in O(m).
* **Search:** Use LPS to skip characters in O(n).
* **Overall complexity:** O(n + m).
