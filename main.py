from core import Engine, LOAD_STRING, PUSH, CALL_BIND, BIND_HTTP_REQ, EXIT

def web_req():
    target = bytes([
        LOAD_STRING, 200, 18, 104, 116, 116, 112, 115, 58, 47, 47, 103, 111, 111, 103, 108, 101, 46, 99, 111, 109,
        PUSH, 19,
        PUSH, 18,
        PUSH, 0,
        CALL_BIND, BIND_HTTP_REQ,
        EXIT,
    ])
    
    proc = Engine(target)
    
    try:
        proc.run()
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    web_req() 
