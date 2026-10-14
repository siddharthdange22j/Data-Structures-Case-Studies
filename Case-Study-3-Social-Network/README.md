# Case Study 3: Social Network Friendship Management Using Graphs

## 1. Introduction
Social networking applications connect people through friendships and other relationships. A social network can be represented as a graph in which each person is a vertex and each friendship is an edge.

This case study uses an **adjacency matrix** to represent friendships in a small undirected social network.

## 2. Problem Statement
Create a program that stores users and their friendships. The program must be able to add a friendship, remove a friendship, check whether two users are friends, and display the friendship matrix.

## 3. Objectives
- Understand graph terminology: vertices and edges.
- Represent an undirected graph with an adjacency matrix.
- Add and remove edges.
- Check whether an edge exists between two vertices.
- Display the graph in matrix form.

## 4. Data Structures Used
- **List:** Stores the user names.
- **Two-dimensional list:** Stores the adjacency matrix.
- **Graph:** Each user is a vertex, and a friendship is an undirected edge.

In the matrix, `1` means the two users are friends and `0` means there is no direct friendship.

## 5. Working Principle
1. Store the list of users.
2. Create a square matrix with one row and one column for every user.
3. Initially set every matrix value to `0`.
4. When a friendship is added between users `i` and `j`, set both `matrix[i][j]` and `matrix[j][i]` to `1`.
5. When a friendship is removed, set both values to `0`.
6. To check a friendship, inspect the corresponding matrix entry.
7. Print the matrix with user names as row and column labels.

## 6. Example
Consider four users: Asha, Rahul, Meera, and Karan. Suppose Asha is friends with Rahul and Meera, while Rahul is friends with Karan.

The adjacency matrix is symmetric because friendships are undirected. For example, if Asha is friends with Rahul, both the Asha–Rahul and Rahul–Asha entries are `1`.

## 7. Time and Space Complexity
| Operation | Complexity |
|---|---|
| Store adjacency matrix | O(V²) space |
| Add friendship | O(1) after user indices are known |
| Remove friendship | O(1) after user indices are known |
| Check friendship | O(1) after user indices are known |
| Display matrix | O(V²) |

In this simple implementation, finding a user's index in the name list takes O(V).

## 8. Applications
- Social network friendship modelling.
- Relationship maps.
- Small undirected network analysis.
- Representing connections between devices or people.

## 9. Advantages
- Easy to understand and visualise.
- Checking a connection is fast after locating the users.
- The symmetric matrix clearly represents undirected friendships.

## 10. Limitations
- Requires O(V²) memory even if there are few friendships.
- Adding a new user requires resizing the matrix.
- Large social networks are usually better represented with adjacency lists or specialised graph storage.

## 11. Conclusion
This case study demonstrates how a graph and adjacency matrix can model friendship relationships. It also shows how basic graph operations can be implemented in Python.

## 12. How to Run
Make sure Python 3 is installed. Open a terminal in this folder and run:

```bash
python social_network.py
```

The sample result is saved in `output.txt`.
