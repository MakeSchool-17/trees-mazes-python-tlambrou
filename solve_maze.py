import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    # Implement solve_dfs
    backtracking = []
    current_cell = 0
    visited_cells = 0
    goal_index = len(m.maze_array) - 1
    goal = m.maze_array[goal_index]
    while current_cell not goal:
        unvisited_neighbors = m.cell_neighbors(current_cell)
        if len(unvisited_neighbors) > 0:
            n_index = random.randint(0, len(unvisited_neighbors))
            new_cell = unvisited_neighbors[n_index]
            m.visit_cell(new_cell)
            current_cell = new_cell


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # TODO: Implement solve_bfs
    pass


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
