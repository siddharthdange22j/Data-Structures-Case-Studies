# Social Network Friendship Management using Adjacency Matrix

## 1. Introduction

A social networking application contains users and connections between users. These relationships can be represented using a Graph Data Structure.

In this case study:

- **User = Vertex**
- **Friendship = Edge**
- **Adjacency Matrix = Graph representation**

An adjacency matrix stores `1` when a friendship exists between two users and `0` when there is no friendship.

## 2. Problem Statement

Design a simple social-network system that represents friendship connections using an Adjacency Matrix.

The system provides the following operations:

1. Add friendship
2. Remove friendship
3. Check whether two users are friends
4. Display the friendship matrix
5. Display friends of a particular user

## 3. Objectives

- Understand Graph Data Structure.
- Understand Adjacency Matrix representation.
- Represent users as vertices.
- Represent friendships as edges.
- Add and remove friendship connections.
- Check friendship between two users.
- Display the complete friendship network.

## 4. Data Structure Used

A graph consists of **vertices and edges**.

For this application:

```text
Vertices → Users
Edges    → Friendships
```

Friendship is represented as an undirected connection. Therefore, if Alice is friends with Bob:

```text
Matrix[Alice][Bob] = 1
Matrix[Bob][Alice] = 1
```

## 5. Example

Users:

```text
Alice
Bob
Charlie
David
```

Friendships:

```text
Alice ↔ Bob
Alice ↔ Charlie
Bob ↔ David
Charlie ↔ David
```

Adjacency Matrix:

| User | Alice | Bob | Charlie | David |
|---|---:|---:|---:|---:|
| Alice | 0 | 1 | 1 | 0 |
| Bob | 1 | 0 | 0 | 1 |
| Charlie | 1 | 0 | 0 | 1 |
| David | 0 | 1 | 1 | 0 |

`1` means friendship exists and `0` means there is no friendship.

## 6. Main Operations

### Add Friendship

```text
Matrix[user1][user2] = 1
Matrix[user2][user1] = 1
```

### Remove Friendship

```text
Matrix[user1][user2] = 0
Matrix[user2][user1] = 0
```

### Check Friendship

Check whether:

```text
Matrix[user1][user2] == 1
```

### Display Friends

Scan the selected user's row and display users whose value is `1`.

## 7. Algorithm

### Add Friendship

```text
1. Find the index of User 1.
2. Find the index of User 2.
3. Set matrix[index1][index2] = 1.
4. Set matrix[index2][index1] = 1.
```

### Remove Friendship

```text
1. Find the index of User 1.
2. Find the index of User 2.
3. Set matrix[index1][index2] = 0.
4. Set matrix[index2][index1] = 0.
```

### Check Friendship

```text
1. Find the indexes of both users.
2. Check matrix[index1][index2].
3. If the value is 1, they are friends.
4. Otherwise, they are not friends.
```

## 8. Complexity Analysis

| Operation | Time Complexity |
|---|---:|
| Check friendship | O(1) |
| Add friendship | O(1) |
| Remove friendship | O(1) |
| Display matrix | O(V²) |
| Memory | O(V²) |

Where `V` is the number of users.

## 9. Advantages

- Simple representation of relationships.
- Very fast friendship lookup.
- Easy to add and remove connections.
- Easy to visualize the complete network.

## 10. Limitations

An adjacency matrix requires O(V²) memory. Therefore, for a very large and sparse social network, it can consume a large amount of memory. An adjacency list is generally more memory-efficient for sparse graphs.

## 11. Applications

- Social networking systems
- Friendship management
- Connection checking
- Mutual-friend analysis
- Network relationship analysis
- Graph-based applications

## 12. Conclusion

This case study demonstrates how a social network can be represented using a Graph and Adjacency Matrix. Users are represented as vertices and friendships as edges. The system can add, remove, check, and display friendship connections.

The adjacency matrix provides fast connection checking, but its O(V²) memory requirement is a limitation for very large sparse networks.

## 13. How to Run

```bash
python social_network.py
```
