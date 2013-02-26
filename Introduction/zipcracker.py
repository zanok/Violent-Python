import sys

import crypt
import zipfile 

from threading import Thread

def extractFile(file,password):
    try:
        file.extractall(pwd=password)
        print '[+] The password is: '+password
        exit(0)
    except:
        pass
    return

def main():
    zfile = zipfile.ZipFile(sys.argv[1])
    dict = open('dictionary.txt','r')
    for word in dict.readlines():
        word = word.strip('\n') 
        thread = Thread(target=extractFile,args=(zfile,word))
        thread.start() 
    print '[-] Password not found.' 


if __name__ == "__main__":
    main()
