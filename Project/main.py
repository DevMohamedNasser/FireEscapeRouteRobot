
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

from maze import MazeVisualizer, START_POS, GOAL_POS, ROWS, COLS
from search_algo import bfs,dfs,ucs,ids,hill_climbing,astar,get_algorithm_stats

# Global variables
visualizer = None
algorithm_name = ""

def display():
    """OpenGL display callback"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    gluLookAt(COLS/2, 25, ROWS/2 + 15, COLS/2, 0, ROWS/2, 0, 1, 0)
    
    visualizer.update_agent()
    visualizer.draw_scene()
    
    glutSwapBuffers()

def reshape(w, h):
    """Handle window reshape"""
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)

def init_opengl():
    """Initialize OpenGL settings"""
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [10, 25, 10, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.4, 0.4, 0.4, 1])
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0.25, 0.25, 0.28, 1)

def run_algorithm(algorithm_choice, move_delay=0.15):
    global visualizer, algorithm_name
    if algorithm_choice.lower() == 'bfs':
        algorithm_name = "BFS (Breadth-First Search)"
        movement_seq, discovered, path, execution_time = bfs(START_POS, GOAL_POS,move_delay=0.15)
    elif algorithm_choice.lower() == 'dfs':
        algorithm_name = "DFS (Depth-First Search)"
        movement_seq, discovered, path, execution_time = dfs(START_POS, GOAL_POS)
    elif algorithm_choice.lower() == 'ucs':
        algorithm_name = "UCS (Uniform Cost Search)"
        movement_seq, discovered, path, execution_time = ucs(START_POS, GOAL_POS)    
    elif algorithm_choice.lower() == 'astar':
        algorithm_name = "A* (A-Star Search)"
        movement_seq, discovered, path, execution_time = astar(START_POS, GOAL_POS)
    elif algorithm_choice.lower() == 'astar':
        algorithm_name = "IDS (Iterative Deepening Search)"
        movement_seq, discovered, path, execution_time = ids(START_POS, GOAL_POS)
    elif algorithm_choice.lower() == 'astar':
        algorithm_name = "Hill Climbing Search"
        movement_seq, discovered, path, execution_time = hill_climbing(START_POS, GOAL_POS)
    
    else:
        print(f"Error: Unknown algorithm '{algorithm_choice}'")
        print("Available: 'bfs', 'dfs', 'astar','ids',''ucs,'hill climbing'")
        return False
    
    if not path:
        print("No path found! Cannot visualize.")
        return False
    
    # Create visualizer
    visualizer = MazeVisualizer(move_delay)
    visualizer.set_algorithm_data(movement_seq, discovered, path)
    
    # Print statistics
    stats = get_algorithm_stats(discovered, movement_seq, path, execution_time)
    print("\n" + "="*50)
    print("ALGORITHM STATISTICS")
    print("="*50)
    print(f"Algorithm: {algorithm_name}")
    print(f"Explored nodes: {stats['nodes_explored']}")
    print(f"Total movements: {stats['total_movements']}")
    print(f"Final path length: {stats['path_length']}")
    print(f"Execution Time: {stats['execution_time']:.6f}")
    print("="*50)
    
    return True

def compare_algorithms():
    """Compare all three algorithms"""
    print("\n" + "="*60)
    print("ALGORITHM COMPARISON")
    print("="*60)
    
    algorithms = [
        ('BFS', bfs),
        ('DFS', dfs),
        ('UCS', ucs),
        ('A*', astar)
        ('IDS', ids)
        ('Hill climbing', hill_climbing)
    ]
    
    results = []
    
    for name, algorithm in algorithms:
        movement_seq, discovered, path , execution_time= algorithm(START_POS, GOAL_POS)
        if path:
            stats = get_algorithm_stats(discovered, movement_seq, path, execution_time)
            stats['name'] = name
            results.append(stats)
    
    # Print comparison table
    print("\n{:<10} {:<20} {:<20} {:<20} {:<15}".format(
        "Algorithm", "Nodes Explored", "Total Movements", "Path Length", "Excecution Time"
    ))
    print("-" * 85)
    
    for result in results:
        print("{:<10} {:<20} {:<20} {:<20} {:<15.2%}".format(
            result['name'],
            result['nodes_explored'],
            result['total_movements'],
            result['path_length'],
            result['excecution_time']
        ))
    
    print("="*60)

def main():
    """Main program entry point"""
    print("\n" + "="*60)
    print("FIRE ESCAPE ROUTE ROBOT - AI PATHFINDING PROJECT")
    print("="*60)
    print(f"Maze Size: {ROWS}x{COLS}")
    print(f"Start Position: {START_POS}")
    print(f"Goal Position: {GOAL_POS}")
    print("="*60)
    
    # Check command line arguments
    if len(sys.argv) < 2:
        print("\nAlgorithms:")
        print("  bfs    - Breadth-First Search")
        print("  dfs    - Depth-First Search")
        print("  astar  - A-Star Search")
        print("  ids    - Itrative Deeping Search")
        print("  ucs    - uniform Cost Search")
        print("  hill_climbing    - Hill Climbing Search")
        print("  compare - Compare all algorithms (no visualization)")
        print("\nExamples:")
        print("  python main.py bfs")
        print("  python main.py astar")
        print("  python main.py compare")
        return
    
    algorithm = sys.argv[1].lower()
    
    # Handle comparison mode
    if algorithm == 'compare':
        compare_algorithms()
        return
        
    # Run algorithm
    if not run_algorithm(algorithm,0.15):
        return
    
    # Initialize OpenGL
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(f"Fire Escape Route - {algorithm_name}".encode())
    
    init_opengl()
    glutDisplayFunc(display)
    glutIdleFunc(glutPostRedisplay)
    glutReshapeFunc(reshape)
    
    print("\nStarting visualization...")
    print("  Phase 1: Watch agent explore the maze")
    print("  Phase 2: Watch agent Follow the optimal path to goal")
    print("\nClose window to exit.")
   
    
    glutMainLoop()

if __name__ == "__main__":
    main()