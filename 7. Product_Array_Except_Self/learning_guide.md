# LeetCode 75 #7 — Product of Array Except Self  
## Complete Learning Guide and Problem-Solving Workbook

---

## 1. Problem Overview

### Problem Name

**Product of Array Except Self**

### Difficulty

**Medium**

### Problem Statement Summary

Given an integer array `nums`, return an array `answer` where:

```python
answer[i] = product of all elements in nums except nums[i]
```

The solution must satisfy two key rules:

1. It must run in **O(n)** time.
2. It must **not use division**.

### Input

```python
nums: List[int]
```

An integer list.

Example:

```python
nums = [1, 2, 3, 4]
```

### Output

```python
answer: List[int]
```

A list of the same length where each position contains the product of every number except the number at that same position.

Example:

```python
answer = [24, 12, 8, 6]
```

### Given Examples

#### Example 1

```python
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

Explanation:

```text
answer[0] = 2 * 3 * 4 = 24
answer[1] = 1 * 3 * 4 = 12
answer[2] = 1 * 2 * 4 = 8
answer[3] = 1 * 2 * 3 = 6
```

#### Example 2

```python
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

The zero makes this interesting because division-based shortcuts become unsafe or complicated. The problem directly forbids division anyway.

### Constraints That Matter

The problem states:

```text
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
```

This is an important clue. It hints that **prefix** and **suffix** products may be useful.

The problem also requires:

```text
O(n) time
No division
```

This immediately rules out the most obvious brute-force approach if implemented with nested loops.

### Why This Problem Is Interesting

This problem is interesting because the brute-force idea is easy to understand, but the optimized solution requires a mental shift:

Instead of asking:

```text
For each index, how do I multiply everything except this element?
```

we learn to ask:

```text
Can I reuse products from the left side and the right side?
```

That shift is a major algorithmic pattern-recognition moment.

### What Makes It Challenging

The challenge is not Python syntax alone. The harder part is discovering the algorithmic structure:

```text
answer[i] = product of everything before i * product of everything after i
```

This requires recognizing that:

- We should not recompute products repeatedly.
- We can carry a running product.
- We can avoid direct `i-1`, `i-2`, `i+1`, `i+2` logic.
- We can use prefix and suffix arrays.
- Multiple sequential loops are still O(n).

---

## 2. Problem Summary in My Own Words

We are given a list of numbers. For every position in the list, we need to calculate the product of all the other numbers except the number at that position.

For example:

```python
nums = [1, 2, 3, 4]
```

At index `0`, the number is `1`, so we multiply everything except `1`:

```text
2 * 3 * 4 = 24
```

At index `1`, the number is `2`, so we multiply everything except `2`:

```text
1 * 3 * 4 = 12
```

At index `2`, the number is `3`, so we multiply everything except `3`:

```text
1 * 2 * 4 = 8
```

At index `3`, the number is `4`, so we multiply everything except `4`:

```text
1 * 2 * 3 = 6
```

So the final answer is:

```python
[24, 12, 8, 6]
```

The important restriction is that we cannot use division. So we cannot simply calculate the total product and divide by each number.

Also, the solution must be O(n), so we cannot use a loop inside another loop for every index.

The central idea becomes:

```text
For each index:
product except self =
product of everything on the left
*
product of everything on the right
```

---

## 3. Initial Brute Force Thinking

### First Instinct

The first instinct was:

```text
If O(n²) were allowed, I could just run a loop inside a loop.
```

That means:

```python
for i in range(len(nums)):
    product = 1
    for j in range(len(nums)):
        if i != j:
            product *= nums[j]
```

This would work logically.

### Why It Seems Reasonable

The problem directly asks:

```text
For each i, multiply everything except nums[i]
```

So the most literal translation is:

```text
Pick one index.
Go through the full array.
Skip that index.
Multiply the rest.
```

That is a correct brute-force interpretation.

### Why It Is Too Slow

For each index `i`, we scan the whole array again.

If there are `n` elements:

- For index `0`, scan about `n` elements.
- For index `1`, scan about `n` elements.
- For index `2`, scan about `n` elements.
- Continue for all `n` indexes.

That gives:

```text
n * n = n²
```

So the brute-force solution is:

```text
Time Complexity: O(n²)
```

The problem explicitly requires:

```text
O(n)
```

So brute force is not acceptable.

### Repeated Work

The brute-force method repeatedly multiplies the same values again and again.

For example, for:

```python
nums = [1, 2, 3, 4]
```

When calculating for index `2`, we multiply:

```text
1 * 2 * 4
```

When calculating for index `3`, we multiply:

```text
1 * 2 * 3
```

The product `1 * 2` is repeated.

The key optimization question becomes:

```text
Can we store reusable products so we do not recompute them?
```

That question leads to the prefix/suffix pattern.

---

## 4. Chronological Learning Journey

This section reconstructs the thinking path in the order it happened.

### Stage 1: Recognizing the O(n²) Trap

The first major observation was:

```text
If the problem allowed O(n²), a nested loop would solve it.
```

This was correct. The brute-force approach is logically valid.

What was missing was the optimization strategy.

The important learning point:

```text
A correct brute-force solution is often the first step toward an optimized solution.
```

We do not reject brute force immediately. We use it to understand the structure of the problem.

### Stage 2: Understanding the Shape of the Answer

For each index `i`, we need:

```text
everything except nums[i]
```

That can be split into two parts:

```text
everything before i
everything after i
```

So:

```text
answer[i] =
product_before_i * product_after_i
```

For:

```python
nums = [1, 2, 3, 4]
```

At index `2`, `nums[2] = 3`.

Everything before index `2`:

```text
1 * 2 = 2
```

Everything after index `2`:

```text
4
```

So:

```text
answer[2] = 2 * 4 = 8
```

This is the core decomposition of the problem.

### Stage 3: Question About Empty Product

A natural question came up:

```text
If there is nothing before i, should it be 0 or 1?
```

For index `0`, there is no element before it.

The correct answer is:

```text
The product of nothing is 1.
```

Reason:

```text
1 is the identity value for multiplication.
```

If we used `0`, it would destroy the result:

```text
0 * anything = 0
```

But if we use `1`, it does not affect the product:

```text
1 * x = x
```

So:

```python
left[0] = 1
```

Rule:

```text
For product problems, empty product = 1.
For sum problems, empty sum = 0.
```

### Stage 4: Initial Confusion About `i-1`, `i-2`, `i-3`

The next question was about how to build the left products:

```text
If we use range, we can get the index.
That way i-1 seems easy.
But what about i-2, i-3, and so on?
```

This was a very important confusion.

The initial mental model was:

```text
For left[i], maybe I need to manually access:
nums[i-1], nums[i-2], nums[i-3], ...
```

That would lead back toward nested logic or complicated indexing.

The breakthrough was:

```text
We do not need to explicitly access i-1, i-2, i-3.
We can carry a running product.
```

### Stage 5: Discovering Running Product

Instead of recomputing:

```text
nums[0]
nums[0] * nums[1]
nums[0] * nums[1] * nums[2]
```

we maintain one variable:

```python
left_current_product = 1
```

Before processing each index `i`, this variable already contains:

```text
product of everything before i
```

Then we do:

```python
left_product.append(left_current_product)
left_current_product *= nums[i]
```

The order matters.

We first use the product because it represents everything before the current index. Then we include `nums[i]` for future indexes.

### Stage 6: Avoiding Special Cases

There was a question:

```text
How do we handle i-1? With if or starting range from 1?
```

The answer was:

```text
Avoid i-1 completely.
```

By using a running product initialized to `1`, we avoid special handling for index `0`.

No `if` needed.

No starting from `1` needed.

The loop can start from `0`:

```python
for i in range(len(nums)):
    left_product.append(left_current_product)
    left_current_product *= nums[i]
```

This is cleaner because the invariant handles the edge case naturally.

### Stage 7: Building the Left Product Array

For:

```python
nums = [1, 2, 3, 4]
```

The left product array is:

```python
left_product = [1, 1, 2, 6]
```

Meaning:

```text
left_product[0] = product before index 0 = 1
left_product[1] = product before index 1 = 1
left_product[2] = product before index 2 = 1 * 2 = 2
left_product[3] = product before index 3 = 1 * 2 * 3 = 6
```

This confirmed the left side logic.

### Stage 8: Understanding Multiple O(n) Loops

Next came a complexity concern:

```text
If we do it again for the right product, won't we run the loop again?
```

Yes, we run another loop.

But:

```text
one loop = O(n)
two loops = O(2n)
three loops = O(3n)
```

In Big-O notation:

```text
O(3n) simplifies to O(n)
```

The important distinction:

```text
Sequential loops are O(n).
Nested loops are O(n²).
```

So doing one pass for left products, one pass for right products, and one pass to combine them is still O(n).

### Stage 9: Moving From Left Products to Right Products

Once the left side was clear, the same idea was applied from the opposite direction.

The right product array means:

```python
right_product[i] = product of everything after index i
```

For:

```python
nums = [1, 2, 3, 4]
```

The right product array is:

```python
right_product = [24, 12, 4, 1]
```

Meaning:

```text
right_product[0] = 2 * 3 * 4 = 24
right_product[1] = 3 * 4 = 12
right_product[2] = 4 = 4
right_product[3] = nothing after index 3 = 1
```

### Stage 10: Understanding Reverse Range

To build the right product array, we loop from right to left:

```python
for i in range(len(nums) - 1, -1, -1):
```

The user's understanding was:

```text
Start from len(nums)-1.
End point should be -1 so that we stop at 0.
range stops one unit before the final boundary.
Step is -1 because we want to decrease by 1.
```

This understanding was correct.

For:

```python
nums = [1, 2, 3, 4]
```

The loop indexes are:

```text
3, 2, 1, 0
```

### Stage 11: Understanding Why Right Product Needs Preallocation

There was a question:

```text
Why do we need to create the list with 0 first for right?
```

The reason:

```python
right_product[i] = right_current_product
```

uses index assignment.

For index assignment to work, that index must already exist.

If we start with:

```python
right_product = []
```

then this fails:

```python
right_product[3] = 1
```

because index `3` does not exist yet.

So we create placeholders:

```python
right_product = [0] * len(nums)
```

For `nums = [1, 2, 3, 4]`:

```python
right_product = [0, 0, 0, 0]
```

Then we fill slots from right to left:

```text
start:       [0, 0, 0, 0]
after i=3:   [0, 0, 0, 1]
after i=2:   [0, 0, 4, 1]
after i=1:   [0, 12, 4, 1]
after i=0:   [24, 12, 4, 1]
```

The `0`s are not product values. They are placeholders.

### Stage 12: Combining Left and Right

There was a question:

```text
Can I do return left_product * right_product?
```

This exposed a Python/data-structure distinction.

If both are lists:

```python
left_product = [1, 1, 2, 6]
right_product = [24, 12, 4, 1]
```

Then this does not work:

```python
left_product * right_product
```

Python does not multiply lists element by element.

Instead, we need:

```python
answer[i] = left_product[i] * right_product[i]
```

So we combine by index:

```python
answer = []

for i in range(len(nums)):
    answer.append(left_product[i] * right_product[i])
```

### Stage 13: Final Accepted Solution

The final solution used three stages:

1. Build left products.
2. Build right products.
3. Combine matching indexes.

The solution was accepted.

That means the user reached a correct O(n) solution without division.

---

## 5. Identified Algorithmic Pattern

### Pattern Name

**Prefix and Suffix Products**

This is a variation of the broader **prefix/suffix precomputation** pattern.

### Pattern Definition

A prefix value stores information from the left side of an index.

A suffix value stores information from the right side of an index.

For this problem:

```python
left_product[i] = product of all values before i
right_product[i] = product of all values after i
```

Then:

```python
answer[i] = left_product[i] * right_product[i]
```

### Why This Pattern Applies Here

The problem asks for the product of all elements except the current element.

That naturally splits into:

```text
elements before current index
elements after current index
```

So the problem has a left-side and right-side structure.

This is the signal:

```text
For each index, I need information from both sides.
```

That often points toward prefix/suffix logic.

### Prefix Product

For:

```python
nums = [1, 2, 3, 4]
```

The prefix/left products are:

```python
[1, 1, 2, 6]
```

Each value excludes the current index.

### Suffix Product

The suffix/right products are:

```python
[24, 12, 4, 1]
```

Each value excludes the current index.

### Final Combination

```text
left:   [1,  1, 2, 6]
right:  [24,12, 4, 1]
answer: [24,12, 8, 6]
```

### Why This Is Not Sliding Window

Sliding window is usually used when we are dealing with a contiguous subarray or substring whose boundaries move.

Here, for each index, we need everything before and everything after. We are not maintaining a variable-size or fixed-size window. So this is not primarily a sliding window problem.

### Why This Is Not Two Pointers

Two pointers often involve two indexes moving toward each other or across the array to find pairs, swap elements, or shrink/grow a search space.

Here, we are making full directional passes:

```text
left to right
right to left
```

Although we use indexes, the core pattern is not two-pointer interaction. It is directional precomputation.

### Similar Problems Where Prefix/Suffix Appears

This pattern appears in problems like:

- Prefix Sum Array
- Range Sum Query
- Trapping Rain Water
- Left and Right Sum Differences
- Find Pivot Index
- Maximum Product Subarray variants
- Minimum/maximum before and after index
- Count elements before/after index
- Product of Array Except Self

### Trigger Signal

When a problem says:

```text
For every index, calculate something using all elements except/current/before/after it.
```

consider:

```text
Can I precompute from the left?
Can I precompute from the right?
Can I combine those two results?
```

---

## 6. Core Mental Models

### Mental Model 1: Everything Except Self = Left Side × Right Side

The most important mental model:

```text
product except nums[i]
=
product of everything before i
*
product of everything after i
```

This transforms a vague problem into a structured one.

Instead of thinking:

```text
How do I skip nums[i] while multiplying everything?
```

think:

```text
What is on the left of i?
What is on the right of i?
```

### Mental Model 2: Running Product Remembers the Past

The initial worry was:

```text
How do I handle i-1, i-2, i-3?
```

The better mental model:

```text
A running product already remembers all previous elements.
```

Example:

```python
nums = [1, 2, 3, 4]
```

When we reach index `3`, the running left product is:

```text
1 * 2 * 3 = 6
```

We do not need to manually access:

```text
nums[2], nums[1], nums[0]
```

The running product carries that information.

### Mental Model 3: Use Product First, Then Update

This is the central implementation rule.

For the left side:

```python
left_product.append(left_current_product)
left_current_product *= nums[i]
```

Why?

Before processing index `i`, `left_current_product` already means:

```text
product of everything before i
```

So we must store it first.

Then we multiply by `nums[i]` so the current number becomes available for the next index.

If we updated first, we would accidentally include `nums[i]` in its own product.

### Mental Model 4: Symmetry Between Left and Right

The right side is the same logic in reverse.

Left pass:

```text
Move left to right.
current product means everything before i.
```

Right pass:

```text
Move right to left.
current product means everything after i.
```

This symmetry is powerful. Once the left side is understood, the right side is not a completely new problem.

### Mental Model 5: Sequential Loops Are Still Linear

A big complexity realization:

```text
Running three separate loops does not mean O(n³).
```

Three sequential loops:

```python
for i in range(n):
    ...

for i in range(n):
    ...

for i in range(n):
    ...
```

are:

```text
O(n) + O(n) + O(n) = O(3n) = O(n)
```

Nested loops are different:

```python
for i in range(n):
    for j in range(n):
        ...
```

That is:

```text
O(n²)
```

### Mental Model 6: Preallocated List Means Existing Slots

For the right product array:

```python
right_product = [0] * len(nums)
```

This creates slots so we can do:

```python
right_product[i] = value
```

The placeholder `0`s do not mean product values. They are simply reserving positions.

### Mental Model 7: Lists Are Not Multiplied Element-by-Element in Python

This does not work:

```python
left_product * right_product
```

because both are lists.

Python supports:

```python
[1, 2] * 3
```

which repeats the list:

```python
[1, 2, 1, 2, 1, 2]
```

But Python does not support direct element-wise multiplication between two lists.

So we use index-by-index multiplication.

---

## 7. Mental Breakthroughs and Realizations

### Breakthrough 1: Empty Product Is 1

#### Trigger

The question:

```text
If there is nothing before i, should it be 0 or 1?
```

#### Correct Understanding

It should be `1`.

#### Why It Matters

This removes the need for special cases.

For index `0`:

```python
left_product[0] = 1
```

For the last index:

```python
right_product[last_index] = 1
```

The value `1` behaves neutrally in multiplication.

---

### Breakthrough 2: Avoid i-1, i-2, i-3

#### Trigger

The question:

```text
i-1 seems easy, but what about i-2, i-3, and so on?
```

#### Correct Understanding

Do not manually access all previous elements.

Use a running product.

#### Why It Matters

This is the move from brute force thinking to linear-time thinking.

Instead of recomputing a range repeatedly, we carry the result forward.

---

### Breakthrough 3: Use Product First, Then Update

#### Trigger

While constructing the left product array.

#### Correct Understanding

At index `i`, the current product represents everything before `i`, so use it first.

Then include `nums[i]` for future indexes.

#### Why It Matters

This prevents the current element from being included in its own answer.

---

### Breakthrough 4: Multiple O(n) Loops Are Still O(n)

#### Trigger

The concern:

```text
If we build right_product too, won't we run another loop?
```

#### Correct Understanding

Yes, but sequential loops add constants.

```text
O(n) + O(n) + O(n) = O(n)
```

#### Why It Matters

This is a fundamental Big-O understanding.

Optimized solutions often use multiple linear passes.

---

### Breakthrough 5: The Right Side Is the Left Side in Reverse

#### Trigger

After understanding left products.

#### Correct Understanding

Right products use the same running product concept, but the loop moves from right to left.

#### Why It Matters

This reduces cognitive load.

Instead of learning a new idea, we reuse the same invariant in the opposite direction.

---

### Breakthrough 6: Preallocation Is Needed for Index Assignment

#### Trigger

The question:

```text
Why do we need to create the list with 0 first for right?
```

#### Correct Understanding

Because:

```python
right_product[i] = value
```

requires index `i` to already exist.

#### Why It Matters

This clarified the difference between:

```python
append()
```

and:

```python
result[i] = value
```

---

### Breakthrough 7: Pattern Recognition Comes From Exposure

#### Trigger

The emotional question:

```text
Why couldn't I find the algorithm, and how can I think like this one day?
```

#### Correct Understanding

The issue was not lack of ability. It was limited exposure to the pattern.

Algorithms are like vocabulary. You learn them by encountering situations where they apply.

#### Why It Matters

This shifted the focus from self-judgment to skill-building.

The goal is not:

```text
Can I invent every pattern instantly?
```

The goal is:

```text
Can I recognize this pattern next time?
Can I explain why it works?
Can I rebuild it without memorizing code?
```

---

## 8. Questions, Confusions, and Discoveries

| My Question / Confusion | Why It Happened | Correct Understanding | Example |
|---|---|---|---|
| If O(n²) were allowed, I could solve it with nested loops. Why not? | The brute-force idea directly matches the problem statement. | Nested loops would be O(n²), but the problem requires O(n). | For every `i`, scanning every `j` gives `n * n`. |
| If there is nothing before `i`, should it be `0` or `1`? | Empty product feels unintuitive at first. | Empty product is `1` because `1` is multiplication identity. | `left_product[0] = 1`. |
| How do we handle `i-1`, `i-2`, `i-3`? | Thinking explicitly about previous indexes. | Use a running product that already contains all previous values. | At index `3`, running product can already be `1 * 2 * 3`. |
| Should we use an `if` for `i-1` or start range from `1`? | Trying to manually handle the first index edge case. | Start from index `0`; running product initialized to `1` handles the edge case. | `left_product.append(1)` at index `0`. |
| Should we build right product too? Won't another loop break O(n)? | Confusion between multiple sequential loops and nested loops. | Sequential loops are still O(n). | Three passes: `O(n) + O(n) + O(n) = O(n)`. |
| How does the right loop range work? | Reverse `range()` boundaries can be tricky. | Use `range(len(nums)-1, -1, -1)` to include index `0`. | For length `4`, indexes are `3, 2, 1, 0`. |
| Can I return `left_product * right_product`? | Thinking mathematically about multiplying arrays. | Python lists do not multiply element-by-element. Combine by index. | `answer.append(left[i] * right[i])`. |
| Why create `right_product = [0] * len(nums)` first? | Unclear difference between append and index assignment. | Index assignment requires existing slots. | `right_product[3] = 1` needs index `3` to exist. |
| Are the `0`s in right_product meaningful? | Placeholder values can look like actual values. | They are only placeholders and will be replaced. | `[0,0,0,0] -> [24,12,4,1]`. |
| Why couldn't I think of this algorithm naturally? | Comparing current ability to polished solutions. | Pattern recognition comes from exposure and reflection. | Next time, "before/after each index" should trigger prefix/suffix thinking. |
| Did I solve a Python problem or an algorithm problem? | Some confusion was about syntax and some about reasoning. | The main challenge was algorithmic pattern recognition, with some Python list mechanics. | Running product = algorithm; preallocated list = Python/data structure mechanics. |

---

## 9. Invariants Discovered

An invariant is a statement that remains true at a specific point during an algorithm.

Invariants are extremely useful because they help us reason about correctness.

### Left Pass Invariant

#### Statement

Before processing index `i`:

```text
left_current_product =
product of all elements before index i
```

#### Why It Remains True

We start with:

```python
left_current_product = 1
```

At index `0`, there is nothing before it, so the invariant is true.

After storing that value, we update:

```python
left_current_product *= nums[i]
```

Now the current element is included for the next index.

So when the loop moves to `i + 1`, `left_current_product` correctly represents the product of all elements before `i + 1`.

#### How It Helps Derive the Code

Because the invariant says the product already represents everything before index `i`, the code becomes:

```python
left_product.append(left_current_product)
left_current_product *= nums[i]
```

No special case is needed.

#### How It Simplifies Reasoning

Instead of thinking:

```text
left[i] = nums[i-1] * nums[i-2] * ...
```

we think:

```text
left_current_product already has that.
```

---

### Right Pass Invariant

#### Statement

Before processing index `i` while moving right to left:

```text
right_current_product =
product of all elements after index i
```

#### Why It Remains True

We start at the last index with:

```python
right_current_product = 1
```

There is nothing after the last index, so this is correct.

After storing it:

```python
right_product[i] = right_current_product
```

we update:

```python
right_current_product *= nums[i]
```

Now `nums[i]` becomes part of the product for the next index to the left.

#### How It Helps Derive the Code

Because the invariant says `right_current_product` already represents everything after index `i`, the code becomes:

```python
right_product[i] = right_current_product
right_current_product *= nums[i]
```

#### How It Simplifies Reasoning

Instead of thinking:

```text
right[i] = nums[i+1] * nums[i+2] * ...
```

we use the carried product.

---

### Combine Step Invariant

#### Statement

For every index `i`:

```text
answer[i] = left_product[i] * right_product[i]
```

#### Why It Remains True

`left_product[i]` excludes `nums[i]` because it only contains elements before index `i`.

`right_product[i]` excludes `nums[i]` because it only contains elements after index `i`.

Multiplying them gives all elements except `nums[i]`.

#### How It Helps Derive the Code

```python
answer.append(left_product[i] * right_product[i])
```

### Why Interviewers Care About Invariants

Interviewers often want to know not only that the code works, but why it works.

An invariant lets you explain correctness clearly:

```text
Before each index, my running product contains exactly the values I need and excludes the current value.
```

That is much stronger than saying:

```text
I saw this solution before.
```

---

## 10. Pen-and-Paper Reasoning

During the conversation, handwritten notes were used to reason about the left product array.

The key idea from the notes was:

```text
For each index i:
left[i] should contain the product of all numbers before i.
```

### Reconstructed Notebook Logic

Given:

```python
nums = [1, 2, 3, 4]
```

We want:

```python
left_product = [1, 1, 2, 6]
```

Index-by-index:

```text
left_product[0] = product before index 0 = nothing = 1

left_product[1] = product before index 1 = nums[0] = 1

left_product[2] = product before index 2 = nums[0] * nums[1]
                = 1 * 2
                = 2

left_product[3] = product before index 3 = nums[0] * nums[1] * nums[2]
                = 1 * 2 * 3
                = 6
```

### OCR Interpretation Summary

The handwritten explanation showed that the user understood:

- We are building a left product array.
- The value at each index should exclude the current element.
- The current running product should be stored first.
- Then the running product should be updated using the current number.
- There is no need to directly access `i-1`, `i-2`, or `i-3`.

### Corrected and Cleaned Version

The clean version of the handwritten reasoning:

```python
left_product = []
left_current_product = 1

for i in range(len(nums)):
    left_product.append(left_current_product)
    left_current_product *= nums[i]
```

### Dry Run From Notes

Initial:

```python
left_product = []
left_current_product = 1
```

At `i = 0`:

```python
left_product.append(1)
# left_product = [1]

left_current_product *= nums[0]
# left_current_product = 1 * 1 = 1
```

At `i = 1`:

```python
left_product.append(1)
# left_product = [1, 1]

left_current_product *= nums[1]
# left_current_product = 1 * 2 = 2
```

At `i = 2`:

```python
left_product.append(2)
# left_product = [1, 1, 2]

left_current_product *= nums[2]
# left_current_product = 2 * 3 = 6
```

At `i = 3`:

```python
left_product.append(6)
# left_product = [1, 1, 2, 6]

left_current_product *= nums[3]
# left_current_product = 6 * 4 = 24
```

Final:

```python
left_product = [1, 1, 2, 6]
```

### Lesson Learned From Pen-and-Paper Work

The handwritten notes were valuable because they revealed the invariant naturally:

```text
Before processing index i,
left_current_product contains the product of everything before i.
```

This is the kind of reasoning that helps build real problem-solving skill.

---

## 11. Step-by-Step Solution Evolution

### Version 1: Brute Force Concept

#### Approach

For every index `i`, multiply every number except `nums[i]`.

#### Why It Works

It directly follows the problem statement.

#### Limitation

It uses nested loops:

```text
O(n²)
```

#### Why Improvement Was Needed

The problem requires:

```text
O(n)
```

---

### Version 2: Split Into Left and Right Products

#### Approach

For each index:

```text
answer[i] =
product of numbers before i
*
product of numbers after i
```

#### Why It Works

Everything except the current number is either before it or after it.

#### Limitation

We still need an efficient way to calculate left and right products.

---

### Version 3: Build Left Product Using Running Product

#### Approach

Move left to right.

Maintain:

```python
left_current_product
```

Before each index, store it.

Then update it.

```python
left_product.append(left_current_product)
left_current_product *= nums[i]
```

#### What Problem It Solved

Avoided manually accessing:

```text
i-1, i-2, i-3
```

#### Limitation

Only solves the left half of the product.

---

### Version 4: Build Right Product Using Running Product

#### Approach

Move right to left.

Maintain:

```python
right_current_product
```

Store it first.

Then update it.

```python
right_product[i] = right_current_product
right_current_product *= nums[i]
```

#### What Problem It Solved

Captured the product of everything after each index.

#### Important Implementation Detail

Because we assign by index, we need:

```python
right_product = [0] * len(nums)
```

---

### Version 5: Combine Left and Right Products

#### Approach

For each index:

```python
answer.append(left_product[i] * right_product[i])
```

#### What Problem It Solved

It produced the final product except self.

#### Final Result

Accepted solution.

---

## 12. Final Accepted Solution

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_current_product = 1
        right_current_product = 1

        left_product = []
        right_product = [0] * len(nums)

        answer = []

        # Build left_product
        # left_product[i] stores the product of everything before index i
        for i in range(len(nums)):
            left_product.append(left_current_product)
            left_current_product *= nums[i]

        # Build right_product
        # right_product[i] stores the product of everything after index i
        for i in range(len(nums) - 1, -1, -1):
            right_product[i] = right_current_product
            right_current_product *= nums[i]

        # Combine left and right products
        # answer[i] = product before i * product after i
        for i in range(len(nums)):
            answer.append(left_product[i] * right_product[i])

        return answer
```

### Explanation of Each Block

#### Initial Running Products

```python
left_current_product = 1
right_current_product = 1
```

Both start at `1` because the product of no elements is `1`.

This handles:

- No elements before the first index
- No elements after the last index

#### Left Product List

```python
left_product = []
```

We use an empty list because we build it from left to right using `append()`.

#### Right Product List

```python
right_product = [0] * len(nums)
```

We preallocate this because we fill it by direct index assignment from right to left.

#### Answer List

```python
answer = []
```

This stores the final result.

#### Left Pass

```python
for i in range(len(nums)):
    left_product.append(left_current_product)
    left_current_product *= nums[i]
```

At each index:

1. Store product of everything before index `i`.
2. Include `nums[i]` for the next index.

#### Right Pass

```python
for i in range(len(nums) - 1, -1, -1):
    right_product[i] = right_current_product
    right_current_product *= nums[i]
```

At each index:

1. Store product of everything after index `i`.
2. Include `nums[i]` for the next index to the left.

#### Combine Pass

```python
for i in range(len(nums)):
    answer.append(left_product[i] * right_product[i])
```

At each index:

```text
product before i * product after i
```

equals product of all numbers except `nums[i]`.

---

## 13. Full Dry Run

### Main Example

```python
nums = [1, 2, 3, 4]
```

---

### Left Product Pass

Initial state:

```python
left_current_product = 1
left_product = []
```

| i | nums[i] | left_current_product before append | left_product after append | left_current_product after update |
|---|---:|---:|---|---:|
| 0 | 1 | 1 | `[1]` | `1 * 1 = 1` |
| 1 | 2 | 1 | `[1, 1]` | `1 * 2 = 2` |
| 2 | 3 | 2 | `[1, 1, 2]` | `2 * 3 = 6` |
| 3 | 4 | 6 | `[1, 1, 2, 6]` | `6 * 4 = 24` |

Final:

```python
left_product = [1, 1, 2, 6]
```

---

### Right Product Pass

Initial state:

```python
right_current_product = 1
right_product = [0, 0, 0, 0]
```

Loop:

```python
for i in range(len(nums) - 1, -1, -1):
```

Indexes:

```text
3, 2, 1, 0
```

| i | nums[i] | right_current_product before assignment | right_product after assignment | right_current_product after update |
|---|---:|---:|---|---:|
| 3 | 4 | 1 | `[0, 0, 0, 1]` | `1 * 4 = 4` |
| 2 | 3 | 4 | `[0, 0, 4, 1]` | `4 * 3 = 12` |
| 1 | 2 | 12 | `[0, 12, 4, 1]` | `12 * 2 = 24` |
| 0 | 1 | 24 | `[24, 12, 4, 1]` | `24 * 1 = 24` |

Final:

```python
right_product = [24, 12, 4, 1]
```

---

### Combine Pass

Initial:

```python
answer = []
```

| i | left_product[i] | right_product[i] | product | answer |
|---|---:|---:|---:|---|
| 0 | 1 | 24 | 24 | `[24]` |
| 1 | 1 | 12 | 12 | `[24, 12]` |
| 2 | 2 | 4 | 8 | `[24, 12, 8]` |
| 3 | 6 | 1 | 6 | `[24, 12, 8, 6]` |

Final:

```python
answer = [24, 12, 8, 6]
```

---

### Brief Dry Run With Zero Example

```python
nums = [-1, 1, 0, -3, 3]
```

Left products:

```python
left_product = [1, -1, -1, 0, 0]
```

Right products:

```python
right_product = [0, 0, -9, 3, 1]
```

Combine:

```text
answer[0] = 1 * 0 = 0
answer[1] = -1 * 0 = 0
answer[2] = -1 * -9 = 9
answer[3] = 0 * 3 = 0
answer[4] = 0 * 1 = 0
```

Final:

```python
[0, 0, 9, 0, 0]
```

This shows why the prefix/suffix approach handles zeros naturally without division.

---

## 14. Complexity Analysis

### Time Complexity

The solution has three loops.

#### Left product loop

```python
for i in range(len(nums)):
```

This is:

```text
O(n)
```

#### Right product loop

```python
for i in range(len(nums) - 1, -1, -1):
```

This is also:

```text
O(n)
```

#### Combine loop

```python
for i in range(len(nums)):
```

This is also:

```text
O(n)
```

Total:

```text
O(n) + O(n) + O(n) = O(3n)
```

In Big-O notation, constants are ignored:

```text
O(3n) = O(n)
```

So the final time complexity is:

```text
Time Complexity: O(n)
```

### Why Multiple Sequential Loops Are Still O(n)

Sequential loops do not multiply each other.

This:

```python
for i in range(n):
    ...

for i in range(n):
    ...
```

is:

```text
O(n) + O(n) = O(2n) = O(n)
```

But this:

```python
for i in range(n):
    for j in range(n):
        ...
```

is:

```text
O(n * n) = O(n²)
```

The difference is:

```text
Sequential loops add.
Nested loops multiply.
```

### Space Complexity

The accepted solution uses:

```python
left_product
right_product
answer
```

Each list has size `n`.

So the space complexity is:

```text
O(n)
```

If we count the output list, space is clearly O(n).

Even if LeetCode does not count the returned output array as extra space, this implementation still uses two additional arrays:

```python
left_product
right_product
```

So the extra working space is:

```text
O(n)
```

### Trade-Off

This solution is very readable and beginner-friendly.

There is a more space-optimized version that uses the answer array itself to store left products, then multiplies right products into it. That avoids separate left and right arrays.

However, the current version is excellent for learning because it makes the algorithm explicit.

---

## 15. Alternative Approaches

### Alternative 1: Brute Force Nested Loops

#### Core Idea

For each index, multiply all other elements.

#### Advantages

- Very easy to understand.
- Direct translation of the problem statement.

#### Disadvantages

- O(n²) time.
- Fails the required O(n) constraint for large inputs.

#### Interview Suitability

Good as a starting explanation, not as the final solution.

It shows you understand the problem before optimizing.

---

### Alternative 2: Division-Based Approach

#### Core Idea

Calculate total product of all numbers, then:

```python
answer[i] = total_product // nums[i]
```

#### Advantages

- Simple when there are no zeros.
- O(n) time.

#### Disadvantages

- Division is forbidden by the problem.
- Zeros complicate the logic.
- Multiple zeros create special cases.

#### Interview Suitability

Not acceptable as the final solution because the problem explicitly forbids division.

However, mentioning why it is rejected can show awareness.

---

### Alternative 3: Prefix/Suffix Arrays

#### Core Idea

Build:

```python
left_product
right_product
```

Then combine them.

#### Advantages

- Clear.
- Easy to reason about.
- Handles zeros naturally.
- O(n) time.
- No division.

#### Disadvantages

- Uses O(n) extra space.

#### Interview Suitability

Very good, especially when explaining the problem for the first time.

---

### Alternative 4: Space-Optimized Prefix/Suffix

#### Core Idea

Instead of storing both `left_product` and `right_product`, store left products directly in `answer`.

Then move from right to left and multiply a running right product into `answer`.

Conceptually:

```text
First pass:
answer[i] = product of everything before i

Second pass:
answer[i] *= product of everything after i
```

#### Advantages

- O(n) time.
- O(1) extra space if the output array is not counted.
- Common interview follow-up.

#### Disadvantages

- Slightly less beginner-friendly.
- The answer array changes meaning during the algorithm.
- Requires stronger invariant tracking.

#### Interview Suitability

Excellent as an optimized follow-up after explaining the clearer two-array version.

---

## 16. Python Knowledge Gained

### `range(len(nums))`

Used to loop over indexes from left to right.

```python
for i in range(len(nums)):
```

For a list of length `4`, this gives:

```text
0, 1, 2, 3
```

### Reverse `range()`

Used to loop from right to left:

```python
for i in range(len(nums) - 1, -1, -1):
```

For length `4`, this gives:

```text
3, 2, 1, 0
```

Breakdown:

```text
start = len(nums) - 1
stop = -1
step = -1
```

The stop is `-1` because Python's `range()` excludes the stop value. So index `0` is included.

### `append()`

Used when building a list from left to right:

```python
left_product.append(left_current_product)
```

This adds a new element to the end of the list.

Starting from:

```python
left_product = []
```

After appending values:

```python
[1]
[1, 1]
[1, 1, 2]
[1, 1, 2, 6]
```

### Index Assignment

Used when assigning to an existing position:

```python
right_product[i] = right_current_product
```

This requires that index `i` already exists.

That is why we create:

```python
right_product = [0] * len(nums)
```

### Preallocating a List

```python
right_product = [0] * len(nums)
```

For `len(nums) == 4`, this creates:

```python
[0, 0, 0, 0]
```

These are placeholders.

### List Multiplication

Python allows:

```python
[0] * 4
```

which gives:

```python
[0, 0, 0, 0]
```

But Python does not allow:

```python
[1, 2] * [3, 4]
```

because list-by-list multiplication is not element-wise.

### Combining Lists by Index

To multiply matching indexes:

```python
answer = []

for i in range(len(nums)):
    answer.append(left_product[i] * right_product[i])
```

This is element-wise combination done manually.

### Type Hints

The LeetCode method uses:

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
```

This means:

- `nums` should be a list of integers.
- The function returns a list of integers.

In LeetCode, `List` is typically provided from:

```python
from typing import List
```

---

## 17. Pattern Recognition Notes for Future Problems

### Future Clues That Suggest Prefix/Suffix

Think about prefix/suffix when the problem says:

```text
For every index...
```

and each answer depends on:

```text
elements before the index
elements after the index
or all elements except the current one
```

### Trigger Phrases

Watch for wording like:

- "except self"
- "product except current"
- "sum of elements before and after"
- "left side and right side"
- "for each index"
- "before index i"
- "after index i"
- "without using nested loops"
- "must be O(n)"
- "no division"

### Common Problem Structures

Prefix/suffix may help when:

```text
answer[i] depends on previous elements
answer[i] depends on future elements
answer[i] depends on both sides
```

Examples:

```text
left sum + right sum
left max + right max
left product * right product
count before + count after
minimum before/after
```

### Similar Problems

- Find Pivot Index
- Left and Right Sum Differences
- Trapping Rain Water
- Product of Array Except Self
- Range Sum Query
- Prefix Sum problems
- Maximum difference using previous minimum
- Count smaller/greater elements on either side

### Transferable Lesson

When brute force recomputes range information again and again, ask:

```text
Can I precompute this information from left to right?
Can I precompute this information from right to left?
Can I combine those precomputed values?
```

---

## 18. Rules to Lock Into Memory

### Algorithm Rules

1. If each answer needs information from before and after an index, think prefix/suffix.
2. Product except self can be split into left product and right product.
3. Empty product is `1`.
4. Use the running product first, then update it.
5. A running variable can remember a whole range.
6. Avoid manually thinking in terms of `i-1`, `i-2`, `i-3` when a cumulative value can handle it.
7. Sequential O(n) loops are still O(n).
8. Nested loops usually create O(n²).
9. Precomputation is useful when brute force repeats range calculations.
10. Invariants explain why the algorithm works.

### Python Rules

1. Use `append()` when growing a list naturally from left to right.
2. Use `[0] * n` when you need existing slots for index assignment.
3. `range(start, stop, step)` excludes `stop`.
4. To include index `0` in a reverse loop, use stop value `-1`.
5. Python does not multiply two lists element-by-element.
6. Combine two lists by looping through indexes.
7. Placeholder values are not necessarily meaningful final values.

### Interview Rules

1. Start with brute force to show understanding.
2. Identify repeated work.
3. Explain the optimization pattern.
4. State the invariant.
5. Dry run clearly.
6. Analyze time and space.
7. Mention possible O(1) extra-space optimization as a follow-up.

---

## 19. Reflection on My Learning Journey

### What I Figured Out Independently

The user correctly identified that:

```text
A nested loop would solve the problem if O(n²) were allowed.
```

This means the basic problem relationship was understood.

The user also correctly understood the reverse range logic:

```python
range(len(nums) - 1, -1, -1)
```

and explained why:

- start should be `len(nums) - 1`
- stop should be `-1`
- step should be `-1`

The user also summarized the algorithm beautifully:

```text
find left products
find right products
combine
avoid i-1/i+1
use the product first
```

That summary shows real understanding.

### Where Guidance Was Needed

Guidance was needed for:

- Empty product being `1`
- Replacing explicit index access with running product
- Understanding why multiple loops are still O(n)
- Understanding why the right product array needed preallocation
- Understanding why list multiplication does not combine elements
- Recognizing the prefix/suffix pattern

These were not failures. They were the exact learning points of the problem.

### How Reasoning Evolved

The reasoning evolved from:

```text
For every index, multiply all other elements.
```

to:

```text
For every index, combine product before it and product after it.
```

Then it evolved further to:

```text
I can compute before/after products using running products.
```

Finally, it became:

```text
The invariant explains why the code works.
```

That is a strong learning progression.

### Important Emotional Realization

At one point, the user asked why they could not naturally discover this algorithm.

The important answer:

```text
Pattern recognition comes from exposure.
```

The goal is not to magically invent every algorithm immediately.

The goal is to:

- Understand the pattern deeply after seeing it.
- Recognize the same structure next time.
- Build the ability to derive the solution from invariants.
- Avoid memorizing code without understanding.

### Growth in Problem-Solving Ability

This session was valuable because the user did not just ask for the solution.

Instead, the user asked questions like:

```text
Why is empty product 1?
How do I avoid i-1, i-2?
Why is another loop still O(n)?
Why do we preallocate right_product?
Can lists be multiplied directly?
```

These are the questions that build real programming skill.

The accepted solution was the result of understanding, not copy-pasting.

---

## 20. Interview Preparation Notes

### How to Explain This Solution in an Interview

A good interview explanation:

```text
The brute-force approach would be to calculate the product of all elements except the current one for every index, but that would be O(n²).

To optimize, I observe that for each index i, the product except self can be split into two parts: product of elements before i and product of elements after i.

I first build a left_product array where left_product[i] stores the product of all elements before i. I use a running product initialized to 1.

Then I build a right_product array from right to left where right_product[i] stores the product of all elements after i.

Finally, for each index, answer[i] is left_product[i] multiplied by right_product[i].

This avoids division and runs in O(n) time.
```

### Important Points to Mention

Mention:

- Brute force is O(n²).
- Division is not allowed.
- Prefix/suffix products solve the problem.
- Empty product is `1`.
- Use product before updating it.
- Multiple passes are still O(n).
- The solution handles zeros naturally.
- Space can be optimized later.

### Common Follow-Up Questions

#### Can you solve it with O(1) extra space?

Yes, if the output array does not count as extra space.

Use the answer array to store left products first, then multiply right products into it while traversing from right to left.

#### Why not use division?

The problem forbids division.

Also, zeros make division-based logic more complicated.

#### What happens if there is one zero?

Only the index containing zero gets the product of all non-zero elements. Others become zero.

The prefix/suffix approach handles this naturally.

#### What happens if there are multiple zeros?

Every result becomes zero.

Again, the prefix/suffix approach handles this naturally.

#### Why initialize running product to 1?

Because `1` is the identity value for multiplication.

#### Why store before updating?

Because the current element should be excluded from its own product.

### Candidate Mistakes to Avoid

1. Using division.
2. Writing nested loops.
3. Initializing empty product as `0`.
4. Updating running product before storing it.
5. Forgetting to include index `0` in the reverse loop.
6. Trying to assign into an empty list by index.
7. Trying to multiply two Python lists directly.
8. Confusing O(3n) with O(n³).
9. Forgetting about zeros.
10. Memorizing the code without understanding the invariant.

### Final Interview-Level Summary

```text
This problem is solved by recognizing that product except self at each index is the product of all elements before that index multiplied by the product of all elements after that index. We compute those two pieces using prefix and suffix running products, then combine them. The key invariant is that before processing an index, the running product contains exactly the product of elements on the side already traversed, excluding the current element.
```

---

## Appendix A: Compact Revision Version

### Pattern

```text
Prefix/Suffix Products
```

### Formula

```text
answer[i] = product_before_i * product_after_i
```

### Left Pass

```python
left_current_product = 1

for i in range(len(nums)):
    left_product.append(left_current_product)
    left_current_product *= nums[i]
```

### Right Pass

```python
right_current_product = 1

for i in range(len(nums) - 1, -1, -1):
    right_product[i] = right_current_product
    right_current_product *= nums[i]
```

### Combine

```python
for i in range(len(nums)):
    answer.append(left_product[i] * right_product[i])
```

### Core Rule

```text
Use product first.
Then update product.
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

### Future Trigger

```text
For each index, need information before and after it.
```

---

## Appendix B: One-Page Memory Card

```text
Problem:
Product of Array Except Self

Constraint:
O(n), no division

Brute force:
For each i, multiply every j != i -> O(n²)

Optimization:
Split into left and right.

answer[i] =
product of everything before i
*
product of everything after i

Empty product:
1

Left invariant:
Before index i,
left_current_product = product before i

Right invariant:
Before index i from right,
right_current_product = product after i

Implementation rule:
Store first, update second.

Python:
append() grows list.
right[i] assignment needs preallocated list.
range(len(nums)-1, -1, -1) includes index 0.
Lists do not multiply element-by-element.

Complexity:
Three sequential loops = O(n), not O(n²).

Interview phrase:
I avoid recomputation by precomputing prefix and suffix products.
```

---

# End of Guide
