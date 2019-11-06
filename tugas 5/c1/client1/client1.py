import Pyro4
import base64
import json
import sys

# namainstance = sys.argv[0] or "fileserver"
namainstance = "fileserver1"

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()
    f.create('slide1.pdf')
    f.update('slide1.pdf', content = 'hai dari client1' )

    # f.create('slide2.pptx')
    # f.update('slide2.pptx', content = open('FFF-slide2.pptx','rb+').read())

    # print(f.list())
    # d = f.read('slide1.pdf')
    # #kembalikan ke bentuk semula ke dalam file name slide1-kembali.pdf
    # open('slide1-kembali.pdf','w+b').write(base64.b64decode(d['data']))

    # k = f.read('slide2.pptx')
    # #kembalikan ke bentuk semula ke dalam file name slide2-kembali.pptx
    # open('slide2-kembali.pptx','w+b').write(base64.b64decode(k['data']))


