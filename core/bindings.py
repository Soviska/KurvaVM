import tls_client
from .instructions import BIND_ADD, BIND_HTTP_REQ

def _bind_add(vm):
    if vm.stack.len() != 2:
        return 0
    
    a = vm.stack.pop()
    b = vm.stack.pop()
    return int(a) + int(b)

def _bind_http_req(vm):
    url_ptr = vm.stack.pop()
    url_len = vm.stack.pop()
    body_ptr = vm.stack.pop()
    
    url = vm.get_string(int(url_ptr), int(url_len))
    print(url)
    
    try:
        session = tls_client.Session(
            client_identifier="chrome_108"
        )
        
        response = session.get(url)
        body = response.content
        
        vm.set_ram(body_ptr, body)
        return 0
    except Exception as e:
        print(e)
        return 0

def get_bindings():
    return {
        BIND_ADD: _bind_add,
        BIND_HTTP_REQ: _bind_http_req
    } 
