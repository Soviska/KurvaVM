import struct

def show_ram(vm):
    print("\n-dump of ram:\n")
    for i, reg in enumerate(vm.mem):
        print(f" [ram+{i}] value: {reg}")

def show_reg(vm):
    print("\n-dump of registers:\n")
    for i, reg in vm.regs.items():
        print(f" [reg+{i}] value: {reg}")

def set_ram(vm, reg, value):
    ptr = len(vm.mem)
    if isinstance(value, bytes):
        vm.mem.extend(value)
    else:
        vm.mem.append(value)
    
    vm.regs[reg] = ptr
    vm.regs[reg + 1] = len(value) if isinstance(value, bytes) else 1

def set_reg(vm, reg, value):
    vm.regs[reg] = value

def get_reg(vm, reg):
    return vm.regs.get(reg, 0)

def get_string(vm, ptr, length):
    result = ""
    for i in range(length):
        if ptr + i < len(vm.mem):
            result += chr(vm.mem[ptr + i])
    return result

def load_string(vm):
    string_length = vm.get_byte()
    result = []
    
    for i in range(string_length):
        result.append(vm.get_byte())
    
    return bytes(result)

def load_array_from_register(vm):
    arr_length = vm.get_byte()
    result = []
    
    for i in range(arr_length):
        result.append(vm.get_reg(vm.get_byte()))
    
    return bytes(result)

def load_long_num(vm):
    num_bytes = []
    for i in range(4):
        num_bytes.append(vm.get_byte())
    
    num = struct.unpack('>i', bytes(num_bytes))[0]
    return num 
