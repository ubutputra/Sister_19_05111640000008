import Pyro4
import socket
uri = "PYRONAME:ubutserver@localhost:7777"

def get_list(hostname):
    gserver = Pyro4.Proxy(uri)
    #check ping ack
    # check = gserver.ping_ack(hostname)
    # if check == True:
    #     print(gserver.list_dir())
    # else:
    #     print('gagal membuat koneksi')
    #end check ping ack
    
    #check heartbeat
    interval = 3
    sequence = 0
    seq_number = gserver.check_heartbeat(interval,'list dir',sequence)
    if(seq_number > 0):
        print('berhasil membuat koneksi')
    else:
        print('gagal membuat koneksi')
    
    #end check heartbeat

   

    
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

# def check_hearbeat()
#     gserver = Pyro4.Proxy(uri)
#     send_string = 'test'
#     respon = gserver.heartbeat(send_string)





if __name__=='__main__':
    hostname = '127.0.0.1'
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
                get_list(hostname)
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
            print("perintah tidak diketahui")
