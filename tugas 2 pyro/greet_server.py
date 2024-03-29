from filemanage import  *
import Pyro4


def start_without_ns():
    daemon = Pyro4.Daemon()
    x_GreetServer = Pyro4.expose(FileManage)
    uri = daemon.register(x_GreetServer)
    print("my URI : ", uri)
    daemon.requestLoop()


def start_with_ns():
    #name server harus di start dulu dengan  pyro4-ns -n localhost -p 7777
    #gunakan URI untuk referensi name server yang akan digunakan
    #untuk mengecek service apa yang ada di ns, gunakan pyro4-nsc -n localhost -p 7777 list
     #multi device tinggal ganti localhost jadi ip, client dan server pakai ip yg sama
    # jalankan command pyro4-ns -n ipmu -p 7777
    daemon = Pyro4.Daemon(host='10.151.254.50')
    ns = Pyro4.locateNS("10.151.254.50",7777)
    x_GreetServer = Pyro4.expose(FileManage)
    uri_greetserver = daemon.register(x_GreetServer)
    print("URI greet server : ", uri_greetserver)
    ns.register("ubutserver", uri_greetserver)
    daemon.requestLoop()


if __name__ == '__main__':
    start_with_ns()
