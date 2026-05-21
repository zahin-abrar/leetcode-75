# LeetCode 75 Problem #6 — Reverse Words in a String  
## Full Learning Guide from Guided Reasoning, Debugging, Pointer Tracing, and In-Place Simulation

---

## 0. Learning Context

This guide documents the full learning journey for **Reverse Words in a String**, including both:

1. The normal Python solution using `split()`, `reverse()`, and `join()`.
2. The follow-up exploration: simulating an **in-place** solution using a mutable character list.

The main value of this session was not only getting an accepted answer. The deeper value came from understanding:

- why the normal solution is straightforward in Python,
- why the follow-up is harder,
- what “in-place” really means,
- how `read` / `write` pointers work,
- how `left` / `right` pointers work,
- why slicing and direct indexing behave differently,
- why leftover characters remain after overwrite-style cleanup,
- how to reason about boundaries and off-by-one cases.

This guide is intentionally detailed. It is meant to be a revision-ready artifact for building real problem-solving skill.

---

# 1. Problem Summary in My Own Words

## 1.1 What the Problem Asks

Given a string `s`, reverse the **order of the words**.

A word is a sequence of non-space characters.

Important rules:

- Words may be separated by one or more spaces.
- The input may contain leading spaces.
- The input may contain trailing spaces.
- The output must contain words in reversed order.
- The output must have exactly one space between words.
- The output must not contain leading or trailing spaces.

So the problem is not simply “reverse the string character by character.”  
It is:

> Reverse the word order, clean up extra spaces, and preserve the characters inside each word.

---

## 1.2 Examples

### Example 1

```python
s = "the sky is blue"
```

Words:

```text
the | sky | is | blue
```

Reverse word order:

```text
blue | is | sky | the
```

Output:

```python
"blue is sky the"
```

---

### Example 2

```python
s = "  hello world  "
```

After removing extra leading/trailing spaces:

```text
hello world
```

Reverse word order:

```text
world hello
```

Output:

```python
"world hello"
```

---

### Example 3

```python
s = "a good   example"
```

The input has multiple spaces between `good` and `example`.

Clean spacing:

```text
a good example
```

Reverse word order:

```text
example good a
```

Output:

```python
"example good a"
```

---

## 1.3 What Needs to Be Reversed?

The **order of the words** must be reversed.

This:

```text
a good example
```

becomes:

```text
example good a
```

But each word remains readable:

```text
example
good
a
```

We do **not** want:

```text
elpmaxe doog a
```

That would be the result of reversing the entire string character by character without fixing individual words.

---

## 1.4 What Must Stay Unchanged?

The characters inside each word must remain in their original order.

For example:

```text
good
```

must remain:

```text
good
```

not:

```text
doog
```

---

## 1.5 Why the Normal Python Solution Is Straightforward

Python gives a very convenient behavior:

```python
s.split()
```

When called without arguments, `split()`:

- ignores leading spaces,
- ignores trailing spaces,
- treats multiple spaces as a single separator,
- returns only the actual words.

Example:

```python
"  hello   world  ".split()
```

returns:

```python
["hello", "world"]
```

So the normal solution becomes:

```text
split into words
reverse words
join with one space
```

This is why the main problem felt closer to Easy when using Python built-ins.

---

## 1.6 Why the Follow-Up Becomes Harder

The follow-up asks:

> If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

This changes the problem significantly.

The normal Python solution uses extra structures:

```python
words = s.split()
```

That creates a list of words, which takes extra space proportional to the input size.

The follow-up asks us to think differently:

- Do not create a list of words.
- Do not build a new output string during the algorithm.
- Modify the existing character storage directly.
- Use only a few pointer variables.

In Python, strings are immutable, so we cannot truly mutate the original string.  
To learn the algorithmic idea, we simulated the follow-up using a list of characters.

---

# 2. Initial Thinking Process

## 2.1 First Proposed Approach

The initial idea was:

1. Split the words into a list.
2. Loop through the list and check for spaces.
3. Create a new list without unnecessary spaces.
4. Reverse the list.
5. Reconstruct the sentence with spaces.

This was a reasonable starting point because the problem is about words and spaces.

---

## 2.2 Key Discovery: `split()` Already Handles Spaces

The first important clarification was how Python’s `split()` behaves.

There was an initial thought that multiple spaces might produce empty strings or separate space elements.

For example:

```python
"a good   example".split()
```

The result is not:

```python
["a", "good", "", "", "example"]
```

Instead, Python gives:

```python
["a", "good", "example"]
```

This means `split()` already removes the extra-space complexity for the normal problem.

---

## 2.3 Normal Python Solution Shape

After understanding `split()`, the plan became:

```text
split into words
reverse the words
join them with one space
```

This gives:

```python
def reverseWords(s: str) -> str:
    split_words = s.split()
    split_words.reverse()
    return " ".join(split_words)
```

This solution was accepted.

---

## 2.4 Why the Problem Felt Too Easy for Medium

The normal Python solution is short and clean.

That created a reasonable question:

> Why is this problem categorized as Medium?

The answer is that the **follow-up** contains the deeper algorithmic challenge.

The main problem can be solved easily with Python built-ins.  
The follow-up asks for in-place manipulation under a mutable-string assumption.

That version requires:

- space cleanup without `split()`,
- reversing the whole character array,
- reversing each word,
- pointer movement,
- boundary reasoning,
- avoiding extra full-size data structures.

---

# 3. Understanding the Follow-Up Problem

## 3.1 What “In-Place” Means

“In-place” means modifying the existing data structure directly instead of creating a separate result structure.

For example, given:

```python
arr = [1, 2, 3, 4]
```

An in-place reverse modifies the same list:

```python
[4, 3, 2, 1]
```

It does not create:

```python
new_arr = [4, 3, 2, 1]
```

In-place usually means:

```text
Use the original storage.
Use only a fixed number of extra variables.
Do not allocate another full-size list/string.
```

---

## 3.2 Why Mutable Strings Matter

The follow-up says:

> If the string data type is mutable in your language...

This matters because some languages let you modify characters directly inside a string-like structure or character array.

Conceptually, if a string were mutable, we could do:

```text
swap character at index left with character at index right
```

directly inside the same memory.

---

## 3.3 Python Strings Are Immutable

In Python:

```python
s = "hello"
```

You cannot do:

```python
s[0] = "H"
```

This raises an error because strings are immutable.

So, in Python, we cannot truly perform the strict follow-up directly on a string.

---

## 3.4 Why We Simulated the Follow-Up with a Character List

To learn the algorithm, we converted the string into a list:

```python
chars = list(s)
```

Example:

```python
list("hello")
```

gives:

```python
["h", "e", "l", "l", "o"]
```

A list is mutable, so we can swap and overwrite characters.

Important distinction:

```text
This simulates the follow-up algorithm.
But converting string to list costs O(n) extra space in Python.
```

So the simulation helps us learn the in-place idea, but it does not strictly satisfy O(1) extra space in Python.

---

## 3.5 Why `split()` Violates the Spirit of the Follow-Up

The follow-up wants us to avoid extra full-size structures.

But:

```python
words = s.split()
```

creates a new list of words.

That list grows with the input size, so it uses O(n) extra space.

For the follow-up, the goal is to operate on the character storage directly.

---

## 3.6 Why Overwrite-Style Algorithms Are Used

In the cleanup phase, we need to remove extra spaces.

One tempting idea was to use `remove()` or `insert()`.

But repeated removing/inserting inside a list can cause elements to shift many times.

Instead, we use an overwrite strategy:

```text
read pointer  -> scans every character
write pointer -> marks where the next valid character should be placed
```

This lets us build the cleaned content at the front of the same list.

---

# 4. High-Level Algorithmic Strategy

The follow-up simulation uses this flow:

```text
1. Clean up spaces
2. Reverse the whole list
3. Reverse each word individually
4. Join the character list into a final string
```

---

## 4.1 Phase 1: Clean Up Spaces

Input:

```text
" and good  example "
```

Cleaned version:

```text
"and good example"
```

This phase removes:

- leading spaces,
- duplicate spaces,
- trailing spaces.

It preserves:

- characters inside words,
- exactly one space between words.

---

## 4.2 Phase 2: Reverse the Whole List

Cleaned:

```text
and good example
```

Reverse all characters:

```text
elpmaxe doog dna
```

Now the **word positions are in the desired reversed order**, but the letters inside each word are reversed.

Original word order:

```text
and | good | example
```

After whole reverse:

```text
elpmaxe | doog | dna
```

The positions correspond to:

```text
example | good | and
```

but each word is backward.

---

## 4.3 Phase 3: Reverse Each Word Individually

After whole reverse:

```text
elpmaxe doog dna
```

Reverse each word:

```text
example good and
```

This fixes the letters inside the words while preserving the reversed word order.

---

## 4.4 Phase 4: Join into Final String

Since we simulated with a character list, the final step is:

```python
"".join(chars)
```

This produces the final string.

---

## 4.5 Why the Order Matters

The order must be:

```text
clean spaces -> reverse whole -> reverse each word
```

If we reverse each word before reversing the whole list, we solve the wrong problem.

If we do not clean spaces first, word detection becomes more complicated because multiple spaces and leading/trailing spaces create messy boundaries.

Cleaning first gives us a simpler invariant:

```text
Words are separated by exactly one space.
There are no leading spaces.
There are no trailing spaces.
```

That makes word boundary detection much easier.

---

## 4.6 Visual Transformation

Starting input:

```text
" and good  example "
```

Cleanup:

```text
"and good example"
```

Whole reverse:

```text
"elpmaxe doog dna"
```

Reverse each word:

```text
"example good and"
```

Final output:

```text
"example good and"
```

---

# 5. Identified Algorithmic Patterns

## 5.1 Same-Direction Two Pointers

Used in cleanup.

Pointers:

```text
read  -> scans from left to right
write -> writes valid characters toward the front
```

Both move in the same direction, but they move differently:

- `read` moves every iteration.
- `write` moves only when a character is kept.

---

## 5.2 Opposite-Direction Two Pointers

Used in reversal.

Pointers:

```text
left  -> starts at beginning
right -> starts at end
```

They move toward each other:

```text
left increases
right decreases
```

At each step, we swap:

```text
chars[left] <-> chars[right]
```

---

## 5.3 In-Place Overwrite Simulation

Cleanup does not remove items immediately.

It overwrites valid characters at the front.

Example:

```text
original: [' ', 'a', ' ', 'b']
after overwrite: ['a', ' ', 'b', 'b'] or similar leftover state
valid region depends on write
```

The full list may still contain old leftover values.

The meaningful content is only:

```python
chars[:write]
```

---

## 5.4 Boundary Tracking

The solution depends heavily on boundary tracking:

- `write` marks the logical end of valid content.
- `left` and `right` mark the range to reverse.
- `word_start_index` marks where a word begins.
- `i - 1` marks where a word ends when `i` points at a space.

---

## 5.5 Range-Based Reversal

A reusable helper reverses any range:

```python
reverse_list(chars, left, right)
```

This helper is used for:

1. Reversing the entire cleaned list.
2. Reversing each individual word.

This is a clean design because the same swap logic is reused with different boundaries.

---

# 6. Pointer & Boundary Mental Models

This was the deepest part of the learning journey.

---

## 6.1 `read` Pointer

The `read` pointer scans the original list.

In cleanup:

```python
for read in range(len(converted_list)):
```

`read` visits every original character.

Mental model:

```text
read = where I am looking
```

It moves through:

```text
0, 1, 2, 3, ...
```

automatically in a `for` loop.

---

## 6.2 `write` Pointer

The `write` pointer marks where the next accepted character should be written.

Mental model:

```text
write = next valid write position
```

It only moves when we keep a character.

If we skip a character, `write` does not move.

---

## 6.3 Why `write` Points to the NEXT Write Position

Suppose we have accepted two characters:

```text
['a', 'b', ...]
```

The valid content occupies indexes:

```text
0 and 1
```

The next place to write is index:

```text
2
```

So:

```text
write = 2
```

This means:

```text
valid region = indexes 0 to write - 1
next write position = write
```

---

## 6.4 `converted_list[:write]` Excludes `write`

This was a key confusion.

In Python slicing:

```python
converted_list[:write]
```

includes indexes:

```text
0 up to write - 1
```

It does **not** include index `write`.

So if:

```text
write = 15
```

then:

```python
converted_list[:15]
```

includes indexes:

```text
0 to 14
```

This is perfect because `write` points to the next empty/write position.

Everything before `write` is the valid content.

---

## 6.5 `converted_list[write - 1]` Accesses the Last Valid Character

Direct indexing behaves differently from slicing.

```python
converted_list[write]
```

means:

```text
give me exactly index write
```

But index `write` is the next write position, not the last valid character.

The last valid character is at:

```python
converted_list[write - 1]
```

This distinction was one of the biggest mental unlocks.

---

## 6.6 Slicing vs Direct Indexing

### Slicing

```python
converted_list[:write]
```

means:

```text
up to but not including write
```

So it automatically excludes `write`.

### Direct indexing

```python
converted_list[write]
```

means:

```text
exactly index write
```

So if you want the last valid written character, you need:

```python
converted_list[write - 1]
```

Memory rule:

```text
Slice endpoint excludes automatically.
Direct index does not.
```

---

## 6.7 Valid Region vs Leftover Region

After cleanup overwrite, the list may look like this:

```python
['a', ' ', 'g', 'o', 'o', 'd', ' ', 'e', 'x', 'a', 'm', 'p', 'l', 'e', ' ', 'e', ' ']
```

This looks confusing because there are extra characters at the end.

But the meaningful content is only:

```python
converted_list[:write]
```

Everything after `write` is leftover old data.

Invariant:

```text
converted_list[0:write] = valid cleaned content
converted_list[write:]  = leftover/garbage old content
```

The physical list length does not automatically shrink.

---

## 6.8 Same-Direction vs Opposite-Direction Pointers

### Cleanup

Cleanup uses same-direction pointers:

```text
read  ->
write ->
```

Reason:

- We are scanning input from left to right.
- We are compacting valid characters toward the front.

---

### Reverse

Reverse uses opposite-direction pointers:

```text
left ->        <- right
```

Reason:

- Reversal requires swapping the beginning with the end.
- Then moving inward.

---

## 6.9 Why `while left < right` Is Cleaner Than `left <= right`

For reversal:

```python
while left < right:
```

is preferred.

If `left == right`, both pointers are on the same character.

Swapping a character with itself does nothing.

Example:

```text
a b c
```

When `left` and `right` both point to `b`, there is no need to swap.

Using `<` avoids one unnecessary operation.

---

## 6.10 Why Last-Word Handling Required Special Logic

In `reverse_each_word`, the initial logic reversed a word when a space was found.

That works for words followed by spaces.

But the final word has no space after it.

Example after whole reverse:

```text
elpmaxe doog dna
```

The loop detects:

```text
elpmaxe
doog
```

because both are followed by spaces.

But:

```text
dna
```

is at the end and has no trailing space.

So after the loop, we need:

```python
reverse_list(l, word_start_index, len(l) - 1)
```

This handles the final word.

---

# 7. Cleanup Phase Deep Dive

The cleanup phase was the most conceptually difficult part.

---

## 7.1 Goal of Cleanup

Input:

```text
" a good  example "
```

Desired cleaned output:

```text
"a good example"
```

We must:

- remove leading spaces,
- remove duplicate spaces,
- preserve one space between words,
- remove trailing spaces.

---

## 7.2 Initial Character Index Map

For:

```text
" a good  example "
```

There are 17 characters, indexed from `0` to `16`.

```text
index : char
0     : ' '
1     : 'a'
2     : ' '
3     : 'g'
4     : 'o'
5     : 'o'
6     : 'd'
7     : ' '
8     : ' '
9     : 'e'
10    : 'x'
11    : 'a'
12    : 'm'
13    : 'p'
14    : 'l'
15    : 'e'
16    : ' '
```

---

## 7.3 Cleanup Rules

For each character:

### Rule 1: Non-space characters are always kept

```text
if current character is not space:
    write it
```

Because words can contain letters and digits, the safest condition is:

```python
char != " "
```

We do not need to check:

```python
char in "abcdefghijklmnopqrstuvwxyz"
```

because the problem allows digits too.

---

### Rule 2: A space is kept only if it separates words

A space should be kept only when:

```text
we have already written something
AND
the previous written character is not a space
```

In code logic:

```python
write > 0 and converted_list[write - 1] != " "
```

This removes:

- leading spaces, because `write == 0`,
- duplicate spaces, because previous written char is already a space.

---

## 7.4 Cleanup Pointer Simulation

Input:

```text
" a good  example "
```

Start:

```text
write = 0
```

| read | char | action | write after | valid region |
|---:|:---:|---|---:|---|
| 0 | `' '` | skip leading space | 0 | `""` |
| 1 | `'a'` | write `'a'` at index 0 | 1 | `"a"` |
| 2 | `' '` | write separator space | 2 | `"a "` |
| 3 | `'g'` | write `'g'` | 3 | `"a g"` |
| 4 | `'o'` | write `'o'` | 4 | `"a go"` |
| 5 | `'o'` | write `'o'` | 5 | `"a goo"` |
| 6 | `'d'` | write `'d'` | 6 | `"a good"` |
| 7 | `' '` | write separator space | 7 | `"a good "` |
| 8 | `' '` | skip duplicate space | 7 | `"a good "` |
| 9 | `'e'` | write `'e'` | 8 | `"a good e"` |
| 10 | `'x'` | write `'x'` | 9 | `"a good ex"` |
| 11 | `'a'` | write `'a'` | 10 | `"a good exa"` |
| 12 | `'m'` | write `'m'` | 11 | `"a good exam"` |
| 13 | `'p'` | write `'p'` | 12 | `"a good examp"` |
| 14 | `'l'` | write `'l'` | 13 | `"a good exampl"` |
| 15 | `'e'` | write `'e'` | 14 | `"a good example"` |
| 16 | `' '` | write possible separator space | 15 | `"a good example "` |

At the end of the loop:

```text
write = 15
```

Valid region before trailing trim:

```python
converted_list[:write]
```

is:

```text
"a good example "
```

It includes a trailing space.

---

## 7.5 Why the Trailing Space Gets Written

At `read = 16`, the character is a space after `example`.

The condition says:

```text
write > 0
and previous written character is not space
```

The previous written character is:

```text
'e'
```

So the space is accepted as a possible separator.

At that moment, the algorithm does not know whether another word will appear later.

Only after the scan finishes do we know it was trailing.

---

## 7.6 Why Post-Processing Is Needed

After scanning, check the last valid character:

```python
converted_list[write - 1]
```

If it is a space:

```python
write -= 1
```

This moves the logical boundary one step back.

Before:

```text
write = 15
valid = "a good example "
```

After:

```text
write = 14
valid = "a good example"
```

---

## 7.7 Why `converted_list[write]` Was Wrong

At the end:

```text
write = 15
```

The last valid character is at:

```text
index 14
```

But:

```python
converted_list[write]
```

checks:

```text
index 15
```

Index `15` is outside the valid region. It contains leftover data.

The correct check is:

```python
converted_list[write - 1]
```

---

## 7.8 Why Leftover Characters Remained

After overwrite, the physical list still has its original length.

Even if we logically cleaned the content, Python does not automatically shrink the list.

Example confusing output:

```python
['a', ' ', 'g', 'o', 'o', 'd', ' ', 'e', 'x', 'a', 'm', 'p', 'l', 'e', ' ', 'e', ' ']
```

The final `'e'` and `' '` are leftovers from the original list.

The valid content is determined by `write`, not by the full list length.

---

# 8. My Questions, Confusions, and Discoveries

| My Question / Confusion | Why It Happened | Correct Understanding | Example |
|---|---|---|---|
| Does `split()` keep extra spaces as separate elements? | I thought multiple spaces might become separate words or blank entries. | Python `split()` without arguments collapses whitespace and ignores leading/trailing spaces. | `" a  b ".split()` gives `["a", "b"]`. |
| Why is this a Medium problem if `split()` solves it easily? | The normal Python solution is short. | The Medium-level challenge is mostly in the in-place follow-up. | `split/reverse/join` is easy; in-place cleanup + reversal is harder. |
| If Python strings are immutable, how can we solve the follow-up? | The follow-up assumes mutable string data. | In Python, we simulate using a character list, but strict O(1) extra space is not achieved. | `chars = list(s)` lets us mutate characters. |
| Why is converting to a list O(n) space? | I was clarifying space complexity. | The list size grows with the input length. | A 10-character string creates a 10-element list. |
| What does “in-place” mean? | I wanted to understand the interview term. | It means modifying the original storage instead of creating a full new result. | Swapping inside the same list. |
| Do we use `remove()` and `add()` for cleanup? | It felt natural to remove spaces directly. | Better to overwrite valid chars using read/write pointers. | `chars[write] = chars[read]`. |
| Why does cleanup not reverse anything? | I expected pointer movement to change order. | Cleanup only compacts valid characters. Reversal happens in a separate phase. | `" ab"` becomes `"ab"`, not `"ba"`. |
| Why do we reverse twice? | Reversing whole string breaks word letters. | Whole reverse fixes word order; per-word reverse fixes letters. | `"a good example"` -> `"elpmaxe doog a"` -> `"example good a"`. |
| Why use same-direction pointers for cleanup? | I was comparing cleanup and reverse logic. | Cleanup scans and writes forward, so read/write move left to right. | `read` scans all chars; `write` tracks valid region. |
| Why use opposite-direction pointers for reverse? | I did not see another way to reverse. | Reversal swaps from both ends inward. | `left = 0`, `right = len(l)-1`. |
| Should reverse stop at the middle? | I wondered why not traverse fully. | Each swap fixes two positions. Continuing past the middle would swap back. | `"abcd"`: swap a/d, b/c, done. |
| Why `while left < right` instead of `<=`? | I originally used `<=`. | When `left == right`, it is the same character, so swap is unnecessary. | Odd-length list middle element stays in place. |
| Why do we need a temporary variable for swap? | I did not consider overwrite order. | Without temp, the first assignment destroys one value. | `a,d` can become `d,d` if not saved. |
| Why did the full list still contain spaces after cleanup? | I printed the entire list. | Overwrite changes valid prefix only; leftover tail remains. | Use `converted_list[:write]`. |
| Why was I confused by printing `converted_list[read]`? | I printed the scanning location instead of valid output. | `read` shows the current source character, not the cleaned result. | Print `converted_list[:write]` for valid content. |
| Why is `write` not the last valid index? | I thought write pointed at the last written char. | `write` points to the next available position. | Last valid index is `write - 1`. |
| Why does `converted_list[:write]` work? | I confused slice endpoint with direct index. | Slice excludes `write`, so it returns indexes `0` to `write-1`. | `arr[:3]` gives indexes `0,1,2`. |
| Why is `converted_list[write]` wrong for checking trailing space? | I directly indexed `write`. | `write` points after the valid region. Check `write - 1`. | Last valid char is at `write - 1`. |
| Why did `converted_list[:write-1]` look correct sometimes? | The last valid char happened to be a trailing space. | Blindly slicing to `write-1` can remove a real character in other cases. | `"example"` would lose `e` if no trailing space. |
| How do we detect words for per-word reversal? | I needed boundaries. | A word starts after a space and ends before the next space. | Space at `i` means word ends at `i-1`. |
| Why set `word_start_index = i + 1`? | I was deriving how to move to the next word. | If `i` is a space, the next word starts at the next character. | After reversing word ending before space, next start is `i+1`. |
| Why did the result become original order again? | I had a bug in `reverse_list`. | The helper ignored the passed `right` value and always reversed to the end. | `right = len(l)-1` overwrote the argument. |
| Why did the last word stay reversed? | The loop only reversed words when it found a following space. | The final word has no trailing space, so reverse it after the loop. | `"dna"` needed final reverse to become `"and"`. |
| Why use `right=None` in default parameters? | I wanted one function for full and range reverse. | `None` lets the function decide default right after knowing `l`. | `if right is None: right = len(l)-1`. |
| What is wrong with `for read in len(list)`? | PyCharm warned about an int. | `len(...)` returns a number, but `for` needs an iterable. | Use `range(len(list))`. |
| What is the difference between `len(l)-1` and `len(l-1)`? | Syntax confusion. | `len(l)-1` means last index. `len(l-1)` is invalid because `l-1` is not a list. | Last index = `len(l) - 1`. |

---

# 9. Important Independent Realizations

## 9.1 Realization: `word_start_index` Should Become `i + 1`

This was a major independent breakthrough.

During per-word reversal, when the scan sees a space at index `i`, the current word ends at:

```python
i - 1
```

After reversing that word, the next word must begin after the space:

```python
i + 1
```

So:

```python
word_start_index = i + 1
```

This was important because it showed understanding of what `i` represents:

```text
i points to the separator space.
The next word starts immediately after that separator.
```

This was not memorized. It was derived from boundary logic.

---

## 9.2 Realization: Slice Endpoint Excludes Automatically

The confusion around:

```python
converted_list[:write]
```

versus:

```python
converted_list[write]
```

was resolved by understanding:

```text
slice endpoint excludes automatically
direct indexing does not
```

This unlocked the cleanup boundary logic.

---

## 9.3 Realization: `write` Points to the Next Empty Position

The key mental model became:

```text
write = where I would write the next valid character
```

Therefore:

```text
valid content is before write
last valid character is write - 1
```

This is a reusable idea across many in-place array problems.

---

## 9.4 Realization: Reverse Requires Opposite-Direction Pointers

Cleanup and reverse are different operations.

Cleanup:

```text
read/write move forward
```

Reverse:

```text
left/right move inward from opposite ends
```

Understanding this difference helped separate the phases mentally.

---

## 9.5 Realization: Temporary Variables Protect Overwritten Values

Without a temporary variable:

```python
l[left] = l[right]
l[right] = l[left]
```

the original `l[left]` is lost.

The correct logic saves it first:

```python
temp = l[left]
l[left] = l[right]
l[right] = temp
```

This showed why assignment order matters in in-place algorithms.

---

## 9.6 Realization: The Last Word Needs Special Handling

The first version of `reverse_each_word()` only reversed when it found a space.

That missed the final word because there is no space after it.

Testing with `"and"` exposed the bug:

```text
dna stayed dna
```

The fix:

```python
reverse_list(l, word_start_index, len(l) - 1)
```

after the loop.

This was a classic edge-case learning moment.

---

# 10. Step-by-Step Solution Evolution

## 10.1 Stage 1: Naive Split / Reverse / Join

The first accepted solution was:

```python
def reverseWords(s: str) -> str:
    split_words = s.split()
    split_words.reverse()
    return " ".join(split_words)
```

Reasoning:

- `split()` extracts real words.
- `reverse()` reverses word order.
- `" ".join()` reconstructs with single spaces.

Problem solved:

```text
Normal LeetCode problem.
```

Remaining learning challenge:

```text
Follow-up in-place simulation.
```

---

## 10.2 Stage 2: Beginning Cleanup Simulation

The follow-up started by converting the string to a list:

```python
converted_list = list(s)
```

This made characters mutable.

The first cleanup loop printed characters using `read`, but the output was confusing because `read` represents the scanning index, not the cleaned output.

Learning:

```text
In pointer problems, what you print matters.
Printing the wrong pointer can mislead you.
```

---

## 10.3 Stage 3: Implementing Overwrite Logic

The cleanup logic was built:

```python
if converted_list[read] != " ":
    converted_list[write] = converted_list[read]
    write += 1
elif write > 0 and converted_list[write - 1] != " ":
    converted_list[write] = converted_list[read]
    write += 1
```

This handles:

- normal characters,
- necessary separator spaces,
- skipped leading/duplicate spaces.

---

## 10.4 Stage 4: Discovering the Valid Region Concept

The full list still contained leftover values.

This led to the realization:

```text
The whole list is not the cleaned output.
Only converted_list[:write] is meaningful.
```

This was a major in-place algorithm concept.

---

## 10.5 Stage 5: Fixing Trailing Space

The algorithm wrote a trailing space when the input ended with a space.

The fix:

```python
if write > 0 and converted_list[write - 1] == " ":
    write -= 1
```

This required understanding:

```text
write is next position
write - 1 is last valid character
```

---

## 10.6 Stage 6: Implementing Full Reverse

A reverse helper was created using `left` and `right`.

First version:

```python
while left <= right:
```

was improved to:

```python
while left < right:
```

because swapping the middle element with itself is unnecessary.

---

## 10.7 Stage 7: Generalizing to Range Reversal

The reverse helper was made flexible:

```python
def reverse_list(l, left=0, right=None):
```

This allowed:

```python
reverse_list(chars)
```

for the whole list and:

```python
reverse_list(chars, word_start, word_end)
```

for individual words.

A bug appeared when `right` was always overwritten:

```python
right = len(l) - 1
```

This ignored the passed word boundary.

Fix:

```python
if right is None:
    right = len(l) - 1
```

---

## 10.8 Stage 8: Implementing Per-Word Reversal

The per-word scan used:

```python
word_start_index = 0
```

When a space was found at `i`, the current word ended at:

```python
i - 1
```

Then:

```python
reverse_list(l, word_start_index, i - 1)
word_start_index = i + 1
```

This reversed each word range.

---

## 10.9 Stage 9: Fixing Final-Word Bug

The loop only caught words followed by a space.

The final word required a post-loop reverse:

```python
reverse_list(l, word_start_index, len(l) - 1)
```

This fixed cases where the last word had multiple characters.

---

## 10.10 Stage 10: Assembling the Final Simulation

Final flow:

```python
cleaned_up_list = clean_up(s)
reversed_list = reverse_list(cleaned_up_list)
result_list = reverse_each_word(reversed_list)
return "".join(result_list)
```

This produced:

```python
"example good and"
```

for:

```python
" and good  example "
```

---

# 11. Final Accepted Code

There are two useful final versions.

---

## 11.1 Main LeetCode Accepted Python Solution

This is the clean solution for the actual Python problem.

```python
def reverseWords(s: str) -> str:
    # split() without arguments:
    # - removes leading/trailing spaces
    # - collapses multiple spaces
    # - returns only real words
    split_words = s.split()

    # reverse() modifies the list in-place
    split_words.reverse()

    # join words using exactly one space
    return " ".join(split_words)
```

### Explanation

```python
split_words = s.split()
```

Extracts words and automatically handles extra spaces.

```python
split_words.reverse()
```

Reverses the word list in-place.

```python
return " ".join(split_words)
```

Rebuilds the sentence with exactly one space between words.

---

## 11.2 Follow-Up Learning Simulation Code

This version simulates in-place behavior using a character list.

```python
def clean_up(s: str) -> list:
    """
    Convert the string into a character list and normalize spaces.

    This removes:
    - leading spaces
    - duplicate spaces
    - trailing spaces

    It keeps:
    - all non-space characters
    - exactly one space between words
    """
    converted_list = list(s)
    write = 0

    for read in range(len(converted_list)):
        # Always keep non-space characters.
        if converted_list[read] != " ":
            converted_list[write] = converted_list[read]
            write += 1

        # Keep one space only if it comes after a written non-space character.
        elif write > 0 and converted_list[write - 1] != " ":
            converted_list[write] = converted_list[read]
            write += 1

    # If the last valid character is a space, remove it logically
    # by moving the write boundary one step back.
    if write > 0 and converted_list[write - 1] == " ":
        write -= 1

    # Return only the valid cleaned region.
    return converted_list[:write]


def reverse_list(l: list, left: int = 0, right: int | None = None) -> list:
    """
    Reverse a list, or a specific range inside the list, in-place.

    If right is not provided, reverse from left to the end.
    """
    if right is None:
        right = len(l) - 1

    while left < right:
        temp = l[left]
        l[left] = l[right]
        l[right] = temp

        left += 1
        right -= 1

    return l


def reverse_each_word(l: list) -> list:
    """
    Reverse each word inside the already whole-reversed list.

    Words are separated by single spaces because cleanup already normalized them.
    """
    i = 0
    word_start_index = 0

    while i < len(l):
        if l[i] == " ":
            word_end_index = i - 1
            reverse_list(l, word_start_index, word_end_index)
            word_start_index = i + 1

        i += 1

    # Reverse the final word, because it is not followed by a space.
    reverse_list(l, word_start_index, len(l) - 1)

    return l


def mutable_simulation(s: str) -> str:
    """
    Simulate the follow-up algorithm using a mutable character list.
    """
    cleaned_up_list = clean_up(s)

    reversed_list = reverse_list(cleaned_up_list)

    result_list = reverse_each_word(reversed_list)

    return "".join(result_list)
```

Example:

```python
print(mutable_simulation(" and good  example "))
```

Output:

```text
example good and
```

---

# 12. Full Dry Run

Dry run for:

```python
s = " and good  example "
```

---

## 12.1 Initial Input

```text
" and good  example "
```

Character list:

```python
[' ', 'a', 'n', 'd', ' ', 'g', 'o', 'o', 'd', ' ', ' ', 'e', 'x', 'a', 'm', 'p', 'l', 'e', ' ']
```

---

## 12.2 Cleanup Phase

Goal:

```text
"and good example"
```

| read | char | action | write after | valid content |
|---:|:---:|---|---:|---|
| 0 | `' '` | skip leading space | 0 | `""` |
| 1 | `'a'` | write | 1 | `"a"` |
| 2 | `'n'` | write | 2 | `"an"` |
| 3 | `'d'` | write | 3 | `"and"` |
| 4 | `' '` | write separator | 4 | `"and "` |
| 5 | `'g'` | write | 5 | `"and g"` |
| 6 | `'o'` | write | 6 | `"and go"` |
| 7 | `'o'` | write | 7 | `"and goo"` |
| 8 | `'d'` | write | 8 | `"and good"` |
| 9 | `' '` | write separator | 9 | `"and good "` |
| 10 | `' '` | skip duplicate | 9 | `"and good "` |
| 11 | `'e'` | write | 10 | `"and good e"` |
| 12 | `'x'` | write | 11 | `"and good ex"` |
| 13 | `'a'` | write | 12 | `"and good exa"` |
| 14 | `'m'` | write | 13 | `"and good exam"` |
| 15 | `'p'` | write | 14 | `"and good examp"` |
| 16 | `'l'` | write | 15 | `"and good exampl"` |
| 17 | `'e'` | write | 16 | `"and good example"` |
| 18 | `' '` | write possible separator | 17 | `"and good example "` |

Now check last valid character:

```python
converted_list[write - 1]
```

This is a space, so:

```python
write -= 1
```

Final cleaned list:

```python
['a', 'n', 'd', ' ', 'g', 'o', 'o', 'd', ' ', 'e', 'x', 'a', 'm', 'p', 'l', 'e']
```

String form:

```text
and good example
```

---

## 12.3 Whole Reverse Phase

Before:

```text
and good example
```

After reversing the entire list:

```text
elpmaxe doog dna
```

List:

```python
['e', 'l', 'p', 'm', 'a', 'x', 'e', ' ', 'd', 'o', 'o', 'g', ' ', 'd', 'n', 'a']
```

Now the word order is effectively reversed, but each word is backward.

---

## 12.4 Word Boundary Detection

After whole reverse:

```text
elpmaxe doog dna
```

Indexes:

```text
0:e
1:l
2:p
3:m
4:a
5:x
6:e
7:' '
8:d
9:o
10:o
11:g
12:' '
13:d
14:n
15:a
```

Detected word ranges:

```text
0 to 6   -> elpmaxe
8 to 11  -> doog
13 to 15 -> dna
```

---

## 12.5 Per-Word Reversal Phase

### First word

```text
elpmaxe
```

Reverse:

```text
example
```

List becomes:

```text
example doog dna
```

---

### Second word

```text
doog
```

Reverse:

```text
good
```

List becomes:

```text
example good dna
```

---

### Final word

```text
dna
```

Reverse:

```text
and
```

List becomes:

```text
example good and
```

---

## 12.6 Final Output

Join the list:

```python
"".join(result_list)
```

Output:

```python
"example good and"
```

---

# 13. Complexity Analysis

## 13.1 Main Python Solution

```python
def reverseWords(s: str) -> str:
    split_words = s.split()
    split_words.reverse()
    return " ".join(split_words)
```

### Time Complexity

```text
O(n)
```

Reason:

- `split()` scans the string.
- `reverse()` scans the word list.
- `join()` builds the result.

Even though there are multiple passes, each pass is linear.

```text
O(n) + O(n) + O(n) = O(n)
```

Constants are dropped.

### Space Complexity

```text
O(n)
```

Reason:

- `split()` creates a list of words.
- `join()` creates the final output string.

---

## 13.2 Follow-Up Simulation

The algorithmic operations on the character list are linear.

### Time Complexity

```text
O(n)
```

Phases:

- cleanup: O(n)
- whole reverse: O(n)
- reverse each word: O(n) total
- join: O(n)

Total:

```text
O(n)
```

### Space Complexity in Python

Actual Python simulation:

```text
O(n)
```

Reason:

```python
list(s)
```

creates a new list of characters.

Also:

```python
converted_list[:write]
```

creates a slice.

### Conceptual Follow-Up Space Complexity

If the language provides a mutable character array as input, and if truncation can be done in-place, the algorithm itself can be considered:

```text
O(1) extra space
```

because it uses only pointer variables:

```text
read, write, left, right, i, word_start_index
```

---

# 14. Alternative Approach Discussion

## 14.1 Built-In Python Approach

The simplest Python approach:

```python
def reverseWords(s: str) -> str:
    return " ".join(reversed(s.split()))
```

or:

```python
def reverseWords(s: str) -> str:
    words = s.split()
    words.reverse()
    return " ".join(words)
```

This is clean and appropriate for Python.

---

## 14.2 True Mutable-String / Character-Array Approach

In a language where the input is a mutable character array, the follow-up approach is:

```text
normalize spaces in-place
reverse whole array
reverse each word
```

This avoids creating a list of words.

---

## 14.3 Readability vs Optimization

The built-in Python solution is more readable.

The follow-up simulation is more educational.

For interviews:

- If asked for a Pythonic solution, use `split/reverse/join`.
- If asked about the follow-up, explain the in-place strategy conceptually.
- If practicing algorithms, implement the pointer-based simulation.

---

# 15. Rules to Lock Into Memory

## 15.1 Core Pointer Rules

- `read` scans original data.
- `write` marks the next valid write position.
- `write` is not the last valid index.
- Last valid index is `write - 1`.
- `converted_list[:write]` gives the valid region.
- `converted_list[write]` gives the next write position, not the last valid character.

---

## 15.2 Slice and Index Rules

- Slicing excludes the endpoint.
- Direct indexing does not exclude anything.
- `arr[:k]` includes indexes `0` through `k-1`.
- `arr[k]` accesses exactly index `k`.

Memory shortcut:

```text
slice endpoint excludes automatically
direct index requires exact position
```

---

## 15.3 In-Place Overwrite Rules

- Overwrite algorithms may leave old values behind.
- The full physical list may not represent the logical result.
- Use a boundary pointer to define valid content.
- The leftover region should be ignored.

Invariant:

```text
arr[:write] = valid content
arr[write:] = leftover old content
```

---

## 15.4 Reversal Rules

- Reversal uses opposite-direction pointers.
- Swap `left` and `right`.
- Move both inward.
- Stop when `left < right` becomes false.
- Use a temporary variable or Python tuple swap to avoid losing data.

---

## 15.5 Reverse Words Trick

To reverse word order in-place:

```text
reverse whole string
reverse each word
```

Why it works:

```text
whole reverse fixes word positions
word reverse fixes letters
```

---

## 15.6 Word Boundary Rules

- A word starts at a non-space character.
- A word ends before a space.
- If `i` points to a space, current word ends at `i - 1`.
- The next word starts at `i + 1`.
- The final word needs handling after the loop because it has no trailing space.

---

## 15.7 Python Syntax Rules

- Use `range(len(l))` to loop over indexes.
- `len(l)` gives length.
- Last valid index is `len(l) - 1`.
- `len(l - 1)` is incorrect.
- Use `right=None` when default depends on the input list.
- `list(s)` creates a character list.
- `"".join(chars)` creates a string from characters.
- `reverse()` modifies a list in-place and returns `None`.

---

# 16. Reflection on My Learning Journey

This problem became much more than a simple string problem.

The normal solution was straightforward:

```text
split -> reverse -> join
```

But the follow-up opened up deeper algorithmic thinking.

The main struggles were not about writing lots of code. They were about understanding:

- what each pointer represents,
- when a pointer moves,
- why `write` points to the next position,
- why `write - 1` is the last valid character,
- why slicing excludes endpoints,
- why leftover values remain after overwrite,
- why reversal needs opposite pointers,
- why the last word needs separate handling.

One of the strongest learning moments was independently deriving:

```python
word_start_index = i + 1
```

That realization came from understanding that:

```text
i points to the space
the next word begins after that space
```

This was a genuine problem-solving breakthrough.

Another major breakthrough was understanding the difference between:

```python
converted_list[:write]
```

and:

```python
converted_list[write - 1]
```

That cleared up confusion around valid regions and off-by-one boundaries.

The debugging process also mattered. Printing the wrong thing caused confusion, but inspecting pointer values, list slices, and exact indexes gradually built the correct mental model.

The biggest growth from this conversation was not simply solving Reverse Words in a String. The bigger achievement was building reusable algorithmic intuition for:

- two-pointer cleanup,
- in-place overwrite,
- range reversal,
- boundary tracking,
- off-by-one reasoning,
- edge-case detection.

These patterns will appear again in many future problems.

The important takeaway:

```text
I did not just copy a solution.
I learned why each part exists.
```

That is real progress in problem-solving skill.

---

# 17. Final Quick Revision Summary

## Normal Python Solution

```python
def reverseWords(s: str) -> str:
    words = s.split()
    words.reverse()
    return " ".join(words)
```

## Follow-Up Concept

```text
clean spaces
reverse whole character array
reverse each word
join/result
```

## Core Mental Model

```text
read/write -> cleanup
left/right -> reversal
write -> next valid position
write - 1 -> last valid character
[:write] -> valid region
```

## Most Important Trick

```text
Reverse whole sentence:
"a good example" -> "elpmaxe doog a"

Reverse each word:
"elpmaxe doog a" -> "example good a"
```

## Most Important Boundary Rule

```text
If i points to a space:
word ends at i - 1
next word starts at i + 1
```

## Most Important Debugging Rule

```text
Do not trust the whole overwritten list.
Trust the valid region defined by write.
```
