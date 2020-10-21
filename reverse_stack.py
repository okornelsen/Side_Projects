import stack

string = "Mr Owl Ate My Metal Worm"
reversed_string = ""

#WITH STACK CLASS
stack = stack.Stack()
for char in string:
  stack.push(char)
while not stack.is_empty():
  reversed_string += stack.pop()
print(reversed_string)

string = "mroW lateM yM etA lwO rM"
reversed_string = ""

# WITHOUT STACK CLASS
for x in range(len(string)):
  reversed_string += string[-1]
  string = string[0:-1]

print(reversed_string)

