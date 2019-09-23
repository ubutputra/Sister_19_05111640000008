import os
 
class FileManage(object):
    def __init__(self):
        pass
    
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
        
if __name__ == '__main__':
    k = FileManage()
    # print(k.get_greet('royyana'))