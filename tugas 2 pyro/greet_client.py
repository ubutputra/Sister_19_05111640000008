import Pyro4
uri = "PYRONAME:ubutserver@localhost:7777"

def get_list():
    gserver = Pyro4.Proxy(uri)
    print(gserver.list_dir())

def get_create(filename):
    gserver = Pyro4.Proxy(uri)
    print(gserver.create_file(filename))

def get_read(filename):
    gserver = Pyro4.Proxy(uri)
    print(gserver.read_file(filename))

def get_delete(filename):
    gserver = Pyro4.Proxy(uri)
    print(gserver.delete_file(filename))

def get_update(filename,content):
    gserver = Pyro4.Proxy(uri)
    print(gserver.update_file(filename,content))



if __name__=='__main__':
    #test_no_ns()
    print('1.list : melihat list file')
    print('2.create  : membuat file')
    print('3.delete : menghapus file')
    print('4.read  : melihat isi file')
    print('5.update : mengupdate/mengappend isi file')


    while True:
        try:
            masukan = input("Masukan perintah :  ")
            if masukan == '1':
                get_list()
            elif masukan == '2':
                filename = input('Nama file: ')
                get_create(filename)
            elif masukan == '3':
                filename = input('Nama file yang di hapus: ')
                get_delete(filename)

            elif masukan == '4':
                filename = input('Nama file yang di baca: ')
                get_read(filename)

            elif masukan == '5':
                filename = input('Nama file yang di update: ')
                content = input('isi fila yang ingin ditambah:')
                get_update(filename,content)


           
            else:
                print("perintah tidak diketahui")
        except ValueError:
            print("Sorry, my only purpose is to talk to N and A")
