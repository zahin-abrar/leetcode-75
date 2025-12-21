# LC75 – Problem 1

## 1768. Merge Strings Alternately (Python)

📌 **Learning-Oriented, AI-Coached Problem Solving Guide**  
📌 Focus: _How the solution was derived, not just the final answer_

---

## 1. Title & Metadata

- **Problem Source:** LeetCode 75
- **Problem Number:** 1768
- **Problem Name:** Merge Strings Alternately
- **Language Used:** Python
- **Approach:** Two-pointer technique
- **Status:** Accepted (All test cases passed)

This document is intentionally written as a **learning artifact**, not a minimal solution explanation.

---

## 2. Why This Document Exists

This document exists to capture the **thinking process** behind solving the problem.

Instead of:

- Copy-pasting an AI-generated solution
- Memorizing code patterns blindly

The goal was to:

- Break the problem down step by step
- Make design decisions explicit
- Understand _why_ certain approaches work and others fail
- Use AI as a **problem-solving coach**, not a shortcut

This also serves as:

- A revision guide for future interviews
- Evidence of responsible AI-assisted learning
- A reusable template for solving similar problems

---

## 3. Problem Summary (In My Own Words)

We are given two strings:

- `word1`
- `word2`

The task is to:

- Merge them by taking characters **alternately**
- Always start with a character from `word1`
- If one string runs out of characters before the other, append the remaining characters of the longer string
- Return the final merged string

The relative order of characters **within each string must be preserved**.

---

## 4. Constraints and Design Implications

Constraints:

- `1 ≤ len(word1), len(word2) ≤ 100`
- Strings contain only lowercase English letters

Design implications:

- Time complexity is not a major concern due to small input size
- Readability and correctness are more important than micro-optimizations
- Using simple string concatenation is acceptable
- Edge cases mainly involve **unequal string lengths**

---

## 5. Identified Algorithmic Pattern: Two-Pointer Technique

Before writing code, the first key question was:

> How many sequences are being processed at the same time?

Since there are **two input strings**, a natural and well-known pattern applies:

### **Two-Pointer Technique**

- One pointer per input string
- Each pointer tracks the current position in its string
- Pointers move forward as characters are consumed

🔒 **Rule to lock into memory**

> Number of sequences = Number of pointers

So for this problem:

- Pointer `i` → tracks position in `word1`
- Pointer `j` → tracks position in `word2`

This pattern guided the entire solution design.

---

## 6. What “Pointer” Means in Python

In algorithm discussions, a “pointer” often refers to a variable that tracks a current position in a sequence.

In Python, this does **not** mean a memory pointer like in C.  
Instead, a pointer is simply an **integer index**.

For this problem:

- Pointer `i` tracks the current index in `word1`
- Pointer `j` tracks the current index in `word2`

Both pointers:

- Start at index `0`
- Move forward manually
- Must be checked against string length before use

---

## 7. Do the Pointers Move Together or Independently?

An initial instinct is to think that the pointers always move together because characters are taken alternately.

However, this is only true **while both strings still have characters**.

Once one string runs out:

- Its pointer must stop
- The other pointer must continue

Example:

- `word1 = "ab"`
- `word2 = "pqrs"`

After alternating characters:

- `word1` is exhausted
- `word2` still has `"rs"`

This means:

- Pointer `i` stops moving
- Pointer `j` continues moving

🔒 **Rule to lock into memory**

> In merge problems, pointers must be able to move independently because inputs can have different lengths.

---

## 8. Function Planning and Responsibilities

Before writing code, it was important to clarify what the function is responsible for.

The function **owns**:

- Traversing both input strings
- Merging characters in the required order
- Returning the final merged string

The function does **not** own:

- Input/output handling
- Printing results
- Validating constraints (inputs are guaranteed valid)

This separation helps keep the solution clean and focused.

---

## 9. Variables to Initialize

To implement the two-pointer approach, three variables are required:

1. A result container to build the merged string
2. A pointer for `word1`
3. A pointer for `word2`

Typical initialization:

- `merged_word` as an empty string
- `i = 0`
- `j = 0`

An important realization:

- Function parameters (`word1`, `word2`) are already initialized
- Reassigning them to themselves is unnecessary and redundant

---

## 10. Python Refresher: Length and Indexing

In Python:

- String length is obtained using `len(word)`
- Characters are accessed using square brackets: `word[i]`

Common mistake to avoid:

- Python does **not** support `word.length()`

All bounds checks in this problem are done using:

- `i < len(word1)`
- `j < len(word2)`

## 11. Loop Condition Decision: `and` vs `or`

After initializing pointers and variables, the next critical decision was choosing the correct loop condition.

A common first attempt is:

```python
while i < len(word1) and j < len(word2):
```
This feels intuitive because alternating characters seems to require both strings to still have characters.

However, this condition causes a logical problem for this task.

The problem statement explicitly says that if one string is longer, the remaining characters must be appended.

Using `and` stops the loop as soon as either string finishes, which prevents leftover characters from being processed.

The correct mental question to ask is:

> “Should the loop stop when one string finishes, or when both are fully consumed?”

The correct answer is: when both are fully consumed.

Therefore, the correct loop condition is:

```python
while i < len(word1) or j < len(word2):
```
🔒 Rule to lock into memory
> Use `or` in the loop condition when you still need to process leftover elements from either input.

---

## 12. Why `if` Checks Are Required Inside the Loop

Using `or` means the loop may continue even when one string has already been exhausted.

This raises an important question:
> How do we avoid accessing characters that no longer exist?

The answer is guarded access using if statements.

Each pointer must be checked independently:

- Only access `word1[i]` if `i < len(word1)`
- Only access `word2[j]` if `j < len(word2)`

This creates a clear separation of responsibilities:

- The `while` loop decides whether to keep looping
- The `if` statements decide whether it is safe to access a specific string

🔒 Rule to lock into memory
> When using `or` in a loop condition, you almost always need `if` guards inside the loop.

---

## 13. Common Bug Encountered and Fixed

During implementation, a common mistake occurred:

```python
if i < word1[i]:
```
This is incorrect because:

- `i` is an integer index
- `word1[i]` is a character

Comparing an index to a character is meaningless and leads to errors.

The correct comparison is always between:

- An index and the length of the string

Correct form:
```python
if i < len(word1):
```
🔒 Rule to lock into memory

> Pointers are compared to lengths, not to characters.

---

## 14. LeetCode Python Requirement: `Solution` Class

LeetCode does not execute standalone functions.

Internally, it runs code equivalent to:

```python
Solution().mergeAlternately(word1, word2)
```
Therefore, a valid Python submission must include:

- A class named `Solution`
- A method with the exact expected name
- The `self` parameter

Failing to follow this structure results in:

```python
NameError: name 'Solution' is not defined
```
---

## 15. Final Accepted Solution

```python
class Solution:
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ''
        i = 0
        j = 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged_word += word1[i]
                i += 1
            if j < len(word2):
                merged_word += word2[j]
                j += 1

        return merged_word
```
This solution:
- Uses two independent pointers
- Correctly handles leftover characters
- Passes all LeetCode test cases

---

## 16. Complexity Analysis

Let: 

- `n` = length of `word1`
- `m` = length of `word2`

### Time Complexity

- O(n + m)

    Each character from both strings is processed exactly once.

### Space Complexity

- O(n + m)

    A new string is created to store the merged result.

Given the constraints (maximum length 100), this is efficient and appropriate.

--- 

## 17. Reusable Template, Reflection, and Next Step

### Reusable Mental Template

When merging or traversing multiple sequences:

- Use one pointer per sequence
- Use or in the loop condition if leftovers must be handled
- Use if checks inside the loop for safe access
- Allow pointers to move independently

This template applies to many problems beyond this one.

### Reflection on AI-Assisted Learning

This solution was not copy-pasted.

Instead:

- AI was used as a problem-solving coach
- Each decision was discussed and justified
- Mistakes were identified and corrected deliberately
- The final code reflects understanding, not memorization

This document itself serves as evidence of that learning process.