import Pyro4

def test_no_ns():
    uri = "PYRO:obj_ad802d86ad5645a2a0db56b059d82fc7@localhost:54804"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))

def test_with_ns():
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    print(gserver.get_greet('ronaldo'))

if __name__=='__main__':
    test_with_ns()
