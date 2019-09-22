import random


class GreetServer(object):
    def __init__(self):
        pass

    def get_greet(self, name='NoName'):
        lucky_number = random.randint(1, 100000)
        return "Hello {}, this is your lucky number {}".format(name, lucky_number)




if __name__ == '__main__':
    # k = GreetServer()
    # print(k.get_greet('royyana'))

    while True:
        try:
            name = input("What is your name ? ").strip()
            if name.startswith("A"):
                print("message for A")
                break
            elif name.startswith("N"):
                print("message for N")
                break
            else:
                print("Sorry, my only purpose is to talk to N and A")
        except ValueError:
            print("Sorry, my only purpose is to talk to N and A")
