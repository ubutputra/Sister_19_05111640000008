from replicamanager import *
import os
import base64

class FileServer3(object):
    def __init__(self):
        pass

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def list(self):
        print("list ops")
        try:
            daftarfile = []
            for x in os.listdir():
                if x[0:4]=='FFF-':
                    daftarfile.append(x[4:])
            return self.create_return_message('200',daftarfile)
        except:
            return self.create_return_message('500','Error')

    def create(self, name='filename000'):
        instance = 'client3'
        nama='FFF-{}' . format(name)
        print("create ops {}" . format(nama))
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "client3"
        filepath = os.path.join(here, subdir, nama)
        dir_client = ReplicaManager.check_instance(self,instance)
        ReplicaManager.create_all(self,name,dir_client)

        try:
            if os.path.exists(filepath):
                return self.create_return_message('102', 'OK','File Exists')
            f = open(filepath,'wb',buffering=0)
            f.close()
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')
    def read(self,name='filename000'):
        nama='FFF-{}' . format(name)
        print("read ops {}" . format(nama))
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "client3"
        filepath = os.path.join(here, subdir, nama)
        try:
            f = open(filepath,'r+b')
            contents = f.read().decode()
            f.close()
            return self.create_return_message('101','OK',contents)
        except:
            return self.create_return_message('500','Error')

    def update(self,name='filename000',content=''):
        instance = 'client3'
        nama='FFF-{}' . format(name)
        print("update {} ops {}" . format(instance,nama))
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "client3"
        filepath = os.path.join(here, subdir, nama)

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open(filepath,'w+b')
            f.write(content.encode())
            f.close()
            dir_client = ReplicaManager.check_instance(self,instance)
            ReplicaManager.update_all(self,name,content,dir_client)
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,name='filename000'):
        nama='FFF-{}' . format(name)
        print("delete ops {}" . format(nama))

        try:
            os.remove(nama)
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')



if __name__ == '__main__':
    k = FileServer3()
    print(k.create('f1'))
    print(k.update('f1',content='wedusku'))
    print(k.read('f1'))
#    print(k.create('f2'))
#    print(k.update('f2',content='wedusmu'))
#    print(k.read('f2'))
    print(k.list())
    #print(k.delete('f1'))

