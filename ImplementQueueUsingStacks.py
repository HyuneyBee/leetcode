class MyQueue:

    def __init__(self):
        self.insert = []
        self.output = []

    def push(self, x: int) -> None:
        self.insert.append(x)

    def pop(self) -> int:
        if not self.output:
            while self.insert:
                self.output.append(self.insert.pop())
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.insert:
                self.output.append(self.insert.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.insert and not self.output