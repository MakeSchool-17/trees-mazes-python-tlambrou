import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # Implement create_dfs
    backtracking = []
    current_cell = random.randint(0, len(m.maze_array) - 1)
    visited_cells = 1

    while visited_cells < m.total_cells:
        unvisited_neighbors = m.cell_neighbors(current_cell)
        if len(unvisited_neighbors) > 0:
            n_index = random.randint(0, len(unvisited_neighbors) - 1)
            new_cell, direction = unvisited_neighbors[n_index]
            # new_cell_x_y = m.x_y(new_cell)
            # if not m.cell_in_bounds(*new_cell_x_y):
            #     print('neighbor out of bounds:', new_cell_x_y)
            m.connect_cells(current_cell, new_cell, direction)
            backtracking.append(current_cell)
            current_cell = new_cell
            visited_cells += 1
        else:
            current_cell = backtracking.pop()
    m.refresh_maze_view()
    m.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
