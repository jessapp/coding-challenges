# In a maze, find the path from the top left square of the grid to the bottom 
# right square of the grid. Some squares will be off-limits

# Take maze and off_limits as lists of tuple coords. Start with last element in the maze
def find_path(maze, off_limits, current = maze[-1], path=[]):

    if current == maze[0]:
        return path

    # Start at bottom right
    for r, c in current:

        # Move upward and leftward until you get to top left
        if (r, c + 1) not in off_limits and (r, c + 1) in maze:
            path.append(current)
            current = (r, c + 1)

        elif (r + 1, c) not in off_limits and (r + 1, c) in maze:
            path.append(current)
            current = (r +1, c)

        else:
            raise Exception

    return find_path(maze, off_limits, current, path)