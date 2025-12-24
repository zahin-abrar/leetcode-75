# LC75 – Problem 2

## 1071. Greatest Common Divisor of Strings (Python)

📌 **Learning-Oriented, AI-Coached Problem Solving Guide**  
📌 Focus: _Deriving invariants and mathematical structure from problem definitions_

---

## 1. Title & Metadata

- **Problem Source:** LeetCode 75
- **Problem Number:** 1071
- **Problem Name:** Greatest Common Divisor of Strings
- **Language Used:** Python
- **Approach:** Mathematical reasoning + string periodicity
- **Status:** Accepted (All test cases passed)

---

## 2. Why This Document Exists

This document exists to capture the **reasoning process** behind solving the problem, not just the final code.

Instead of:
- Memorizing tricks
- Copy-pasting editorial logic

The goal was to:
- Start from the formal problem definition
- Identify necessary conditions (invariants)
- Translate string behavior into mathematical reasoning
- Use AI as a **problem-solving coach**, not a shortcut

This document also serves as:
- A revision guide for interviews
- Evidence of responsible AI-assisted learning
- A reusable reference for similar problems

---

## 3. Problem Summary (In My Own Words)

A string `t` is said to divide another string `s` if `s` can be formed by repeating `t` one or more times.

Given two strings `str1` and `str2`, the task is to find the longest possible string `x` such that both `str1` and `str2` can be constructed by repeating `x`.

If no such common base string exists, the result should be an empty string.

---

## 4. Constraints and Design Implications

- String lengths can be up to 1000 characters.
- Brute-force checking of all substrings is unnecessary.
- A mathematical approach is more appropriate than simulation.
- Linear-time string operations are acceptable.

---

## 5. Identified Algorithmic Pattern & Key Insight

### Assumption
If a non-empty string `x` divides both `str1` and `str2`, then both strings must be constructed by repeating the same base pattern.

### Key Property
If both strings are made from the same repeating base, then concatenating them in any order should produce the same result:
str1 + str2 == str2 + str1


### Early Rejection Logic
If this property does not hold, it proves that no common base pattern exists.  
The algorithm can immediately return an empty string without further computation.

---

## 6. Key Decisions and Why They Work

- If a string divides another string, its length must divide the length of that string.
- Since the divisor string must divide **both** strings, its length must be a common divisor of both lengths.
- To return the **largest** valid divisor string, the greatest common divisor (GCD) of the two lengths is used.
- The prefix of length `gcd(len(str1), len(str2))` gives the required string.

---

## 7. Final Accepted Code

```python
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            gcd_len = math.gcd(len(str1), len(str2))
            return str1[:gcd_len]
        else:
            return ""
```

### Why this code is correct
- The concatenation check guarantees both strings share the same repeating base
- `math.gcd` finds the maximum possible valid base length
- Slicing the prefix extracts the divisor string directly
- No unnecessary loops or extra validations are required

---

## 8. Complexity Analysis

- **Time Complexity:**  
  \( O(n + m) \), where `n` and `m` are the lengths of `str1` and `str2`.  
  This comes from the concatenation comparison and slicing.

- **Space Complexity:**  
  \( O(n + m) \) due to temporary string concatenation during the comparison.

---

## 9. Rules to Lock into Memory

- Always translate the problem description into a mathematical or structural model.
- Focus on the definition first; examples are only for confirmation.
- When assuming a solution exists, ask what must always be true.
- For repetition-based string problems, think in terms of length divisibility.
- Look for early rejection conditions before solving the full problem.
- Once an invariant is proven, trust it and avoid redundant checks.
