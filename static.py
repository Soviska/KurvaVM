from core import Engine, LOAD_STRING, LOAD_NUM, ADD, COMP_EQUAL, COND_JUMP, EXIT

def test_comp():
    seq = bytes([
        LOAD_STRING, 200, 13, 105, 109, 32, 107, 97, 110, 121, 101, 32, 119, 101, 115, 116,
        LOAD_NUM, 13, 5,
        LOAD_NUM, 14, 3,
        ADD, 15, 13, 14,
        ADD, 16, 14, 14,
        COMP_EQUAL, 17, 15, 16,
        COND_JUMP, 17, 0,
        EXIT,
    ])
    
    vm = Engine(seq)
    
    try:
        vm.run()
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    test_comp() 
