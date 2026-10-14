# Case Study 6: GPS navigation using a weighted graph and Dijkstra's algorithm
import heapq


def dijkstra(graph, start, destination):
    if start not in graph or destination not in graph:
        raise ValueError("Start and destination must exist in the graph.")

    distances = {place: float("inf") for place in graph}
    previous = {place: None for place in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        distance, place = heapq.heappop(heap)
        if distance != distances[place]:
            continue
        if place == destination:
            break
        for neighbour, road_distance in graph[place]:
            new_distance = distance + road_distance
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = place
                heapq.heappush(heap, (new_distance, neighbour))

    if distances[destination] == float("inf"):
        return None, float("inf")

    path, current = [], destination
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1], distances[destination]


if __name__ == "__main__":
    roads = {
        "Home": [("Bus Stop", 2), ("Market", 5)],
        "Bus Stop": [("Home", 2), ("College Gate", 2), ("Library", 4)],
        "Market": [("Home", 5), ("Library", 1), ("Hospital", 8)],
        "College Gate": [("Bus Stop", 2), ("Library", 1), ("Hospital", 6)],
        "Library": [("Bus Stop", 4), ("Market", 1), ("College Gate", 1), ("Hospital", 3)],
        "Hospital": [("Market", 8), ("College Gate", 6), ("Library", 3)],
    }
    start, destination = "Home", "Hospital"
    path, distance = dijkstra(roads, start, destination)
    print("GPS / NAVIGATION SYSTEM")
    print("Start:", start)
    print("Destination:", destination)
    if path:
        print("Shortest route:", " -> ".join(path))
        print(f"Total distance: {distance} km")
    else:
        print("No route is available.")
