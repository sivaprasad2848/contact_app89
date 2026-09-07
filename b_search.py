from collections import deque
dq = deque()
dq.append(10)
dq.append(20)
dq.appendleft(30)
dq.popleft()
print(dq.size)  # Output: deque([10, 20])
