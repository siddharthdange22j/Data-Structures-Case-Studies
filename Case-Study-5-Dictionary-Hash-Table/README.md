# Case Study 5: Dictionary Application Using Hash Tables with Collision Resolution

## 1. Introduction
A dictionary application stores words and their meanings and lets users search for a word. Searching a long list sequentially can take O(n) time. A hash table can usually find a stored word much faster by mapping it to a bucket using a hash function.

This case study implements a small dictionary using a custom hash table and **separate chaining** to resolve collisions.

## 2. Problem Statement
Develop a dictionary that stores words and meanings. The application should support adding a new word, updating an existing meaning, searching for a word, deleting a word, and displaying the table. If two words map to the same bucket, both must remain stored correctly.

## 3. Objectives
- Understand hash tables and hash functions.
- Map words to bucket indices.
- Understand why collisions occur.
- Implement collision resolution using separate chaining.
- Perform insert, search, update, delete, and display operations.
- Analyse average and worst-case complexity.

## 4. Data Structures and Technique Used
- **Hash table:** A fixed-size list of buckets.
- **Bucket:** A list containing entries assigned to the same index.
- **Hash function:** Adds the character codes of a word and takes the remainder after division by the table size.
- **Separate chaining:** Keeps colliding entries together in the same bucket.

The hash function is intentionally simple for teaching. A production dictionary would use a more robust hash function.

## 5. Working Principle
1. Convert a word into a bucket index using the hash function.
2. For adding a word, inspect that bucket.
3. If the word already exists, update its meaning; otherwise append a new entry.
4. For searching, inspect only the bucket calculated for the word.
5. For deletion, find the word in its bucket and remove that entry.
6. For display, print every bucket and its entries.
7. If different words have the same index, separate chaining stores them together instead of overwriting either entry.

## 6. Example
Suppose the dictionary stores words such as `algorithm`, `binary`, `graph`, `heap`, `queue`, and `stack`.

The hash function may map more than one word to the same bucket. This is a **collision**. With separate chaining, the bucket holds a list of entries, so all words remain accessible.

## 7. Time and Space Complexity
| Operation | Average Case | Worst Case |
|---|---:|---:|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Update | O(1) | O(n) |
| Delete | O(1) | O(n) |

The average case assumes a reasonably distributed hash function and a controlled load factor. Storage is O(m + n), where m is the number of buckets and n is the number of entries.

## 8. Applications
- Dictionaries and glossaries.
- Contact lookup.
- Symbol tables in compilers.
- Caching and indexing.
- Word lookup in language-learning applications.

## 9. Advantages
- Usually faster than scanning every word.
- Collision resolution prevents entries from being lost.
- Supports adding, updating, searching, and deleting entries.

## 10. Limitations
- Poor hash distribution can create long chains.
- The sample table has a fixed size and does not resize automatically.
- The hash function is simple and intended for learning, not security or production use.

## 11. Conclusion
This case study demonstrates how a hash table stores and retrieves dictionary entries. Separate chaining provides a straightforward way to resolve collisions and preserve every word and meaning.

## 12. How to Run
Make sure Python 3 is installed. Open a terminal in this folder and run:

```bash
python dictionary_hash_table.py
```

The sample result is saved in `output.txt`.
