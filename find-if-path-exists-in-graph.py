# lxx789 John Benfield Project 5: Find if Path Exists in Graph
# CS 3343: Analysis of Algorithms Summer 2024

n = int(input("Enter total no. of graph nodes: "))
dict_graph = {}
for i in range(n):
    key = int(input("Enter Node: "))
    values = [int(neighbor) for neighbor in input(f"Enter Node {key}'s Neighbor: ").split()]
    dict_graph[key] = values

start = int(input("Enter start node: "))
end = int(input("Enter end node: "))

print("The Graph: ", dict_graph)
print("Start Node: ", start)
print("End Node: ", end)


def find_if_path_exists_in_graph(graph_to_search, start, end):
    # Create a queue and push the source node into it
    queue = [[start]]
    # Create a visited set in order to mark the visited nodes
    visited = set()

    # While the queue is not empty
    while queue:
        # Retrieve the head of the queue and mark it as visited
        path = queue.pop(0)
        vertex = path[-1]

        # Check if the retrieved node is the destination node
        if vertex == end:
            return True, "Path found!", path

        # Otherwise, traverse all the adjacent nodes of the retrieved node that are not visited
        elif vertex not in visited:
            for neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(vertex)

    # If we can't find the destination node after traversing all nodes, return false
    return False, 'Path Does Not Exist!!!'


# Example usage
print(find_if_path_exists_in_graph(dict_graph, start, end))
