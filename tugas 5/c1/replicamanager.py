import os
import base64
class ReplicaManager(object):
    def __init__(self):
        pass
    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def check_instance(self,nama_instance):
        dir_client = []
        if(nama_instance == 'client1'):
            dir_client.append('client2')
            dir_client.append('client3')
            return dir_client
            # print (dir_client)
        elif(nama_instance == 'client2'):
            dir_client.append('client1')
            dir_client.append('client3')
            return dir_client

        elif(nama_instance == 'client3'):
            dir_client.append('client1')
            dir_client.append('client2')
            return dir_client

    def create_all(self,name,dir_client):
        # print(instance)
        # dir_client = self.check_instance(instance)
        # print (dir_client)
        nama='FFF-{}' . format(name)
        print("create ops {}" . format(nama))
        here = os.path.dirname(os.path.realpath(__file__))
        subdir1 = dir_client[0]
        subdir2 = dir_client[1]
        filepath1 = os.path.join(here, subdir1, nama)
        filepath2 = os.path.join(here, subdir2, nama)

        try:
            f = open(filepath1,'wb',buffering=0)
            print("create ops {} {}" . format(subdir1,nama))
            print("create ops {} {}" . format(subdir2,nama))


            f = open(filepath2,'wb',buffering=0)

            f.close()
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')
    
    def update_all(self,name,content,dir_client):

        nama='FFF-{}' . format(name)
        print("update ops {}" . format(nama))
        here = os.path.dirname(os.path.realpath(__file__))
        subdir1 = dir_client[0]
        subdir2 = dir_client[1]

        filepath1 = os.path.join(here, subdir1, nama)
        filepath2 = os.path.join(here, subdir2, nama)


        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open(filepath1,'w+b')
            f.write(content.encode())
            f.close()
            print("update ops {} {}" . format(subdir1,nama))

            f = open(filepath2,'w+b')
            f.write(content.encode())
            f.close()
            print("update ops {} {}" . format(subdir,nama))
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

if __name__ == '__main__':
    k = ReplicaManager()
    k.create_all()
