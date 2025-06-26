import logging
from .instructions import *
from .stack import Stack
from .bindings import get_bindings
from .memory import show_ram, set_ram, get_string, show_reg, set_reg, get_reg, load_string

class Engine:
    def __init__(self, code):
        self.PTR = PTR
        self.code = code
        self.mem = []
        self.stack = Stack()
        self.regs = {PTR: 0}
        self.ops = {}
        self.binds = {}
        self._init()
        
        print(f"cde: {list(code)}")
    
    def _init(self):
        self.ops = get_ops()
        self.binds = get_bindings()
    
    def get_byte(self):
        result = self.code[self.regs[PTR]]
        self.regs[PTR] += 1
        return result
    
    def get_dst_left_right(self):
        return self.get_byte(), self.get_byte(), self.get_byte()
    
    def get_reg(self, reg):
        return get_reg(self, reg)
    
    def set_reg(self, reg, value):
        set_reg(self, reg, value)
    
    def set_ram(self, ptr, data):
        set_ram(self, ptr, data)
    
    def get_ram(self, ptr):
        if ptr < len(self.mem):
            return self.mem[ptr]
        return 0
    
    def load_string(self):
        return load_string(self)
    
    def get_string(self, ptr, length):
        return get_string(self, ptr, length)
    
    def show_reg(self):
        show_reg(self)
    
    def show_ram(self):
        show_ram(self)
    
    def run(self):
        while self.regs[PTR] < len(self.code):
            op = self.get_byte()
            
            if op not in self.ops:
                raise ValueError(f"invalid op: {op}")
            
            self.ops[op](self)
            logging.info(f"[ptr+{self.regs[PTR]}] {op} - {self.regs}")
        
        self.show_reg()
        self.show_ram()
        self.stack.show_stack()
        return None 
