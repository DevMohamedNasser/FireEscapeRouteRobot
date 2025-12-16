from collections import deque
import heapq
import time
from maze import get_neighbors

def get_path_between(start_pos, end_pos, parent_map):
    
    if start_pos == end_pos:
        return []
    
    # Build path from start_pos to root
    path_from_start = []
    current = start_pos
    while current is not None:
        path_from_start.append(current)
        current = parent_map.get(current)
    
    # Build path from end_pos to root
    path_from_end = []
    current = end_pos
    while current is not None:
        path_from_end.append(current)
        current = parent_map.get(current)
    
    # Find common ancestor (lowest common ancestor)
    path_from_start_set = set(path_from_start)
    common_ancestor = None
    for node in path_from_end:
        if node in path_from_start_set:
            common_ancestor = node
            break
    
    if common_ancestor is None:
        return []
    
    # Build backtrack path: start -> common ancestor
    backtrack_path = []
    current = start_pos
    while current != common_ancestor:
        current = parent_map.get(current)
        if current is not None:
            backtrack_path.append(current)
    
    # Build forward path: common ancestor -> end
    forward_path = []
    current = end_pos
    while current != common_ancestor:
        forward_path.append(current)
        current = parent_map.get(current)
    forward_path.reverse()
    
    # Combine paths
    return backtrack_path + forward_path

def handle_goal_reached(
    current,
    goal,
    parent_map,
    discovered_nodes,
    movement_sequence,
    start_time,
    algo_name,
    path_label
):
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Goal found at {goal}!")
    print(f"Algorithm: {algo_name}")
    print(f"Execution time: {execution_time:.6f} seconds")

    # Reconstruct path
    final_path = []
    temp = current
    while temp is not None:
        final_path.append(temp)
        temp = parent_map[temp]
    final_path.reverse()

    print(f"  Explored nodes: {len(discovered_nodes)}")
    print(f"  Total movements: {len(movement_sequence)}")
    print(f"  {path_label}: {len(final_path)}")
    print("=" * 50 + "\n")

    return movement_sequence, discovered_nodes, final_path, execution_time

def bfs(start, goal, move_delay=0.15):
    start_time = time.time()

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    movement_sequence = [start]
    discovered_nodes = {start}
    current_position = start

    while queue:
        current = queue.popleft()

        if current_position != current:
            path_to_current = get_path_between(current_position, current, parent)
            movement_sequence.extend(path_to_current)
            current_position = current
            

        if current == goal:
            return handle_goal_reached(
                current=current,
                goal=goal,
                parent_map=parent,
                discovered_nodes=discovered_nodes,
                movement_sequence=movement_sequence,
                start_time=start_time,
                algo_name="BFS",
                path_label="Shortest path length"
            )

        for neighbor in get_neighbors(current[0], current[1]):
            if neighbor not in visited:
                visited.add(neighbor)
                discovered_nodes.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

def dfs(start,goal):

    
    return            
                
def ucs(start,goal):


    return

def hill_climbing(start,goal):


    return

def astar(start,goal):


    return

def ids(start,goal):


    return

def get_algorithm_stats(discovered_nodes, movement_sequence, final_path, execution_time):
    """Return statistics for comparison"""
    return {
        "nodes_explored": len(discovered_nodes),
        "total_movements": len(movement_sequence),
        "path_length": len(final_path),
        "execution_time": execution_time
    }