# University: International Hellenic University (IHU).
# Department: Information and Electronic Engineering (IEE).
# Course: Advanced Topics of Artificial Intelligence. 
# Project: Implementation of BFS and DFS algorithm.
# Creator/Developer: Oikonomou Alexandros.
# RN: 2019119
# ---------------- Depth First Search (DFS) Algorithm ---------------- #


# DFS Characteristics:
# 1. Knowing the initial state and the desired
#    final states, DFS performs a blind search
#    on the graph to find one of the final states.
# 2. He chooses to expand the whole-front with the 
#    situation located deeper in the search tree.
# 3. It has a Stack structure.


# Create the Graph, using an Adjacency List named "myGraph". The Adjacency List is considered the most suitable 
# data structure for representing relationships or connections between nodes in a graph. The content of the Adjacency 
# List essentially shows which nodes are neighbors to each other. Therefore, for each node in the graph, the adjacency 
# list will store a collection of its other neighboring nodes.
myGraph = {    # Creating the Adjacency List named "myGraph".
    'I': ['A', 'B', 'D'],  # Is the initial state (node I) of the graph. Node I has neighbors A, B and D.
    'A': ['B', 'G1'],      # Node A has nodes B and G1 as neighbors.
    'B': ['A', 'C'],       # Node B has nodes A and C as neighbors.
    'C': ['I', 'G2', 'F'], # Node C has nodes I, G2 and F as neighbors.
    'D': ['I', 'C', 'E'],  # Node D has nodes I, C and E as neighbors.
    'E': ['G3'],           # Node E has node G1 as a neighbor.
    'F': ['D', 'G3'],      # Node F has nodes D and G3 as neighbors.
    'G1': [],  # Is the 1st target state (node G1) of the graph. Node G1 has no neighbors.
    'G2': [],  # Is the 2nd target state (node G2) of the graph. Node G2 has no neighbors.
    'G3': []   # Is the 3rd target state (node G3) of the graph. Node G3 has no neighbors.
}

# Creating the DFS_Graph_Search() function with graph, start and goals arguments. This function represents
# the Depth First Search (DFS) algorithm applied to the graph (1st argument), in order to search for a smart 
# path from a start node (2nd argument) to one of the target nodes/goals (3rd argument). In our case the graph will 
# be "myGraph", the initial node will be I and the target nodes will be G1, G2 and G3 which will be passed parametrically to the function.
def DFS_Graph_Search(graph, start, goals): # Creating the function DFS_Graph_Search(graph, start, goals).

    stack = [(start, [start])]  # Initializing the stack as a list containing a tuple with the start node
                                # start and the [start] list representing the initial path starting from the start node.
    
    visited = []    # Initializing an empty list named visited to
                    # keep track of the nodes that DFS has visited.

    # Starting a while loop that will continue as long as the stack is NOT empty.
    while stack:
        node, path = stack.pop()   # Removes and returns the top ".pop()" element from the stack,
                                   # which is a tuple containing the current node and the path
                                   # (path) followed to reach this node.
        
        visited.append(node)   # Marks the current node as visited
                               # inserting it with ".append()" in the visited list.

        # Checking if the current node is one of the target nodes (G1, G2 or G3).
        if node in goals:
            return node, path, visited  # If indeed the current node is one of the target nodes, then the function
                                        # returns this node as the target node, the path of the graph that
                                        # followed to reach the target node and also the visited list.

        # Creating iteration for each neighbor of the current node in the graph.
        # Note that here the order of the graph must be reversed using "reversed()" to preserve the behavior of the stack.
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:  # Checking if the neighbor has not already been visited and is therefore not in the visited list.
                new_path = path + [neighbor]  # Creating a new path (new_path) as a list and adding the neighbor to the current path (path).
                stack.append((neighbor, new_path))  # Finally, the new tuple is inserted into the stack, representing the node
                                                    # neighbor and the new path (new_path) followed to reach it.

    return None, None, None # If the while loop completes without finding even one
                            # target node, the function returns None for each argument.

initial_state = 'I' # Creating and initializing the variable initial_state with the value 'I',
                    # which will represent the initial state/initial node of the graph.

goal_states = ['G1', 'G2', 'G3']   # Creating and initializing the goal_states list with the elements
                                   # 'G1','G2' and 'G3', which will represent the target states of the graph.

# Calls DFS_Graph_Search() with arguments: myGraph (the graph), initial_state (the initial state I)
# and goal_states (the goal states 'G1','G2' and 'G3'). The function returns the three values: target_node,
# graph_path and visited_order. These variables are assigned the function's return values corresponding to:
# 1. The target node found.
# 2. The path followed from the initial node to the target node.
# 3. All nodes in order that were visited by the algorithm, regardless of whether they belong to the solution path.
target_node, graph_path, visited_order = DFS_Graph_Search(myGraph, initial_state, goal_states)

# Checking if the visited_order variable is not None,
# meaning that a path to the target node was found.
if visited_order is not None:
    print("Target node found:", target_node) # Printing the target node found by DFS.
    print("Graph Path from initial node I to target node:", " -> ".join(graph_path)) # Printing the path followed from the initial node to the target node.
    print("All Nodes visited in order:", visited_order) # Printing all nodes in order that were visited by DFS, regardless of whether they belong to the solution path.
else: # Else (Meaning that the visited_order variable is None -> so no path to a target node was found).
    print("No path to the goal node found...") # Printing the message "No path to the goal node found...".