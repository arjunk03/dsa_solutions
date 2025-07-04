from itertools import product

a = [1, 2, 3]
b = ['a', 'b', 'c']

data = product(a, b)
print("Cartesian Product:")
print(list(data))

## Implement Undo/Redo functionality using Deque
from collections import deque

class UndoRedo():
    def __init__(self):
        self.undo_stack = deque()
        self.redo_stack = deque()
    
    def do_something(self, action):
        self.undo_stack.append(action)
        # self.redo_stack.clear()
        print(f"Action performed: {action}")
    
    def undo(self):
        val = self.undo_stack.pop() if self.undo_stack else None
        if val is None:
            print("No actions to undo")
            return
        self.redo_stack.append(val)
        print(f"Undo action: {val}")
    
    def redo(self):
        if self.redo_stack:
            val = self.redo_stack.pop()
            self.undo_stack.append(val)
            print(f"Redo action: {val}")
        else:
            print("No actions to redo")

# Example usage
undo_redo = UndoRedo()
undo_redo.do_something("Action 1")
undo_redo.do_something("Action 2")
undo_redo.undo()
undo_redo.redo()
undo_redo.undo()
undo_redo.redo()
undo_redo.redo()  # No actions to redo  
undo_redo.undo()  # Undo action: Action 2
undo_redo.undo()  # Undo action: Action 1
undo_redo.undo()  # No actions to undo      