boundary = "#"

offsets = {
  "right":  (0,1),
  "left":   (0,-1),
  "up":     (-1,0),
  "down":   (1,0)
}

def read_maze(filename):
  try:
    with open(filename) as myfile:
      maze = []
      readlines = myfile.readlines()
      for line in readlines:
        maze_row = []
        stripped_line = line.strip("\n")
        for char in stripped_line:
          maze_row.append(char)
        maze.append(maze_row)
      columns = len(maze[0])
      for row in maze:
        if len(row) != columns:
          print("The maze isn't well designed.")
          raise SystemExit
      return maze

  except OSError:
    print("There was a problem with the file you have selected.")
    raise SystemExit

if __name__ == "__main__":
  maze = read_maze("simple_maze.txt")
  for row in maze:
    print(row)

def is_valid_position(maze, position):
  i, j = position
  row_count = len(maze)
  col_count = len(maze[0])
  return 0 <= i < row_count and 0 <= j < col_count and maze[i][j] != boundary

def get_trail(predecessors, start, goal):
  current_position = goal
  path = []
  while current_position != start:
    path.append(current_position)
    current_position = predecessors[current_position]
  path.append(start)
  path.reverse()
  return path
