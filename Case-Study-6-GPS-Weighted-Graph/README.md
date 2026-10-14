# Case Study 6: GPS / Navigation System Using a Weighted Graph

## 1. Introduction
Navigation systems help users find a route between locations. A road network can be modelled as a weighted graph: locations are vertices, roads are edges, and edge weights represent distance. A shortest-path algorithm can then find a low-distance route.

This case study models a small illustrative road network and uses **Dijkstra's algorithm** to find the shortest route.

## 2. Problem Statement
Represent a set of locations and the roads connecting them as a weighted graph. Given a starting location and a destination, calculate the shortest route and its total distance.

## 3. Objectives
- Understand weighted graphs and adjacency lists.
- Represent roads and distances in Python.
- Implement Dijkstra's shortest-path algorithm.
- Use a min-heap priority queue to choose the closest unprocessed location.
- Reconstruct and display the route.
- Handle a destination that cannot be reached.

## 4. Data Structures and Algorithm Used
- **Dictionary / adjacency list:** Maps each location to its neighbours and road distances.
- **Min-heap:** Efficiently selects the location with the smallest known distance.
- **Distance table:** Stores the best known distance from the start.
- **Predecessor table:** Stores the previous location on the best route.
- **Dijkstra's algorithm:** Finds shortest paths when edge weights are non-negative.

## 5. Working Principle
1. Set the start location's distance to zero and all other distances to infinity.
2. Insert the start location into the min-heap.
3. Remove the location with the smallest distance.
4. For each neighbouring location, calculate the distance through the current location.
5. If this distance is shorter than the stored distance, update it and record the predecessor.
6. Add the updated neighbour to the heap.
7. Continue until the destination is reached or the heap is empty.
8. Follow predecessor links backwards from the destination to reconstruct the route.

## 6. Example
The demonstration includes locations such as Home, Bus Stop, Market, College Gate, Library, and Hospital. Road weights are illustrative distances in kilometres. The program calculates a shortest route from Home to Hospital based on those weights.

## 7. Time and Space Complexity
With an adjacency list and binary min-heap:
- **Time:** O((V + E) log V), commonly stated for a standard heap-based implementation.
- **Space:** O(V + E) for the graph and algorithm tables.

Here V is the number of vertices and E is the number of edges.

## 8. Applications
- GPS and route-planning demonstrations.
- Campus navigation.
- Network routing.
- Delivery route planning when distance is the chosen cost.
- Pathfinding in maps and games.

## 9. Advantages
- Finds a shortest path when all edge weights are non-negative.
- Works with weighted road networks.
- The predecessor table allows the full route to be reconstructed, not just the distance.

## 10. Limitations
- Does not use live GPS coordinates, maps, traffic, road closures, or travel-time estimates.
- Standard Dijkstra's algorithm is not suitable for negative edge weights.
- The example assumes each road can be travelled in both directions.

## 11. Conclusion
This case study demonstrates how a weighted graph represents a road network and how Dijkstra's algorithm finds the shortest route. It combines graph representation, a priority queue, distance updates, and route reconstruction.

## 12. How to Run
Make sure Python 3 is installed. Open a terminal in this folder and run:

```bash
python gps_navigation.py
```

The sample result is saved in `output.txt`.
