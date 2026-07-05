import heapq

def dijkstra_custom(graph, start_node, end_node, factor):
    
  

    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start_node)]

    

    while priority_queue:

        
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == end_node:
            break


        for neighbor, properties in graph[current_node].items():
            
            if factor == 'distance':
                cost = properties['distance']
                
            elif factor == 'risk':
                
                if properties['risk'] == 'low':
                    cost = 0
                    
                elif properties['risk'] == 'medium':
                    cost = 1

                else:
                    cost = 2
                
            elif factor == 'type':
                cost = 0 if properties['type'] == 'highway' else 1
                
                
                
            else:
                raise ValueError("unvalid factor")

            new_distance = current_distance + cost
            

            if new_distance < distances[neighbor]:
                
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

                

    path = []
    current = end_node

    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    path.reverse()

    return path, distances[end_node]


# A graph 

graph = {
    'A': {'B': {'distance': 5, 'risk': 'low', 'type': 'local'}, 'C': {'distance': 10, 'risk': 'high', 'type': 'highway'}},
    'B': {'D': {'distance': 12, 'risk': 'high', 'type': 'local'},'F': {'distance': 1, 'risk': 'low', 'type': 'local'}},
    'C': {'E': {'distance': 10, 'risk': 'medium', 'type': 'highway'}},
    'D': {'E': {'distance': 1, 'risk': 'low', 'type': 'local'}, 'F': {'distance': 2, 'risk': 'low', 'type': 'local'}},
    'E': {'F': {'distance': 5, 'risk': 'medium', 'type': 'local'}},
    'F': {}
}

start_node = input("Please enter the start point.")

end_node = input("Please enter the end point.")

factor = input("Please enter the factor you want to calculate the best path based on.")

shortest_path, cost = dijkstra_custom(graph, start_node, end_node, factor)

print(f"the best path from point {start_node} to point {end_node} based on {factor} is ((({shortest_path}))).")
print(f"this path based on the {factor} factor has the cost of ((({cost}))).")
