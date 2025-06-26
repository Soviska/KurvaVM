class Stack:
    def __init__(self):
        self.memory = []
    
    def show_stack(self):
        print("\n-dump of stack:\n")
        for i, mem in enumerate(self.memory):
            print(f" [mem+{i}] value: {mem}")
    
    def pop(self):
        if len(self.memory) == 0:
            return 0
        
        val = self.memory[-1]
        self.memory = self.memory[:-1]
        return val
    
    def push(self, value):
        self.memory.append(value)
    
    def len(self):
        return len(self.memory)
    
    def top(self):
        if len(self.memory) == 0:
            return 1
        return self.memory[-1] 
