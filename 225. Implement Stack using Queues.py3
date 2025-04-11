from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Primary queue
        self.q2 = deque()  # Secondary queue

    def push(self, x: int) -> None:
        # Enqueue the new element to q2
        self.q2.append(x)
        # Transfer all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # Dequeue from q1, which has the current stack elements
        return self.q1.popleft()

    def top(self) -> int:
        # Peek at the front of q1
        return self.q1[0]

    def empty(self) -> bool:
        # Check if q1 is empty
        return not self.q1
