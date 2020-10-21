from helper import get_trail, offsets, is_valid_position, read_maze
from queue_fifo import Queue

def breadth_first_search(maze, start_pos, goal_pos):
  queue = Queue()
  queue.enqueue(start_pos)
  predecessors = {start_pos: None}

  while not queue.is_empty():
    current_pos = queue.dequeue()
    if current_pos == goal_pos:
      return get_trail(predecessors, start_pos, goal_pos)
    for direction in ["up", "right", "down", "left"]:
      row_offset, col_offset = offsets[direction]
      neighbor_pos = (current_pos[0] + row_offset, current_pos[1] + col_offset)
      if is_valid_position(maze, neighbor_pos) and neighbor_pos not in predecessors:
        queue.enqueue(neighbor_pos)
        predecessors[neighbor_pos] = current_pos
  return None

if __name__ == "__main__":
 # TEST 1
  maze = read_maze("simple_maze.txt")
  for row in maze:
    print(row)
  start_pos = (1,1)
  goal_pos = (4,4)
  result = breadth_first_search(maze, start_pos, goal_pos)
  assert result == [(1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]

 # TEST 2
  maze = read_maze("simple_maze.txt")
  start_pos = (1,1)
  goal_pos = (0,0)
  result = breadth_first_search(maze, start_pos, goal_pos)
  assert result is None