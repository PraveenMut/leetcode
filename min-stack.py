from typing import List, Tuple

class CustomList(list):
    def pop(self):
        popped = self[-1]
        self.__delitem__(len(self)-1)
        return popped
    

class MinStack:

    def __init__(self):
        self.stack : List[Tuple[int,int]] = CustomList()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(self.stack[-1][1],val)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
