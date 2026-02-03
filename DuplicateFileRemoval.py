# Automation script which accept directory name from user and display all names & checksum of files from that directory.

from sys import *
import os
import hashlib
import time
import datetime

def deleteFile(dict1):
    result = list(filter(lambda x : len(x) > 1, dict1.values()))

    icnt = 0
    if len(result) > 0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0
    else:
        print("No duplicate files found")    

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()
    
    return hasher.hexdigest()


def FindDuplicated(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, filelist in os.walk(path):
            print("Current Folder is : ",dirName)
            for filen in filelist:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid path")

def printDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results)> 0:
        print("Duplicate Found")

        print("The following files are identical")

        icnt = 0
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
    else:
        print("No duplicate files found")    

def main():
    print("----- Marvellous Infosystem by Piyush Khairnar ------")

    print("Application name : "+argv[0])

    if (len(argv) != 2):
        print("Erroe : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse specific directory and display checksun of files")
        exit()
    
    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : Application AbsolutePath_of_Directory Extension")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = FindDuplicated(argv[1])
        printDuplicate(arr)
        endTime = time.time()

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception as E:
        print("Error : Inavlid input ",E)

if __name__ == "__main__":
    main()
