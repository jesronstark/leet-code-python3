class MyQueue:
    def __init__(self):
        # Initialize two stacks
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # Push element onto the input stack
        self.stack_in.append(x)

    def pop(self) -> int:
        # If output stack is empty, transfer elements from input stack
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Pop and return the top element from the output stack
        return self.stack_out.pop()

    def peek(self) -> int:
        # If output stack is empty, transfer elements from input stack
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Return the top element from the output stack without removing it
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.stack_in and not self.stack_out
