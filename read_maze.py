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