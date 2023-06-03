# Deque in python

# Deque is a collection of data in python
# Python’s collections module provides a class called deque
# Deque designed to provide fast and memory-efficient ways to append and pop item from both ends of the underlying data structure

# Create a deque from 0 to 9
from collections import deque
que = deque(range(10))
print(que)

# Append
que.append(24)
print(que)

# Appendleft
que.appendleft(19)
print(que)

# Pop
que.pop()
print(que)

# Popleft
que.popleft()
print(que)

# Rotate
que.rotate()        # Default +1
print(que)

que.rotate(-1)      # One step back
print(que)

# Extend
que.extend([66,77])
print(que)

# Extendleft
que.extendleft([32,24,45])
print(que)