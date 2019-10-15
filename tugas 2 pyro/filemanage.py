import os
import time
import threading

class FileManage(object):
    def __init__(self):
        self.current_heartbeat = {}
        self.last_heartbeat = {}
        self.name_service = ["File Service"]
        self.save_service("File Service")
    
    def create_file(self,filename=""):
        value = ''
        path = os.getcwd()
        namafile = filename
        filename = os.path.join(path,filename)
        f = open(filename, "w+")
        f.write(value)
        f.close()
        return " file {} berhasil dibuat".format(namafile)
    
    def read_file(self,filename=""):
        path = os.getcwd()
        namafile = filename
        filename = os.path.join(path,filename)
        if(os.path.exists(filename)):
            f = open(filename,"r")
            if f.mode == "r":
                contents = f.read()
                return contents
        else:
            return "file tidak ditemukan"

    def delete_file(self,filename=""):
        path = os.getcwd()
        namafile = filename
        filename = os.path.join(path,filename)
        if(os.path.exists(filename)):
            os.remove(filename)
            return("file {} berhasil dihapus").format(namafile)
        else:
            return "file tidak ditemukan"

    def list_dir(self):
        arr = os.listdir()
        return arr 
    
    def update_file(self,filename="",content=""):
        path = os.getcwd()
        namafile = filename
        filename = os.path.join(path,filename)
        if(os.path.exists(filename)):
            f = open(filename,"w+")
            f.write(content)
            f.close()
            return "file berhasil di update"    
        else:
            return "file tidak ditemukan"
    
    
    
    def ping_ack(self,hostname):
        T = 5
        t_end = time.time() + T
        #t_end = time.time() + 60 * T
        #60 second * 15 minute
        while time.time() < t_end:
            respon = self.check_ping(hostname)
            print(respon)

        if respon == "Network Active":
            print("Berhasil Membuat Koneksi")
            return True
        else:
            print("Gagal Membuat Koneksi")
            return False

    def check_ping(self,hostname):
        
        response = os.system("ping -c 1 " + hostname)
        # and then check the response...
        if response == 0:
            pingstatus = "Network Active"
        else:
            pingstatus = "Network Error"

        return pingstatus
    
    def check_heartbeat(self,interval,service,sequence):
        while True:
            # for service in self.name_service:
            #self.current_heartbeat[service] = sequence
            self.last_heartbeat[service] = sequence
            #for iterasi in range(sequence,limit):
            sequence = self.send_heartbeat(self.last_heartbeat[service])
            
            self.current_heartbeat[service] = sequence
            if(self.last_heartbeat[service] < self.current_heartbeat[service]):
                self.last_heartbeat = self.current_heartbeat
                print('Sequence number:',self.current_heartbeat[service])
                respon = sequence
            return respon
            time.sleep(interval)
        
           
                
    def send_heartbeat(self,seq_number):
        seq_number = seq_number + 1
        return seq_number 

    def save_service(self,name_service):
        self.current_heartbeat[name_service] = 0
        self.last_heartbeat[name_service] = 0







if __name__ == '__main__':
    k = FileManage()
    # print(k.get_greet('royyana'))