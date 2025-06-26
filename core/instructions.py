PTR = 100

LOAD_STRING = 1
LOAD_NUM = 2
LOAD_FLOAT = 3
LOAD_LONG_NUM = 4
LOAD_ARRAY = 5

PROPACCESS = 10
FUNC_CALL = 11
EVAL = 12
CALL_BCFUNC = 13
RETURN_BCFUNC = 14
COPY = 15
EXIT = 16
COND_JUMP = 17
JUMP = 18
JUMP_COND_NEG = 19
BCFUNC_CALLBACK = 20
PROPSET = 21
TRY = 22
THROW = 23

COMP_EQUAL = 50
COMP_NOT_EQUAL = 51
COMP_LESS_THAN = 54
COMP_GREATHER_THAN = 55
COMP_LESS_THAN_EQUAL = 56
COMP_GREATHER_THAN_EQUAL = 57

ADD = 100
MUL = 101
SUB = 102
DIV = 103

POP = 110
PUSH = 111
LEN = 112
TOP = 113

CALL_BIND = 120
BIND_ADD = 121
BIND_HTTP_REQ = 122

def _copy(vm):
    dst = vm.get_byte()
    src = vm.get_byte()
    vm.set_reg(dst, vm.get_reg(src))

def _jump(vm):
    offset = vm.get_byte()
    vm.set_reg(PTR, offset)

def _cond_jump(vm):
    cond = vm.get_byte()
    offset = vm.get_byte()
    
    if vm.get_reg(cond) == 1:
        vm.set_reg(PTR, offset)

def _jump_cond_neg(vm):
    cond = vm.get_byte()
    offset = vm.get_byte()
    
    if vm.get_reg(cond) != 1:
        vm.set_reg(PTR, offset)

def _exit(vm):
    vm.set_reg(PTR, len(vm.code))

def _load_string(vm):
    dst = vm.get_byte()
    string_data = vm.load_string()
    vm.set_ram(dst, string_data)

def _load_num(vm):
    dst = vm.get_byte()
    val = vm.get_byte()
    vm.set_reg(dst, val)

def _load_float(vm):
    vm.set_reg(PTR, 0)

def _load_long_num(vm):
    vm.set_reg(PTR, 0)

def _load_array(vm):
    dst = vm.get_byte()
    vm.set_reg(dst, 0)

def _comp_equal(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    
    result = 1 if left_val == right_val else 0
    vm.set_reg(dst, result)

def _comp_not_equal(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    
    result = 1 if left_val != right_val else 0
    vm.set_reg(dst, result)

def _comp_less_than(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    
    result = 1 if left_val < right_val else 0
    vm.set_reg(dst, result)

def _comp_greater_than(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    
    result = 1 if left_val > right_val else 0
    vm.set_reg(dst, result)

def _comp_less_than_equal(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    
    result = 1 if left_val <= right_val else 0
    vm.set_reg(dst, result)

def _comp_greater_than_equal(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    
    result = 1 if left_val >= right_val else 0
    vm.set_reg(dst, result)

def _add(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    vm.set_reg(dst, left_val + right_val)

def _mul(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    vm.set_reg(dst, left_val * right_val)

def _div(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    vm.set_reg(dst, left_val // right_val if right_val != 0 else 0)

def _sub(vm):
    dst, left, right = vm.get_dst_left_right()
    left_val = vm.get_reg(left)
    right_val = vm.get_reg(right)
    vm.set_reg(dst, left_val - right_val)

def _pop(vm):
    vm.stack.pop()

def _push(vm):
    val = vm.get_byte()
    vm.stack.push(val)

def _len(vm):
    dst = vm.get_byte()
    vm.set_reg(dst, vm.stack.len())

def _top(vm):
    dst = vm.get_byte()
    vm.set_reg(dst, vm.stack.top())

def _call_bind(vm):
    bind_id = vm.get_byte()
    if bind_id in vm.binds:
        vm.binds[bind_id](vm)

def get_ops():
    return {
        EXIT: _exit,
        LOAD_STRING: _load_string,
        LOAD_NUM: _load_num,
        LOAD_FLOAT: _load_float,
        LOAD_LONG_NUM: _load_long_num,
        LOAD_ARRAY: _load_array,
        COMP_EQUAL: _comp_equal,
        COMP_NOT_EQUAL: _comp_not_equal,
        COMP_LESS_THAN: _comp_less_than,
        COMP_GREATHER_THAN: _comp_greater_than,
        COMP_LESS_THAN_EQUAL: _comp_less_than_equal,
        COMP_GREATHER_THAN_EQUAL: _comp_greater_than_equal,
        ADD: _add,
        MUL: _mul,
        DIV: _div,
        SUB: _sub,
        JUMP: _jump,
        COND_JUMP: _cond_jump,
        JUMP_COND_NEG: _jump_cond_neg,
        COPY: _copy,
        CALL_BIND: _call_bind,
        POP: _pop,
        PUSH: _push,
        LEN: _len,
        TOP: _top
    } 
